odoo.define('outbound_report_echarts', function (require) {
    "use strict";
    var core = require('web.core');
    var AbstractAction = require('web.AbstractAction');
    var Widget = require('web.Widget');
    var _t = core._t;

var outbound_report_echarts = AbstractAction.extend({
    template: 'outbound_report_template',
    init: function(parent, action){
        this._super(parent, action);
        this.url = action.params.url;
    },
    get_outbound_div_dom:function(){
        var els = this.$el;
        var outbound_div_dom = '';
        for(var i = 0;i<els.length;i++){
            if(els[i]['id'] == 'outbound_div'){
                outbound_div_dom = els[i];
                break;
            }
        }
        return outbound_div_dom;
    },
    start: function(){
        var self = this;
        // var chartdiv = document.createElement('div');
        // chartdiv.style= "width: 600px;height:500px;";
        // chartdiv.id= 'echarts_funnel_div';
        //
        // $('.o_content')[0].appendChild(chartdiv);
        //debugger;


        //查询行数据，加载行
        this._rpc({
//        model: 'outbound.final',
        model: 'res.partner',
//        method: 'get_outbound_report_data',
        method: 'get_customer_loss_data',
        //args: [query]
        })
        .then(function(datas){
            if(datas){
                var outbound_div_dom = self.get_outbound_div_dom();
                var myChart = echarts.init(outbound_div_dom);
                var option = {
                    title: {
                        text: '出库报表',
                        //subtext: '漏斗视图'
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    toolbox: {
                        feature: {
                            //dataView: {readOnly: false},
                            //restore: {},
                            saveAsImage: {}
                        }
                    },
                    legend: {
//                        data: datas
                        top:20,
                        data: ['潜在客户','意向客户','准客户','成交客户']
                    },
                    calculable: true,
                    series: [
                        {
                            name:'',
                            type:'funnel',
                            left: '6%',
                            top: 70,
                            //x2: 80,
                            bottom: 60,
                            width: '80%',
                            // height: {totalHeight} - y - y2,
                            min: 0,
                            max: 100,
                            minSize: '10%',
                            maxSize: '90%',
                            sort: 'descending',
                            gap: 10,
                            color:['#e28282','#dadc5e','#61d26f','#5094b5'],
                            // label: {
                            //     show: true,
                            //     position: 'inside'
                            // },
                            labelLine: {
                                length: 40,
                                lineStyle: {
                                    width: 1,
                                    type: 'solid'
                                }
                            },
                            itemStyle: {
                                normal: {
                                    borderColor: '#fff',        //每一块的边框颜色
                                    borderWidth: 0,             //每一块边框的宽度
                                    shadowBlur: 30,             //整个外面的阴影厚度
                                    shadowOffsetX: 0,
                                    shadowOffsetY: 30,          //每一块的x轴的阴影
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'    //阴影颜色
                                }

                                // borderColor: '#fff',
                                // borderWidth: 1
                            },
                            emphasis: {
                                label: {
                                    fontSize: 20
                                }
                            },
                            data: datas
                            //     [
                            //     {value: 60, name: '访问'},
                            //     {value: 40, name: '咨询'},
                            //     {value: 20, name: '订单'},
                            //     {value: 80, name: '点击'},
                            //     {value: 100, name: '展现'}
                            // ]
                        }
                    ]
                };
                myChart.setOption(option);
            }

        });





    },
    destroy: function () {
        // var funnel_div = document.getElementById("echarts_funnel_div");
        // if(funnel_div){
        //     funnel_div.remove();
        // }
    }
});

core.action_registry.add('outbound_report_echarts', outbound_report_echarts);

// return {
//     customer_loss_funnel: customer_loss_funnel,
// };

});