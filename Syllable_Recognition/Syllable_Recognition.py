# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)
from word_verification.audio_verification import record_audio
import assemblyai as aai

aai.settings.api_key = "87ad71043abe48c19e892598609fd8d2"
transcriber = aai.Transcriber()

record_audio(2, "Syllable_Record.wav")
# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("Syllable_Record.wav")

# print(transcript.text)