from odoo import models, fields, api

class TestModel(models.Model):
    _name = 'test.model'
    _description = "Test Model"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    number = fields.Integer(string="Number")
    created_date = fields.Date(string="Created Date")
    created_time = fields.Datetime(string="Created Time")
    float_no = fields.Float(string="Float Number")
    document = fields.Binary(string="Binary")
    true = fields.Boolean(string="True?")
    yes_no = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Yes or No')
    false = fields.Boolean(string="False?")

    document_creator = fields.Many2one("res.partner", "Создатель документа", default=lambda self: self.env.user.id, required = True)
    responsible_partner_id = fields.Many2one("res.partner", "Ответственный")
    clients = fields.One2many("test.model.line", "test_model_id", string="Clients")

    option_one =fields.Boolean(string="Опция 1")
    option_two =fields.Boolean(string="Опция 2")
    select_all =fields.Boolean(string="Выбрать все")

    @api.onchange("option_one", "option_two")
    def onchange_state(self):
        if self.option_one and self.option_two:
            self.select_all = True
        else:
            self.select_all = False 

    @api.onchange("select_all")
    def onchange_select_all(self):
        if self.select_all:
            self.option_one = True
            self.option_two = True
        else:
            self.option_one = False
            self.option_two = False
    
    def open_wizard(self):
        wizard = self.env["test.model.create.partner"].create({"test": self.id})
        return {
            "name": "Wizard",
            "type": "ir.actions.act_window",
            "res_model": "test.model.create.partner",
            "res_id": wizard.id,
            "view_mode": "form",
            "target": "new",
        }
        

class TestModelLine(models.Model):
    _name = "test.model.line"

    test_model_id = fields.Many2one("test.model", "Test Model")
    partner_id = fields.Many2one("res.partner", "Partner")
    email = fields.Char(related="partner_id.email", string="Email")
