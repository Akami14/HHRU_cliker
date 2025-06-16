from selenium import webdriver
from hhru_func_2 import loggin_and_click



if __name__ == "__main__":
    login = '' # type the mail

    url_2 = 'https://vladimir.hh.ru/search/vacancy?from=resumelist&education=not_required_or_not_specified&resume=2b455687ff0b4d5c470039ed1f43475a586f6c&search_field=name&search_field=description&search_field=company_name&work_format=REMOTE&enable_snippets=false&forceFiltersSaving=true'
    driver = webdriver.Firefox()
    loggin_and_click(driver, login, url_2)
    #print(window_handles)
    #vacancy_cliks(url_2)
    ### its finaly work and easie than swicth bu buttoms
    page_name = '&page='
    #print(driver.window_handles)


    for p_number in range(40):
        #print(p_number)
        next_page = url_2 + page_name+str(p_number)
        #print(driver.getWindowHandles())
        #driver.switchTo().window()
        #driver.get(next_page)
        #vacancy_cliks(next_page)

        #driver.close()
