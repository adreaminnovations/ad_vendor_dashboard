# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from babel.dates import format_date

class VendorDashboardController(http.Controller):

    @http.route('/vendor/dashboard/data', type='json', auth='user')
    def get_vendor_dashboard_data(self):
        user = request.env.user
        partner = user.partner_id

        # Products owned by vendor
        products = request.env['product.template'].sudo().search([('owner_id', '=', user.id)])
        approved_products = products.filtered(lambda p: p.status == 'approved')

        # Purchase Orders linked to vendor
        purchase_orders = request.env['purchase.order'].sudo().search([
            ('partner_id', '=', partner.id)
        ])

        ongoing_orders = purchase_orders.filtered(lambda po: po.state in ('draft', 'sent'))
        completed_orders = purchase_orders.filtered(lambda po: po.state in ('done', 'purchase'))
        cancelled_orders = purchase_orders.filtered(lambda po: po.state == 'cancel')

        # Active subscription (from confirmed sale order)
        subscription = request.env['sale.order'].sudo().search([
            ('partner_id', '=', partner.id),
            ('subscription_status', '=', 'b')
        ], limit=1)

        sub_data = {}
        if subscription:
            sub_data = {
                "name": subscription.name or "",
                "status": subscription.subscription_status or "",
                "recurrence": subscription.recurrance_id.name or "",
                "next_invoice_date": format_date(subscription.next_invoice_date, format="long", locale=request.env.lang) if subscription.next_invoice_date else "",
                "recurr_until": format_date(subscription.recurr_until, format="long", locale=request.env.lang) if subscription.recurr_until else "",
            }

        return {
            "total_products": len(products),
            "approved_products": len(approved_products),
            "ongoing_orders": len(ongoing_orders),
            "completed_orders": len(completed_orders),
            "cancelled_orders": len(cancelled_orders),
            "total_orders": len(purchase_orders),
            "subscription": sub_data,
        }
