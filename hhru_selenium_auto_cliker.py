from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
#import requests
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('path/to/binary')
login = ''
password = ''
vacancy = ' '
letter ='....'
url = 'https://vladimir.hh.ru/'
driver = webdriver.Firefox()
driver.get("about:preferences")
driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//*[@id='defaultZoom']"))
ActionChains(driver).click(driver.find_element(By.XPATH, "//*[@value='50']")).perform()
# r'C:\Users\PC\Desktop\DataScience\hhru\hhru_selenium\geckodriver'

driver.get(url=url)
sleep(0.9) # иначе стр не прогружается команда ниже не пмогает
driver.implicitly_wait(90)


### Логинемся
b1 = driver.find_element(By.XPATH, '//div/div/div[3]/div/div/div/div/div[5]/a').click()
login_form = driver.find_element(By.XPATH, '//div/div/div[1]/div[4]/div[1]/div/div/div/div/div/div[1]/div/div/div[2]/form/fieldset/input')
login_form.send_keys(login)

b2 = driver.find_element(By.XPATH,"//div/div/div[1]/div[4]/div[1]/div/div/div/div/div/div[1]/div/div/div[2]/form/div[4]/button[2]").click()
password_form = driver.find_element(By.XPATH, '//div/div/div[1]/div[4]/div[1]/div/div/div/div/div/div[1]/div/div/form/div[2]/fieldset/input')
password_form.send_keys(password)
b3 = driver.find_element(By.XPATH, '//div/div/div[1]/div[4]/div[1]/div/div/div/div/div/div[1]/div/div/form/div[6]/button[1]/span').click()
sleep(0.9)


### Поиск вакансии
driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div/div[3]/div[1]/div/div/div/div[7]/span/button/span[2]/span').click()
find_vacancy = driver.find_element(By.XPATH, '//*[@id="a11y-search-input"]')
find_vacancy.send_keys(vacancy) ## отправка нахвания вакансии в поле
b4 = driver.find_element(By.XPATH, '//*[@id="supernova_search_form"]/div/div[2]/button/span/span[2]').click() #щелчек для поиска








### Прокрутка и получение количества страниц
driver.execute_script("scrollTo(0, document.body.scrollHeight)")

number_pages = int(driver.find_element(By.XPATH, '//div/span[6]/span[@class="pager-item-not-in-short-range"]/a/span').text)
print(number_pages)
driver.execute_script("window.scrollTo(0, 0)")


for _ in range(number_pages):
    list_of_vacancy = driver.find_elements(By.XPATH, '//a[@class = "bloko-button bloko-button_kind-primary"]')

    ### Отклики
    for i, el in enumerate(list_of_vacancy):
        #next_vacancy = '//div' + str([(4 + i)]) + '/div/div/div/div/a[@class="bloko-button bloko-button_kind-primary"]'

        print(i)
        try:
            el.click()
            #if for_letter: for_letter = el.find_element(By.XPATH, '//*[@id="RESPONSE_MODAL_FORM_ID"]/div/div/textarea')
            #for_letter.send_keys(letter)
            sleep(5.5)
            el.find_element(By.XPATH, '//div[5]/button[1]').click() #//div[5]/button[2]
            sleep(1.5)

            #el.find_element(By.XPATH, '//div[5]/button[@class="bloko-button bloko-button_kind-primary"]').click()
        except ElementClickInterceptedException:
            driver.back()
            #print('ElementClickInterceptedException')
        sleep(1.5)


        driver.execute_script("window.scrollBy(0, 900)")

        #print(next_vacancy)
        #try:
            #element = driver.find_element(By.XPATH, next_vacancy)
            #driver.execute_script("arguments[0].scrollIntoView(true);", element)
        #except NoSuchElementException:
            #pass

        #sleep(0.5)






    go_next_button = driver.find_element(By.XPATH, '//div[@class="pager"]/a/span').click()



    #print(9)
    #sleep(10.5)
driver.close()
