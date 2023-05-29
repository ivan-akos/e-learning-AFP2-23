from selenium import webdriver
from selenium.webdriver.common.by import By
from exceptions import TestFailure

def main(driver):
	# Navigate to sing up
	driver.find_element(By.ID, 'signup').click()
	# Save number of success messages currently displayed
	#	assuming there could be a bug (or some strange intended behaviour)
	#	where multiple messages are displayed,
	#	but it is not related what we are testing
	base_success_message_count = len(driver.find_elements(By.CLASS_NAME, 'alert-success'))
	# Enter data
	driver.find_element(By.ID, 'neptun').send_keys('seleni')
	driver.find_element(By.ID, 'first_name').send_keys('selenium')
	driver.find_element(By.ID, 'last_name').send_keys('selenium')
	driver.find_element(By.ID, 'email').send_keys('selenium@noreply.com')
	driver.find_element(By.ID, 'password').send_keys('selenium')
	# Registration attempt
	driver.find_element(By.ID, 'register-submit').click()
	# Test success
	success_message_count = len(driver.find_elements(By.CLASS_NAME, 'alert-success'))
	if success_message_count != base_success_message_count+1:
		raise TestFailure
