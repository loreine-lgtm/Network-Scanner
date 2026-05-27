# TsanaShield Network Scanner

A Python network scanner that discovers all active devices on a network and identifies them by hostname.

## Built by
Tsanang Momo Loreine — Year 2 Computer Science (Cybersecurity Track)

## How it works
- Scans a /24 network range
- Pings each address to check if a device is active
- Resolves hostnames for identified devices

## How to run
```bash
python3 scanner.py
```

## Tools used
- Python 3
- socket
- ipaddress
- subprocess
