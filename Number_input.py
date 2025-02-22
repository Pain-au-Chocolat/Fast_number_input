# Script made by Andrej Szegeny a.k.a Speed3DBall

import tkinter as tk
from tkinter import Toplevel
from tkinter import PhotoImage
from tkinter import Button
from time import sleep
from random import uniform
import pyautogui
from pyautogui import press, write

image_path = 'parameters.png'
pyautogui.PAUSE = 0.01

def navod_click():

    newWindow = Toplevel(GUI_window)
    newWindow.title("Navod na pouzitie")
    newWindow.geometry("600x600")
    navod_label = tk.Label(newWindow,
                    text="Tento program bude automaticky stlacat klavesnicu podla pred-definovanych parametrov.\n"
                         "Po kliknuti na START sa zapne 3 sekundovy odpocet, treba myskou kliknut na prve volne\n"
                         "pole do ktoreho bude program vkladat cisla. Prve pole musi byt vzdy uplne hore a vlavo.\n"
                         "Program bol navrhnuty vyhradne na fungovanie pre Excel.\n"
                         "Nikdy po kliknuti START nemaj aktivny kurzor mimo excelu, program bude stlacat tlacidla\n"
                         "bez ohladu na to kde sa kurzor nachadza a moze tak sposobit problemy.\n\n\n"
                         "Takto vyzera priklad. Tabulka so 4 riadkami a 7 stlpcami.\n"
                         "Toleranciami si zvolime rozsah v akom sa budu nahodne cisla vpisovat.\n"
                         "Ihned po kliknuti na START treba kurzorom kliknut na zelene policko.\n"
                         "Je vyznacene na zeleno lebo je uplne hore a uplne vlavo odkial pojdu udaje do tablky.",
                    font=("Arial", 10, "bold")
                    )
    navod_label.pack(pady=40)
    image_label = tk.Label(newWindow, image=image)
    image_label.pack()

def START_click():
    higher_value = str(higher_value_input.get()).replace(',', '.')
    lower_value = str(lower_value_input.get()).replace(',', '.')
    rows = str(rows_input.get()).replace(',', '.')
    columns = str(columns_input.get()).replace(',', '.')
    decimals = (decimals_input.get())
    if decimals == "":
        decimals = 2

    GUI_window.wm_state('iconic')
    sleep(3)
    switcher = "DOWN"

    for i in range(int(columns)):
        for j in range(int(rows)):
            write(str(value_Randomizer(float(lower_value), float(higher_value), int(decimals))))
            if j != int(rows)-1:
                if switcher == "DOWN":
                    press(['down'])
                elif switcher == "UP":
                    press(['up'])
            elif j == int(rows)-1:
                press(['right'])
                if switcher == "DOWN":
                    switcher = "UP"
                elif switcher == "UP":
                    switcher = "DOWN"

def value_Randomizer(low, high, decimal):
    return round(uniform(float(low), float(high)), int(decimal))

def TurboSwitch():
    if toggle_button.config('text')[-1] == 'RYCHLE':
        toggle_button.config(text='STREDNE')
        pyautogui.PAUSE = 0.05
    elif toggle_button.config('text')[-1] == 'STREDNE':
        toggle_button.config(text='POMALE')
        pyautogui.PAUSE = 0.10
    elif toggle_button.config('text')[-1] == 'POMALE':
        toggle_button.config(text='RYCHLE')
        pyautogui.PAUSE = 0.01

GUI_window = tk.Tk()
GUI_window.geometry("600x510")
GUI_window.resizable(False, False)
GUI_window.title("Vkladac Cisel")
GUI_window.configure(background='#28c6de')

image = PhotoImage(file=image_path)

name = tk.Label(GUI_window,
                 text="Vkladac cisel",
                 anchor=tk.CENTER,
                 bg="#1966fa",
                 height=2,
                 width=15,
                 bd=3,
                 font=("Arial", 20, "bold"),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                )

author = tk.Label(GUI_window,
                 text="Vytvoril Andrej Szegeny pre KMS <3",
                 anchor=tk.CENTER,
                 bg="#1966fa",
                 height=1,
                 width=30,
                 bd=0,
                 font=("Arial", 8, "bold"),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                )

