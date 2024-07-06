#Import the openai Library
from openai import OpenAI

# Create an api client
client = OpenAI(api_key="")

# Load audio file
audio_file = open("arabic_sample_audio_1.mp3", "rb")

# Transcribe
transcription = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)
# Print the transcribed text
print(transcription.text)