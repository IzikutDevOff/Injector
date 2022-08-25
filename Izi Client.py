import os
import tkinter as tk
from turtle import width
import requests
import threading
import os
import json
import bitcoin
import webbrowser
from os import name, chdir, rmdir, mkdir, rename, listdir 
from pystyle import Colorate, Colors, System, Center, Write, Anime
window = tk.Tk()
width = 800
height = 500
window.title("Izi Client | Waiting for Authentification")
window.geometry(str(width)+"x"+str(height))
Write.Input("Enter your Liscence -> ",
            Colors.purple, interval=0.019, input_color=Colors.white)
os.system("start Injection")