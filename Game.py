"""
The implementation of the Space Invader game, using the Display, Light, Button, and Buzzer Classes. 
GPT4 model was used to consult logic and check for errors.
"""

from Button import *
from Buzzer import *
from Displays import *
from LightStrip import *
import random
import time

# Define colors for aliens
Alien_Colors = {
    'white': WHITE,
    'red': RED,
    'yellow': YELLOW,
    'blue': BLUE
}

class AlienBase:
    """
    Represents the base of an alien in the game.
    Handles the color and size of the alien base.
    """
    def __init__(self, lightstrip):
        """
        Initialize the alien base with a random color and size of 1.
        """
        self.color = random.choice(list(Alien_Colors.values()))
        self.size = 1  # Initial size of alien base
        self.lightstrip = lightstrip
        self.lightstrip.setColor(self.color, self.size)  # Set the initial color on the lightstrip
    
    def grow(self):
        """
        Increases the size of the alien base by 1, up to a maximum of 16.
        Updates the lightstrip to reflect the new size.
        """
        if self.size < 16:  # Check to prevent the size from exceeding 16
            self.size += 1
            self.lightstrip.setColor(self.color, self.size)

    def is_at_fullsize(self):
        """
        Checks if the alien base has reached its full size.
        """
        return self.size >= 16

class Player:
    """
    Represents the player in the game.
    Handles the player's score.
    """
    def __init__(self):
        """
        Initialize the player with a score of 0.
        """
        self.score = 0

    def hit(self):
        """
        Increments the player's score by 1 when the player hits an alien.
        """
        self.score += 1 

    def miss(self):
        """
        Decrements the player's score by 1 when the player misses an alien.
        Prevents the score from going negative.
        """
        if self.score > 0:  # Prevents the score from going negative
            self.score -= 1

class Game:
    """
    Represents the main game logic.
    Handles the game loop, display updates, and interactions with other components.
    """
    def __init__(self):
        """
        Initialize the game with display, lightstrip, buzzer, buttons, alien bases, and player.
        """
        self._display = LCDDisplay(sda=0, scl=1, i2cid=0)  # Initialize the LCD display using I2C
        self._lightstrip = LightStrip(name='Neo', pin=2, numleds=16)
        self._buzzer = PassiveBuzzer(17)
        self._buttons = [Button(21, 'white', buttonhandler=self.button_pressed),
                         Button(20, 'red', buttonhandler=self.button_pressed),
                         Button(19, 'yellow', buttonhandler=self.button_pressed),
                         Button(18, 'blue', buttonhandler=self.button_pressed)]
        self._alien_bases = [AlienBase(self._lightstrip) for _ in range(4)]  # Assuming 4 alien bases
        self._player = Player()
        self._last_hit_color = None

    def start(self):
        """
        Starts the game loop.
        Sets up the initial state and runs the loop until an alien base reaches full size.
        """
        self._lightstrip.setBrightness(1)  # Set brightness to 100%
        self._display.reset()  # Clear the display at the start
        self._lightstrip.on()  # Turn on the lightstrip
        while not any(alien_base.is_at_fullsize() for alien_base in self._alien_bases):
            self._update_display()
            self._check_for_hits()
            self._grow_aliens()
            self._check_game_over()
            time.sleep(1)  # Slow down the game loop by 1 second

    def _update_display(self):
        """
        Updates the display with the current score of the player.
        """
        self._display.showText(f"Score: {self._player.score}", row=0, col=0)

    def _check_for_hits(self):
        """
        Checks if the last hit color matches any alien base's color.
        If a match is found, the player scores a hit and the alien base shrinks.
        """
        if self._last_hit_color:
            for alien_base in self._alien_bases:
                if alien_base.color == self._last_hit_color:
                    self._player.hit()
                    alien_base.size = max(alien_base.size - 1, 0)
                    self.lightstrip.setColor(alien_base.color, alien_base.size)
                    self._last_hit_color = None
                    return True
        return False

    def _grow_aliens(self):
        """
        Grows each alien base by 1 size.
        """
        for alien_base in self._alien_bases:
            alien_base.grow()

    def _check_game_over(self):
        """
        Checks if any alien base has reached full size, indicating game over.
        """
        if any(alien_base.is_at_fullsize() for alien_base in self._alien_bases):
            self._end_game()

    def _end_game(self):
        """
        Ends the game.
        Displays the game over message and the player's final score.
        Plays a tone on the buzzer and turns off the lightstrip.
        """
        self._display.showText("Game Over!", row=1, col=0)
        self._display.showNumber(self._player.score, row=1, col=11)
        self._buzzer.play_tone('A4', 500)
        self._lightstrip.off()

    def button_pressed(self, button):
        """
        Handles button press events.
        Determines the color of the pressed button and processes hits accordingly.
        """
        button_color = Alien_Colors[button.color_name]
        self._last_hit_color = button_color
        for alien_base in self._alien_bases:
            if alien_base.color == button_color:
                alien_base.size = max(alien_base.size - 1, 0)
                self.lightstrip.setColor(alien_base.color, alien_base.size)
                self._player.hit()
                break
