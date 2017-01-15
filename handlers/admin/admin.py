import logging


from flask import Blueprint, render_template, request, redirect, make_response

#from models import repo_model
#from models import user_model
#from models import log_model
from handlers.base import Handler


class AdminPage(Handler):
	
	def get(self):
		return self.render("admin/admin-page.html")
