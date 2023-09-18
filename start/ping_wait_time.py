from time import sleep
from sys import exit

def ping_wait_for_time(func, current_hour:int, current_minute:int):
    wait_time:int = 0
    print("Ping starts by default at 8:00 AM")
    if current_hour < 8:
        hr_diff_8hr = 8 - current_hour
        AM_hr_diff_in_sec = hr_diff_8hr * 3600
        current_minute_to_sec = current_minute * 60
        wait_time  = AM_hr_diff_in_sec - current_minute_to_sec
    elif current_hour > 18:
        hr_diff_24hr = 24 - current_hour
        time_plus_8hr = 8 + hr_diff_24hr
        PM_time_diff_in_sec = time_plus_8hr * 3600
        current_minute_to_sec = current_minute * 60
        wait_time  = PM_time_diff_in_sec  - current_minute_to_sec
    else:
        hr_diff_in_sec = 8 * 3600
        current_minute_to_sec = current_minute * 60
        wait_time = hr_diff_in_sec - current_minute_to_sec
    try:
        sleep(wait_time)
        func()
    except:
        if(KeyboardInterrupt):
            print("^c")
            exit()
        else:
            print("error")
if __name__ == "__main__":
    ping_wait_for_time()