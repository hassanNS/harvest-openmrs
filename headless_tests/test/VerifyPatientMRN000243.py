from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import base_test
import os
class VerifyPatientMRN00024301(unittest.TestCase):
    def setUpNA(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8004/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_verify_patient_m_r_n00024301(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("To The Demo!").click()
        driver.find_element_by_css_selector("div.heading").click()
        driver.find_element_by_link_text("MRN").click()
        driver.find_element_by_css_selector("div.field-search.search > input.input-block-level").clear()
        driver.find_element_by_css_selector("div.field-search.search > input.input-block-level").send_keys("MRN000243")
        driver.find_element_by_css_selector("div.actions > button.btn.btn-mini").click()
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_xpath("//div[@id='content']/div/div[2]/div[3]/div/div[3]/div/button[2]").click()
        
        try:
            driver.find_element_by_link_text("MRN000243").click()
            assert 1
        except:
            driver.get_screenshot_as_file("{0}/{1}/{2}/{3}/{4}".format(os.getcwd(),"headless_tests","test","screen_shots","VerifyPatientMRN000243.png"))
            assert 0, "Link MRN000243 not found"
            
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
