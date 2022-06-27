from tkinter import *
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


#  tkinter ayarları
ws = Tk()     
ws.title("Blacklist Sorgulama")
ws.geometry("500x250")
ws.configure(bg='#1b5563')

#Selenium webdriver ayarları
driver = webdriver.Firefox()
driver.get("https://mxtoolbox.com/blacklists.aspx" ) #tarayıcıyı linke yolluyoruz
driver.minimize_window()

#butonun fonksiyonu
def btnClick():
    #output'u siliyoruz (önceki sonuçlarla karışmaması için)
    os.remove('output.txt')

    #textboxtan metni boşluklardan ayırıp dizi oluşturuyoruz
    urlsInput= urlTb.get() 
    urls = urlsInput.split(' ')
    
    for url in urls:
        driver.get("https://mxtoolbox.com/blacklists.aspx" )

        #siteden textbox bulunuyor, önce silinip sonra url yollanıyor
        checkTxt = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$ucToolhandler$txtToolInput")
        checkTxt.clear()
        checkTxt.send_keys(url)

        #butona basılıyor
        checkBtn = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$ucToolhandler$btnAction")
        checkBtn.click()
        time.sleep(12)
       
        #Sonuçlar alınıyor notepade yazılıyor
        result = driver.find_element(by=By.XPATH, value='/html/body/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/span/div/div[3]')
        result_text = str(result.text)
        with open('output.txt', 'a') as f:
                f.write(result_text)
                f.write('\n'*10)
    
    Label(ws, text="İşlem tamamlandı", pady=15, bg='#1b5563').grid(row=2 , rowspan=1)
    
    return 0
    

urlLbl = Label(ws, text="URL'i girin", pady=15, padx=10, bg='#1b5563') #label1
urlTb = Entry(ws) #textbox

findBtn = Button(ws, text=" Bul! ", command=btnClick ) #buton

#widgetlarıın konumaları
urlLbl.grid(row=0, column=0)
urlTb.grid(row=0, column=1)
findBtn.grid(row=1, columnspan=2)

ws.mainloop()