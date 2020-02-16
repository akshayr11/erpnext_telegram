# -*- coding: utf-8 -*-
# Copyright (c) 2020, Youssef Restom and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.desk.doctype.notification_log.notification_log import enqueue_create_notification

class ExtraNotificationLog(Document):
	def after_insert(self):
		self.make_notification_log()


	def make_notification_log(self):
			alert_doc = frappe.get_doc(self.doctype_name,self.doc_name)
			users = [alert_doc.owner, alert_doc.modified_by]
			notification_doc = {
				'type': 'Share',
				'document_type': self.doctype_name,
				'subject': self.subject,
				'document_name': self.doc_name,
				'from_user': frappe.session.user
			}
			
			enqueue_create_notification(users, notification_doc)
	