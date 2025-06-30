from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException

#driver = webdriver.Firefox()


def loggin_and_click(driver, login, url):
    ### Логинемся
    driver.get("about:preferences")
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//*[@id='defaultZoom']"))
    ActionChains(driver).click(driver.find_element(By.XPATH, "//*[@value='50']")).perform()

    driver.get(url=url)
    driver.implicitly_wait(90)

    driver.find_element(By.XPATH, '//div/div/div[1]/div[3]/div[1]/div/div/div/div[6]/a').click() #/
    driver.find_element(By.XPATH,'//div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/form/div/div[3]/button[1]').click()

    sleep(0.5)
    #a = driver.find_element(By.XPATH,'//div/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div[1]/div/div[2]/div[2]/input')
    a = driver.find_element(By.CLASS_NAME,"magritte-field___9S8Tw_7-2-20") # xh-highlight

    ActionChains(driver).move_to_element(a).click(a).send_keys(login).perform()
    sleep(5.40) # cause we waiting sms
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.implicitly_wait(9)
        list_of_vacancy = driver.find_elements(By.XPATH, '//div[1]/div/div/div/div[2]/div[2]/div/a/div/span/span').copy() #    //div[1]/div/div/div/div[2]/div[2]/div/a'   //div[1]/div/div/div/div[2]/div[2]/div/a/div/span/span[contains(@class, "magritte-button__label___zplmt")]#'//a[@class = "bloko-button bloko-button_kind-primary"]/span'
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
        range_of_list = len(list_of_vacancy)
        print(len(list_of_vacancy))
        for i, el in enumerate(list_of_vacancy):
            print(i, el)
            driver.execute_script('arguments[0].scrollIntoView()', el)
            ActionChains(driver).move_to_element(el).click(el).perform()
            sleep(0.5)
            #just click
            try:
                sleep(1.05)
                b1 = driver.find_element(By.XPATH, '//button[contains(@data-qa, "vacancy-response-submit-popup")]/div/span/span')
                ActionChains(driver).move_to_element(b1).click(b1).perform()
            except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException):
                print('E1')



            try: ## просто отклик
                sleep(.40)
                a = driver.find_element(By.XPATH, '//button[contains(@data-qa,"vacancy-response-submit-popup")]/div/span/span').click() #vacancy-response-submit-popup
                print(a)
                ActionChains(driver).move_to_element(a).click(a)
            except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
                print('E3, just click on vacancy')

            """   
            try:
                sleep(.5)
                driver.find_element(By.XPATH,
                              '//button[contains(@data-qa,"relocation-warning-abort")]').click()  # отклик в другой стране

                ActionChains(driver).click(driver.find_element(By.XPATH, '/button[contains(@data-qa,"relocation-warning-abort")]')).perform()

          except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
              print('E2')


          try: ## ост случаи
              el.find_element(By.XPATH,'//button[contains(@data-qa,"response-popup-close")]').click()
          except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
              print('E4 close x')
              """

            try:
                crosser = driver.find_element(By.XPATH, '/html/body/div[154]/div/div[1]/div[1]/div/div[2]/span/div/button/span')
                crosser.click()
            except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
                print('E5 close x')

            #driver.execute_script("window.scrollBy(0, 900)")

            if 'applicant' in driver.current_url.split('/'):
                driver.back()





