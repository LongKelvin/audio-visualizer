import pygame
from audio_input import AudioInput
from db_calculator import DBCalculator
from visualizer import Visualizer
import numpy as np
import pyaudio
import time

def main():
    audio = AudioInput()
    db_calculator = DBCalculator(-100,0,150)
    visualizer = Visualizer()

    def stream_callback(in_data, frame_count, time_info, status):
        audio_data = np.frombuffer(in_data, dtype=np.float32)
        db_level = db_calculator.calculate_db(audio_data)
        visualizer.update(audio_data, db_level)
        return (in_data, pyaudio.paContinue)


    audio.start_stream(stream_callback)

    try:
        while visualizer.check_events():
            time.sleep(0.1)  # Add a small delay to reduce CPU usage
    except KeyboardInterrupt:
        pass
    finally:
        audio.stop_stream()
        pygame.quit()

if __name__ == "__main__":
    main()
