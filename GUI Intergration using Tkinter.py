import tkinter as tk
from tkinter import filedialog
import pydub
from pydub import AudioSegment
from pydub.playback import play
from scipy.signal import butter, lfilter
import numpy as np

# Custom low-pass filter
def low_pass_filter(audio, cutoff_freq):
    nyquist = 0.5 * audio.frame_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(5, normal_cutoff, btype='low', analog=False)
    audio_data = np.frombuffer(audio.raw_data, dtype=np.int16)
    filtered_data = lfilter(b, a, audio_data)
    return AudioSegment(
        data=filtered_data.astype(np.int16).tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=audio.sample_width,
        channels=audio.channels
    )

# Custom high-pass filter
def high_pass_filter(audio, cutoff_freq):
    nyquist = 0.5 * audio.frame_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(5, normal_cutoff, btype='high', analog=False)
    audio_data = np.frombuffer(audio.raw_data, dtype=np.int16)
    filtered_data = lfilter(b, a, audio_data)
    return AudioSegment(
        data=filtered_data.astype(np.int16).tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=audio.sample_width,
        channels=audio.channels
    )

def load_tracks(melody_path, harmony_path, bass_path, percussion_path):
    """
    Load WAV format tracks.
    """
    melody = AudioSegment.from_wav(melody_path)
    harmony = AudioSegment.from_wav(harmony_path)
    bass = AudioSegment.from_wav(bass_path)
    percussion = AudioSegment.from_wav(percussion_path)

    return melody, harmony, bass, percussion

def mix_calm(melody, harmony, bass, percussion):
    """
    Mix tracks for a calm emotion.
    """
    # Reduce percussion strength
    percussion = percussion - 10

    # Emphasize bass and harmony with low-pass filters
    bass = low_pass_filter(bass, 100) + 5
    harmony = low_pass_filter(harmony, 150) + 3

    # Mix tracks
    mixed = melody.overlay(harmony).overlay(bass).overlay(percussion)

    return mixed

def mix_sad(melody, harmony, bass, percussion):
    """
    Mix tracks for a sad emotion.
    """
    # Apply high-pass filters to reduce high frequencies
    melody = high_pass_filter(melody, 1000)
    harmony = high_pass_filter(harmony, 1000)

    # Reduce volume
    melody = melody - 5
    harmony = harmony - 5

    # Add reverb-like effect using repetition
    bass = bass + bass - 10

    # Mix tracks
    mixed = melody.overlay(harmony).overlay(bass).overlay(percussion)

    return mixed

def mix_energetic(melody, harmony, bass, percussion):
    """
    Mix tracks for an energetic emotion.
    """
    # Speed up tempo
    melody = melody.set_frame_rate(int(melody.frame_rate * 1.1))
    harmony = harmony.set_frame_rate(int(harmony.frame_rate * 1.1))
    bass = bass.set_frame_rate(int(bass.frame_rate * 1.1))

    # Enhance percussion track
    percussion = percussion + 5

    # Mix tracks
    mixed = melody.overlay(harmony).overlay(bass).overlay(percussion)

    return mixed

def export_mixed_audio(mixed_audio, output_path):
    """
    Export mixed audio to WAV file.
    """
    mixed_audio.export(output_path, format="wav")

def browse_file(entry):
    """
    Browse file and update entry field.
    """
    filename = filedialog.askopenfilename(title="Select WAV file", filetypes=[("WAV files", "*.wav")])
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def mix_and_export():
    """
    Mix tracks based on selected emotion and export mixed audio.
    """
    melody_path = melody_entry.get()
    harmony_path = harmony_entry.get()
    bass_path = bass_entry.get()
    percussion_path = percussion_entry.get()

    if not melody_path or not harmony_path or not bass_path or not percussion_path:
        status_label.config(text="Please select all tracks.")
        return

    emotion = emotion_var.get()
    if not emotion:
        status_label.config(text="Please select an emotion.")
        return

    melody, harmony, bass, percussion = load_tracks(melody_path, harmony_path, bass_path, percussion_path)

    if emotion == "Calm":
        mixed_audio = mix_calm(melody, harmony, bass, percussion)
    elif emotion == "Sad":
        mixed_audio = mix_sad(melody, harmony, bass, percussion)
    elif emotion == "Energetic":
        mixed_audio = mix_energetic(melody, harmony, bass, percussion)

    output_path = f"{emotion.lower()}_mixed.wav"
    export_mixed_audio(mixed_audio, output_path)

    status_label.config(text=f"Mixed audio exported to {output_path}")

root = tk.Tk()
root.title("Emotion-Based Music Mixer")

# Create track entry fields
melody_label = tk.Label(root, text="Melody:")
melody_label.grid(row=0, column=0, padx=5, pady=5)
melody_entry = tk.Entry(root, width=50)
melody_entry.grid(row=0, column=1, padx=5, pady=5)
melody_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(melody_entry))
melody_browse_button.grid(row=0, column=2, padx=5, pady=5)

harmony_label = tk.Label(root, text="Harmony:")
harmony_label.grid(row=1, column=0, padx=5, pady=5)
harmony_entry = tk.Entry(root, width=50)
harmony_entry.grid(row=1, column=1, padx=5, pady=5)
harmony_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(harmony_entry))
harmony_browse_button.grid(row=1, column=2, padx=5, pady=5)

bass_label = tk.Label(root, text="Bass:")
bass_label.grid(row=2, column=0, padx=5, pady=5)
bass_entry = tk.Entry(root, width=50)
bass_entry.grid(row=2, column=1, padx=5, pady=5)
bass_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(bass_entry))
bass_browse_button.grid(row=2, column=2, padx=5, pady=5)

percussion_label = tk.Label(root, text="Percussion:")
percussion_label.grid(row=3, column=0, padx=5, pady=5)
percussion_entry = tk.Entry(root, width=50)
percussion_entry.grid(row=3, column=1, padx=5, pady=5)
percussion_browse_button = tk.Button(root, text="Browse", command=lambda: browse_file(percussion_entry))
percussion_browse_button.grid(row=3, column=2, padx=5, pady=5)

# Create emotion selection dropdown
emotion_var = tk.StringVar()
emotion_var.set("Select Emotion")
emotion_options = ["Calm", "Sad", "Energetic"]
emotion_dropdown = tk.OptionMenu(root, emotion_var, *emotion_options)
emotion_dropdown.grid(row=4, column=1, padx=5, pady=5)

# Create mix and export button
mix_and_export_button = tk.Button(root, text="Mix and Export", command=mix_and_export)
mix_and_export_button.grid(row=5, column=1, padx=5, pady=5)

# Create status label
status_label = tk.Label(root, text="")
status_label.grid(row=6, column=1, padx=5, pady=5)

root.mainloop()
