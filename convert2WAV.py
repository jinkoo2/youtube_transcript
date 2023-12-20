import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def convert_mp4_to_wav(mp4_file_path, wav_file_path):
    # Load the video file
    video = VideoFileClip(mp4_file_path)

    # Extract the audio
    audio = video.audio

    # Write the audio to a temporary file
    temp_file_path = "temp_audio.mp3"
    audio.write_audiofile(temp_file_path)

    # Read the temporary file with pydub
    sound = AudioSegment.from_file(temp_file_path)

    # Convert to mono and export as WAV
    sound = sound.set_channels(1)
    sound.export(wav_file_path, format="wav")

    # Remove the temporary file
    os.remove(temp_file_path)

# Usage
mp4_file_path = 'C:/Temp/streams/2/2.mp4'
# Load the video file
video = VideoFileClip(mp4_file_path)

# Extract the audio
audio = video.audio

# Write the audio to a temporary file
temp_file_path = mp4_file_path.replace('.mp4', '.mp3')
print('saving to ...', temp_file_path)
audio.write_audiofile(temp_file_path)

# Read the temporary file with pydub
sound = AudioSegment.from_mp3(temp_file_path)

# Convert to mono and export as WAV
sound = sound.set_channels(1)
wav_file_path = mp4_file_path.replace('.mp4', '.wav')
print('saving to ...', wav_file_path)
sound.export(wav_file_path, format="wav")

#wav_file_path =  mp4_file_path.replace('.mp4', '.wav')
#convert_mp4_to_wav(mp4_file_path, wav_file_path)