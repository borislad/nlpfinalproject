import librosa
import numpy as np
import sounddevice as sd
from scipy.io import wavfile

def record_audio(duration, output_file):
    # Set the sampling rate and number of channels
    sample_rate = 44100  # CD quality audio
    channels = 1  # Mono audio

    # Calculate the number of samples based on the duration
    num_samples = int(duration * sample_rate)

    # Record audio from the microphone
    audio = sd.rec(num_samples, samplerate=sample_rate, channels=channels)
    sd.wait()  # Wait for the recording to complete

    # Save the recorded audio to a WAV file
    wavfile.write(output_file, sample_rate, audio)

def validate_sound(audio_file1, audio_file2):
    # Load the audio files
    signal1, sr1 = librosa.load(audio_file1, sr=None)
    signal2, sr2 = librosa.load(audio_file2, sr=None)

    # Ensure both signals have the same sample rate
    if sr1 != sr2:
        print("Error: Sample rates of the two audio files do not match.")
        return

    # Normalize the signals to have the same length
    min_length = min(len(signal1), len(signal2))
    signal1 = signal1[:min_length]
    signal2 = signal2[:min_length]

    # Compute the similarity between the signals
    similarity = np.dot(signal1, signal2) / (np.linalg.norm(signal1) * np.linalg.norm(signal2))

    # Set a similarity threshold
    similarity_threshold = 0.9

    # Compare the similarity with the threshold
    if similarity >= similarity_threshold:
        print("Sound validation successful. The audio signals match.")
    else:
        print("Sound validation failed. The audio signals do not match.")

# Example usage
audio_file1 = "recorded_audio1.wav"
audio_file2 = "recorded_audio.wav"


# Example usage
recording_duration = 5  # Duration in seconds
output_file = "recorded_audio.wav"
record_audio(recording_duration, output_file)
# validate_sound(audio_file1, audio_file2)