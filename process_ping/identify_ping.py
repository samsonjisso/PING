from process_ping.execute_ping import ping_ip
from process_ping.downIps_ping import downIps

def identify_ping(ip_address, downStatus):
    """Pings an IP address and returns the results."""  
    result = ping_ip(ip_address)
    if result == 0:
        return "UP"
    else:
        return downIps(ip_address, downStatus) 

if __name__ == "__main__":
    identify_ping()
