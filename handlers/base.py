#!/usr/bin/env python
# -*- coding: utf-8 -*-

import jinja2

import os
import logging
import urllib
import json
import time
#from utils import admin_utils

from flask import Blueprint, render_template, request, make_response, redirect
from flask.views import MethodView




class Handler(MethodView):
	
	def __init__(self):
		#logging.error("logging from handler")
		pass

	def get(self):
		logging.info("logging from handler get")

	def get_cookies(self):
		#logging.error(request.cookies.get("username"))
		pass
	
	def render_str(self, template, **params):
		#t = jinja_env.get_template("maintenance.html")
		t = jinja_env.get_template(template)
		return t.render(params)

	def write(self, *args, **kw):
		"""
		write function to the website
		"""
		#self.response.out.write(*args, **kw)
		pass
	def auth_user(self):
		"""
			cookies based auth
		"""
		"""
		user_cookie = request.cookies.get("username")
		user_logged_in = False
		username = ""

		if user_cookie and utils.check_secure_val(user_cookie):
			username = user_cookie.split('|')[0]
			user_logged_in = True

		return username, user_logged_in
		"""
		pass
	
	def render(self, template, **kw):
		#logging.error("template_dir: %s" % template_dir)
		#self.write(self.render_str("maintenance.html", **kw))
		"""
		country= self.request.headers.get('X-AppEngine-Country')
		logging.info("country %s" % self.request.headers.get('Host')[0:9])
		host = self.request.headers.get('Host')
		if country != "US" and host[0:9] != "localhost":
			self.write(country)
		else:
			self.write(self.render_str(template, **kw))
		"""
		#self.write(self.render_str(template, **kw))
		return render_template(template, **kw)


	def render_404(self):
		"""
		user_cookie = request.cookies.get("username")
		user_logged_in = False
		username = ""

		if user_cookie and utils.check_secure_val(user_cookie):
			username = user_cookie.split('|')[0]
			user_logged_in = True
		
		if user_logged_in:
			return render_template("404.html", username=username, user_logged_in=user_logged_in)
		else:
			redirect_to_index = redirect('/login')
			
			response = make_response(redirect_to_index)
			
			return response
		"""
		pass