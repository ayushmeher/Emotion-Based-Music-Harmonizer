import pydub
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import low_pass_filter, high_pass_filter, speedup

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
    bass = low_pass_filter(bass, 100).apply_gain(+5)
    harmony = low_pass_filter(harmony, 150).apply_gain(+3)

    # Mix tracks
    mixed = melody.overlay(harmony).overlay(bass).overlay(percussion)

    return mixed

def mix_sad(melody, harmony, bass, percussion):
    """
    Mix tracks for a sad emotion.
    """
    # Apply low-pass filters to reduce high frequencies
    melody = high_pass_filter(melody, 1000)
    harmony = high_pass_filter(harmony, 1000)

    # Reduce volume
    melody = melody - 5
    harmony = harmony - 5

    # Add reverb-like effect using repetition
    bass = bass + 2
    bass = bass.overlay(bass, times=2).apply_gain(-10)

    # Mix tracks
    mixed = melody.overlay(harmony).overlay(bass).overlay(percussion)

    return mixed

def mix_energetic(melody, harmony, bass, percussion):
    """
    Mix tracks for an energetic emotion.
    """
    # Speed up tempo
    melody = speedup(melody, 1.1)
    harmony = speedup(harmony, 1.1)
    bass = speedup(bass, 1.1)

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

def main():
    # Load tracks
    melody_path = "melody.wav"
    harmony_path = "harmony.wav"
    bass_path = "bass.wav"
    percussion_path = "percussion.wav"
    melody, harmony, bass, percussion = load_tracks(melody_path, harmony_path, bass_path, percussion_path)

    # Get user emotion input
    emotion = input("Enter your emotion (calm, sad, energetic): ")

    # Mix tracks based on user emotion
    if emotion == "calm":
        mixed_audio = mix_calm(melody, harmony, bass, percussion)
    elif emotion == "sad":
        mixed_audio = mix_sad(melody, harmony, bass, percussion)
    elif emotion == "energetic":
        mixed_audio = mix_energetic(melody, harmony, bass, percussion)
    else:
        print("Invalid emotion input.")
        return

    # Export mixed audio
    output_path = "mixed_audio.wav"
    export_mixed_audio(mixed_audio, output_path)

    print("Mixed audio exported to", output_path)

if __name__ == "__main__":
    main()
