import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_apply_leave(self): 
        
        browser = self.browser 
        browser.get("https://opensource-demo.orangehrmlive.com/") 
        time.sleep(5)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input").send_keys("2022-09-08")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input").send_keys("2022-09-09")
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/button").click()
        time.sleep(5)
        
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/h6").text
        
        self.assertIn('Apply', response_data)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
