from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def func(text1, text2, text3):

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://roadpolice.am/hy")

        wait = WebDriverWait(driver, 15)

        
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "#index_page_steps > div > div > ul > li:nth-child(2) > button > span > span"
                )
            )
        ).click()

        
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#psn-va")
            )
        ).send_keys(text1)

        
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#license_number-va")
            )
        ).send_keys(text2)

       
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#phone-number")
            )
        ).send_keys(text3)

      
        wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#drivers-login-submit")
            )
        ).click()

        

        time.sleep(5)

        result = driver.find_element(By.TAG_NAME, "body").text

        return result

    except Exception as ex:
        return f"Սխալ՝ {ex.__class__.__name__}: {ex}"

    finally:
        driver.quit()
