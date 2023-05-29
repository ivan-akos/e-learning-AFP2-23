from selenium import webdriver
from selenium.webdriver.common.by import By
from exceptions import TestFailure

def main(driver):
	# Navigate to sing up
	driver.find_element(By.ID, 'login').click()
	# Enter data
	driver.find_element(By.ID, 'neptun').send_keys('seleni')
	driver.find_element(By.ID, 'password').send_keys('selenium')
	# Registration attempt
	driver.find_element(By.ID, 'login-submit').click()
	# Test success
	#	the logout button appearing is assumed to be a good enough indicator
	#	the next line throws on error
	driver.find_element(By.ID, 'logout')
