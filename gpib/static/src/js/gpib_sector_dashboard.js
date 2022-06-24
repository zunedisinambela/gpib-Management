odoo.define('gpib.gpib_sector_dashboard', function (require) {
    "use strict";

    var ActionMixin = require('web.ActionMixin');
    var core = require('web.core');
    var session = require('web.session');
    var ajax = require('web.ajax');
    var rpc = require('web.rpc');
    var ActionManager = require('web.ActionManager');
    var view_registry = require('web.view_registry');
    var web_client = require('web.web_client');
    var Widget = require('web.Widget');

    var QWeb = core.qweb;

    var _t = core._t;
    var _lt = core._lt;
    var map;

    var GpibSectorDashboard = Widget.extend(ActionMixin, {
        hasControlPanel: true,
        template: "SectorDashboardMain",
        events: {
        },
        init: function(parent, context) {
            this._super(parent, context);
        },
        start: function() {
            var self = this;
            self.get_sector_data();
        },
        get_sector_data: function() {
            var self = this;
            rpc.query({
                model: 'gpib.sector',
                method: 'get_data',
                args: []
            })
            .then(function(result){
                self.sectors = result;

                if(result){
                    $('.o_sector_dashboard').html(QWeb.render('SectorDashboardContent', {widget: self}));
                }
                else {
                    $('.o_sector_dashboard').html(QWeb.render('SectorDashboardWarning', {widget: self}));
                    return;
                }
            });
        }
    });

    core.action_registry.add('gpib_gpib_sector_dashboard', GpibSectorDashboard);
    return GpibGpibSectorDashboard;
});