from util.downDataFormatter import downDataFormatter
from process_ping.execute_ping import ping_ip
from datetime import datetime
from time import strftime, localtime
from util.push_formatter import push_formatted
from push_notification.push_alert import push_notifiction

def downIps(ip_address, downStatus):
    print("=== down ip found ===")
    last_resultCode = ping_ip(ip_address, pingLoop = 1)
    # assign the arranged datas
    if last_resultCode != -1:
        dumpData = downDataFormatter(
            downStatus
        )
        formattedToPush = push_formatted(dumpData.downJson)
        time_now = datetime.now().time()
        period = strftime("%p", localtime())
        if period == "AM" and time_now.hour >= 9:
            push_notifiction(formattedToPush)
        elif period == "PM":
            push_notifiction(formattedToPush)
        return dumpData.formattedJson