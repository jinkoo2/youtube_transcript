from pydub import AudioSegment

def get_sampling_rate(file_path):
    audio = AudioSegment.from_file(file_path)
    return audio.frame_rate

# Usage
#file_path = 'path/to/your/audiofile.mp3'  # Can be .mp3, .wav, .ogg, etc.
file_path = 'C:/Temp/streams/2/2.wav'

sampling_rate = get_sampling_rate(file_path)
print("Sampling Rate:", sampling_rate, "Hz")
