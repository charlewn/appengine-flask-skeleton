from core import db
from datetime import datetime

class Model(object):
	"""
		Model Object created for common functions
	"""

	#sign_in_count = db.Column(db.Integer, nullable=False, default=0)
	#current_sign_in_on = db.Column()
	
	def put(self):
		"""
		Save a model instance.

		:return: Model instance
		"""
		db.session.add(self)
		db.session.commit()

	def delete(self):
		"""
		
		Delete a model instance
		:return db.session.commit()'s result

		"""
		db.session.delete(self)
		db.session.commit()

class FileModel(object):
	
	def put(self):
		"""
		Save a model instance.

		:return: Model instance
		"""
		db.session.add(self)
		db.session.commit()

	def delete(self):
		"""
		
		Delete a model instance
		:return db.session.commit()'s result

		"""
		db.session.delete(self)
		db.session.commit()