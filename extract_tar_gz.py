import tarfile

file_path = './deepspeech/audio-0.9.3.tar.gz'

with tarfile.open(file_path, 'r:gz') as tar:
        print('extracting...')
        tar.extractall(path='./deepspeech/')

print('done.')
