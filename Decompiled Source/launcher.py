import tkinter as tk
import os
import sys
import webbrowser
import atexit
import wget
import time
from PIL import Image, ImageTk

def resource_path(relative_path):
  base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
  return os.path.join(base_path, relative_path)

bck = resource_path('bck.png')
icon = resource_path('icon.ico')
discordicon = resource_path('discord.png')
helpicon = resource_path('howto.png')
websiteicon = resource_path('website.png')
xray = resource_path('xray')
proxifier = resource_path('proxifier')
os.system('taskkill/im Proxifier.exe')
os.remove(f'''{xray}/config.json''')
time.sleep(2)
url = '<censored>'
wget.download(url, out = xray)

def discord(*args, **kwargs):
  url = 'https://discord.gg/iratlantisrp'
  webbrowser.open(url)


def website(*args, **kwargs):
  url = 'https://atlantisrp.ir'
  webbrowser.open(url)


def active():
  os.system(f'''start {proxifier}/Proxifier.exe''')
  os.system(f'''start {xray}/wxray.exe''')


def howto(*args, **kwargs):
  howtoapp = tk.Tk()
  howtoapp.title('How to use')
  howtoapp.geometry('400x130')
  howtoapp.resizable(False, False)
  howtoapp.wm_iconbitmap(icon)
  label12 = tk.Label(howtoapp, width = 50, height = 8, background = '#136975', font = 'TimesNewRoman 10 bold', foreground = 'white', text = 'Step 1 : Remove any dns or proxy applied on your system.\nStep 2 : If you live in Iran then click on Iran button\n otherwise click on Global\n \n Enjoy and have fun :)')
  label12.place(x = -2, y = 0)
  howtoapp.mainloop()


def on_exit():
  os.system('taskkill/im Proxifier.exe')
  os.system('taskkill/im wxray.exe')


def iran():
  url = 'https://sv.atlantisrp.ir/connect.php'
  webbrowser.open(url)


def kharej():
  url = 'https://sv.atlantisrp.ir/connectout.php'
  webbrowser.open(url)

app = tk.Tk()
bg = tk.PhotoImage(file = bck)
helpphoto = tk.PhotoImage(file = helpicon)
dokme = tk.Button(app, image = helpphoto, command = howto, height = 50, width = 50, background = 'grey', highlightthickness = 0, bd = 0)
dokme.place(y = 15, x = 15)
canvas = tk.Canvas(app, width = 600, height = 300)
canvas.place(x = -2, y = 0)
canvas.create_image((0, 0), anchor = 'nw', image = bg)
app.title('Atlantis Launcher')
app.geometry('598x300')
app.wm_attributes('-transparentcolor', 'grey')
app.resizable(False, False)
app.wm_iconbitmap(icon)
webdis = Image.open(websiteicon).resize((35, 35))
WebPhoto = ImageTk.PhotoImage(webdis)
web = canvas.create_image((558, 95), anchor = 'nw', image = WebPhoto)
canvas.tag_bind(web, '<Button-1>', website)
photdis = Image.open(discordicon).resize((35, 35))
DiscordPhoto = ImageTk.PhotoImage(photdis)
dis = canvas.create_image((558, 55), anchor = 'nw', image = DiscordPhoto)
canvas.tag_bind(dis, '<Button-1>', discord)
label_frame = tk.LabelFrame(canvas, text = '', highlightthickness = 0, bd = 1)
label = tk.Label(label_frame, text = 'Atlantis; All rights reserverd. By : MmD', font = 'TimesNewRoman 10', highlightthickness = 0, bd = 0) # typo issue reserved is correct :D
canvas.create_window((5, 277), anchor = 'nw', window = label_frame)
label.pack()
helpphoto = tk.PhotoImage(file = helpicon)
chick = canvas.create_image((550, 5), anchor = 'nw', image = helpphoto)
canvas.tag_bind(chick, '<Button-1>', howto)
submit_button = tk.Button(app, text = 'Iran', foreground = 'white', command = iran, background = '#136975', font = 'TimesNewRoman 10 bold', highlightthickness = 0, bd = 0, width = 9, height = 2)
submit_button.place(y = 260, x = 520)
submit_button2 = tk.Button(app, text = 'Global', command = kharej, background = '#136975', foreground = 'white', font = 'TimesNewRoman 10 bold', highlightthickness = 0, bd = 0, width = 9, height = 2)
submit_button2.place(y = 260, x = 420)
submit_button3 = tk.Button(app, text = 'Active', command = active, background = '#136975', foreground = 'white', font = 'TimesNewRoman 10 bold', highlightthickness = 0, bd = 0, width = 9, height = 2)
submit_button3.place(y = 260, x = 320)
app.mainloop()
atexit.register(on_exit)