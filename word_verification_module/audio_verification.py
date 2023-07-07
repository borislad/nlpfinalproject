import librosa
import numpy as np
import sounddevice as sd
from scipy.io import wavfile
import scipy.signal as sps
import soundfile as sf

def record_audio(duration, output_file):
    # Set the sampling rate and number of channels
    sample_rate = 44100  # CD quality audio
    channels = 1  # Mono audio

    # Calculate the number of samples based on the duration
    num_samples = int(duration * sample_rate)

    # Record audio from the microphone
    print("Recording audio...")
    audio = sd.rec(num_samples, samplerate=sample_rate, channels=channels)
    sd.wait()  # Wait for the recording to complete

    # Save the recorded audio to a WAV file
    wavfile.write(output_file, sample_rate, audio)

def compare_audio_files(file1, file2):
    # Load the audio files
    audio1, sample_rate1 = sf.read(file1)
    audio2, sample_rate2 = sf.read(file2)

    # Resample the audio signals if necessary
    if sample_rate1 != sample_rate2:
        audio2 = sps.resample(audio2, len(audio1))

    # Perform Fourier Transform on the audio signals
    spectrum1 = np.abs(np.fft.fft(audio1))
    spectrum2 = np.abs(np.fft.fft(audio2))

    # Normalize the spectra
    spectrum1 /= np.max(spectrum1)
    spectrum2 /= np.max(spectrum2)

    # Calculate the similarity measure (e.g., correlation coefficient)
    similarity = np.corrcoef(spectrum1, spectrum2)[0, 1]

    # Print the similarity score
    print("Similarity score:", similarity)

    # Set a similarity threshold
    similarity_threshold = 0.6

    # Compare the similarity with the threshold
    if similarity >= similarity_threshold:
        print("Sound validation successful. The audio signals match.")
        return True
    else:
        print("Sound validation failed. The audio signals do not match.")
        return False

# Example usage
# C:\Users\shabi\PycharmProjects\nlpfinalproject\word_verification_module
# audio_file1 = "C:\Users\shabi\PycharmProjects\nlpfinalproject\word_verification_module\Syllable_Record_chron_Fast.wav"
# audio_file1 = "C:\\Users\\shabi\\PycharmProjects\\nlpfinalproject\\word_verification_module\\Syllable_Record_chron_Fast.wav"

# audio_file1 = "Syllable_Record.wav"
# audio_file2 = "C:\\Users\\shabi\\PycharmProjects\\nlpfinalproject\\word_verification_module\\Syllable_Record_chron_Slow.wav"
# audio_file2 = "C:\Users\shabi\PycharmProjects\nlpfinalproject\word_verification_module\Syllable_Record_chron_Slow.wav"

# Recoding syllables for syllables_audio dir
# recording_duration = 2  # Duration in seconds
# output_file = r"C:\Users\shabi\PycharmProjects\nlpfinalproject\word_verification_module\syllables_audio/" + "ment" + ".wav"
# record_audio(recording_duration, output_file)
# print("Finished Recording")
# compare_audio_files(audio_file1, audio_file2)