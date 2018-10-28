from odoo import models, fields, api

class xml(models.Model):
    _name = 'xml'

    #name = fields.Char()
    #value = fields.Integer()
    #value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()

    #@api.depends('value')
    #def _value_pc(self):
    #    self.value2 = float(self.value) / 100

    rfc_emisor = fields.Text(string="RFC Emisor")
    nombre_emisor = fields.Text(string="Nombre Emisor")
    rfc_receptor = fields.Text(string="RFC Receptor")
    nombre_receptor = fields.Text(string="Nombre Receptor")
    subtotal = fields.Float(string="Subtotal")
    total = fields.Float(string="Total")


