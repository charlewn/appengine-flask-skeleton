import logging

#handlers/repository
from flask import Blueprint, render_template, request, redirect, make_response


#from models import user_model
#from models import log_model
from handlers.base import Handler

class Support(Handler):
	def get(self):
		return self.render("support.html")

class Index(Handler):
	def get(self):
		return self.render("index.html")