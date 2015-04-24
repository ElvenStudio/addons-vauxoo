# -*- coding: utf-8 -*-
from openerp.addons.website_sale.controllers.main import website_sale
from openerp.http import request


class website_sale(website_sale):

    def get_attribute_value_ids(self, product):
        cr, uid, context, pool = request.cr, request.uid, request.context,\
            request.registry
        product_obj = pool['product.product']
        res = super(website_sale, self).get_attribute_value_ids(product)
        new_res = []
        for re in res:
            stock_state = product_obj.browse(cr, uid, [re[0]],
                                             context)[0].stock_state
            re.append(int(stock_state))
            new_res.append(re)
        return new_res