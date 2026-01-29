from odoo import models, api, fields
from datetime import timedelta


class MoreLiveConfigParams(models.AbstractModel):
    _name = "more_live.config.params"
    _description = "More Live Config Params"

    @api.model
    def update_config_params(self):
        icp = self.env["ir.config_parameter"].sudo()

        key = "database.expiration_date"

        today = fields.Date.today()
        new_date = today + timedelta(days=30)  # o los días que quieras

        icp.set_param(key, fields.Date.to_string(new_date))
