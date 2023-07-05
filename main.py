import yt_dlp as ytdlp
import os
import ffmpeg

def downloading():
    link = input('Введите ссылку(Введите "convert" чтобы приступить конвертации файлов): ')
    
    if link != 'convert':
        options = {
            'skip-download' : True,
            'format': 'mp4',
            'outtmpl': 'video/%(title)s.%(ext)s'
        }

        with ytdlp.YoutubeDL(options) as ytd:
            ytd.download([link])

        converting()

    else:
        converting()



def converting():
    chose = input('Все файлы в дериктории "video/" будут конвертированы в .mp3 [yes/no]:')
    
    if chose == 'yes':
        for file in os.listdir('video/'):
            if file.endswith((".mp4", ".MP4")):
                file_name = file.split('.')[0]
                
                name = file_name + ".mp3"

                stream = ffmpeg.input(f'video/{file}')
                stream = ffmpeg.output(stream, f'mp3/{name}')
                ffmpeg.run(stream)
    
    elif chose == 'no':
        downloading()
        
    else:
        print("Ошибка ввода")
        
                               
if __name__ == '__main__':
    downloading()