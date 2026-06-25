app_name = "darkbrown_md"
app_title = "DarkBrown MD Dashboard"
app_publisher = "DarkBrown Real Estate"
app_description = "Managing Director monitoring dashboard for DarkBrown Real Estate"
app_email = "admin@darkbrown.qa"
app_license = "mit"

# The MD dashboard is a standalone website page served at /md-dashboard.
# It is mobile-first (off the Desk) and gated to the Managing Director role
# in the page controller (www/md-dashboard.py -> get_context).

# Website route rules (optional pretty alias; the file already serves at /md-dashboard)
website_route_rules = [
    {"from_route": "/md-dashboard", "to_route": "md-dashboard"},
]
