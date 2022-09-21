from sqlite3 import Row
import tkinter as tk
import requests
import bs4
from setuptools import Command
win=tk.Tk()
win.geometry('500x500')
lab=tk.Label(text='websitelink')
ent=tk.Entry()
def function():
    website_link=ent.get()
    mainvar=requests.get(website_link)
    cortvar=bs4.BeautifulSoup(mainvar.text,'lxml')
    webpage_tittle=cortvar.select('title')
    print(webpage_tittle[0].text)
but=tk.button(text='submit', Command=function())
lab.grid(row=0,column=0)
ent.grid(row=0,column=1)
but.grid(row=0,column=1)
win.mainloop()
