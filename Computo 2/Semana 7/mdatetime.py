import time
import os

while True:
    hora = time.strftime("%H:%M:%S")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(hora)
    time.sleep(1)