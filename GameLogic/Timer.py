import time
import pygame

from Components.Styles import draw_text
from Components.Config import GAME_DURATION, CLOSE_TO_END_BY, WHITE, RED

class Timer:
    def __init__(self):
        self.game_time = GAME_DURATION
        self.alert_user = False
        self.color = WHITE
        self.time_close = CLOSE_TO_END_BY
        self.timesup_audio = pygame.mixer.Sound("assets/audio/beep.mp3")

    def start(self):
        self.start = time.time()

    def time_passed(self):
        return round((time.time() - self.start), 0)

    def time_end(self):
        return self.time_passed() >= self.game_time

    def check_time(self):
        if self.alert_user:
            return

        if (self.time_passed() + self.time_close) >= self.game_time:
            self.color = RED
            self.alert_user = True
            

    def alert(self):
        if self.time_end():
            return

        if self.alert_user:
            self.timesup_audio.play()
            self.time_close = 0
            self.alert_user = False

    def tick(self, screen):
        self.check_time()
        self.display(screen)
        self.alert()

    def display(self, screen):
        passed = int(self.time_passed())
        
        sec = passed % 60
        minutes = passed // 60
        time = f'{minutes} : {sec}'

        draw_text(screen, 32, time, 40, 20, self.color)