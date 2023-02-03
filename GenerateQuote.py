from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import unittest
import time

class RentalCoverInstantQuote(unittest.TestCase):

    def setUp(self):
        #load website
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.rentalcover.com/")
 
    def test_get_instant_quote(self):
        # Wait for Accept Button
        # Wait for the CSS selector to load
        accept_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cky-btn-accept[data-cky-tag='accept-button']"))
        )

        # Find the text "Accept" and click on the accept button
        if accept_button.text == "ACCEPT":
            accept_button.click()

        
        # Select Renting Country                
        rentcountry_field = WebDriverWait(self.driver, 20).until(
         EC.visibility_of_element_located((By.CLASS_NAME, "QuoteForm-destination-select.form-control.ui-autocomplete-input.Field-input"))
        )
        rentcountry_field.click()
        rentcountry_field.send_keys("United States")
        
        # Select Date
        # Wait until the "From Date" field is visible
        from_date_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "QuoteForm_FromDate-datepicker")),   
        )

        # Click the "From Date" field to open the date picker
        from_date_field.click()

        # Click the desired date
        from_date_element = self.driver.find_element(By.XPATH, "//a[text()='7']")
        from_date_element.click()

        """
        # Wait until the "To Date" field is visible
        to_date_field = WebDriverWait(self.driver, 20).until(
              EC.visibility_of_element_located((By.ID, "QuoteForm_ToDate-datepicker"))
         )

        # Fill the "To Date" field
        to_date_field.click()
        """
        to_date_element = self.driver.find_element(By.XPATH, "//a[text()='9']")
        to_date_element.click()
            
        
        #country of residence
        # Wait for the hyperlink to be visible
        change_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "change"))
        )

        # Click the hyperlink
        change_link.click()

        # Select Country of Residence
        destcountry_field = WebDriverWait(self.driver, 20).until(
         EC.visibility_of_element_located((By.CLASS_NAME, "QuoteForm-country-select.form-control.ui-autocomplete-input.Field-input"))
        )
        destcountry_field.click()
        destcountry_field.send_keys("United States")
                        
        #Click on Get Quote
        # Wait until the button is visible
        #getquote_button = WebDriverWait(self.driver, 10).until(
        #    EC.visibility_of_element_located((By.XPATH, "//button[text()='Get Your Instant Quote']"))
        #)
        # Locate the button using a CSS class and text
        getquote_button = WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='QuoteForm-submit Form-submit btn btn-warning btn-lg btn-block' and span[@class='btn-text' and text()='Get Your Instant Quote']]")),
        EC.visibility_of_element_located((By.CLASS_NAME, "QuoteForm-product-options.row"))
        )

        
        # Click on the button
        getquote_button.click()
                       
        
        # Locate the button using a CSS class and text
        getquote_button = WebDriverWait(self.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@class='QuoteForm-submit Form-submit btn btn-warning btn-lg btn-block' and span[@class='btn-text' and text()='Get Your Instant Quote']]")),
        EC.visibility_of_element_located((By.CLASS_NAME, "QuoteForm-product-options row"))
        )
        
        # Click on the button
        getquote_button.click()
        

        # Wait for 10 seconds
        time.sleep(10)
        self.driver.quit()
       

    def tearDown(self):
        pass
 

if __name__ == "__main__":
    unittest.main()


