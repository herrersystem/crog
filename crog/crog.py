from __future__ import absolute_import
from __future__ import print_function
import os


class Crog:
	CRONJOB_DIR = '/etc/cron.d/'
	LOG_FILE = '/var/log/crop.log'

	def __init__(self, name, minute, hour, month='*', week_day='*', 
		month_day='*'):
		
		import sys

		self.name = name
		self.minute = str(minute)
		self.hour = str(hour)
		self.month = str(month)
		self.week_day = str(week_day)
		self.month_day = str(month_day)
		self.user = 'root'
		self.pathscript = os.path.abspath(sys.argv[0])
		self.log = False


	def get_cronjobs(self, params):
		base = '{} {} {} {} {} {} {}'.format(
			self.minute,
			self.hour,
			self.month_day,
			self.month,
			self.week_day,
			self.user,
			self.pathscript
		)
		path = self.CRONJOB_DIR + self.name
		cronjobs = ''
		
		if params:
			for ps in params:
				cronjob = base

				for p in ps:
					cronjob += ' ' + str(p)
				cronjobs += cronjob + '\n'
		else:
			cronjobs = base + '\n'

		return cronjobs


	def check_exist(self, params):
		import hashlib

		exist = False
		path = self.CRONJOB_DIR + self.name

		if os.path.isfile(path):
			cronjobs = self.get_cronjobs(params).encode()
			current_cronjobs_hash = b''

			with open(path, 'rb') as f:
				content = b''

				for line in f:
					content += line

				current_cronjobs_hash = hashlib.md5(content).hexdigest()
			cronjobs_hash = hashlib.md5(cronjobs).hexdigest()

			if cronjobs_hash == current_cronjobs_hash:
				exist = True

		return exist


	def create(self, params):
		cronjobs = self.get_cronjobs(params)
		path = self.CRONJOB_DIR + self.name

		with open(path, 'w') as f:
			f.write(cronjobs)
		
		print('[crop] config file %s was created.' % self.name)
		print(cronjobs)


	def logging(self, response):
		from datetime import datetime

		with open(self.LOG_FILE, 'w') as f:
			f.write('{} executed at {} with response : {}'.format(
				self.name,
				datetime.now(),
				response
			))


	def load(self, params=[]):
		def decorator(func):
			def wrapper(*args, **kwargs):

				if self.check_exist(params):
					response = func(*args, **kwargs)
					if self.log:
						self.logging(response)
				else:
					self.create(params)

			return wrapper
		return decorator

