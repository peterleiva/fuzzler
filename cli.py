#!/usr/bin/env python3

import sys
from net_client import NetClient

def main():
    if len(sys.argv) != 3:
        print("Usage: fuzzler.py <host> <port>")
        exit(1)

    host, port = sys.argv[1:]
    port = int(port)

    print(f"[+] Connecting to {host}:{port}...")

    client = NetClient(host, port)
    client.connect()
    
    client.send("A" * 1000)
    
    # print(f"[+] Closing to {host}:{port}...")
    # client.close()

if __name__ == "__main__":
    main()