from datetime import datetime

class Timer:

    def __init__(self, title) -> None:
        self.title = title
        self.start = datetime.now()

    def stop(self):
        end = datetime.now()
        print(f"{self.title} - {end - self.start}")
