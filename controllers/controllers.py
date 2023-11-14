# -*- coding: utf-8 -*-
# from odoo import http


# class IndexScrumManagement(http.Controller):
#     @http.route('/index_scrum_management/index_scrum_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/index_scrum_management/index_scrum_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('index_scrum_management.listing', {
#             'root': '/index_scrum_management/index_scrum_management',
#             'objects': http.request.env['index_scrum_management.index_scrum_management'].search([]),
#         })

#     @http.route('/index_scrum_management/index_scrum_management/objects/<model("index_scrum_management.index_scrum_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('index_scrum_management.object', {
#             'object': obj
#         })
