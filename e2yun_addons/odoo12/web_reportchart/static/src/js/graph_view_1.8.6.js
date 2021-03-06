odoo.define('web.GraphView_1.8.6', function (require) {
    'use strict';
    var ajax = require('web.ajax');
    var core = require('web.core');
    var Widget = require('web.Widget');
    var qweb = core.qweb;
    var _t = core._t;
    var GraphView = require('web.GraphView');


    GraphView.include({
        jsLibs: [
            '/web/static/lib/nvd3/d3.v3.js',
            '/web_reportchart/static/lib/nvd3/nv.d3.js',
            '/web/static/src/js/libs/nvd3.js',
             '/web_reportchart/static/lib/echart/echarts.js'
        ],
        init: function (viewInfo, params) {
            this._super.apply(this, arguments);
            var self = this;
        },
        willStart: function () {
            var self = this;
            return $.when(this._super.apply(this, arguments));
        },
        start: function () {
            var self = this;
            return this._super.apply(this, arguments);
        },


    });
});
