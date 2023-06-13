import os.path

from pytube import YouTube
import tkinter
import customtkinter as ct


# noinspection PyBroadException
def start_download():
    try:
        yt_link = link_field.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()

        title.configure(text=yt_object.title, text_color='white')
        finish_label.configure(text='')
        video.download()
        finish_label.configure(text='Video baixado')
    except:
        finish_label.configure(text='Erro no download', text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    porcent_of_complete = bytes_download / total_size * 100
    porcent = str(int(porcent_of_complete))
    progress_percent.configure(text=porcent + '%')
    progress_percent.update()

    # atualizar barra de progresso
    prog_bar.set(float(porcent_of_complete) / 100)


# Configuracoes do sistema
ct.set_appearance_mode('System')
ct.set_default_color_theme('green')

# definindo tamanho da janela
app = ct.CTk()
app.geometry('600x400')
app.minsize(width=500, height=300)
app.title('Video downloader')
app.iconbitmap(os.path.relpath('assets/logo.ico'))

# adicionar elementos visuais
title = ct.CTkLabel(app, text='Informe o link do video para baixar')
title.pack(padx=10, pady=10)

# campo do link
url_var = tkinter.StringVar()
link_field = ct.CTkEntry(app, width=350, height=40, textvariable=url_var)
link_field.pack(padx=10, pady=10)

# download finalizado
finish_label = ct.CTkLabel(app, text='')
finish_label.pack(padx=10, pady=10)

# porcentagem de progresso
progress_percent = ct.CTkLabel(app, text='0%')
progress_percent.pack(padx=10, pady=10)

prog_bar = ct.CTkProgressBar(app, width=400, corner_radius=20)
prog_bar.set(0)
prog_bar.pack(padx=10, pady=10)

# botao de download
btn_download = ct.CTkButton(app, text='Download', command=start_download)
btn_download.pack(padx=10, pady=10)

# rodar a aplicacao
app.mainloop()
