# Purchase Order Budget Control — Mentor Solution (Odoo 19)

## Setup
Add this directory to `addons_path`, update the apps list, and install `purchase_budget_control`. Depends on `purchase`.

## Functional behavior
- Computed and stored `budget_level`: Low < 5000; Medium from 5000 through 25000 inclusive; High > 25000.
- `requires_manager` is True only for High.
- A non-manager cannot confirm High orders; an empty order cannot be confirmed.
- The standard `button_confirm()` is called with `super()` after validation.
- `get_budget_summary()` returns a dictionary for a **single** record (`ensure_one`).

## Manual test cases
1. Prepare an order with valid lines at totals 4999, 5000, 25000, 25001 (adjust price/taxes to obtain exact total).
2. Verify classification and `requires_manager` at each boundary.
3. Confirm a Medium order as an ordinary user.
4. Attempt to confirm a High order as an ordinary user: expect `UserError`.
5. Confirm the same High order as a user in `purchase.group_purchase_manager`.
6. Attempt to confirm an order without lines: expect `UserError`.
7. Confirm multiple orders via ORM to validate recordset handling.
8. Check `get_budget_summary()` for a single record; multiple records intentionally raise `Expected singleton`.

## Mentor notes
- The manager check represents **role authorization**, not a persistent approval record.
- Amounts are evaluated in each order's currency; no currency conversion is implemented.
- This is a training reference, not a production-ready approval system.
- No `sudo()` is used to bypass security.
- The UI view uses the standard form view ID in Odoo 19; verify against your exact installed build.
