# Source Generated with Decompyle++
# File: fixed/PYZ-00.pyz_extracted/Common/Backend.pyc (Python 3.9)

from Common.Transaction import purchase
from datetime import date
from time import strptime, time
import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

def Bill_store(obj, lst):
    c.execute('create table if not exists bills (\n            cust_name text,\n            ph_num text,\n            bill_num integer,\n            item_names text,\n            item_id text,\n            purity text,\n            gold_grwt real,\n            gold_ntwt real,\n            silver_grwt real,\n            silver_ntwt real,\n            trans_type text,\n            amount integer,\n            cash integer,\n            card integer,\n            card_machine text,\n            UPI integer,\n            UPI_type text,\n            cheque integer,\n            cheque_num integer,\n            debt integer,\n            URD integer,\n            URD_name text,\n            URD_goldgrwt real,\n            URD_goldntwt real,\n            URD_silvergrwt real,\n            URD_silverntwt real,\n            other integer,\n            othername text,\n            date text)')
    conn.commit()
    temp_bill = Bill_num()
    c.execute('insert into bills values (\n        :cust_name,\n        :ph_num,\n        :bill_num,\n        :items_name,\n        :item_id,\n        :purity,\n        :gold_grwt,\n        :gold_ntwt,\n        :silver_grwt,\n        :silver_ntwt,\n        :trans_type,\n        :amount,\n        :cash,\n        :card,\n        :card_machine,\n        :UPI,\n        :UPI_type,\n        :cheque,\n        :cheque_num,\n        :debt,\n        :URD,\n        :URD_name,\n        :URD_goldgrwt,\n        :URD_goldntwt,\n        :URD_silvergrwt,\n        :URD_silverntwt,\n        :other,\n        :othername,\n        :date)', {
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
        'date': obj.date })
    conn.commit()
    if obj.URD_goldgrwt > 0:
        Sale_store({
            1: purchase('Gold Purchase', obj.URD_name, obj.URD_goldgrwt, obj.URD_goldntwt, obj.URD) }, temp_bill)
    if obj.URD_silvergrwt > 0:
        Sale_store({
            1: purchase('Silver Purchase', obj.URD_name, obj.URD_silvergrwt, obj.URD_silverntwt, obj.URD) }, temp_bill)
    Sale_store(lst, temp_bill)


def Bill_num():
    c.execute('select max(bill_num) from bills\n    ')
    Bill_num = c.fetchone()
    if Bill_num[0] == None:
        return 1
    return None[0] + 1


def Get_Billsday(date):
    c.execute('select * from bills where date=:date', {
        'date': date })
    retval = c.fetchall()
    return retval


def Get_delBills():
    c.execute('select bill_num, cust_name, trans_type, amount, date from bills order by bill_num desc')
    retval = c.fetchall()
    return retval


def Get_specificbills(name, billnum, ttype):
    if ttype == 'Shree plus':
        ttype = 'Misc plus'
    if ttype == 'Shree minus':
        ttype = 'Misc minus'
    if name == '':
        if billnum == '':
            c.execute('select bill_num, cust_name, trans_type,amount, date from bills where trans_type=:ttype order by bill_num desc', {
                'ttype': ttype })
        elif ttype == 'None':
            c.execute('select bill_num, cust_name, trans_type,amount, date from bills where bill_num=:billnum order by bill_num desc', {
                'billnum': billnum })
        else:
            c.execute('select bill_num, cust_name, trans_type,amount, date from bills where trans_type=:ttype, bill_num=:billnum order by bill_num desc', {
                'ttype': ttype,
                'billnum': billnum })
    elif billnum == '':
        if ttype == 'None':
            c.execute('select bill_num, cust_name, trans_type, amount, date from bills where cust_name=:cust_name order by bill_num desc', {
                'cust_name': name })
        else:
            c.execute('select bill_num, cust_name, trans_type, amount, date from bills where cust_name=:cust_name, ttype=:ttype order by bill_num desc', {
                'cust_name': name,
                'ttype': ttype })
    retval = c.fetchall()
    return retval


def del_billnum(billnum):
    c.execute('delete from bills where bill_num=:billnum', {
        'billnum': billnum })
    conn.commit()


def Sale_store(lst, num):
