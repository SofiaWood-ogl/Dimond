import time

class stopwatch: 
  def __init__(self):
    self.start_time= 0
    self.elapsed_time =0
    self.running= False

  def start(self):
    if not self.running:
      self.start_time=time.time()
      self.running=True

  def stop(self):
    if self.running:
      self.elapsed_time += time.time() - self.start_time
      self.running=False

  def reset(self):
    self.start_time= 0
    self.elapsed_time=0
    self.running=False

  def get_time(self):
    if self.running: 
      return self.elapsed_time+ time.time() -self.start_time
    else:
      return self.elapsed_time

  def display_time(self):
    elapsed= self.get_time()
    minutes, seconds = divmod(elapsed, 60) 
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

if __name__ =="__main__" :
  stopwatch=Stopwatch()


   stopwatch.start()
    time.sleep(2)
    stopwatch.stop()

    print(f"It took", {stopwatch.display_time()},"this long to complete this round of hangman.")
