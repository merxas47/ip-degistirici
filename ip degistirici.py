import os
import time

ip_addresses = ["192.168.1.100", "192.168.1.101", "192.168.1.102",]

while True:
    for ip in ip_addresses:
        os.system(f"ifconfig eth0 down")
        os.system(f"ifconfig eth0 {ip}")
        os.system("ifconfig eth0 up")
        print(f"IP address changed to {ip}")
        time.sleep(5)
