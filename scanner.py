import subprocess
import ipaddress
import socket

network = ipaddress.ip_network("172.16.9.0/24", strict=False)

def ping(ip):
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", str(ip)],
        capture_output=True
    )
    return result.returncode == 0

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(str(ip))
        return hostname[0]
    except socket.herror:
        return "Unknown"

print("Starting scan on network: 172.16.9.0/24")
print("Please wait...")
print("")

active_devices = []

for ip in network.hosts():
    if ping(ip):
        hostname = get_hostname(ip)
        print(f"Device found: {ip}  →  {hostname}")
        active_devices.append({"ip": str(ip), "hostname": hostname})

print("")
print("Scan complete!")
print(f"Total devices found: {len(active_devices)}")
