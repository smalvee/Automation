from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class OrangeHRMLogin():
    def loginTest_001(self):
        driver = webdriver.Firefox(executable_path="D:\\pythonProject\\Automation\\Drivers\\geckodriver_0.31.0.exe")

        driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
        time.sleep(3)

        # WebElements
        username = driver.find_element(By.ID, "input-email")
        element_text = username.text
        print(element_text)

        #driver.close()


test_obj = OrangeHRMLogin()
test_obj.loginTest_001()
