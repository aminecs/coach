from elevenlabs import play
from elevenlabs.client import ElevenLabs

import os

client = ElevenLabs(
  api_key=os.environ.get("ELEVEN_API_KEY")
)

def speak(text: str):
    audio = client.generate(
            text=text,
            voice="Goggins V1",
            model="eleven_multilingual_v2"
    )
    play(audio)


def get_voices():
    response = client.voices.get_all()
    print(response.voices)