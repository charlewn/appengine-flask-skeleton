# -*- coding: utf-8 -*-

import logging
import main
import random
import string

from datetime import datetime

from google.appengine.ext import ndb


class User(ndb.Model):
	
	username = ndb.StringProperty(required=True)
	
	pic_uri = ndb.BlobProperty()

	password = ndb.StringProperty(required=True)

	email = ndb.StringProperty(required=True)

	created = ndb.DateTimeProperty(auto_now_add=True)

	#administrative
	activated = ndb.BooleanProperty(default=False)

	reset_password = ndb.BooleanProperty(default=False)