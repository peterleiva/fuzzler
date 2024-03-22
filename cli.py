#!/usr/bin/env python3

import sys
from net_client import NetClient

def main():
    if len(sys.argv) != 3:
        print("Usage: fuzzler.py <host> <port>")
        exit(1)

    host, port = sys.argv[1:]
    port = int(port)


    data = "A"
    body = [data]
    for i in range(1, 50):
        body.append(data * (100 * i))
    
    print(f"[+] Connecting to {host}:{port}...")
    client = NetClient(host, port)
    client.connect()
    
    
    for data in body:
        print(f"[+] Sending {len(data)} bytes...")
        client.send(data)

    print(f"[+] Closing to {host}:{port}...")
    client.close()

if __name__ == "__main__":
    main()