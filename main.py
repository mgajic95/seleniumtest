from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def run_google_test():
    # kreiranje chromeoptions objekta i putanja do chromedirevera
    chrome_options = Options()
    chrome_options.binary_location = '/chromedriver'

    # otvaranje google search-a
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com/")

    # trazenje search polja i kucanje facebook
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("facebook")

    # kliktanje na search dugme
    search_box.send_keys(Keys.RETURN)

    # vreme cekanja da se rezultat ocita
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Facebook")))

    # trazenje linka za facebook sajt
    facebook_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Facebook")
    facebook_link.click()

    # vreme cekanja da se rezultat ocita
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

    # trazenje email i password polja i ukucavanje invalidemail i invalidpassword
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("invalidemail")

    password_input = driver.find_element(By.NAME, "pass")
    password_input.send_keys("invalidpassword")

    # trazenje i kliktanje Log in buttona koristeci Link Text
    login_button = driver.find_element(By.LINK_TEXT, "Log In")
    login_button.click()

    # cekanje na  error message da se pojavi
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),"
                                                                                    " 'Pogrešna lozinka')]")))
        print("Error message 'Pogrešna lozinka' found.")
    except TimeoutException:
        print("Error message 'Pogrešna lozinka' not found.")

    # zatvaranje drivera
    driver.quit()

# pokretanje
if __name__ == "__main__":
    run_google_test()



