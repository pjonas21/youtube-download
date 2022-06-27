from pytube import YouTube

link = input(str("Informe o link do vídeo: "))

yt = YouTube(link)

videomp4 = yt.streams.get_highest_resolution()

try: 
    videomp4.download() 
except: 
    print("Erro no download!") 
print('Video baixado!')