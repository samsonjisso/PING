from json import load
from pathlib import Path
from process_ping.identify_ping import identify_ping

def open_file_ping():
   """Pings a list of IP addresses and prints the results."""
   file_path  = Path(__file__).parent / "ip_addresses.json"
   with open(file_path, "r") as file:
      jsonData = load(file)
      print("=============================")

      for ip_address in jsonData:
        ip_address = ip_address.strip()
        downStatus = jsonData[ip_address]["DownStatus"]
        print(f"Pinging {ip_address}: {identify_ping(ip_address, downStatus)}")
   
      print("=============================")

if __name__ == "__main__":
   open_file_ping()
