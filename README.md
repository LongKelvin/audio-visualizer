

## Real-Time Audio Waveform Visualizer

This project is a personal Python-based real-time audio waveform visualizer using `pygame` for visualization and `pyaudio` for capturing audio input. 

The visualizer responds to live audio and dynamically changes the waveform color based on the sound level (dB). 

Additionally, a shadow effect creates a glowing visual for an enhanced experience.


## Features

* **dB real-time capture**: Continuously measures and displays the current decibel (dB) level of the audio input.
* **Real-time waveform visualization**: Display live audio waveform based on microphone input.
* **Dynamic color changes**: The waveform color changes smoothly depending on the current dB level.
* **Glow/Shadow effect**: Adds depth and aesthetics to the waveform rendering.

## Installation

Clone the repository and install the required dependencies using the following command:

```bash
git clone https://github.com/LongKelvin/audio-visualizer.git
cd audio-visualizer
pip install -r requirements.txt
```


## Running the Visualizer

After installing the dependencies, you can run the visualizer using:

Bash

```
python main.py
```


## Usage

The application will start a window showing the live waveform from your microphone input. 
The waveform will dynamically change its color depending on the volume level (measured in dB). 

Press Ctrl+C in the terminal or close the window to stop the application.