from odoo import api, models, fields

class TestModelCreatePartner(models.TransientModel):
    _name = "test.model.create.partner"

    name = fields.Char("Имя")
    test = fields.Many2one("test.model")

    def just_create(self):
        partner = self.env["res.partner"].create({"name": self.name})
        self.test.clients.create({"test_model_id": self.test.id, "partner_id": partner.id})
        return {'type': 'ir.actions.act_window_close'}
    
    def create_and_open(self):
        partner = self.env["res.partner"].create({"name": self.name})
        self.test.clients.create({"test_model_id": self.test.id, "partner_id": partner.id})
        return {
            "name": "Партнёр",
            "type": "ir.actions.act_window",
            "res_model": "res.partner",
            "res_id": partner.id,
            "view_mode": "form",
            "target": "current",
        }
