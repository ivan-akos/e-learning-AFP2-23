import os
import glob
import importlib
import traceback
from selenium import webdriver
from exceptions import TestFailure, DependencyFailure
import config

driver = webdriver.Chrome(executable_path=config.CHROME_BINARY_PATH)

tests = {
			'test_-_01_-_signup.py' : 0,
			'test_-_02_-_signin.py' : 0,
			'test_-_03_-_create_course.py' : 0,
			'test_-_04_-_delete_course.py' : 0
}

for t in tests:
	tmf = os.path.basename(t).rsplit(".", 1)[0]
	driver.get(config.TARGET_URL)	# Allways reset to index
	print('Running ', tmf, ': ', end='', sep='')
	m = importlib.import_module(tmf)
	try:
		try:
			for i in m.depends_on:
				try:
					if tests[i] != 1:
						raise DependencyFailure
					pass
				except KeyError:
					continue
		except AttributeError:
			pass
	except DependencyFailure:
		tests[t] = 0
		print('skipping.')
		continue
	try:
		m.main(driver)
		tests[t] = 1
		print('success.')
	except Exception as e:
		print('failure.')
		print(traceback.format_exc())

driver.close()
