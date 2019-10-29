# -*- coding: utf-8 -*-
from odoo import api, fields, models


class OutboundDetail(models.Model):
    _name = 'outbound.detail'
    _description = '出库明细'

    POSID = fields.Char('pos交货单编号')
    VBELN = fields.Char('SAP交货单号')
    BOLNR = fields.Char('提单')
    VKORG = fields.Char('销售组织')
    KUNNR = fields.Char('客户编号')
    KUNAG = fields.Char('售达方')
    VSBED = fields.Char('装运条件')
    LFDAT = fields.Datetime('交货日期')
    WERKS = fields.Char('工厂')
    FHWRK = fields.Char('工厂中的生产资源/工具')
    TRAID = fields.Char('运输方式ID')
    LFART = fields.Char('交货类型')
    LIFSK = fields.Char('交货冻结(抬头)')
    WBSTK = fields.Char('货物移动状态总计')
    salesorderid = fields.Char('销售订单号')
    status = fields.Selection([('A', '新建'), ('B', '准传输'), ('C', '传输')], string='交货单状态')
    delete = fields.Char('删除标记,X为删除')
    # delete属性在pos中为del,与系统名冲突
    remark = fields.Char('抬头文本')
    deltime = fields.Datetime('删除时间')
    deloperator = fields.Char('删除人')
    statustext = fields.Char('状态文本')
    saporderflag = fields.Char('SAP提交状态')
    sapmessage = fields.Char('sap返回信息')
    operatedatetime = fields.Datetime('操作时间')
    creditstatus = fields.Char('交货单信用状态')
    cmgst = fields.Char('信用状态')
    stras = fields.Char('工厂地点')
    creator = fields.Char('创建人')
    createdatetime = fields.Datetime('创建时间')
    createuserid = fields.Char('创建用户ID')
    updateuserid = fields.Char('更新用户ID')
    vipname = fields.Char('客户姓名')
    address = fields.Char('客户地址')
    telephone = fields.Char('接货人电话')
    updater = fields.Char('更新人')
    updatedatetime = fields.Datetime('更新时间')
    yanhuo = fields.Char('是否验货')
    shoufei = fields.Char('收费情况')
    fuwu = fields.Char('服务态度')
    nengli = fields.Char('作业能力')
    beizhu = fields.Char('备注')
    huifangren = fields.Char('回访人')
    yingshoukuan = fields.Char('应收款')
    printcount = fields.Char('')
    printer = fields.Char('打印人')
    wuliushang = fields.Char('物流商')
    wuliushangtext = fields.Char('物流商文本')
    wuliudanhao = fields.Char('物流单号')
    approve = fields.Char('审批')
    subdate = fields.Date('过账时间')
    approvename = fields.Char('审批人')
    approvedate = fields.Date('审批时间')
    freight = fields.Char('是否运费')
    deliveries = fields.Char('是否二次送货')
