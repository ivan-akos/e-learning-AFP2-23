import os
import glob
import importlib
import traceback
from selenium import webdriver
from exceptions import TestFailure
import config

driver = webdriver.Chrome(executable_path=config.CHROME_BINARY_PATH)
driver.get(config.TARGET_URL)

for t in glob.glob(os.path.dirname(__file__) + '/' + 'test*'):
	t = os.path.basename(t).rsplit(".", 1)[0]
	print('Running ', t, ': ', end='', sep='')
	m = importlib.import_module(t)
	try:
		m.main(driver)
		print('success.', sep='')
	except Exception as e:
		print('failure.', end='', sep='')
		print(traceback.format_exc())
