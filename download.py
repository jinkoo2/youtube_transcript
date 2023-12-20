from pytube import YouTube
import os
import shutil

url = 'https://www.youtube.com/watch?v=daUlPrnl-h4'
#YouTube(url).streams.first().download()

def mkdir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

out_dir = 'c:/temp/streams'
mkdir(out_dir)

print('downloading...'+url)

for i,stream in enumerate(YouTube(url).streams):
    print(i,stream)
    stream_dir = os.path.join(out_dir, str(i))
    print(stream_dir)
    mkdir(stream_dir)
    shutil.rmtree(stream_dir)
    stream.download(output_path=stream_dir)
    newfilename = os.listdir(stream_dir)[0]
    newfilepath = os.path.join(stream_dir, newfilename)
    root, ext = os.path.splitext(newfilename)

    os.rename(newfilepath, os.path.join(stream_dir, f'{i}{ext}'))
    
print('done')
