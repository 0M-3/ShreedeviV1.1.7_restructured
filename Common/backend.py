"""Low-level data access for PyBookKeeper.

This module directly mirrors the recovered ``Common/Backend.py`` module.
The data model consists of a bill header (``bills`` table) plus several
detail tables (``GoldSale``, ``SilverSale``, ``OldOrder``, ``NO``, ``VC``,
``GP`` and ``SP``).
"""

import sqlite3
from datetime import date

from Common.transaction import purchase


conn = sqlite3.connect('database.db')
c = conn.cursor()


def Bill_store(obj, sale_items):
    """Persist a completed Bill together with every item in ``sale_items``."""
    c.execute("""
        create table if not exists bills (
            cust_name text,
            ph_num text,
            bill_num integer,
            item_names text,
            item_id text,
            purity text,
            gold_grwt real,
            gold_ntwt real,
            silver_grwt real,
            silver_ntwt real,
            trans_type text,
            amount integer,
            cash integer,
            card integer,
            card_machine text,
            UPI integer,
            UPI_type text,
            cheque integer,
            cheque_num integer,
            debt integer,
            URD integer,
            URD_name text,
            URD_goldgrwt real,
            URD_goldntwt real,
            URD_silvergrwt real,
            URD_silverntwt real,
            other integer,
            othername text,
            date text
        )
    """)
    conn.commit()

    temp_bill = Bill_num()

    c.execute("""
        insert into bills values (
            :cust_name,
            :ph_num,
            :bill_num,
            :items_name,
            :item_id,
            :purity,
            :gold_grwt,
            :gold_ntwt,
            :silver_grwt,
            :silver_ntwt,
            :trans_type,
            :amount,
            :cash,
            :card,
            :card_machine,
            :UPI,
            :UPI_type,
            :cheque,
            :cheque_num,
            :debt,
            :URD,
            :URD_name,
            :URD_goldgrwt,
            :URD_goldntwt,
            :URD_silvergrwt,
            :URD_silverntwt,
            :other,
            :othername,
            :date
        )
    """, {
        'cust_name': obj.cust_name,
        'ph_num': obj.ph_num,
        'bill_num': temp_bill,
        'items_name': obj.items_name,
        'item_id': obj.item_id,
        'purity': obj.purity,
        'gold_grwt': obj.gold_grwt,
        'gold_ntwt': obj.gold_ntwt,
        'silver_grwt': obj.silver_grwt,
        'silver_ntwt': obj.silver_ntwt,
        'trans_type': obj.trans_type,
        'amount': obj.amount,
        'cash': obj.cash,
        'card': obj.card,
        'card_machine': obj.card_machine,
        'UPI': obj.UPI,
        'UPI_type': obj.UPI_type,
        'cheque': obj.cheque,
        'cheque_num': obj.cheque_num,
        'debt': obj.debt,
        'URD': obj.URD,
        'URD_name': obj.URD_name,
        'URD_goldgrwt': obj.URD_goldgrwt,
        'URD_goldntwt': obj.URD_goldntwt,
        'URD_silvergrwt': obj.URD_silvergrwt,
        'URD_silverntwt': obj.URD_silverntwt,
        'other': obj.other,
        'othername': obj.othername,
        'date': obj.date,
    })
    conn.commit()

    if obj.URD_goldgrwt > 0:
        Sale_store({
            1: purchase('Gold Purchase', obj.URD_name, obj.URD_goldgrwt,
                        obj.URD_goldntwt, obj.URD)
        }, temp_bill)

    if obj.URD_silvergrwt > 0:
        Sale_store({
            1: purchase('Silver Purchase', obj.URD_name, obj.URD_silvergrwt,
                        obj.URD_silverntwt, obj.URD)
        }, temp_bill)

    Sale_store(sale_items, temp_bill)


def Bill_num():
    """Return the next available bill number."""
    c.execute('select max(bill_num) from bills')
    row = c.fetchone()
    if row[0] is None:
        return 1
    return row[0] + 1


def Get_Billsday(date):
    """Return every bill recorded on ``date`` (``YYYY-MM-DD``)."""
    c.execute('select * from bills where date=:date', {'date': date})
    return c.fetchall()


def Get_delBills():
    """Return a delete/search summary of all bills."""
    c.execute('select bill_num, cust_name, trans_type, amount, date '
                'from bills order by bill_num desc')
    return c.fetchall()


