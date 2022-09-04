import requests
from bs4 import BeautifulSoup as bs
from time import sleep

from playwright.sync_api import Playwright, sync_playwright, expect

URL = 'http://100.64.18.175:8080/'

response = requests.get(URL)

if response.status_code == 200:
        print(f'\nCodigo: {response.status_code} ACESSO AUTORIZADO')
else:
        print(f'\nCodigo: {response.status_code} ACESSO NEGADO')

doc_html = ''' 

<div id="DevicesNum">8</div>
<tbody id="DevicesCartb">
<tr><td>Unknown_60:35:73:a4:27:99</td></tr>
<tr><td>Galaxy-S8</td></tr>
<tr><td>Unknown_e6:4f:3d:b3:cc:35</td></tr>
<tr><td>dlinkap</td></tr>
<tr><td>Mariano</td></tr>
<tr><td>Galaxy-A21s</td></tr>
<tr><td>Unknown_96:90:09:58:ae:97</td></tr>
<tr><td>Unknown_f8:77:b8:c6:28:61</td></tr></tbody>



'''

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://100.64.18.175:8080/
    page.goto("http://100.64.18.175:8080/")


    # Click input[name="name"]
    page.locator("input[name=\"name\"]").click()

    # Press V with modifiers
    page.locator("input[name=\"name\"]").fill('AdminGPON')
    sleep(3)

    # Click input[name="pswd"]
    page.locator("input[name=\"pswd\"]").click()

    # Press V with modifiers
    page.locator("input[name=\"pswd\"]").fill('ALC#FGU')
    sleep(5)

    # Click text=Login
    page.locator("text=Login").click()
    #page.wait_for_url("http://100.64.18.175:8080/")
    sleep(5)

    soup = bs(doc_html, 'html.parser')
    print(soup)



    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
'''
soup = bs(response.content, 'html.parser')
print(soup)
'''
