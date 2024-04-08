from selenium import webdriver
from selenium.webdriver.common.by import By
import seleniumbase
from selenium_stealth import stealth

TOP = 100

webpage = 'https://www.ozon.ru/category/telefony-i-smart-chasy-15501/'

driver = seleniumbase.Driver(browser='chrome', headless=False, uc=True)
wait = webdriver.Chrome.implicitly_wait(driver, 500.00)

stealth(driver,
        languages=["ru-Ru", "ru"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        wait=wait
        )

driver.get(webpage + '?sorting=rating')

XPATH = '//div[@class="i1x xi1"]//a'

link_elements = driver.find_elements(By.XPATH, XPATH)


def smartphone_links():
    global link_elements, XPATH, TOP
    links = []
    i = 1
    while len(links) < TOP:
        for link_element in link_elements:
            smartphone_filter = link_element.get_attribute("textContent").split()
            if 'Смартфон' in smartphone_filter and len(links) < TOP:
                href = link_element.get_attribute('href')
                links.append(href)
        i += 1
        driver.get(webpage + f'?page={i}&sorting=rating')
        link_elements = driver.find_elements(By.XPATH, XPATH)
    driver.quit()
    return links
