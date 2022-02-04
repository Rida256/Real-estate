from odoo import http
from odoo.http import request

class realEstate(http.Controller):

    @http.route('/hello', auth="public")
    def hello(self, **kw):
        return "Hello World"
    
    @http.route('/hello_user', auth="user")
    def hello_user(self, **kw):
        return "Hello %s" %(request.env.user.name)

    @http.route('/hello_world')
    def hello_template(self, **kw):
        return request.render('myestate.hello_world')


    

    @http.route('/hello_template_user')
    def hello_template_user(self, **kw):
        property = request.env['estate.property'].search([('state', '=', 'sold')])
        return request.render('myestate.hello_ritu', { 'name': "ritu", 'property': property })