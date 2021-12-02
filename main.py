from sqlite3.dbapi2 import IntegrityError
from tkinter import ttk,messagebox
from tkinter import *
import sqlite3
import os
from tkinter import font
from PIL import ImageTk,Image
from datetime import datetime
from Login_screen.Front_main import Front_principal

def main():
    window=Tk()
    application=Front_principal(window)
    window.mainloop()

if __name__=='__main__':
    main()