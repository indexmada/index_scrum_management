# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Project(models.Model):
	_inherit = "project.project"

	to_user_ids = fields.Many2many(comodel_name="res.users", string="Dédié à")

	@api.model
	def create(self, vals):
	    self.clear_caches()
	    return super(Project, self).create(vals)

	def write(self, vals):
	    self.clear_caches()
	    return super(Project, self).write(vals)

class ResUsers(models.Model):
	_inherit = "res.users"

	project_ids = fields.Many2many(comodel_name="project.project", string="Projet", compute="compute_project_ids")

	def compute_project_ids(self):
		for rec in self:
			rec.project_ids = self.env['project.project'].sudo().search([]).filtered(lambda x: rec.id in x.to_user_ids.ids)