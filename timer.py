import time

class stopwatch: 
  def __init__(self):
    self.start_time= 0
    self.elapsed_time =0
    self.running= False
#this is to have a the stopwatch begin at 0.
  
  def start(self):
    if not self.running:
      self.start_time=time.time()
      self.running=True
#this is to start the timer. This will get changed once the hangman program is complete. Reason: the variables are needed in order to start at the begining.

  def stop(self):
    if self.running:
      self.elapsed_time += time.time() - self.start_time
      self.running=False
#This is to stop the timer. This will also get changed once the hangman program is complete. Reason: the variables are needed on order to end once the round of hangman game is complete.

  def reset(self):
    self.start_time= 0
    self.elapsed_time=0
    self.running=False
#This is to make sure the stopwatch is restet for the next round of hangman.     

  def get_time(self):
    if self.running: 
      return self.elapsed_time+ time.time() -self.start_time
    else:
      return self.elapsed_time
#This will allows us to save the time and later show the amount of time it took.   

  def display_time(self):
    elapsed= self.get_time()
    minutes, seconds = divmod(elapsed, 60) 
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
#This will show the user the amount of time it took to complete.     

if __name__ =="__main__" :
  stopwatch=Stopwatch()


   stopwatch.start()
    time.sleep(2)
    stopwatch.stop()

    print(f"It took", {stopwatch.display_time()},"this long to complete this round of hangman.")

#Parts will be changed once all coding for other parts are finished.
