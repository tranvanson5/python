# audio_utils.py
import pygame

def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(10)  # Limit the frame rate of the loop
    except pygame.error as e:
        print(f"Pygame error occurred: {e}")
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        print("Keyboard interrupt received, stopping audio playback.")
    finally:
        pygame.mixer.quit()

# Initialize Pygame and Pygame mixer when this module is imported
pygame.init()
pygame.mixer.init()
