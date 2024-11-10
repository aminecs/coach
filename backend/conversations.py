import os
import signal

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("ELEVEN_API_KEY")

client = ElevenLabs(api_key=API_KEY)

def start_conversation(status_queue):
    conversation = Conversation(
        # API client and agent ID.
        client,
        AGENT_ID,

        # Assume auth is required when API_KEY is set.
        requires_auth=bool(API_KEY),

        # Use the default audio interface.
        audio_interface=DefaultAudioInterface(),

        # Simple callbacks that print the conversation to the console.
        callback_agent_response=lambda response: print(f"Agent: {response}"),
        callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
        callback_user_transcript=lambda transcript: print(f"User: {transcript}"),

        # Uncomment if you want to see latency measurements.
        callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),
        status_queue=status_queue
    )

    conversation.start_session()

    signal.signal(signal.SIGINT, lambda sig, frame: conversation.end_session())

    conversation_id = conversation.wait_for_session_end()
    print(f"Conversation ID: {conversation_id}")
    return conversation

def onboarding():
    conversation = Conversation(
        # API client and agent ID.
        client,
        "pfuQ8L6Tyqs2qPTAmZ5n",

        # Assume auth is required when API_KEY is set.
        requires_auth=bool(API_KEY),

        # Use the default audio interface.
        audio_interface=DefaultAudioInterface(),

        # Simple callbacks that print the conversation to the console.
        callback_agent_response=lambda response: print(f"Agent: {response}"),
        callback_agent_response_correction=lambda original, corrected: print(f"Agent: {original} -> {corrected}"),
        callback_user_transcript=lambda transcript: print(f"User: {transcript}"),

        # Uncomment if you want to see latency measurements.
        callback_latency_measurement=lambda latency: print(f"Latency: {latency}ms"),
        status_queue=None
    )

    conversation.start_session()

    return conversation