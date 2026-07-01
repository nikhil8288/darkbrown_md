import frappe


def set_md_home(login_manager):
    """After login, send Managing Director users straight to the MD dashboard.
    Skips admins/system managers so they still land on Desk for setup work.
    """
    user = login_manager.user
    roles = set(frappe.get_roles(user))

    if "Managing Director" in roles and not (roles & {"System Manager", "Administrator"}):
        frappe.local.response["home_page"] = "/md-dashboard"
