#!/usr/bin/env python3
"""
safe_api_client.py
A small command-line tool to send credentials to your own server endpoint.

Usage:
    autosql.py -u myuser@example.com -p MyPass123 -U https://example.com/signup -A "Mozilla/5.0"
"""

import argparse
import requests

# command line argument
parser = argparse.ArgumentParser(description="send credentials to your server endpoint")
parser.add_argument("-u", "--username", required=True, help="Username or email")
parser.add_argument("-p", "--password", required=True, help="Password")
parser.add_argument("-U", "--url", required=True, help="Target URL to send to")
parser.add_argument("-A", "--agent", default="MyCLIClient/1.0",
                    help="User-Agent string to send (default MyCLIClient/1.0)")

args = parser.parse_args()

# --- Build payload ---
payload = {
    "email": args.username,
    "password": args.password,
}

# --- Headers (including User-Agent) ---
headers = {
    "User-Agent": args.agent,
    "Content-Type": "application/x-www-form-urlencoded",
}

try:
    resp = requests.post(args.url, data=payload, headers=headers, timeout=15)
    print(f"Status: {resp.status_code}")
    print(f"Response (first 500 chars):\n{resp.text[:500]}")
except requests.RequestException as e:
    print("Error sending request:", e)