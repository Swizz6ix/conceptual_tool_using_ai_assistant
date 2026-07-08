import time


def loading(message:str = 'Launching', duration:int = 2):
    for _ in range(duration * 4):
        for dots in [". ", ".. ", "..."]:
            print(f"\r{message}{dots}", end="", flush=True)
            time.sleep(0.25)
    print("\rLaunching...Done!      ")