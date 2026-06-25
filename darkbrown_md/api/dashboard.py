"""Whitelisted data methods for the MD dashboard.

STATUS: stubs only. The dashboard currently renders on the static demo data
baked into md-dashboard.html (renderVals()). Next session we replace each
renderVals() array with a frappe.call to one of these methods, keyed by tab
and timeframe.

Every method is read-only and gated to the Managing Director role.

Data-model dependency (LOCKED, see README): these methods assume
  - Sales Invoice per tenant  -> native AR / arrears ageing
  - one Cost Center per building -> native per-building P&L
so per-building margin and arrears come from native ERPNext, not hand-rolled.
"""

import frappe
from frappe import _

_ALLOWED = {"Managing Director", "System Manager", "Administrator"}


def _guard():
    roles = set(frappe.get_roles(frappe.session.user))
    if not (roles & _ALLOWED):
        frappe.throw(_("Not permitted"), frappe.PermissionError)


def _range_for(tf):
    """Return (start, end) dates for a timeframe key.

    tf in {today, month, quarter, year}. Fixed-horizon cards
    (Forward PDC #5, Expiring #8) ignore tf.
    """
    import datetime as _dt

    today = _dt.date.today()
    if tf == "today":
        return today, today
    if tf == "month":
        return today.replace(day=1), today
    if tf == "quarter":
        q_start_month = 3 * ((today.month - 1) // 3) + 1
        return today.replace(month=q_start_month, day=1), today
    if tf == "year":
        return today.replace(month=1, day=1), today
    return today.replace(day=1), today


@frappe.whitelist()
def get_overview(tf="month"):
    _guard()
    # TODO: cards, alerts, per_building, collected_vs_billed, approvals, arrears
    return {"_stub": True, "tf": tf}


@frappe.whitelist()
def get_portfolio(tf="month", view="buildings"):
    _guard()
    # TODO: strip, buildings (+inline units), units flat list
    return {"_stub": True, "tf": tf, "view": view}


@frappe.whitelist()
def get_tenants(tf="month"):
    _guard()
    # TODO: strip, tenant book, agreement health, churn
    return {"_stub": True, "tf": tf}


@frappe.whitelist()
def get_finance(tf="month", sub="pnl"):
    _guard()
    # TODO: pnl / receivables / pdc / payables (+liquidity running position)
    return {"_stub": True, "tf": tf, "sub": sub}


@frappe.whitelist()
def get_maintenance():
    _guard()
    # TODO: kpis, open requests, by-building
    return {"_stub": True}
