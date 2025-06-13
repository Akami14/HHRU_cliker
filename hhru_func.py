from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException

driver = webdriver.Firefox()


def loggin(driver, login, url):
    ### Логинемся
    driver.get("about:preferences")
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//*[@id='defaultZoom']"))
    ActionChains(driver).click(driver.find_element(By.XPATH, "//*[@value='50']")).perform()

    driver.get(url=url)
    driver.implicitly_wait(40)

    driver.find_element(By.XPATH, '//div/div/div[1]/div[3]/div[1]/div/div/div/div[6]/a').click() #/
    driver.find_element(By.XPATH,'//div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/form/div/div[3]/button[1]').click()
    #driver.find_element(By.XPATH, '//div/div/div[1]/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/label[2]/div/div/div').click()
    sleep(0.5)
    a = driver.find_element(By.CLASS_NAME,"magritte-field___9S8Tw_7-2-13")
    ActionChains(driver).move_to_element(a).click(a).send_keys(login).perform()
    sleep(60) # cause we waiting sms



def vacancy_cliks(url):
    while True:
        driver.get(url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.implicitly_wait(9)
        list_of_vacancy = driver.find_elements(By.XPATH, '//div[1]/div/div/div/div[2]/div[2]/div/a/div/span/span[contains(@class, "magritte-button__label___zplmt")]').copy() #'//a[@class = "bloko-button bloko-button_kind-primary"]/span'
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        ### Отклики
        for i, el in enumerate(list_of_vacancy):
            print(i)
            el.click()
            response = driver.find_element(By.XPATH, "//div/div[3]/div/div/div/div/div[2]/button/div/span/span[contains(@class, 'magritte-button__label___zplmt_5-3-10')]")
            ActionChains(driver).move_to_element(response).click(response)


            if driver.current_url.split('/')[3] == 'applicant':
                driver.back()
            driver.execute_script("window.scrollBy(0, 800)")




