from selenium import webdriver
import config

driver = webdriver.Chrome(executable_path=config.CHROME_BINARY_PATH)
driver.get(config.TARGET_URL)

while 1:
	pass
