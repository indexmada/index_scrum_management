# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import json
from odoo.tools import date_utils

class HrAttendance(models.Model):
	_inherit = "hr.attendance"

	recap = fields.Text("Recapitulation Tâches")

	def save_recap_task(self):
		self.employee_id.attendance_manual('hr_attendance.hr_attendance_action_my_attendances')
		return {
			'type': 'ir.actions.client',
			'name': _("Présence"),
			'tag': "hr_attendance_my_attendances",
			'target': "main",
		}

class HrEmployee(models.Model):
	_inherit = "hr.employee"

	def add_task_recap(self, next_action, *args, **kwargs):
		attendance_id = self.env['hr.attendance'].sudo().search([('employee_id', '=', self.id), ('check_out', '=', False), ('check_in', '!=', False)], limit = 1)
		if attendance_id:
			return {
				'action': {
					'type': 'ir.actions.act_window',
					'name': _('Recap. Tâche'),
					'view_mode': 'form',
					'res_model': 'hr.attendance',
					'target': 'new',
					'res_id': attendance_id.id,
					"view_id": self.env.ref('index_scrum_management.recap_form').id,
					"next_action": next_action,
					'views': [(self.env.ref('index_scrum_management.recap_form').id, 'form')],
				}
			}
		else:
			return {
				'warning': 'Désolé, une erreur s\'est produit!'
			}