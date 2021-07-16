from gtts import gTTS
import random
import tkinter as tk
from pydub import AudioSegment
import os



app = tk.Tk()
app.title("Text To Music Convertor.")
app.geometry("400x200")
input_text = tk.Label(app, text="Enter text buddy!!!.",font='Verdana 10 bold').place(x=10,y=20)
text_type = tk.StringVar()
input_entry = tk.Entry(app, width=33,textvariable=text_type).place(x=160 , y=20)

def submit():
    # print("in submit.")
    input_str =text_type.get()
    tts = gTTS(text =input_str,lang ='en')
    file_number =random.randint(1,10000)
    tts.save(f'{file_number}.mp3')
    file_path =os.system(f'{file_number}.mp3')
    song = AudioSegment.from_mp3(file_path)
    play(song)

def reset():
    # print("in reset.")
    text_type.set('')

def cancel():
    # print("in cancel.")
    app.destroy()

submit_btn = tk.Button(app, text = "Submit" ,font='Verdana 10 bold',bg ="orange",command =submit).place(x=10, y=130)
reset_btn = tk.Button(app, text = "Reset" ,font='Verdana 10 bold',bg ="white",command =reset).place(x=80, y=130)
cancel_btn = tk.Button(app, text = "Exit" ,font='Verdana 10 bold',bg ="green",command =cancel).place(x=140, y=130)


app.mainloop()