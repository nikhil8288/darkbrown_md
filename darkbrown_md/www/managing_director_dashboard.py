import frappe

# Login is required for this page. Guests get redirected to /login.
no_cache = 1


def get_context(context):
    # 1. Must be logged in.
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login?redirect-to=/managing_director_dashboard"
        raise frappe.Redirect

    # 2. Must hold the Managing Director role (or be System Manager/Administrator).
    roles = frappe.get_roles(frappe.session.user)
    allowed = {"Managing Director", "System Manager", "Administrator"}
    if not allowed.intersection(roles):
        frappe.throw(
            "You do not have access to the Managing Director Dashboard.",
            frappe.PermissionError,
        )

    # 3. Values the template can render server-side.
    context.no_cache = 1
    context.full_name = frappe.utils.get_fullname(frappe.session.user)
    context.company = frappe.defaults.get_defaults().get("company") or "DarkBrown RealEstate"
    context.currency = "QAR"

    return context
