import time
import datetime
import pygame

sound_file = 'alarm.mp3'
pygame.init()


def set_alarm():
    alarm_time = input(f'Enter a time for alarm (HH:MM:SS); ').strip()

    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        while now != alarm_time:
            print(now)
            time.sleep(1)
            now = datetime.datetime.now().strftime("%H:%M:%S")

        print("WAKE UP!")

        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)

        pygame.mixer.music.play()

        order = input('What do you want to next: quit or set again?(q / s) ').lower()
        while order != 'q' and order != 's':
            order = input('What do you want to next: quit or set again?(q / s) ').lower()

        if order == 'q':
            print('Thank you for using AlarmClock, Have a nice day!')
            exit()
        elif order == 's':
            pygame.mixer.music.stop()
            set_alarm()


set_alarm()









