
# Emotion-Based Music Harmonizer

The **Emotion-Based Music Harmonizer** is a Python-based tool that allows users to mix multiple audio tracks (melody, harmony, bass, and percussion) based on a chosen emotion — calm, sad, or energetic. Using `pydub` for audio processing and `tkinter` for a GUI, this harmonizer adjusts elements in each track to evoke the desired emotional tone and exports the final mixed audio in WAV format.

## Project Structure

The project consists of two main files:

- **Emotion_Based_Music_Harmonizer.py**: Contains the core audio processing functions and handles the mixing logic.
- **GUI_Integration_Using_Tkinter.py**: Provides a graphical interface for selecting music tracks and emotion options, and allows exporting the final mixed audio.

## Features

- **Emotion-Based Mixing**: Choose from calm, sad, or energetic moods, each applying unique audio effects.
- **Track Customization**: Each emotion uses specific processing effects, such as volume adjustments, speed changes, and frequency filtering.
- **Audio Export**: Save the mixed output as a WAV file with an emotion-specific filename.

## Requirements

- Python 3.x
- [pydub](https://github.com/jiaaro/pydub) for audio processing
- tkinter (pre-installed with Python)

To install `pydub`, run:
```bash
pip install pydub
```

### System Requirements
Ensure `ffmpeg` or `libav` is installed for `pydub` to handle WAV file formats.

## Usage

### Command-Line Interface (CLI):
1. Run `Emotion_Based_Music_Harmonizer.py`:
    ```bash
    python Emotion_Based_Music_Harmonizer.py
    ```
2. Provide paths to `melody`, `harmony`, `bass`, and `percussion` WAV files.
3. Enter an emotion (`calm`, `sad`, or `energetic`).
4. The script mixes the tracks and saves the output as `mixed_audio.wav`.

### GUI Application:
1. Run `GUI_Integration_Using_Tkinter.py` to open the graphical interface:
    ```bash
    python GUI_Integration_Using_Tkinter.py
    ```
2. Use the "Browse" buttons to load WAV files for each track.
3. Select an emotion from the dropdown.
4. Click **Mix and Export** to create and save the mixed audio file.

## Emotion-Based Mixing Details

Each emotion applies unique adjustments to create the desired soundscape:

- **Calm**: Reduces percussion volume, adds low-pass filters to bass and harmony for a soothing effect.
- **Sad**: Lowers high frequencies, reduces volume, and adds a reverb-like effect to bass for a melancholic tone.
- **Energetic**: Increases tempo, emphasizes percussion, and overlays all tracks for a high-energy mix.

## Function Overview

- `load_tracks()`: Loads WAV files as `pydub` audio segments.
- `mix_calm()`, `mix_sad()`, `mix_energetic()`: Adjusts audio based on chosen emotion.
- `export_mixed_audio()`: Exports the mixed audio as a WAV file.

### GUI Components

- **File Browsing**: Load WAV files for each track using "Browse" buttons.
- **Emotion Selection**: Choose an emotion from a dropdown menu.
- **Mix and Export**: Generates and saves the mixed audio file based on the selected emotion.

## Example

To create a calm mix:

1. Load `melody.wav`, `harmony.wav`, `bass.wav`, and `percussion.wav`.
2. Select "Calm" in the dropdown.
3. Click **Mix and Export**.
4. The output file `calm_mixed.wav` is saved in the directory.

## Contributing

Contributions are welcome! Feel free to submit pull requests to add new features or report any issues.

## Output

![Screenshot 2024-10-29 172157](https://github.com/user-attachments/assets/aa6dfe14-97fc-4f72-8ee3-f0be1a51992c)
