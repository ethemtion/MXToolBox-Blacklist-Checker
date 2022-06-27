from gettext import gettext
from tkinter import *
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# configure workspace
ws = Tk()
ws.title("Blacklist Sorgulama")
ws.geometry("500x250")
ws.configure(bg='#1b5563')

driver = webdriver.Firefox()
driver.get("https://mxtoolbox.com/blacklists.aspx" )
driver.minimize_window()


def btnClick():
    #Label(ws, text="Bekleniyor", pady=15, bg='#1b5563').grid(row=2 , rowspan=1)
    urlsInput= urlTb.get()
    #page = requests.get(url)
    os.remove('output.txt')
    urls = urlsInput.split(' ')
    for url in urls:
        driver.get("https://mxtoolbox.com/blacklists.aspx" )
        
        
        
        checkTxt = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$ucToolhandler$txtToolInput")
        checkTxt.clear()
        checkTxt.send_keys(url)
        checkBtn = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$ucToolhandler$btnAction")
        checkBtn.click()
        time.sleep(11)
        # result = driver.find_element(by=By.CLASS_NAME, value="tool-result-body")
        # print(result.get_attribute('value'))
        
        result = driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/span/div/div[3]')
        result_text = str(result.text)
        with open('output.txt', 'a') as f:
                f.write(result_text)
                f.write('\n'*10)
    
    Label(ws, text="İşlem tamamlandı", pady=15, bg='#1b5563').grid(row=2 , rowspan=1)
    
    return 0
    

urlLbl = Label(ws, text="URL'i girin", pady=15, padx=10, bg='#1b5563')
urlTb = Entry(ws)

findBtn = Button(ws, text=" Bul! ", command=btnClick )

urlLbl.grid(row=0, column=0)
urlTb.grid(row=0, column=1)
findBtn.grid(row=1, columnspan=2)

ws.mainloop()