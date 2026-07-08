import itertools
import time


def spinner(message:str = 'Loading', seconds:float = 2.0):
    for c in itertools.cycle("|/-\\"):
        print(f"\r{message} {c}", end="", flush=True)
        time.sleep(0.1)
        seconds -= 0.1

        if seconds <= 0.0:
            break
    print("\r" + " " * 30, end="\r")