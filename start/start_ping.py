from time import localtime, strftime
from util.delayCounter import delay
from process_ping.open_file_ping import open_file_ping
from ping_wait_time import ping_wait_for_time
from datetime import datetime
  
def start():  
  time_now = datetime.now().time()
  period = strftime("%p", localtime())
  if (period == "AM"):
    if (time_now.hour >= 8 and time_now.hour < 9):
      open_file_ping()
      delay(sleepTime = 3)
    elif(time_now.hour >= 9):
      open_file_ping()
      delay()
    else:
        ping_wait_for_time(start, current_hour=time_now.hour, current_minute= time_now.minute)
  elif (period == "PM"):
    if (time_now.hour <= 18):
      open_file_ping()
      delay()
    else:
       ping_wait_for_time(start, current_hour=time_now.hour, current_minute= time_now.minute)
if __name__ == "__main__":
  start()