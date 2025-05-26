
from selenium import webdriver
from hhru_func import loggin, vacancy_cliks

login = '' # type the mail

url_2 = 'https://vladimir.hh.ru/search/vacancy?from=suggest_post&ored_clusters=true&enable_snippets=true&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line&experience=noExperience&search_field=name&search_field=company_name&search_field=description&text=Data+science'
driver = webdriver.Firefox()

if __name__ == "__main__":
    loggin(driver, login, url_2)
    vacancy_cliks(url_2)
    ### its finaly work and easie than swicth bu buttoms
    page_name = '&page='


    for p_number in range(40):
        next_page = url_2 + page_name+str(p_number)
        driver.get(next_page)
        vacancy_cliks(next_page)

        driver.close()
