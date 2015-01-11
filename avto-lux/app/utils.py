import os, sys, json
import smtplib
from app.configparser import config

class CollectHandlersException(Exception):
	def __repr__(self, e, list):
		return "{0}, {1}".format(e, list)



def collect_handlers(*args):
	def sort_func():
		pass

	routes  = []
	for item in args:
		routes += item
	routeslist = [(lambda y: y + '/' if not y.endswith('/') else y)(x[0]) for x in routes]
	duplicated = { x for x in routeslist if routeslist.count(x) > 1 }
	if len(duplicated) > 0:
		raise CollectHandlersException("Duplicate routes! {0}".format(duplicated))

	# print("Sorted: {0}".format(sorted(routes, key=sort_func, reverse=False)))
	# return sorted(routes, key=lambda x: x[0], reverse=True)
	return routes


def error_log(error):
	print("An error occured! \n{0}".format(error))
	sys.exit(1)


def get_json_localization():
	print(os.getcwd())
	f = open(os.getcwd() + '/static/client-local.json', 'r')
	jn = json.loads(''.join([line for line in f]))
	f.close()
	return jn


def send_mail(msg=None):
	mailc = config('MAIL')
	to = mailc['MAIN_RECIPIENT']
	gmail_user = mailc['USER']
	gmail_pwd = mailc['PASS']

	smtpserver = smtplib.SMTP(mailc['SMTP_PROVIDER']['HOST'], mailc['SMTP_PROVIDER']['PORT'])
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	header = 'To:' + to + '\n' + 'From: WEBSITE:: avto-lux.ru\n' + 'Subject:testing \n'
	msg = msg or ''
	smtpserver.sendmail(gmail_user, to, msg)
	smtpserver.close()