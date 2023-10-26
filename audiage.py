import multiprocessing
import tkinter as tk
import webbrowser
import requests
import customtkinter as ctk
from IPython.utils.py3compat import execfile
from PIL.ImageTk import PhotoImage
from _cffi_backend import callback
from googletrans import Translator
from PIL import ImageTk, Image
import openai
#from modelscope.pipelines import pipeline
#from modelscope.outputs import OutputKeys
from authtoken import auth_token
import speech_recognition as sr
import replicate
import os
from torch import autocast
import imgwav
# import config
import numpy as np
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline



# @title functions
os.environ["REPLICATE_API_TOKEN"]="YOUR_REPLICATE_API_TOKEN_KEY"
def image_grid(imgs, rows, cols):
    assert len(imgs) == rows * cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols * w, rows * h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i % cols * w, i // cols * h))
    return grid


def recordvoice(lang):
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            try:
                text1 = r.recognize_google(audio, language=lang)
            except:
                pass
            return text1


# Create the app
app = tk.Tk()
app.geometry("1920x2080")
app.title("AUDIAGE")
ctk.set_appearance_mode("dark")
bg = Image.open("background.png")
bg=bg.resize((200,200))
bg = ImageTk.PhotoImage(bg)
# Show image using label
ctk.CTkLabel(master=app, image=bg, text="", width=198, height=198).place(x=650, y=0)
text = ctk.CTkEntry(app, height=40, width=512, text_color="black", fg_color="white")
text.place(x=504, y=365)
prompt = ctk.CTkButton(master=app, height=40, width=120, text_color="black", fg_color="orange",font=('Arial',16),
                       command=lambda: text.insert(0, recordvoice("en-IN")))
prompt.place(x=300, y=310)
prompt.configure(text="Record in English")
prompt_kan = ctk.CTkButton(master=app, height=40, width=120, text_color="black", fg_color="orange",font=('Arial',16),
                       command=lambda: text.insert(0, recordvoice("kn-IN")))
prompt_kan.place(x=500, y=310)
prompt_kan.configure(text="Record in Kannada")
prompt_hin = ctk.CTkButton(master=app, height=40, width=120, text_color="black", fg_color="orange",font=('Arial',16),
                       command=lambda: text.insert(0, recordvoice("hi-IN")))
prompt_hin.place(x=700, y=310)
prompt_hin.configure(text="Record in Hindi")

prompt_tel = ctk.CTkButton(master=app, height=40, width=120, text_color="black", fg_color="orange",font=('Arial',16),
                       command=lambda: text.insert(0, recordvoice("te-IN")))
prompt_tel.place(x=900, y=310)
prompt_tel.configure(text="Record in Telugu")

prompt_tam = ctk.CTkButton(master=app, height=40, width=120, text_color="black", fg_color="orange",font=('Arial',16),
                       command=lambda: text.insert(0, recordvoice("ta-IN")))
prompt_tam.place(x=1100, y=310)
prompt_tam.configure(text="Record in Tamil")

# stop = ctk.CTkButton(master=app,height=40,width=120,text_color="white",fg_color="black",command=)
"""lmain = ctk.CTkLabel(master=app, height=256, width=256)
lmain.place(x=5, y=165)
lmain1 = ctk.CTkLabel(master=app, height=256, width=256)
lmain1.place(x=505, y=165)
lmain2 = ctk.CTkLabel(master=app, height=256, width=256)
lmain2.place(x=965, y=165)
lmain3 = ctk.CTkLabel(master=app, height=256, width=256)
lmain3.place(x=5, y=595)
lmain4 = ctk.CTkLabel(master=app, height=256, width=256)
lmain4.place(x=565, y=595)
lmain5 = ctk.CTkLabel(master=app, height=256, width=256)
lmain5.place(x=965, y=595)"""

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16,
                                               use_auth_token=auth_token)
pipe.to(device)


