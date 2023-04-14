from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import tkinter as tk
from tkinter import messagebox
from tkinter import *

root = Tk()
root.title("Otomatic Mail Sender Bot")
root.resizable(False, False)

canvas = Canvas(root, height = 600, width = 900, bg = "#849ca9")
canvas.pack()

logo_frame = Frame(root, bg = "#d2dae2", relief = "ridge", bd = 4)
logo_frame.place(relx = 0.1, rely = 0.05, relwidth = 0.8, relheight = 0.15)

receiver_frame = Frame(root, bg = "#d2dae2", relief = "ridge", bd = 4, highlightbackground = "black")
receiver_frame.place(relx = 0.1, rely = 0.22, relwidth = 0.35, relheight = 0.73)

message_frame = Frame(root, bg = "#d2dae2", relief = "ridge", bd = 4, highlightbackground = "black")
message_frame.place(relx = 0.47, rely = 0.22, relwidth = 0.43, relheight = 0.73)

Label(logo_frame, text = "Mail Sender Otomation", font = ("Courier", 20, "bold"),  bg = "#d2dae2").pack(side = "top", padx = 10, pady = 25)

Label(receiver_frame, text = "Receiver Info", font = ("Courier", 13, "bold"), bg = "#d2dae2").pack(anchor = N, padx = 5, pady = (5, 5))
receiver_text = Text(receiver_frame, height = 20, width = 30)
receiver_text.configure(bg = "#ecf0f1", fg = "black", font = ("Courier", 11))
receiver_text.pack(anchor = N, padx = 15, pady = (5, ))

def save():
    global receiver_mails
    receiver_mails = receiver_text.get("1.0", "end-1c")
    receiver_mails = receiver_mails.split("\n")
    messagebox.showinfo("Başarılı İşlem", "Mesajınızı göndereceğiniz mailler başarıyla kaydedildi.")
    receiver_text.delete("1.0", "end")
    
save_button = Button(receiver_frame, text = "Save", font = "Courier 12 bold", command = save, bd = 2, relief = "groove", highlightbackground="black", width = 15)
save_button.pack(anchor = N, padx = 5, pady = 10)

Label(message_frame, text = "Message Content", font = ("Courier", 13, "bold"), bg = "#d2dae2").pack(anchor = N, padx = 5, pady = 5)
message_text = Text(message_frame, height = 20, width = 35)
message_text.configure(bg = "#ecf0f1", fg = "black", font = ("Courier", 11))
message_text.pack(anchor = N, padx = 5, pady = (5, ))


mail_subject = "Ödeme Sayfasına Gelip Döndünüz :("
def send():
    mail_message = message_text.get("1.0", "end-1c")
    message_text.delete("1.0", "end")
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\umut_\\AppData\\Local\\Google\\Chrome\\User Data')
    options.add_argument('--profile-directory=Default')
    driver = webdriver.Chrome(options=options)
    sleep(1)
    driver.get("https://gmail.com")
    sleep(2)
    count = 0
    mailListesi = receiver_mails
    for i in range(len(mailListesi)):
        olustur = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div")
        olustur.click()
        sleep(0.5)
        receiverInput = driver.find_element(By.XPATH, "//input[@role='combobox']")
        receiverInput.send_keys(mailListesi[count])
        sleep(0.5)
        subjectInput = driver.find_element(By.XPATH, "//input[@name='subjectbox']")
        subjectInput.send_keys(mail_subject)
        sleep(0.5)
        mailMessageInput = driver.find_element(By.XPATH, "//div[@aria-label='İleti Gövdesi']")
        mailMessageInput.send_keys(mail_message)
        sleep(0.5)
        sendInput = driver.find_element(By.XPATH, "//div[@aria-label='Gönder (Ctrl-Enter)']")
        sendInput.click()
        count += 1
    messagebox.showinfo("Başarılı İşlem", "Mailler başarıyla gönderildi.")
    
send_button = Button(message_frame, text = "Send", font = "Courier 12 bold", command = send, bd = 2, relief = "groove", highlightbackground = "black", width = 20)
send_button.pack(anchor = N, padx = 5, pady = 10)

root.mainloop()