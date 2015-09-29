from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://ap1.salesforce.com")
driver.quit()