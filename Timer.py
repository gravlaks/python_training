import time
class Timer:
    def __init__(self, duration):
        self.startTime = time.time()
        self.duration = duration
    def timeout(self):
        return time.time()-self.startTime>self.duration

    def reset(self):
        self.startTime = time.time()
