"""Generate daily summary Word documents (and optionally convert them to PDF)."""

import os
from datetime import date, timedelta

from docx import Document
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn

from Common.backend import Get_Billsday, Get_opn

WNS_COLS_NUM = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}num'


def set_number_of_columns(section, cols):
    """Set the number of columns for a section using XML."""
    section._sectPr.xpath('./w:cols')[0].set(WNS_COLS_NUM, str(cols))


def del_para(para):
    """Remove a paragraph from its document."""
    p = para._element
    p.getparent().remove(p)
    p._p = None
    p._element = None


def _add_total_row(table, label, ntwt, col):
    """Append a totals row to ``table``."""
    cells = table.add_row().cells
    cells[0].text = label
    cells[col].text = str(ntwt)


def gen_billtoday(today):
    """Generate a Word report for the given ISO date ``today``."""
    from docx2pdf import convert

    db = Get_Billsday(today)
    opn = Get_opn(today)
    print(db)

    doc = Document()
    sec1 = doc.add_section(WD_SECTION.ODD_PAGE)
    set_number_of_columns(sec1, 2)

    doc.add_heading(f'Opening Cash-{opn}', level=2)

    # Section headings and tables are kept as references for totals later.
    headings = {}
    tables = {}

    headings['ss'] = doc.add_heading('Silver Sale', level=2)
    tables['ss'] = doc.add_table(rows=1, cols=4)
    tables['ss'].style = 'Table Grid'
    tables['ss'].rows[0].cells[0].text = 'Amount'
    tables['ss'].rows[0].cells[1].text = 'Item'
    tables['ss'].rows[0].cells[2].text = 'Gr Wt'
    tables['ss'].rows[0].cells[3].text = 'Nt Wt'

    headings['shp'] = doc.add_heading('Misc/Shree Aaya', level=2)
    tables['shp'] = doc.add_table(rows=1, cols=2)
    tables['shp'].style = 'Table Grid'
    tables['shp'].rows[0].cells[0].text = 'Amount'
    tables['shp'].rows[0].cells[1].text = 'Type'

    headings['oo'] = doc.add_heading('Old Order', level=2)
    tables['oo'] = doc.add_table(rows=1, cols=5)
    tables['oo'].style = 'Table Grid'
    tables['oo'].rows[0].cells[0].text = 'Amount'
    tables['oo'].rows[0].cells[1].text = 'Cust Name'
    tables['oo'].rows[0].cells[2].text = 'Item'
    tables['oo'].rows[0].cells[3].text = 'Gr Wt'
    tables['oo'].rows[0].cells[4].text = 'Nt Wt'

    headings['gs'] = doc.add_heading('Gold Sale', level=2)
    tables['gs'] = doc.add_table(rows=1, cols=5)
    tables['gs'].style = 'Table Grid'
    tables['gs'].rows[0].cells[0].text = 'Item'
    tables['gs'].rows[0].cells[1].text = 'Gr Wt'
    tables['gs'].rows[0].cells[2].text = 'Nt Wt'
    tables['gs'].rows[0].cells[3].text = 'Name'
    tables['gs'].rows[0].cells[4].text = 'Amount'

    headings['no'] = doc.add_heading('New Order', level=2)
    tables['no'] = doc.add_table(rows=1, cols=6)
    tables['no'].style = 'Table Grid'
    tables['no'].rows[0].cells[0].text = 'Est Amt'
    tables['no'].rows[0].cells[1].text = 'Adv'
    tables['no'].rows[0].cells[2].text = 'Name'
    tables['no'].rows[0].cells[3].text = 'Item'
    tables['no'].rows[0].cells[4].text = 'Gr Wt'
    tables['no'].rows[0].cells[5].text = 'Nt Wt'

    headings['vc'] = doc.add_heading('VC', level=2)
    tables['vc'] = doc.add_table(rows=1, cols=5)
    tables['vc'].style = 'Table Grid'
    tables['vc'].rows[0].cells[0].text = 'Amount'
    tables['vc'].rows[0].cells[1].text = 'Name'
    tables['vc'].rows[0].cells[2].text = 'Item'
    tables['vc'].rows[0].cells[3].text = 'Gr Wt'
    tables['vc'].rows[0].cells[4].text = 'Nt Wt'

    doc.add_section(WD_SECTION.NEW_COLUMN)

    headings['sp'] = doc.add_heading('Silver Purchase', level=2)
    tables['sp'] = doc.add_table(rows=1, cols=4)
    tables['sp'].style = 'Table Grid'
    tables['sp'].rows[0].cells[0].text = 'Amount'
    tables['sp'].rows[0].cells[1].text = 'Item'
    tables['sp'].rows[0].cells[2].text = 'Gr Wt'
    tables['sp'].rows[0].cells[3].text = 'Nt Wt'

    headings['shm'] = doc.add_heading('Misc/Shree Gaya', level=2)
    tables['shm'] = doc.add_table(rows=1, cols=2)
    tables['shm'].style = 'Table Grid'
    tables['shm'].rows[0].cells[0].text = 'Amount'
    tables['shm'].rows[0].cells[1].text = 'Type'

    headings['be'] = doc.add_heading('Bank Entries', level=2)
    tables['be'] = doc.add_table(rows=1, cols=3)
    tables['be'].style = 'Table Grid'
    tables['be'].rows[0].cells[0].text = 'Amount'
    tables['be'].rows[0].cells[1].text = 'Type'
    tables['be'].rows[0].cells[2].text = 'Name'

    headings['ex'] = doc.add_heading('Expenses', level=2)
    tables['ex'] = doc.add_table(rows=1, cols=2)
    tables['ex'].style = 'Table Grid'
    tables['ex'].rows[0].cells[0].text = 'Amount'
    tables['ex'].rows[0].cells[1].text = 'Type'

    headings['gp'] = doc.add_heading('Gold Purchase', level=2)
    tables['gp'] = doc.add_table(rows=1, cols=5)
    tables['gp'].style = 'Table Grid'
    tables['gp'].rows[0].cells[0].text = 'Item'
    tables['gp'].rows[0].cells[1].text = 'Gr Wt'
    tables['gp'].rows[0].cells[2].text = 'Nt Wt'
    tables['gp'].rows[0].cells[3].text = 'Name'
    tables['gp'].rows[0].cells[4].text = 'Amount'

    doc.add_heading('Closing Cash', level=2)

    totals = {
        'gs': 0, 'ss': 0, 'oo': 0, 'no': 0, 'vc': 0,
        'gp': 0, 'sp': 0, 'shp': 0, 'shm': 0, 'ex': 0,
    }
    ntwt = {'gs': 0, 'ss': 0, 'gp': 0, 'sp': 0}

    for row in db:
        print(row)
        trans_type = row[10]

        if trans_type == 'Gold Sale':
            r = tables['gs'].add_row().cells
            r[0].text = str(row[3])
            r[1].text = str(row[6])
            r[2].text = str(row[7])
            r[3].text = str(row[0])
            r[4].text = str(row[11])
            totals['gs'] += row[11]
            ntwt['gs'] += row[7]

        elif trans_type == 'Silver Sale':
            r = tables['ss'].add_row().cells
            r[0].text = str(row[11])
            r[1].text = str(row[3])
            r[2].text = str(row[6])
            r[3].text = str(row[7])
            totals['ss'] += row[11]
            ntwt['ss'] += row[7]

        elif trans_type == 'Old Order':
            r = tables['oo'].add_row().cells
            r[0].text = str(row[11])
            r[1].text = str(row[0])
            r[2].text = str(row[3])
            r[3].text = str(row[6])
            r[4].text = str(row[7])
            totals['oo'] += row[11]

        elif trans_type == 'New Order':
            r = tables['no'].add_row().cells
            r[0].text = str(row[4])
            r[1].text = str(row[11])
            r[2].text = str(row[0])
            r[3].text = str(row[3])
            r[4].text = str(row[6])
            r[5].text = str(row[7])
            totals['no'] += row[11]

        elif trans_type == 'VC':
            r = tables['vc'].add_row().cells
            r[0].text = str(row[11])
            r[1].text = str(row[0])
            r[2].text = str(row[3])
            r[3].text = str(row[6])
            r[4].text = str(row[7])
            totals['vc'] += row[11]

        elif trans_type == 'Gold Purchase':
            r = tables['gp'].add_row().cells
            r[0].text = str(row[3])
            r[1].text = str(row[6])
            r[2].text = str(row[7])
            r[3].text = str(row[0])
            r[4].text = str(row[11])
            totals['gp'] += row[11]
            ntwt['gp'] += row[7]

        elif trans_type == 'Silver Purchase':
            r = tables['sp'].add_row().cells
            r[0].text = str(row[11])
            r[1].text = str(row[3])
            r[2].text = str(row[6])
            r[3].text = str(row[7])
            totals['sp'] += row[11]
            ntwt['sp'] += row[7]

        elif trans_type == 'Misc Plus':
            r = tables['shp'].add_row().cells
            r[0].text = str(row[11])
            r[1].text = str(row[0])
            totals['shp'] += row[11]

        elif trans_type == 'Misc Minus':
            r = tables['shm'].add_row().cells
            r[0].text = str(row[11])
            r[1].text = str(row[0])
            totals['shm'] += row[11]

        elif trans_type == 'Expense':
            r = tables['ex'].add_row().cells
            r[0].text = str(row[11])
            r[1].text = str(row[0])
            totals['ex'] += row[11]

        # Credit note (debt) goes to Shree Gaya
        if row[19] > 0:
            r = tables['shm'].add_row().cells
            r[0].text = str(row[11])
            r[1].text = f"{row[0]} (CR)"
            totals['shm'] += row[11]

        # Bank entries
        if row[13] != 0:
            r = tables['be'].add_row().cells
            r[0].text = str(row[13])
            r[1].text = str(row[14])
            r[2].text = str(row[0])
        if row[15] != 0:
            r = tables['be'].add_row().cells
            r[0].text = str(row[15])
            r[1].text = str(row[16])
            r[2].text = str(row[0])
        if row[17] != 0:
            r = tables['be'].add_row().cells
            r[0].text = str(row[17])
            r[1].text = f"Chq-{row[18]}"
            r[2].text = str(row[0])

    # Add totals to headings
    headings['gs'].add_run(f' - {totals["gs"]}')
    headings['ss'].add_run(f' - {totals["ss"]}')
    headings['oo'].add_run(f' - {totals["oo"]}')
    headings['no'].add_run(f' - {totals["no"]}')
    headings['vc'].add_run(f' - {totals["vc"]}')
    headings['gp'].add_run(f' - {totals["gp"]}')
    headings['sp'].add_run(f' - {totals["sp"]}')
    headings['shp'].add_run(f' -  {totals["shp"]}')
    headings['shm'].add_run(f' - {totals["shm"]}')
    headings['ex'].add_run(f' - {totals["ex"]}')

    # Total rows for sections with net-weight columns
    _add_total_row(tables['gs'], 'Total', ntwt['gs'], col=2)
    _add_total_row(tables['ss'], 'Total', ntwt['ss'], col=3)
    _add_total_row(tables['gp'], 'Total', ntwt['gp'], col=2)
    _add_total_row(tables['sp'], 'Total', ntwt['sp'], col=3)

    # Remove the blank paragraph inserted by the first section
    del_para(doc.paragraphs[0])

    os.makedirs('pdf', exist_ok=True)
    filename = f'{today}.docx'
    doc.save(filename)
    try:
        convert(filename, f'pdf/{today}.pdf')
    except Exception as exc:
        print(f'doc2pdf conversion failed: {exc}')


def gen_sum(today):
    """Generate a summary report for the date ``today`` (``DD-MM-YYYY``).

    The exact layout has not yet been fully recovered from the bytecode.
    """
    raise NotImplementedError(
        "gen_sum layout is still being reconstructed from the bytecode"
    )
