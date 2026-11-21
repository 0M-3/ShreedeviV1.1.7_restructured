"""Simple data containers used by PyBookKeeper.

These classes are nothing more than structured records.  They are created in the
UI layer (``Common.frontend_window``) and consumed by ``Common.backend``.
"""


class GoldSell:
    """One gold item sold to a customer."""

    def __init__(self, cust_name, ph_num, pr_name, id, gr_wt, nt_wt, amount,
                 purity, date):
        self.cust_name = cust_name
        self.ph_num = ph_num
        self.pr_name = pr_name
        self.id = id
        self.gr_wt = gr_wt
        self.nt_wt = nt_wt
        self.amount = amount
        self.purity = purity
        self.date = date

    def __repr__(self):
        return (
            f"GoldSell(customer={self.cust_name}, phone={self.ph_num}, "
            f"item={self.pr_name}, id={self.id}, gr_wt={self.gr_wt}, "
            f"nt_wt={self.nt_wt}, amount={self.amount})"
        )


class SilverSell:
    """One silver item sold to a customer."""

    def __init__(self, cust_name, ph_num, pr_name, id, gr_wt, nt_wt, amount,
                 purity, date):
        self.cust_name = cust_name
        self.ph_num = ph_num
        self.pr_name = pr_name
        self.id = id
        self.gr_wt = gr_wt
        self.nt_wt = nt_wt
        self.amount = amount
        self.purity = purity
        self.date = date

    def __repr__(self):
        return (
            f"SilverSell(customer={self.cust_name}, phone={self.ph_num}, "
            f"item={self.pr_name}, id={self.id}, gr_wt={self.gr_wt}, "
            f"nt_wt={self.nt_wt}, amount={self.amount})"
        )


class OldOrder:
    """An old-order exchange transaction (gold/silver)."""

    def __init__(self, type, amount, item, grwt, ntwt):
        self.type = type
        self.amount = amount
        self.item = item
        self.grwt = grwt
        self.ntwt = ntwt


class NO:
    """A new order booking record."""

    def __init__(self, Est, Adv, item, Ggrwt=None, Gntwt=None, Sgrwt=None,
                 Sntwt=None):
        self.Est = Est
        self.Adv = Adv
        self.item = item
        self.Ggrwt = Ggrwt
        self.Gntwt = Gntwt
        self.Sgrwt = Sgrwt
        self.Sntwt = Sntwt


class VC:
    """A valuation/credit note entry."""

    def __init__(self, type, amount, item, grwt, ntwt):
        self.type = type
        self.amount = amount
        self.item = item
        self.grwt = grwt
        self.ntwt = ntwt


class purchase:
    """A purchase (used for scrap/old metal bought by the shop)."""

    def __init__(self, ptype, item=None, grwt=None, ntwt=None, amount=None):
        self.type = ptype
        self.item = item
        self.grwt = grwt
        self.ntwt = ntwt
        self.amount = amount


class Bill:
    """Header record for a complete bill."""

    def __init__(self, cust_name, ph_num, items_name, item_id, purity,
                 gold_grwt, gold_ntwt, silver_grwt, silver_ntwt, trans_type,
                 amount, cash, card, card_machine, UPI, UPI_type, cheque,
                 cheque_num, debt, URD, URD_name, URD_goldgrwt,
                 URD_goldntwt, URD_silvergrwt, URD_silverntwt, other,
                 othername, date):
        self.cust_name = cust_name
        self.ph_num = ph_num
        self.items_name = items_name
        self.item_id = item_id
        self.purity = purity
        self.gold_grwt = gold_grwt
        self.gold_ntwt = gold_ntwt
        self.silver_grwt = silver_grwt
        self.silver_ntwt = silver_ntwt
        self.trans_type = trans_type
        self.amount = amount
        self.cash = cash
        self.card = card
        self.card_machine = card_machine
        self.UPI = UPI
        self.UPI_type = UPI_type
        self.cheque = cheque
        self.cheque_num = cheque_num
        self.debt = debt
        self.URD = URD
        self.URD_name = URD_name
        self.URD_goldgrwt = URD_goldgrwt
        self.URD_goldntwt = URD_goldntwt
        self.URD_silvergrwt = URD_silvergrwt
        self.URD_silverntwt = URD_silverntwt
        self.other = other
        self.othername = othername
        self.date = date

    def __repr__(self):
        return (
            f"Bill(customer={self.cust_name}, phone={self.ph_num}, "
            f"type={self.trans_type}, amount={self.amount})"
        )
