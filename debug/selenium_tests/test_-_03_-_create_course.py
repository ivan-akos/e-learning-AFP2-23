from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from exceptions import TestFailure
import config

depends_on = [
	'test_-_02_-_signin.py'
]

def main(driver):
	# Navigate to course list
	driver.find_element(By.ID, 'courses-redirect').click()
	# Enter data
	driver.find_element(By.ID, 'course-create-title').send_keys('selenium')
	# Creation attempt
	driver.find_element(By.ID, 'course-create-submit').click()
	# Test success
	sleep(0.5)
	driver \
		.find_element(By.ID, 'course-table') \
		.find_element(By.XPATH, '''//*[contains(text(), 'selenium')]''')
