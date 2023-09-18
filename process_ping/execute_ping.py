from subprocess import run
from time import sleep
from sys import exit

def ping_ip(ipAddress, pause_minute:int = 0, pingLoop:int = 1):
    try:
        if pause_minute != 0:
            pause_minute *= 60
            sleep(pause_minute)
        pingResult = run(["ping", "-n", f"{pingLoop}", ipAddress], capture_output=True)
    except:
        if KeyboardInterrupt:
            print("control -c")
            exit()
        elif Exception:
            print({" ping_ip function Exception": Exception})
        else:
            print("error occured")
    return pingResult.returncode

if __name__ == "__main__":
    ping_ip()