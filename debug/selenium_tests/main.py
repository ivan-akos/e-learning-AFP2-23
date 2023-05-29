import os
import glob
import importlib
import traceback
from selenium import webdriver
from exceptions import TestFailure
import config

driver = webdriver.Chrome(executable_path=config.CHROME_BINARY_PATH)

for t in glob.glob(os.path.dirname(__file__) + '/' + 'test*'):
	driver.get(config.TARGET_URL)	# Allways reset to index
	t = os.path.basename(t).rsplit(".", 1)[0]
	print('Running ', t, ': ', end='', sep='')
	m = importlib.import_module(t)
	try:
		m.main(driver)
		print('success.')
	except Exception as e:
		print('failure.')
		print(traceback.format_exc())
