/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

class VendorDashboard extends Component {
    setup() {
        this.state = useState({
            loading: true,
            total_products: 0,
            approved_products: 0,
            ongoing_orders: 0,
            completed_orders: 0,
            cancelled_orders: 0,
            total_orders: 0,
            subscription: {}, // full dictionary now
        });

        this.actionService = this.env.services.action;

        onWillStart(async () => {
            const data = await rpc("/vendor/dashboard/data");
            Object.assign(this.state, data, { loading: false });
        });
    }

    openMyProducts() {
        this.openAction("ad_vendor_dashboard.action_vendor_my_products");
    }
    openApprovedProducts() {
        this.openAction("ad_vendor_dashboard.action_vendor_approved_products");
    }
    openTotalOrders(){
        this.openAction("ad_vendor_dashboard.action_vendor_my_orders");
    }
    openOngoingOrders() {
        this.openAction("ad_vendor_dashboard.action_vendor_ongoing_orders");
    }
    openCompletedOrders() {
        this.openAction("ad_vendor_dashboard.action_vendor_completed_orders");
    }
    openCancelledOrders() {
        this.openAction("ad_vendor_dashboard.action_vendor_cancelled_orders");
    }

    async openAction(action_xml_id) {
        try {
            await this.actionService.doAction(action_xml_id);
        } catch (err) {
            console.warn("Action not found:", action_xml_id, err);
        }
    }
}

VendorDashboard.template = "ad_vendor_dashboard.MainTemplate";
registry.category("actions").add("ad_vendor_dashboard.client_action", VendorDashboard);
