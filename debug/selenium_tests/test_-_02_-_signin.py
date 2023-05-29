from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from exceptions import TestFailure
import config

def main(driver):
	# Navigate to sing up
	driver.find_element(By.ID, 'login').click()
	# Enter data
	driver.find_element(By.ID, 'neptun').send_keys(config.LOGIN_NAME)
	driver.find_element(By.ID, 'password').send_keys(config.LOGIN_PASSWORD)
	# Registration attempt
	driver.find_element(By.ID, 'login-submit').click()
	# Test success
	#	the logout button appearing is assumed to be a good enough indicator
	#	the following throws on error
	sleep(0.5)
	driver.find_element(By.ID, 'logout')
