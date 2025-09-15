import datetime
import time
import sys
import pygame
pygame.mixer.init()
alam_sound="alam_project\\alam.wav"

def main()-> None:
    while True:
        try:
            now=datetime.datetime.today()
            current_time=now.replace(microsecond=0).time()

            print(f"TIME:{current_time}\n")
            user_input=input("H M S or exit:").strip().lower()
            if user_input.startswith("e"):
                sys.exit()
            
            user_input=datetime.datetime.strptime(user_input,"%H %M %S").time()

            result=compare(usertime=user_input,current_time=current_time)
            if result is None:
                continue
            display_time(user_input)

        except Exception as e:
            print(f"Continuing...\n{e}")
            continue

def compare(usertime,current_time):
    if usertime > current_time:
        return True
    
    print("Time not valid!!")
    return None
    
def display_time(usertime):
    while True:
        try:
            now=datetime.datetime.today()
            currant_time=now.replace(microsecond=0).time()
            if usertime >= currant_time:
                print(f"{currant_time}",end="\r")
                sys.stdout.flush()

            elif usertime <= currant_time:
                print("Wake UP!!😴")
                pygame.mixer.music.load(alam_sound)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                return True
            time.sleep(1)
        except Exception as e:
            print(f"Continue!!\n{e}")

if __name__ =="__main__":
    print("================")
    print("===alam clock===")
    print("================")
    main()
