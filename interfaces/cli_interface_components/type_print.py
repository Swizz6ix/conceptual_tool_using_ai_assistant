import time


def type_print(text, delay = 0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()