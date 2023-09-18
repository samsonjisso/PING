from tqdm import tqdm
from time import sleep, localtime, time, strftime
from sys import exit
#delay function 
def delay(sleepTime:float = 108, msg:str = "next ping on : "):
    try:
        tqdmCount = sleepTime * 100
        time_now = time()
        three_hr_after = time_now + tqdmCount
        timeFormatted = strftime("%I %M %p", localtime(three_hr_after))
        for i in tqdm (range(100), desc=msg + timeFormatted):
            sleep(sleepTime)
    except :
        if(KeyboardInterrupt):
            print("control -c")
            exit()
        elif(Exception):
            print(Exception)

if __name__ == "__main__":
    delay()