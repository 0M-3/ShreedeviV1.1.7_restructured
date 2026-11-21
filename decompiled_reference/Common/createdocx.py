# Source Generated with Decompyle++
# File: fixed/PYZ-00.pyz_extracted/Common/createdocx.pyc (Python 3.9)

from configparser import SectionProxy
from Common.Backend import Get_Billsday, Get_Sale_store, Get_opn
from datetime import date, timedelta
from docx import Document
from docx.oxml.ns import qn
from docx.enum.section import WD_SECTION
dte = date.today()
WNS_COLS_NUM = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}num'

def set_number_of_columns(section, cols):
    ''' sets number of columns through xpath. '''
    section._sectPr.xpath('./w:cols')[0].set(WNS_COLS_NUM, str(cols))


def del_para(para):
    p = para._element
    p.getparent().remove(p)
    p._p = None
    p._element = None


def gen_billtoday(today):
    convert = convert
    import docx2pdf
    import os
    db = Get_Billsday(today)
    opn = Get_opn(today)
    print(db)
    billdoc = Document()
    sec1 = billdoc.add_section(WD_SECTION.ODD_PAGE)
    set_number_of_columns(sec1, 2)
    opening = billdoc.add_heading(f'''Opening Cash-{opn}''', 2, **('level',))
    SSh = billdoc.add_heading('Silver Sale', 2, **('level',))
    SSp = billdoc.add_table(1, 4, **('rows', 'cols'))
    SSp.style = 'TableGrid'
    SSpr = SSp.rows[0].cells
    SSpr[0].text = 'Amount'
    SSpr[1].text = 'Item'
    SSpr[2].text = 'Gr Wt'
    SSpr[3].text = 'Nt Wt'
    SHPh = billdoc.add_heading('Misc/Shree Aaya', 2, **('level',))
    SHPp = billdoc.add_table(1, 2, **('rows', 'cols'))
    SHPp.style = 'TableGrid'
    SHPp.rows[0].cells[0].text = 'Amount'
    SHPp.rows[0].cells[1].text = 'Type'
    OOh = billdoc.add_heading('Old Order', 2, **('level',))
    OOp = billdoc.add_table(1, 5, **('rows', 'cols'))
    OOp.style = 'TableGrid'
    OOp.rows[0].cells[0].text = 'Amount'
    OOp.rows[0].cells[1].text = 'Cust Name'
    OOp.rows[0].cells[2].text = 'Item'
    OOp.rows[0].cells[3].text = 'Gr Wt'
    OOp.rows[0].cells[4].text = 'Nt Wt'
    GSh = billdoc.add_heading('Gold Sale', 2, **('level',))
    GSp = billdoc.add_table(1, 5, **('rows', 'cols'))
    GSp.style = 'TableGrid'
    GSp.rows[0].cells[0].text = 'Item'
    GSp.rows[0].cells[1].text = 'Gr Wt'
    GSp.rows[0].cells[2].text = 'Nt Wt'
    GSp.rows[0].cells[3].text = 'Name'
    GSp.rows[0].cells[4].text = 'Amount'
    NOh = billdoc.add_heading('New Order', 2, **('level',))
    NOp = billdoc.add_table(1, 6, **('rows', 'cols'))
    NOp.style = 'TableGrid'
    NOp.rows[0].cells[0].text = 'Est Amt'
    NOp.rows[0].cells[1].text = 'Adv'
    NOp.rows[0].cells[2].text = 'Name'
    NOp.rows[0].cells[3].text = 'Item'
    NOp.rows[0].cells[4].text = 'Gr Wt'
    NOp.rows[0].cells[5].text = 'Nt Wt'
    VCh = billdoc.add_heading('VC', 2, **('level',))
    VCp = billdoc.add_table(1, 5, **('rows', 'cols'))
    VCp.style = 'TableGrid'
    VCp.rows[0].cells[0].text = 'Amount'
    VCp.rows[0].cells[1].text = 'Name'
    VCp.rows[0].cells[2].text = 'Item'
    VCp.rows[0].cells[3].text = 'Gr Wt'
    VCp.rows[0].cells[4].text = 'Nt Wt'
    section = billdoc.add_section(WD_SECTION.NEW_COLUMN)
    SPh = billdoc.add_heading('Silver Purchase', 2, **('level',))
    SPp = billdoc.add_table(1, 4, **('rows', 'cols'))
    SPp.style = 'TableGrid'
    SPp.rows[0].cells[0].text = 'Amount'
    SPp.rows[0].cells[1].text = 'Item'
    SPp.rows[0].cells[2].text = 'Gr Wt'
    SPp.rows[0].cells[3].text = 'Nt Wt'
    SHMh = billdoc.add_heading('Misc/Shree Gaya', 2, **('level',))
    SHMp = billdoc.add_table(1, 2, **('rows', 'cols'))
    SHMp.style = 'TableGrid'
    SHMp.rows[0].cells[0].text = 'Amount'
    SHMp.rows[0].cells[1].text = 'Type'
    BEh = billdoc.add_heading('Bank Entries', 2, **('level',))
    BEp = billdoc.add_table(1, 3, **('rows', 'cols'))
    BEp.style = 'TableGrid'
    BEp.rows[0].cells[0].text = 'Amount'
    BEp.rows[0].cells[1].text = 'Type'
    BEp.rows[0].cells[2].text = 'Name'
    Exh = billdoc.add_heading('Expenses', 2, **('level',))
    Exp = billdoc.add_table(1, 2, **('rows', 'cols'))
    Exp.style = 'TableGrid'
    Exp.rows[0].cells[0].text = 'Amount'
    Exp.rows[0].cells[1].text = 'Type'
    GPh = billdoc.add_heading('Gold Purchase', 2, **('level',))
    GPp = billdoc.add_table(1, 5, **('rows', 'cols'))
    GPp.style = 'TableGrid'
    GPp.rows[0].cells[0].text = 'Item'
    GPp.rows[0].cells[1].text = 'Gr Wt'
    GPp.rows[0].cells[2].text = 'Nt Wt'
    GPp.rows[0].cells[3].text = 'Name'
    GPp.rows[0].cells[4].text = 'Amount'
    CCh = billdoc.add_heading('Closing Cash', 2, **('level',))
    (GStotal, SStotal, OOtotal, NOtotal, VCtotal, GPtotal, SPtotal, SHPtotal, SHMtotal, EXtotal) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    (SSntwt, GSntwt, GPntwt, SPntwt) = (0, 0, 0, 0)
    for i in db:
        print(i)
        if i[10] == 'Gold Sale':
            GSrow = GSp.add_row().cells
            GSrow[0].text = str(i[3])
            GSrow[1].text = str(i[6])
            GSrow[2].text = str(i[7])
            GSrow[3].text = str(i[0])
            GSrow[4].text = str(i[11])
            GStotal += i[11]
            GSntwt += i[7]
        elif i[10] == 'Silver Sale':
            SSrow = SSp.add_row().cells
            SSrow[0].text = str(i[11])
            SSrow[1].text = str(i[3])
            SSrow[2].text = str(i[6])
            SSrow[3].text = str(i[7])
            SStotal += i[11]
            SSntwt += i[7]
        elif i[10] == 'Old Order':
            OOrow = OOp.add_row().cells
            OOrow[0].text = str(i[11])
            OOrow[1].text = str(i[0])
            OOrow[2].text = str(i[3])
            OOrow[3].text = str(i[6])
            OOrow[4].text = str(i[7])
            OOtotal += i[11]
        elif i[10] == 'New Order':
            NOrow = NOp.add_row().cells
            NOrow[0].text = str(i[4])
            NOrow[1].text = str(i[11])
            NOrow[2].text = str(i[0])
            NOrow[3].text = str(i[3])
            NOrow[4].text = str(i[6])
            NOrow[5].text = str(i[7])
            NOtotal += i[11]
        elif i[10] == 'VC':
            VCrow = VCp.add_row().cells
            VCrow[0].text = str(i[11])
            VCrow[1].text = str(i[0])
            VCrow[2].text = str(i[3])
            VCrow[3].text = str(i[6])
            VCrow[4].text = str(i[7])
            VCtotal += i[11]
        elif i[10] == 'Gold Purchase':
            GProw = GPp.add_row().cells
            GProw[0].text = str(i[3])
            GProw[1].text = str(i[6])
            GProw[2].text = str(i[7])
            GProw[3].text = str(i[0])
            GProw[4].text = str(i[11])
            GPtotal += i[11]
            GPntwt += i[7]
        elif i[10] == 'Silver Purchase':
            SProw = SPp.add_row().cells
            SProw[0].text = str(i[11])
            SProw[1].text = str(i[3])
            SProw[2].text = str(i[6])
            SProw[3].text = str(i[7])
            SPtotal += i[11]
            SPntwt += i[7]
        elif i[10] == 'Misc Plus':
            SHProw = SHPp.add_row().cells
            SHProw[0].text = str(i[11])
            SHProw[1].text = str(i[0])
            SHPtotal += i[11]
        elif i[10] == 'Misc Minus':
            SHMrow = SHMp.add_row().cells
            SHMrow[0].text = str(i[11])
            SHMrow[1].text = str(i[0])
            SHMtotal += i[11]
        elif i[10] == 'Expense':
            Exprow = Exp.add_row().cells
            Exprow[0].text = str(i[11])
            Exprow[1].text = str(i[0])
            EXtotal += i[11]
        if i[19] > 0:
            SHMrow = SHMp.add_row().cells
            SHMrow[0].text = str(i[11])
            SHMrow[1].text = str(i[0] + ' (CR)')
            SHMtotal += i[11]
        if j[13] != 0:
            BEprow = BEp.add_row().cells
            BEprow[0].text = str(j[13])
            BEprow[1].text = str(j[14])
            BEprow[2].text = str(j[0])
        if i[15] != 0:
            BEprow = BEp.add_row().cells
            BEprow[0].text = str(j[15])
            BEprow[1].text = str(j[16])
            BEprow[2].text = str(j[0])
        if i[17] != 0:
            BEprow = BEp.add_row().cells
            BEprow[0].text = str(j[17])
            BEprow[1].text = f'''Chq-{i[18]}'''
            BEprow[2].text = str(j[0])
            continue
            GSh.add_run(f''' - {GStotal}''')
            GSlastline = GSp.add_row().cells
            GSlastline[0].text = 'Total'
            GSlastline[2].text = str(GSntwt)
            SSh.add_run(f''' - {SStotal}''')
            SSlastline = SSp.add_row().cells
            SSlastline[0].text = 'Total'
            SSlastline[3].text = str(SSntwt)
            OOh.add_run(f''' - {OOtotal}''')
            NOh.add_run(f''' - {NOtotal}''')
            VCh.add_run(f''' - {VCtotal}''')
            GPh.add_run(f''' - {GPtotal}''')
            GPlastline = GPp.add_row().cells
            GPlastline[0].text = 'Total'
            GPlastline[2].text = str(GPntwt)
            SPh.add_run(f''' - {SPtotal}''')
            SPlastline = SPp.add_row().cells
            SPlastline[0].text = 'Total'
            SPlastline[3].text = str(SPntwt)
            SHPh.add_run(f''' -  {SHPtotal}''')
            SHMh.add_run(f''' - {SHMtotal}''')
            Exh.add_run(f''' - {EXtotal}''')
            para1 = billdoc.paragraphs[0]
            del_para(para1)
            
            try:
                billdoc.save(f'''{today}.docx''')
            finally:
                pass
            import os
            os.rmdir(f'''{today}.docx''')
            billdoc.save(f'''{today}.docx''')
            
            try:
                convert(f'''{today}.docx''', f'''pdf\\{today}pdf.pdf''')
            finally:
                pass
            print('doc2pdf not working')
            return None




def gen_sum(today):
