# Source Generated with Decompyle++
# File: fixed/PYZ-00.pyz_extracted/Common/Frontendlogic.pyc (Python 3.9)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from Common.Backend import Bill_store, Get_delBills, Get_specificbills, del_billnum, Get_Sale_store
from Common.Transaction import GoldSell, SilverSell, OldOrder, Bill, VC, NO, purchase
from datetime import date
from Common.URDdialog import Ui_Dialog
from Common.createdocx import gen_billtoday, gen_sum
from Common.OpeningBackend import Opening
from Common.CCCalcBackend import CCCalc
from Common.MakingCalcBackend import Making

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self = None):
        super(MainWindow, self).__init__()
        loadUi('Common\\Frontend.ui', self)
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.opening = QtWidgets.QDialog()
        self.opnui = Opening()
        None((lambda : self.ClosingCash()))
        None((lambda : self.MakingCalc()))
        self.OnlyInt = QtGui.QIntValidator()
        None((lambda : self.Switch_Widgets()))
        self.nextlist = { }
        self.pagenum = 0
        self.golditemnames = QtWidgets.QCompleter([
            'ERG',
            'NCK',
            'CHK',
            'SMS',
            'MS',
            'PDT',
            'BNG',
            'GBR',
            'LBR',
            'LR',
            'GR',
            'CH',
            'LKT',
            'GB',
            'BBR',
            'BR',
            'BCH',
            'TIKA',
            'FERWA'])
        self.Gold_itemname.setCompleter(self.golditemnames)
        self.Gold_itemname_2.setCompleter(self.golditemnames)
        self.Gold_itemname_3.setCompleter(self.golditemnames)
        self.Gold_itemname_4.setCompleter(self.golditemnames)
        self.Gold_itemname_5.setCompleter(self.golditemnames)
        self.GP_Itemname.setCompleter(self.golditemnames)
        self.GP_Itemname_2.setCompleter(self.golditemnames)
        self.GP_Itemname_3.setCompleter(self.golditemnames)
        self.GP_Itemname_4.setCompleter(self.golditemnames)
        self.GP_Itemname_5.setCompleter(self.golditemnames)
        self.silveritemnames = QtWidgets.QCompleter([
            'PAYAL',
            'FERWA',
            'THALI',
            'BRACELET',
            'RINGS'])
        self.Silver_itemname.setCompleter(self.silveritemnames)
        self.Silver_itemname_2.setCompleter(self.silveritemnames)
        self.Silver_itemname_3.setCompleter(self.silveritemnames)
        self.Silver_itemname_4.setCompleter(self.silveritemnames)
        self.Silver_itemname_5.setCompleter(self.silveritemnames)
        self.SP_Itemname.setCompleter(self.silveritemnames)
        self.SP_Itemname_2.setCompleter(self.silveritemnames)
        self.SP_Itemname_3.setCompleter(self.silveritemnames)
        self.SP_Itemname_4.setCompleter(self.silveritemnames)
        self.SP_Itemname_5.setCompleter(self.silveritemnames)
        OOcomp = QtWidgets.QCompleter([
            'ERG',
            'NCK',
            'CHK',
            'SMS',
            'MS',
            'PDT',
            'BNG',
            'GBR',
            'LBR',
            'LR',
            'GR',
            'CH',
            'LKT',
            'GB',
            'BBR',
            'BR',
            'BCH',
            'TIKA',
            'PAYAL',
            'FERWA',
            'THALI',
            'BRACELET',
            'RINGS'])
        self.Old_Order_Itemname.setCompleter(OOcomp)
        self.Old_Order_Itemname_2.setCompleter(OOcomp)
        self.Old_Order_Itemname_3.setCompleter(OOcomp)
        self.Old_Order_Itemname_4.setCompleter(OOcomp)
        self.Old_Order_Itemname_5.setCompleter(OOcomp)
        self.New_Order_Itemname.setCompleter(OOcomp)
        self.New_Order_Itemname_2.setCompleter(OOcomp)
        self.New_Order_Itemname_3.setCompleter(OOcomp)
        self.New_Order_Itemname_4.setCompleter(OOcomp)
        self.New_Order_Itemname_5.setCompleter(OOcomp)
        self.VC_Itemname.setCompleter(OOcomp)
        self.VC_Itemname_2.setCompleter(OOcomp)
        self.VC_Itemname_3.setCompleter(OOcomp)
        self.VC_Itemname_4.setCompleter(OOcomp)
        self.VC_Itemname_5.setCompleter(OOcomp)
        self.URDitemname.setCompleter(OOcomp)
        self.URDitemname_2.setCompleter(OOcomp)
        self.URDitemname_3.setCompleter(OOcomp)
        self.URDitemname_4.setCompleter(OOcomp)
        self.URDitemname_5.setCompleter(OOcomp)
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 150)
        None((lambda : self.GoldNext()))
        None((lambda : self.SilverNext()))
        None((lambda : self.OONext()))
        None((lambda : self.VC_Next()))
        None((lambda : self.GP_Next()))
        None((lambda : self.SP_Next()))
        None((lambda : self.GoldPrevious()))
        None((lambda : self.SilverPrevious()))
        None((lambda : self.OOPrevious()))
        None((lambda : self.VC_Previous()))
        None((lambda : self.GP_Previous()))
        None((lambda : self.SP_Previous()))
        None((lambda : self.GoldSell_withmessage()))
        None((lambda : self.SilverSell_withmessage()))
        None((lambda : self.Old_Order_submit()))
        None((lambda : self.New_Order_submit()))
        None((lambda : self.Shree_submit()))
        None((lambda : self.VC_submit()))
        None((lambda : self.GP_submit()))
        None((lambda : self.SP_submit()))
        None((lambda : self.Expense_submit()))
        None((lambda : self.del_search()))
        None((lambda : self.del_entry()))
        self.DocDate.setInputMask('99-99-9999')
        self.DocDate.setText(date.today().strftime('%d-%m-%Y'))
        self.DocSummary.setInputMask('99-99-9999')
        self.DocSummary.setText(date.today().strftime('%d-%m-%Y'))
        None((lambda : self.Doc_gen()))
        self.SumStartdate.setInputMask('99-99-9999')
        self.SumStartdate.setText(date.today().strftime('%d-%m-%Y'))
        self.SumEnddate.setInputMask('99-99-9999')
        self.SumEnddate.setText(date.today().strftime('%d-%m-%Y'))
        self.Summarytree.setColumnCount(2)
        None((lambda : self.Summary_show()))
        None((lambda : self.Gold_ntwt.setValue(self.Gold_grwt.value())))
        None((lambda : self.Gold_ntwt_2.setValue(self.Gold_grwt_2.value())))
        None((lambda : self.Gold_ntwt_3.setValue(self.Gold_grwt_3.value())))
        None((lambda : self.Gold_ntwt_4.setValue(self.Gold_grwt_4.value())))
        None((lambda : self.Gold_ntwt_5.setValue(self.Gold_grwt_5.value())))
        None((lambda : self.Silver_ntwt.setValue(self.Silver_grwt.value())))
        None((lambda : self.Silver_ntwt_2.setValue(self.Silver_grwt_2.value())))
        None((lambda : self.Silver_ntwt_3.setValue(self.Silver_grwt_3.value())))
        None((lambda : self.Silver_ntwt_4.setValue(self.Silver_grwt_4.value())))
        None((lambda : self.Silver_ntwt_5.setValue(self.Silver_grwt_5.value())))
        None((lambda : self.Old_Order_ntwt.setValue(self.Old_Order_grwt.value())))
        None((lambda : self.Old_Order_ntwt_2.setValue(self.Old_Order_grwt_2.value())))
        None((lambda : self.Old_Order_ntwt_3.setValue(self.Old_Order_grwt_3.value())))
        None((lambda : self.Old_Order_ntwt_4.setValue(self.Old_Order_grwt_4.value())))
        None((lambda : self.Old_Order_ntwt_5.setValue(self.Old_Order_grwt_5.value())))
        None((lambda : self.New_Order_ntwt.setValue(self.New_Order_grwt.value())))
        None((lambda : self.New_Order_ntwt_2.setValue(self.New_Order_grwt_2.value())))
        None((lambda : self.New_Order_ntwt_3.setValue(self.New_Order_grwt_3.value())))
        None((lambda : self.New_Order_ntwt_4.setValue(self.New_Order_grwt_4.value())))
        None((lambda : self.New_Order_ntwt_5.setValue(self.New_Order_grwt_5.value())))
        None((lambda : self.VC_ntwt.setValue(self.VC_grwt.value())))
        None((lambda : self.VC_ntwt_2.setValue(self.VC_grwt_2.value())))
        None((lambda : self.VC_ntwt_3.setValue(self.VC_grwt_3.value())))
        None((lambda : self.VC_ntwt_4.setValue(self.VC_grwt_4.value())))
        None((lambda : self.VC_ntwt_5.setValue(self.VC_grwt_5.value())))
        None((lambda : self.GP_ntwt.setValue(self.GP_grwt.value())))
        None((lambda : self.GP_ntwt_2.setValue(self.GP_grwt_2.value())))
        None((lambda : self.GP_ntwt_3.setValue(self.GP_grwt_3.value())))
        None((lambda : self.GP_ntwt_4.setValue(self.GP_grwt_4.value())))
        None((lambda : self.GP_ntwt_5.setValue(self.GP_grwt_5.value())))
        None((lambda : self.SP_ntwt.setValue(self.SP_grwt.value())))
        None((lambda : self.SP_ntwt_2.setValue(self.SP_grwt_2.value())))
        None((lambda : self.SP_ntwt_3.setValue(self.SP_grwt_3.value())))
        None((lambda : self.SP_ntwt_4.setValue(self.SP_grwt_4.value())))
        None((lambda : self.SP_ntwt_5.setValue(self.SP_grwt_5.value())))
        None((lambda : self.Gold_TotalAmount()))
        None((lambda : self.Gold_TotalAmount()))
        None((lambda : self.Gold_TotalAmount()))
        None((lambda : self.Gold_TotalAmount()))
        None((lambda : self.Gold_TotalAmount()))
        None((lambda : self.Silver_TotalAmount()))
        None((lambda : self.Silver_TotalAmount()))
        None((lambda : self.Silver_TotalAmount()))
        None((lambda : self.Silver_TotalAmount()))
        None((lambda : self.Silver_TotalAmount()))
        None((lambda : self.Old_Order_TotalAmount()))
        None((lambda : self.Old_Order_TotalAmount()))
        None((lambda : self.Old_Order_TotalAmount()))
        None((lambda : self.Old_Order_TotalAmount()))
        None((lambda : self.Old_Order_TotalAmount()))
        None((lambda : self.New_Order_TotalAmount()))
        None((lambda : self.New_Order_TotalAmount()))
        None((lambda : self.New_Order_TotalAmount()))
        None((lambda : self.New_Order_TotalAmount()))
        None((lambda : self.New_Order_TotalAmount()))
        None((lambda : self.VC_TotalAmount()))
        None((lambda : self.VC_TotalAmount()))
        None((lambda : self.VC_TotalAmount()))
        None((lambda : self.VC_TotalAmount()))
        None((lambda : self.VC_TotalAmount()))
        None((lambda : self.GP_TotalAmount()))
        None((lambda : self.GP_TotalAmount()))
        None((lambda : self.GP_TotalAmount()))
        None((lambda : self.GP_TotalAmount()))
        None((lambda : self.GP_TotalAmount()))
        None((lambda : self.SP_TotalAmount()))
        None((lambda : self.SP_TotalAmount()))
        None((lambda : self.SP_TotalAmount()))
        None((lambda : self.SP_TotalAmount()))
        None((lambda : self.SP_TotalAmount()))
        self.URD_multiple.clicked.connect(self.URDdialog)
        self.URD_multiple_2.clicked.connect(self.URDdialog)
        self.URD_multiple_3.clicked.connect(self.URDdialog)
        self.URD_multiple_4.clicked.connect(self.URDdialog)
        self.OnlyInt = QtGui.QIntValidator()
        self.Gold_phnumber.setValidator(self.OnlyInt)
        self.Silver_phnumber.setValidator(self.OnlyInt)
        self.Old_Order_phnum.setValidator(self.OnlyInt)
        self.New_Order_phnum.setValidator(self.OnlyInt)
        self.VC_phnum.setValidator(self.OnlyInt)
        self.GP_phnum.setValidator(self.OnlyInt)
        self.SP_phnum.setValidator(self.OnlyInt)
        self.ChequeNo.setValidator(self.OnlyInt)
        self.ChequeNo_2.setValidator(self.OnlyInt)
        self.ChequeNo_3.setValidator(self.OnlyInt)
        self.ChequeNo_4.setValidator(self.OnlyInt)
        self.ChequeNo_5.setValidator(self.OnlyInt)
        self.ChequeNo_6.setValidator(self.OnlyInt)
        self.ChequeNo_7.setValidator(self.OnlyInt)
        self.Del_Bnum.setValidator(self.OnlyInt)
        self.GoldCardgroup = QtWidgets.QButtonGroup()
        self.GoldCardgroup.addButton(self.Gold_Cardmachine)
        self.GoldCardgroup.addButton(self.Gold_Cardmachine_2)
        self.GoldCardgroup.addButton(self.Gold_Cardmachine_3)
        self.GoldCardgroup.addButton(self.Gold_Cardmachine_4)
        self.SilverCardgroup = QtWidgets.QButtonGroup()
        self.SilverCardgroup.addButton(self.Silver_Cardmachine)
        self.SilverCardgroup.addButton(self.Silver_Cardmachine_2)
        self.SilverCardgroup.addButton(self.Silver_Cardmachine_3)
        self.SilverCardgroup.addButton(self.Silver_Cardmachine_4)
        self.OOCardgroup = QtWidgets.QButtonGroup()
        self.OOCardgroup.addButton(self.Old_Order_Cardmachine)
        self.OOCardgroup.addButton(self.Old_Order_Cardmachine_2)
        self.OOCardgroup.addButton(self.Old_Order_Cardmachine_3)
        self.OOCardgroup.addButton(self.Old_Order_Cardmachine_4)
        self.NOCardgroup = QtWidgets.QButtonGroup()
        self.NOCardgroup.addButton(self.New_Order_Cardmachine)
        self.NOCardgroup.addButton(self.New_Order_Cardmachine_2)
        self.NOCardgroup.addButton(self.New_Order_Cardmachine_3)
        self.NOCardgroup.addButton(self.New_Order_Cardmachine_4)
        self.VCCardgroup = QtWidgets.QButtonGroup()
        self.VCCardgroup.addButton(self.VC_Cardmachine)
        self.VCCardgroup.addButton(self.VC_Cardmachine_2)
        self.VCCardgroup.addButton(self.VC_Cardmachine_3)
        self.VCCardgroup.addButton(self.VC_Cardmachine_4)
        self.GoldUPIgroup = QtWidgets.QButtonGroup()
        self.GoldUPIgroup.addButton(self.UPI_BharatPe)
        self.GoldUPIgroup.addButton(self.UPI_GPay)
        self.GoldUPIgroup.addButton(self.UPI_Other)
        self.SilverUPIgroup = QtWidgets.QButtonGroup()
        self.SilverUPIgroup.addButton(self.UPI_BharatPe_2)
        self.SilverUPIgroup.addButton(self.UPI_GPay_2)
        self.SilverUPIgroup.addButton(self.UPI_Other_2)
        self.OOUPIgroup = QtWidgets.QButtonGroup()
        self.OOUPIgroup.addButton(self.UPI_BharatPe_3)
        self.OOUPIgroup.addButton(self.UPI_GPay_3)
        self.OOUPIgroup.addButton(self.UPI_Other_3)
        self.NOUPIgroup = QtWidgets.QButtonGroup()
        self.NOUPIgroup.addButton(self.UPI_BharatPe_4)
        self.NOUPIgroup.addButton(self.UPI_GPay_4)
        self.NOUPIgroup.addButton(self.UPI_Other_4)
        self.VCUPIgroup = QtWidgets.QButtonGroup()
        self.VCUPIgroup.addButton(self.UPI_BharatPe_5)
        self.VCUPIgroup.addButton(self.UPI_GPay_5)
        self.VCUPIgroup.addButton(self.UPI_Other_5)
        self.Shgroup = QtWidgets.QButtonGroup()
        self.Shgroup.addButton(self.Shree_plus)
        self.Shgroup.addButton(self.Shree_minus)
        self.Docgroup = QtWidgets.QButtonGroup()
        self.Docgroup.addButton(self.DocCustom)
        self.Docgroup.addButton(self.DocDaily)
        self.Docgroup.addButton(self.DocSum)
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment()))
        None((lambda : self.update_payment))
        None((lambda : self.update_payment))
        None((lambda : self.update_payment))
        None((lambda : self.update_payment))
        None((lambda : self.URD_ntwt.setValue(self.URD_grwt.value())))
        None((lambda : self.URD_ntwt_2.setValue(self.URD_grwt_2.value())))
        None((lambda : self.URD_ntwt_3.setValue(self.URD_grwt_3.value())))
        None((lambda : self.URD_ntwt_4.setValue(self.URD_grwt_4.value())))
        None((lambda : self.URD_ntwt_5.setValue(self.URD_grwt_5.value())))
        None((lambda : self.connectdialog_withtransfer()))
        None((lambda : self.Old_order_switch()))
        None((lambda : self.VC_switch()))
        self.NO_switch()
        None((lambda : self.NO_switch()))
        self.GP_switch()
        None((lambda : self.GP_switch()))
        None((lambda : self.GP_switch()))
        None((lambda : self.GP_switch()))
        self.SP_switch()
        None((lambda : self.SP_switch()))
        None((lambda : self.SP_switch()))
        None((lambda : self.SP_switch()))
        None((lambda : self.Doc_switch()))
        self.show()

    
    def ClosingCash(self):
        self.ccash = CCCalc()

    
    def MakingCalc(self):
        self.mcalc = Making()

    
    def Doc_gen(self):
        datetime = datetime
        import datetime
        if self.DocStacked.currentIndex() == 1:
            dte = datetime.strptime(self.DocDate.text(), '%d-%m-%Y')
            gen_billtoday(datetime.strftime(dte, '%Y-%m-%d'))
        if self.DocStacked.currentIndex() == 2:
            gen_sum(self.DocSummary.text())

    
    def Summary_show(self):
