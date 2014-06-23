from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, \
    NoAlertPresentException
import unittest, time


class VerifyNavigationHeadersTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "http://0.0.0.0:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_verify_navigation_headers(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("To The Demo!").click()
        driver.find_element_by_link_text("Workspace").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "div.query-list"):
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_link_text("Query").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "div.heading"):
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        driver.find_element_by_link_text("Results").click()
        driver.find_element_by_link_text("Workspace").click()
        driver.find_element_by_css_selector("button.close").click()
        driver.find_element_by_css_selector("span.brand").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()