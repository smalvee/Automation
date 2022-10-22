from selenium import webdriver
import time


class Cookie():
    def add_cookie(self):
        driver = webdriver.Firefox(executable_path="D:\\pythonProject\\Automation\\Drivers\\geckodriver_0.31.0.exe")
        driver.maximize_window()

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        # Delete all cookies from the browser session
        driver.delete_all_cookies()

        # Add the cookie to the driver instance
        driver.add_cookie({
            "name": "orangehrm",
            "value": "27819d910a6c8c18e2a564496e7a3a59",
        })

        # View all cookies in the browser session
        print((driver.get_cookies()))
        time.sleep(3)

        driver.refresh()

        print(driver.current_url)
        time.sleep(3)

        driver.close()


test_obj = Cookie()
test_obj.add_cookie()