def Get_specificbills(name, billnum, ttype):
    """Search bills by customer name, bill number and/or transaction type."""
    if ttype == 'Shree plus':
        ttype = 'Misc plus'
    if ttype == 'Shree minus':
        ttype = 'Misc minus'

    if name == '':
        if billnum == '':
            c.execute("""
                select bill_num, cust_name, trans_type, amount, date
                from bills
                where trans_type=:ttype
                order by bill_num desc
            """, {'ttype': ttype})
        elif ttype == 'None':
            c.execute("""
                select bill_num, cust_name, trans_type, amount, date
                from bills
                where bill_num=:billnum
                order by bill_num desc
            """, {'billnum': billnum})
        else:
            c.execute("""
                select bill_num, cust_name, trans_type, amount, date
                from bills
                where trans_type=:ttype and bill_num=:billnum
                order by bill_num desc
            """, {'ttype': ttype, 'billnum': billnum})
    elif billnum == '':
        if ttype == 'None':
            c.execute("""
                select bill_num, cust_name, trans_type, amount, date
                from bills
                where cust_name=:cust_name
                order by bill_num desc
            """, {'cust_name': name})
        else:
            c.execute("""
                select bill_num, cust_name, trans_type, amount, date
                from bills
                where cust_name=:cust_name and ttype=:ttype
                order by bill_num desc
            """, {'cust_name': name, 'ttype': ttype})

    return c.fetchall()


def del_billnum(billnum):
    """Delete a bill header by bill number."""
    c.execute('delete from bills where bill_num=:billnum', {'billnum': billnum})
    conn.commit()


def Sale_store(lst, num):
    """Persist individual sale/purchase records.

    ``lst`` is a dict whose values are instances of the data classes defined in
    ``Common.transaction``.  The type name of each value determines the detail
    table used.
    """
    for _, obj in lst.items():
        obj_type = type(obj).__name__

        if obj_type == 'GoldSell':
            c.execute("""
                create table if not exists GoldSale(
                    billnum integer,
                    custname text,
                    ph_num text,
                    item_name text,
                    id integer,
                    grwt real,
                    ntwt real,
                    amount integer,
                    purity text,
                    date text
                )
            """)
            conn.commit()
            c.execute("""
                insert into GoldSale values(
                    :billnum,
                    :custname,
                    :ph_num,
                    :item_name,
                    :id,
                    :grwt,
                    :ntwt,
                    :amount,
                    :purity,
                    :date
                )
            """, {
                'custname': obj.cust_name,
                'billnum': num,
                'ph_num': obj.ph_num,
                'item_name': obj.pr_name,
                'id': obj.id,
                'grwt': obj.gr_wt,
                'ntwt': obj.nt_wt,
                'amount': obj.amount,
                'purity': obj.purity,
                'date': obj.date,
            })
            conn.commit()

        elif obj_type == 'SilverSell':
            c.execute("""
                create table if not exists SilverSale (
                    billnum integer,
                    cust_name text,
                    ph_num text,
                    item_name text,
                    id integer,
                    grwt real,
                    ntwt real,
                    amount integer,
                    purity text,
                    date text
                )
            """)
            conn.commit()
            c.execute("""
                insert into SilverSale values(
                    :billnum,
                    :cust_name,
                    :ph_num,
                    :item_name,
                    :id,
                    :grwt,
                    :ntwt,
                    :amount,
                    :purity,
                    :date
                )
            """, {
                'billnum': num,
                'cust_name': obj.cust_name,
                'ph_num': obj.ph_num,
                'item_name': obj.pr_name,
                'id': obj.id,
                'grwt': obj.gr_wt,
                'ntwt': obj.nt_wt,
                'amount': obj.amount,
                'purity': obj.purity,
                'date': obj.date,
            })
            conn.commit()

        elif obj_type == 'OldOrder':
            c.execute("""
                create table if not exists OldOrder(
                    billnum integer,
                    type text,
                    amount integer,
                    item text,
                    grwt real,
                    ntwt real
                )
            """)
            conn.commit()
            c.execute("""
                insert into OldOrder values (
                    :billnum,
                    :type,
                    :amount,
                    :item,
                    :grwt,
                    :ntwt
                )
            """, {
                'type': obj.type,
                'billnum': num,
                'amount': obj.amount,
                'item': obj.item,
                'grwt': obj.grwt,
                'ntwt': obj.ntwt,
            })
            conn.commit()

        elif obj_type == 'NO':
            c.execute("""
                create table if not exists NO(
                    billnum integer,
                    Est integer,
                    Adv integer,
                    item text,
                    Ggrwt real,
                    Gntwt real,
                    Sgrwt real,
                    Sntwt real
                )
            """)
            conn.commit()
            c.execute("""
                insert into NO values (
                    :billnum,
                    :Est,
                    :Adv,
                    :item,
                    :Ggrwt,
                    :Gntwt,
                    :Sgrwt,
                    :Sntwt
                )
            """, {
                'Est': obj.Est,
                'billnum': num,
                'Adv': obj.Adv,
                'item': obj.item,
                'Ggrwt': obj.Ggrwt,
                'Gntwt': obj.Gntwt,
                'Sgrwt': obj.Sgrwt,
                'Sntwt': obj.Sntwt,
            })
            conn.commit()

        elif obj_type == 'VC':
            c.execute("""
                create table if not exists VC(
                    billnum integer,
                    type text,
                    item text,
                    amount integer,
                    grwt real,
                    ntwt real
                )
            """)
            conn.commit()
            c.execute("""
                insert into VC values (
                    :billnum,
                    :type,
                    :item,
                    :amount,
                    :grwt,
                    :ntwt
                )
            """, {
                'type': obj.type,
                'billnum': num,
                'item': obj.item,
                'amount': obj.amount,
                'grwt': obj.grwt,
                'ntwt': obj.ntwt,
            })
            conn.commit()

        elif obj_type == 'purchase':
            if obj.type == 'Gold Purchase':
                c.execute("""
                    create table if not exists GP(
                        billnum integer,
                        item text,
                        grwt real,
                        ntwt real,
                        amount integer,
                        date text
                    )
                """)
                conn.commit()
                c.execute("""
                    insert into GP values (
                        :billnum,
                        :item,
                        :grwt,
                        :ntwt,
                        :amount,
                        :date
                    )
                """, {
                    'item': obj.item,
                    'billnum': num,
                    'grwt': obj.grwt,
                    'ntwt': obj.ntwt,
                    'amount': obj.amount,
                    'date': date.today(),
                })
                conn.commit()

            elif obj.type == 'Silver Purchase':
                c.execute("""
                    create table if not exists SP(
                        billnum integer,
                        item text,
                        grwt real,
                        ntwt real,
                        amount integer,
                        date text
                    )
                """)
                conn.commit()
                c.execute("""
                    insert into SP values (
                        :billnum,
                        :item,
                        :grwt,
                        :ntwt,
                        :amount,
                        :date
                    )
                """, {
                    'item': obj.item,
                    'billnum': num,
                    'grwt': obj.grwt,
                    'ntwt': obj.ntwt,
                    'amount': obj.amount,
                    'date': date.today(),
                })
                print('SP')
                conn.commit()


