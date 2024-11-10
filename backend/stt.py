import sounddevice as sd
import soundfile as sf
import numpy as np
import requests
import json
import wave
import os
from groq import Groq
from scipy.io import wavfile
import text

def text_to_speech(client, filename="tts_output.wav"):
    with open(filename, "rb") as file:
        # Create a translation of the audio file
        translation = client.audio.translations.create(
        file=(filename, file.read()), # Required audio file
        model="whisper-large-v3", # Required model to use for translation
        prompt="Specify context or spelling",  # Optional
        response_format="json",  # Optional
        temperature=0.0  # Optional
        )
        # Print the translation text
        return translation.text

def record_audio(duration=5, sample_rate=44100, channels=1):
    """Record audio from microphone"""
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=channels
    )
    sd.wait()
    return recording, sample_rate

def save_audio(recording, sample_rate, filename="recording.wav"):
    """Save recorded audio to file"""
    wavfile.write(filename, sample_rate, recording)
    return filename

def stt(param):
    if param == "coach":
        return "Goggins"
    elif param == "goal":
        return "5k"

    api_key = os.environ.get("GROQ_API")
    client = Groq(api_key=api_key)
    
    # Record audio
    duration = 8  # seconds
    recording, sample_rate = record_audio(duration)
    
    # Save recorded audio
    audio_file = save_audio(recording, sample_rate)
    print(f"Audio saved to {audio_file}")

    # Translate audio to text
    transcription = text_to_speech(client, audio_file)
    print(f"Transcription: {transcription}")
    if param == "name":
        return text.get_response(f"From the following, extract the name of the user, respond with the name and nothing else: {transcription}")
    elif param == "motivation":
        return text.get_response(f"From the following, extract the goals of the user, respond with the goals and nothing else: {transcription}")