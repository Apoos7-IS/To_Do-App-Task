from odoo import models, fields

class ToDoTask(models.Model):
    _name = "todo.task"
    
    name = fields.Char()
    task_name = fields.Char()
    assign_to_id = fields.Many2one('res.partner')
    description = fields.Char()
    due_date = fields.Date()
    status = fields.Selection([
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("completed", "Completed")
    ], default = 'new')

    