info = tk.Label(GUI_window,
                 text="!! Pri prvom spusteni si precitaj navod pre lepsie pochopenie programu !!",
                 anchor=tk.CENTER,
                 bg="red",
                 height=2,
                 width=60,
                 bd=0,
                 font=("Arial", 12, "bold"),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                )

navod_button = tk.Button(GUI_window,
                   text="NAVOD NA POUZITIE",
                   command=navod_click,
                   activebackground="blue",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12, "bold"),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

toggle_label = tk.Label(GUI_window,
                 text="Rychlost vpisovania:",
                 anchor=tk.CENTER,
                 bg="gray",
                 height=1,
                 width=16,
                 bd=1,
                 font=("Arial", 10),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                )

toggle_button = Button(text="RYCHLE", width=7, font=("Arial", 9, "bold"),bg="yellow",bd=3, command=TurboSwitch)

higher_value_label = tk.Label(GUI_window,
                 text="Horna tolerancia:",
                 anchor=tk.CENTER,
                 bg="#1900ff",
                 height=2,
                 width=15,
                 bd=0,
                 font=("Arial", 12, "bold"),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                )

higher_value_input = tk.Entry(GUI_window,
                 font=('calibre',12,'bold'),
                 width=15
                 )


lower_value_label = tk.Label(GUI_window,
                 text="Dolna tolerancia:",
                 anchor=tk.CENTER,
                 bg="#1900ff",
                 height=2,
                 width=15,
                 bd=0,
                 font=("Arial", 12, "bold"),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                )

lower_value_input = tk.Entry(GUI_window,
                 font=('calibre',12,'bold'),
                 width=15
                 )

rows_label = tk.Label(GUI_window,
                 text="Riadky:",
                 anchor=tk.CENTER,
                 bg="#1900ff",
                 height=2,
                 width=15,
                 bd=0,
                 font=("Arial", 12, "bold"),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                )

rows_input = tk.Entry(GUI_window,
                 font=('calibre',12,'bold'),
                 width=15
                 )

columns_label = tk.Label(GUI_window,
                 text="Stlpce:",
                 anchor=tk.CENTER,
                 bg="#1900ff",
                 height=2,
                 width=15,
                 bd=0,
                 font=("Arial", 12, "bold"),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                )

columns_input = tk.Entry(GUI_window,
                 font=('calibre',12,'bold'),
                 width=15
                 )

decimals_label = tk.Label(GUI_window,
                 text="Desatinne miesta:",
                 anchor=tk.CENTER,
                 bg="#1900ff",
                 height=2,
                 width=15,
                 bd=0,
                 font=("Arial", 12, "bold"),
                 fg="white",
                 justify=tk.CENTER,
                 relief=tk.RAISED,
                )

decimals_input = tk.Entry(GUI_window,
                 font=('calibre',12,'bold'),
                 width=15
                 )

START_button = tk.Button(GUI_window,
                   text="START",
                   command=START_click,
                   activebackground="red",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="green",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 20, "bold"),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=1,
                   width=7,
                   wraplength=100)

name.grid(row=0, column=0,pady=10, columnspan=3)
author.grid(row=0, column=0,pady=15, columnspan=3, sticky="S")
info.grid(row=1, column=0,pady=3, columnspan=3)
navod_button.grid(row=2, column=0, pady=7, columnspan=3)
toggle_label.grid(row=2, column=2, pady=7,padx=5, columnspan=3, sticky="W")
toggle_button.grid(row=2, column=2, pady=7,padx=12, columnspan=3, sticky="E")
higher_value_label.grid(row=3, column=0,columnspan=2, pady=2)
higher_value_input.grid(row=3, column=1,columnspan=3, pady=2)
lower_value_label.grid(row=4, column=0, columnspan=2, pady=2)
lower_value_input.grid(row=4, column=1,columnspan=3, pady=2)
rows_label.grid(row=5, column=0, columnspan=2, pady=2)
rows_input.grid(row=5, column=1,columnspan=3, pady=2)
columns_label.grid(row=6, column=0, columnspan=2, pady=2)
columns_input.grid(row=6, column=1,columnspan=3, pady=2)
decimals_label.grid(row=7, column=0, columnspan=2, pady=2)
decimals_input.grid(row=7, column=1,columnspan=3, pady=2)
START_button.grid(row=8, column=0, pady=7, columnspan=3)

GUI_window.mainloop()
