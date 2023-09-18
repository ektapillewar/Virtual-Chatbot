import tkinter as tk
from tkinter import ttk
import os
import tempfile
from nltk.chat.util import Chat, reflections
from gtts import gTTS
import pygame

pygame.mixer.init()

bot_responses = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am just a computer program, but I am doing well. How can I assist you?']),
    (r'what is your name?', ['I am a chatbot. You can call me virtual bot.']),
    (r'quit|bye', ['Goodbye!', 'Have a great day!']),
]

chatbot = Chat(bot_responses, reflections)

def get_response():
    user_input = user_entry.get()
    chat.config(state=tk.NORMAL)
    chat.insert(tk.END, "You: " + user_input + "\n")
    user_entry.delete(0, tk.END)

    if user_input.lower() == 'quit':
        chatbot_response = "Chatbot: Goodbye!"
    else:
        chatbot_response = chatbot.respond(user_input)
        speak_response(chatbot_response)

    chat.insert(tk.END, chatbot_response + "\n")
    chat.config(state=tk.DISABLED)
    chat.yview_moveto(1)

def speak_response(text):
    tts = gTTS(text)
    temp_audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio_file.name)
    temp_audio_file.close()

    audio_file_path = os.path.abspath(temp_audio_file.name)

    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

def on_enter(event):
    get_response()

root = tk.Tk()
root.title("Chatbot GUI")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)

background_image = tk.PhotoImage(file="background_image.png")

background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

chat_frame = ttk.Frame(root)
chat_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

custom_font = ("Courier", 12)

chat = tk.Text(chat_frame, width=40, height=25, state=tk.DISABLED, wrap=tk.WORD, bg="white", font=custom_font)
scrollbar = tk.Scrollbar(chat_frame, command=chat.yview)
chat.config(yscrollcommand=scrollbar.set)
chat.pack(fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar.config(bg="black", troughcolor="black")

input_frame = ttk.Frame(root)
input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(1, weight=0)

input_background_label = tk.Label(input_frame, image=background_image)
input_background_label.place(relwidth=1, relheight=1)

user_entry = ttk.Entry(input_frame, width=60)
user_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
user_entry.bind("<Return>", on_enter)

send_button = ttk.Button(input_frame, text="Send", command=get_response)
send_button.grid(row=0, column=1, padx=5, pady=5, sticky="e")

root.geometry("500x600")
root.mainloop()