def generate():
    with autocast(device):
        app1 = tk.Toplevel(app)
        app1.geometry("1920x2080")
        app1.title("Output")
        translator = Translator()
        result = translator.translate(text.get())
        num_cols = 3
        num_rows = 2
        prompt1 = result.text
        image1 = pipe(prompt1, guidance_scale=8.5).images[0]
        image1.save('image1.png')
        image1 = Image.open('image1.png')
        img1 = image1.resize((300, 300))
        img1 = ImageTk.PhotoImage(img1)
        # lmain.configure(image=img1)
        image2 = pipe(prompt1, guidance_scale=8.5).images[0]
        image2.save('image2.png')
        image2 = Image.open('image2.png')
        img2 = image2.resize((300, 300))
        img2 = ImageTk.PhotoImage(img2)
        # lmain1.configure(image=img2)
        image3 = pipe(prompt1, guidance_scale=8.5).images[0]
        image3.save('image3.png')
        image3 = Image.open('image3.png')
        img3 = image3.resize((300, 300))
        img3 = ImageTk.PhotoImage(img3)
        # lmain2.configure(image=img3)
        image4 = pipe(prompt1, guidance_scale=8.5).images[0]
        image4.save('image4.png')
        image4 = Image.open('image4.png')
        img4 = image4.resize((300, 300))
        img4 = ImageTk.PhotoImage(img4)
        # img4 = ImageTk.PhotoImage(image4)
        # lmain3.configure(image=img4)
        image5 = pipe(prompt1, guidance_scale=8.5).images[0]
        image5.save('image5.png')
        image5 = Image.open('image5.png')
        img5 = image5.resize((300, 300))
        img5 = ImageTk.PhotoImage(img5)
        # lmain4.configure(image=img5)
        image6 = pipe(prompt1, guidance_scale=8.5).images[0]
        image6.save('image6.png')
        image6 = Image.open('image6.png')
        img6 = image6.resize((300, 300))
        img6 = ImageTk.PhotoImage(img6)
        # lmain5.configure(image=img6)
        label = ctk.CTkLabel(master=app1,
                             text="Generated Images:",
                             width=120,
                             font=("Times New Roman",20),
                             text_color="black",
                             height=35,
                             corner_radius=8)
        label.place(x=700, y=0)
        ctk.CTkLabel(master=app1, image=img6, text="", width=298, height=298).place(x=300, y=40)
        ctk.CTkLabel(master=app1, image=img1, text="", width=298, height=298).place(x=620, y=40)
        ctk.CTkLabel(master=app1, image=img2, text="", width=298, height=298).place(x=940, y=40)
        ctk.CTkLabel(master=app1, image=img3, text="", width=298, height=298).place(x=300, y=380)
        ctk.CTkLabel(master=app1, image=img4, text="", width=298, height=298).place(x=620, y=380)
        ctk.CTkLabel(master=app1, image=img5, text="", width=298, height=298).place(x=940, y=380)


label2 = ctk.CTkLabel(master=app,
                      width=1520,
                      text="AUDIAGE: Generating Multimedia Content using Stable Diffusion",
                      font=('Times New Roman',40),
                      text_color="black",
                      anchor="center",
                      height=70,
                      corner_radius=8)

label2.place(x=0, y=170)

label1 = ctk.CTkLabel(master=app,
                      width=1520,
                      text="Your Suggestions will appear here",
                      text_color="grey",
                      anchor="center",
                      height=35,
                      font=('Arial',20),
                      corner_radius=8)

label1.place(x=0, y=580)


def gen_video():

    output = replicate.run("cjwbw/damo-text-to-video:1e205ea73084bd17a0a3b43396e49ba0d6bc2e754e9283b2df49fad2dcf95755",input={"prompt": text.get(),"num_frames":50,"num_inference_steps":50})
    print(output)
    res = requests.get(output)
    open("video.mp4","wb").write(res.content)
    
    imgwav.combinevideoaudio()



def suggestsomething():
    if (len(text.get()) == 0):
        strsuggestion = "Here is a Text To Image prompt formula: (image we're prompting),(5 descriptive keywords),(resolution of the image)," \
                        "(time of the day),(style of photograph). Generate only one prompt in less than 20 words, not even 'prompt:' based on this formula"
    else:
        strsuggestion = "Here is a Text To Image prompt formula: (image we're prompting),(5 descriptive keywords),(resolution of the image)," \
                        "(time of the day),(style of photograph). Generate only one prompt in less than 20 words based on the keyword:" + text.get()
    messages = [
        {"role": "user", "content": strsuggestion},
    ]
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    reply = reply.replace('Prompt:', '')
    label1.configure(text=reply)
    label1.configure(text_color="black")


def gen_audio():
    str1='python music.py '+text.get()
    os.system(str1)
    imgwav.combineimageaudio()


gen_image = ctk.CTkButton(master=app, height=40, width=120, text_color="white", fg_color="green", font=('Arial',16),command=generate)
gen_image.configure(text="Generate Image")
gen_image.place(x=500, y=415)

gen_vid = ctk.CTkButton(master=app, height=40, width=120, text_color="white", fg_color="green", font=('Arial',16), command=gen_video)
gen_vid.configure(text="Generate Video")
gen_vid.pack()
gen_vid.bind("<Button-1>", lambda e: webbrowser.open_new('path_to_directory/record1.mp4'))
gen_vid.place(x=700, y=415)

gen_aud = ctk.CTkButton(master=app, height=40, width=120, text_color="white", fg_color="green", font=('Arial',16),command=gen_audio)
gen_aud.configure(text="Generate Music")
gen_aud.pack()
gen_aud.bind("<Button-1>", lambda e: webbrowser.open_new('path_to_directory/record.mp4'))
gen_aud.place(x=900, y=415)

openai.api_key = 'YOUR_OPENAI_API_KEY'


def puttext():
    text.delete(0, tk.END)
    text.insert(0, label1.cget("text"))


suggestion_btn1 = ctk.CTkButton(master=app, height=40, width=120, text_color="white", fg_color="Blue",font=('Arial',16),
                                command=suggestsomething)
suggestion_btn1.place(x=600, y=710)
suggestion_btn1.configure(text="Create Suggestion")

suggestion_btn = ctk.CTkButton(master=app, height=40, width=120, text_color="white", fg_color="Blue",font=('Arial',16),
                               command=puttext)
suggestion_btn.place(x=800, y=710)
suggestion_btn.configure(text="Use Suggestion")


app.mainloop()
