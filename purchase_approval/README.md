## Summary

Implemented a custom Purchase Order Approval workflow for Odoo 19.

## Business Requirements

- Purchase orders above 15,000 require approval.
- Only Purchase Managers can approve or reject requests.
- Approval state and approver information are tracked.
- Previous approval is invalidated after relevant order changes.
- Purchase confirmation is blocked when required approval is missing.

## Implementation

- Extended purchase.order.
- Added approval workflow methods.
- Added approval fields to the purchase order form.
- Added automated tests for approval and security scenarios.

## Testing

- [ ] Approval request flow
- [ ] Purchase Manager authorization
- [ ] Confirmation without approval
- [ ] Approval invalidation after price changes
- [ ] Direct writes to protected fields
- [ ] Boundary value testing
- [ ] Compatibility with standard Odoo purchase approval settings

## Review Notes

The module does not modify Odoo core files.