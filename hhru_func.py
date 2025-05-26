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
    driver.implicitly_wait(90)



    driver.find_element(By.XPATH, '//div/div/div[1]/div[3]/div[1]/div/div/div/div[6]/a').click() #/
    driver.find_element(By.XPATH,'//div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/form/div/div[3]/button[1]').click()
    driver.find_element(By.XPATH, '//div/div/div[1]/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/label[2]/div/div/div').click()

    login_form = driver.find_element(By.XPATH, '//div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div[1]/div/div[2]/div[1]/input')
    login_form.send_keys(login)
    ## type the code from mail
    driver.find_element(By.XPATH,"//div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/form/div/div/div[6]/button[1]").click()
    sleep(3)



def vacancy_cliks(url):
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.implicitly_wait(5)
        list_of_vacancy = driver.find_elements(By.XPATH, '//div[1]/div/div/div/div[2]/div[2]/div/a/div/span/span[contains(@class, "magritte-button__label___zplmt_5-3-5")]').copy() #'//a[@class = "bloko-button bloko-button_kind-primary"]/span'
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        ### Отклики
        for i, el in enumerate(list_of_vacancy):
            print(i)
            try:
                #sleep(1.05)
                el.click()
            except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException):
                print('E1')
            try:
                sleep(.5)
                el.find_element(By.XPATH,
                                '//button[contains(@data-qa,"relocation-warning-abort")]').click()  # отклик в другой стране

                ActionChains(driver).click(driver.find_element(By.XPATH, '/button[contains(@data-qa,"relocation-warning-abort")]')).perform()

            except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
                print('E2')

            try: ## просто отклик
                sleep(.40)
                el.find_element(By.XPATH, '//button[contains(@data-qa,"vacancy-response-submit-popup")]').click() #vacancy-response-submit-popup
            except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
                print('E3, just click on vacancy')


            try: ## ост случаи
                el.find_element(By.XPATH,'//button[contains(@data-qa,"response-popup-close")]').click()
            except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
                print('E4 close x')

            if driver.current_url.split('/')[3] == 'applicant':
                driver.back()
            driver.execute_script("window.scrollBy(0, 800)")