def Get_Sale_store(startdate, enddate):
    """Return daily sale/purchase totals between two dates.

    Dates are expected in ``DD-MM-YYYY`` format.  The returned value is a
    dictionary mapping ``"Gold Sale"``, ``"Silver Sale"``, ``"Gold Purchase"``
    and ``"Silver Purchase"`` to lists of records.
    """
    from datetime import datetime, timedelta

    dte = datetime.strptime(startdate, '%d-%m-%Y')
    enddte = datetime.strptime(enddate, '%d-%m-%Y')

    if dte > enddte:
        return None

    temp_dict = {
        'Gold Purchase': [],
        'Gold Sale': [],
        'Silver Purchase': [],
        'Silver Sale': [],
    }
    temp_lst = []

    while (dte + timedelta(days=1)) != enddte:
        strdate = dte.strftime('%Y-%m-%d')
        print(strdate)

        try:
            c.execute("""
                select item_name, ntwt, amount
                from GoldSale
                where date=:date
                order by item_name
            """, {'date': strdate})
            temp_lst = c.fetchall()
            if temp_lst:
                temp_dict['Gold Sale'].append(temp_lst)
        except Exception:
            print('GS')

        try:
            c.execute("""
                select item_name, ntwt, amount
                from SilverSale
                where date=:date
                order by item_name
            """, {'date': strdate})
            temp_lst = c.fetchall()
            if temp_lst:
                temp_dict['Silver Sale'].append(temp_lst)
        except Exception:
            print('SS')

        try:
            c.execute("""
                select item, ntwt, amount
                from GP
                where date=:date
                order by item
            """, {'date': strdate})
            temp_lst = c.fetchall()
            print(temp_lst)
            if temp_lst:
                temp_dict['Gold Purchase'].append(temp_lst)
        except Exception:
            print('GP')

        try:
            c.execute("""
                select item, ntwt, amount
                from SP
                where date=:date
                order by item
            """, {'date': strdate})
            temp_lst = c.fetchall()
            print(temp_lst)
            if temp_lst:
                temp_dict['Silver Purchase'].append(temp_lst)
        except Exception:
            print('SP')

        dte += timedelta(days=1)

    return temp_dict


def Store_Opening(grate, srate, opncash):
    """Persist the daily opening rates and opening cash."""
    c.execute("""
        create table if not exists Opening (
            Sno integer,
            GoldRate integer,
            SilverRate integer,
            OpeningCash integer,
            date text
        )
    """)
    conn.commit()

    c.execute('select max(Sno) from Opening')
    temp_sno = c.fetchone()
    if temp_sno[0] is None:
        temp_sno = 1
    else:
        temp_sno = temp_sno[0] + 1

    c.execute("""
        insert into Opening values (
            :Sno,
            :GoldRate,
            :SilverRate,
            :OpeningCash,
            :date
        )
    """, {
        'Sno': temp_sno,
        'GoldRate': grate,
        'SilverRate': srate,
        'OpeningCash': opncash,
        'date': date.today(),
    })
    conn.commit()


def Get_opn(today):
    """Return the opening cash for the supplied ISO date string."""
    c.execute('select OpeningCash from Opening where date=:date',
              {'date': today})
    temp_opn = c.fetchone()
    if temp_opn is None:
        temp_opn = (0,)
    return temp_opn[0]
