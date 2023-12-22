import deepspeech
import wave
import numpy as np

def deepspeech_transcribe(audio_file, model_file, scorer_file=None):
    # Load DeepSpeech model
    print(f'Loading...'+model_file)
    model = deepspeech.Model(model_file)
    if scorer_file:
        model.enableExternalScorer(scorer_file)

    # Load the audio file
    with wave.open(audio_file, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)
        print("Audio file loaded, performing speech-to-text...")

    # Check if audio needs to be resampled
    if rate != model.sampleRate():
        raise ValueError(f"Invalid sample rate: {rate}. DeepSpeech model requires {model.sampleRate()}")

    # Perform speech-to-text
    data16 = np.frombuffer(buffer, dtype=np.int16)
    text = model.stt(data16)
    return text

# Paths to your model, scorer, and audio file
model_file_path = './deepspeech/deepspeech-0.9.3-models.pbmm'
scorer_file_path = './deepspeech/deepspeech-0.9.3-models.scorer' # Optional
audio_file_path = './deepspeech/audio/2830-3980-0043.wav'

# Transcribe audio
transcription = deepspeech_transcribe(audio_file_path, model_file_path, scorer_file_path)
print("Transcription:", transcription)
