# -*- coding: utf-8 -*-

from osv import fields
from osv import osv
from tools.translate import _
import time
import random
from datetime import datetime

class sprint_kanban(osv.osv): 

	def set_done(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state':'done'}, context=context)
		return True
	
	def set_cancel(self, cr, uid, ids, context=None):
		
		self.write(cr, uid, ids, {'state':'cancelled'}, context=context)
		return True

	def set_pending(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state':'pending'}, context=context)
		return True

	def set_open(self, cr, uid, ids, context=None):
		self.write(cr, uid, ids, {'state':'open'}, context=context)
		return True

	
	
	_name = 'sprint.kanban'
	_inherit = ['mail.thread', 'ir.needaction_mixin']
	_columns = {
	            'name': fields.char('Name Sprint',264, required=True),
	            'project_id': fields.many2one('project.project','Project',ondelete="cascade"),
	            'description': fields.text('Description'),
	            'datestart': fields.date('Start Date'),
	            'dateend': fields.date('End Date'),
	            'color': fields.integer('Color Index'),
	            'members': fields.many2many('res.users', 'project_user_rel', 'project_id', 'uid', 'Project Members',states={'close':[('readonly',True)], 'cancelled':[('readonly',True)]}),
				'priority': fields.selection([('4','Very Low'), ('3','Low'), ('2','Medium'), ('1','Important'), ('0','Very important')], 'Priority', select=True),
	            'state': fields.selection([('draft','New'),('open','In Progress'), ('cancelled', 'Cancelled'),('pending','Pending'),('done', 'Done')], 'Status', required=True,),
	            'user_id': fields.many2one('res.users', 'Assigned to'),
	            }
	_defaults = {
        
        'state': 'draft',
        'priority': '1',
     
    }            
   
sprint_kanban()	

class sprint_kanban_tasks(osv.osv):

    _inherit = 'project.task'
    
    _columns={
	 
	    'sprint_id':fields.many2one('sprint.kanban','Sprint',ondelete="cascade"),
	 
		
		
 }
sprint_kanban_tasks()

