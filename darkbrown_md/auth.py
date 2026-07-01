import frappe


def set_md_home(login_manager=None):
    if frappe.session.user == "Administrator":
        return
    if "Managing Director" in frappe.get_roles(frappe.session.user):
        frappe.local.response["home_page"] = "/managing_director_dashboard"
