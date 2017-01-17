# -*- coding: utf-8 -*-

import logging
import main
import random
import string
#import psycopg2
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

class User(db.Model, nsql.Model):
	"""
		General users info and user settings
	"""
	__tablename__ = "User"
	
	id = db.Column('user_id',db.Integer , primary_key=True)
	
	username = db.Column('username', db.String(20), unique=True , index=True)
	
	password = db.Column('password' , db.String(100))

	#password_hash = db.Column('password_hash', db.String(128)) #token based auth
	
	email = db.Column('email',db.String(50),unique=True , index=True)

	active = db.Column(db.SmallInteger(), default=0)