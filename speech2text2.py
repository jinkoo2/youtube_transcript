import deepspeech
import os
import wave
import numpy as np

# Load the pre-trained model
model_file_path = './data/deepspeech-0.9.3-models.pbmm'  # Replace with the path to the model file
print('Loading model...'+model_file_path)
model = deepspeech.Model(model_file_path)

scorer_file_path = './data/deepspeech-0.9.3-models.scorer' 
if os.path.exists(scorer_file_path):
    print('Enabling score...'+scorer_file_path)
    model.enableExternalScorer(scorer_file_path)

#audio_file = './data/audio/2830-3980-0043.wav'
#audio_file = 'c:/Temp/streams/2/2.wav'
audio_file = './data/converted.wav'
if not os.path.exists(audio_file):
    print('audio file not found...'+audio_file)
    exit(-1)

print('Loading audio file...'+audio_file)
#with open(audio_file, 'rb') as f:
#    audio_data = f.read()

with wave.open(audio_file, 'rb') as w:
    frames = w.readframes(w.getnframes())
    audio_data = np.frombuffer(frames, dtype=np.int16)

# Perform speech recognition
print('Performing speech recognision...')
text = model.stt(audio_data)
print('==== TEXT ====')
print(text)

outfile = audio_file+".output.txt"
print("Writing text to..."+outfile)
with open(outfile, 'w') as file:
    file.write(text)

print('done.')