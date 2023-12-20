from pytube import YouTube
import os

url = 'https://www.youtube.com/watch?v=daUlPrnl-h4'
#YouTube(url).streams.first().download()

def mkdir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

out_dir = 'c:/temp/audio'
mkdir(out_dir)

print('downloading...'+url)

for i,stream in enumerate(YouTube(url).streams.filter(only_audio=True)):
    print(i,stream)
    stream_dir = os.path.join(out_dir, str(i))
    print(stream_dir)
    mkdir(stream_dir)
    stream.download(output_path=stream_dir)
    
print('done')
