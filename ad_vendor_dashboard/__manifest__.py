# -*- coding: utf-8 -*-
{
    "name": "Vendor Dashboard",
    "version": "18.0.1.0",
    "summary": "Dashboard interface for vendors to track products, orders, and performance.",
    "description": "Provides a base structure for the vendor dashboard module.",
    "author": "ADream Innovations",
    'website': 'https://adreaminnovations.odoo.com',
    "license": "LGPL-3",
    "category": "Sales/Vendor Management",
    "depends": [
        "web",
        "portal",
        "website",
        "sale",
        "stock",
        "ad_vendor_management",
        "ad_vendor_portal",
        "purchase",
    ],
    "data": [
        "views/menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "ad_vendor_dashboard/static/src/js/vendor_dashboard.js",
            "ad_vendor_dashboard/static/src/xml/vendor_dashboard.xml",
            "ad_vendor_dashboard/static/src/css/vendor_dashboard.css",
        ]
    },
    "application": False,
    "installable": True,
    "auto_install": False,
    'images': ['static/description/banner.png']
}
