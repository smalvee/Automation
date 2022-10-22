from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class KGDLogin():
    def kgd_login(self):
        driver = webdriver.Firefox(executable_path="D:\\pythonProject\\Automation\\Drivers\\geckodriver_0.31.0.exe")
        #driver.maximize_window()

        driver.get("http://127.0.0.1:8000/dashboard")
        time.sleep(2)

        # Delete all cookies from the browser session
        driver.delete_all_cookies()

        # Add the cookie to the driver instance
        driver.add_cookie({
            "name": "laravel_session",
            "value": "eyJpdiI6Ing1dFU4N3dzUUNZK2VZK044TWR1VEE9PSIsInZhbHVlIjoiRjMrd1VsNll3N3gxZS83K2dZNk9RYlp0REp1WmNBTngvNVFRSWRmN3lwTDVzQ3lDWlQ5Vk1zeXkrN3ArUVEyT0RqWHR5S3lJbWwyY29FdWc2Ry91TXAvUGFiZU40V09vU0NoZGVrR3JJZUR1ZGVyQ1RLZHJndk0zODN2dUVHZ0YiLCJtYWMiOiI0YjA2ZGU0ZDhhOTUxYTkzZDc3NTNiMmVkNTkwNGQzNGM0YTI2ZGIwYjIwNWU3ZDFhMDE2OWVkOGMzNGM2MTczIiwidGFnIjoiIn0%3D",
        })

        # View all cookies in the browser session
        print((driver.get_cookies()))
        time.sleep(2)
        driver.refresh()
        time.sleep(1)

        profile = driver.find_element(By.XPATH, "/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a/p").click()
        property_dropdown = driver.find_element(By.XPATH, "/html/body/div[@class='wrapper']/aside[1]/div//nav[@class='mt-2']/ul[@role='menu']/li[3]/a[@href='#']/p").click()
        view_dropdown = driver.find_element(By.XPATH, "/html/body/div[@class='wrapper']/aside[1]/div//nav[@class='mt-2']/ul[@role='menu']/li[3]/ul[@class='nav nav-treeview']//a[@href='/properties/14']/p[.='View Property']").click()



        #driver.close()


test_obj = KGDLogin()
test_obj.kgd_login()
