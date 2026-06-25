# DarkBrown MD Dashboard (`darkbrown_md`)

Managing Director monitoring dashboard for DarkBrown Real Estate. Mobile-first,
read-only, dark cocoa brand theme. Served as a website page at **`/md-dashboard`**
(off the Desk so it works well on a phone), gated to the **Managing Director** role.

## What's in this app

- `www/md-dashboard.html` — the full branded dashboard (5 tabs: Overview, Portfolio,
  Tenants & Leasing, Finance, Maintenance). Currently renders on **static demo data**
  baked into the page logic (`renderVals()`), so you can see and approve the live UI.
- `www/md-dashboard.py` — server-side guard. Redirects guests to login, throws
  PermissionError for anyone without the Managing Director (or System Manager) role.
- `public/js/support.js` — the dc-runtime that renders the design. Vendored as-is.
- `api/dashboard.py` — whitelisted, role-guarded data methods (stubs). Next step:
  replace each `renderVals()` array with a `frappe.call` to these, keyed by tab + timeframe.

## Install (on your Frappe Cloud private bench `darkbrown-prod`)

```bash
# from the bench directory
bench get-app darkbrown_md /path/to/darkbrown_md      # or push to a git repo and get-app the URL
bench --site darkbown.u.frappe.cloud install-app darkbrown_md
bench --site darkbown.u.frappe.cloud clear-cache
bench build --app darkbrown_md
```

On Frappe Cloud you typically: push this folder to a Git repo, add it to your bench
via the Frappe Cloud dashboard (Apps → Add App → from your repo), then install on the site.

Then visit `https://darkbown.u.frappe.cloud/md-dashboard` while logged in as a user
who has the **Managing Director** role.

## Data-model dependency (LOCKED)

Finance numbers assume the locked accounting model:
- **Sales Invoice per tenant** → native AR / arrears ageing (Current / 1–30 / 31–60 / 60+)
- **one Cost Center per building** → native per-building P&L (gross margin = income − head-lease)

PDC Cheque DocType tracks cheque lifecycle only; money posts via native Payment Entry / GL.
Until that model is in place and reconciled, the Finance tab on real data will be wrong —
which is why this first deploy is the **UI on demo data**.

## Next session

Wire functionality tab by tab: Overview first (exercises most metrics), then Portfolio,
Tenants, Finance sub-views, Maintenance shell. Swap `renderVals()` arrays for `frappe.call`
results from `api/dashboard.py`.
