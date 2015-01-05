import yaml
import os, sys


class Config:
	def __init__(self):
		conf_path = os.path.join(os.getcwd(), 'config.yaml')
		if os.environ.get('CONFIG_PATH'):
			conf_path = os.environ.get('CONFIG_PATH')

		fd = open(conf_path, 'r')
		config = yaml.load(''.join(fd.readlines()))
		fd.close()

		if os.environ.get('PORT'):
			config['PORT'] = os.environ.get('PORT')
		if os.environ.get('HOST'):
			config['HOST'] = os.environ.get('HOST')
		if os.environ.get('DATABASE_PORT'):
			config['DATABASE']['PORT'] = os.environ.get('DATABASE_PORT')
		if os.environ.get('DATABASE_HOST'):
			config['DATABASE']['HOST'] = os.environ.get('DATABASE_HOST')
		if os.environ.get('DATABASE_DBNAME'):
			config['DATABASE']['DBNAME'] = os.environ.get('DATABASE_DBNAME')
		if os.environ.get('DATABASE_USER'):
			config['DATABASE']['USER'] = os.environ.get('DATABASE_USER')
		if os.environ.get('DATABASE_PASS'):
			config['DATABASE']['PASS'] = os.environ.get('DATABASE_PASS')

		self.config = config

	def __call__(self, key):
		return self.config[key]


config = Config()