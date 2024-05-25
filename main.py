import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

from Game import *

# Example usage
game = Game()
game.start()