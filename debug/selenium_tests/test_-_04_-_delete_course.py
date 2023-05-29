from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from exceptions import TestFailure
import config

depends_on = [
	'test_-_02_-_signin.py'
]

def main(driver):
	# Navigate to course list
	driver.find_element(By.ID, 'courses-redirect').click()
	# Select the first course belonging to the user
	course = driver \
		.find_element(By.XPATH, "//*[contains(@class, 'course-owner')]/*[text() = '{0}']" \
								.format(config.LOGIN_NAME)) \
		.find_element(By.XPATH, "../..")
	course_code = course.find_element(By.CLASS_NAME, "course-code")
	course = course.find_element(By.CLASS_NAME, "course-name") \
					.find_element(By.XPATH, "./child::node()[1]")
	# Scroll into view
	driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL, Keys.END);
	sleep(0.5)
	# Click
	course.click()
	sleep(0.5)
	# Open Update menu
	driver.find_element(By.ID, 'course-update-redirect').click()
	sleep(0.5)
	# Delete
	driver.find_element(By.ID, 'course-delete').click()
	sleep(1)
	# Test for success
	try:
		driver \
			.find_element(By.XPATH, "//*[contains(text, '{0}')]") \
			.format(course_code)
		raise TestFailure
	except NoSuchElementException:
		pass
