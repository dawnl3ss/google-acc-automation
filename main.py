from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def main(name, lastname):
    # Créer une instance du navigateur
    driver = webdriver.Chrome()

    # Accéder à la page de connexion
    driver.get("https://accounts.google.com/signup/v2/createaccount?biz=false&cc=FR&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dautomatiser%2Bla%2Bcr%25C3%25A9ation%2Bde%2Bcompte%2Bgoogle%26rlz%3D1C1CHBF_frFR950FR950%26oq%3Dautomatiser%2Bla%2Bcr%25C3%25A9ation%2Bde%2Bcompte%2Bgoogle%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOTIGCAEQRRhA0gEIOTExNmowajeoAgCwAgA%26sourceid%3Dchrome%26ie%3DUTF-8&dsh=S67301666%3A1689791009110672&flowEntry=SignUp&flowName=GlifWebSignIn&hl=fr&authuser=0")

    time.sleep(1)


    name_field = driver.find_element("id", "firstName")
    name_field.send_keys(name)


    lastname_field = driver.find_element("id", "lastName")
    lastname_field.send_keys(lastname)

    time.sleep(1)

    next_button = driver.find_element("class name", "lw1w4b")
    next_button.click()

    time.sleep(1)

    day_field = driver.find_element("id", "day")
    day_field.send_keys("1")

    month_field = Select(driver.find_element("id", "month"))
    month_field.select_by_index("5")

    year_field = driver.find_element("id", "year")
    year_field.send_keys("1994")

    gnder_field = Select(driver.find_element("id", "gender"))
    gnder_field.select_by_index(1)

    next_button = driver.find_element("class name", "lw1w4b")
    next_button.click()

    create_my_own = driver.find_element("class name", "zJKIV")

    """email = driver.find_element("id", "identifierId")
    email.send_keys(name + "." + lastname + "1959595")"""

    while True: pass

if __name__ == '__main__':
    name, lastname = ("Paul", "Dujardin")
    main(name, lastname)