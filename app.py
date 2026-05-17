import os
import requests
import time

TOKEN = "8989165610:AAHISf-9CV4xmLWDRNV91jUlOk-RqEd45-A"
CHAT_ID = "1721410650"

def send_alert(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg})

def get_failed_logins():
    cmd = "grep 'Failed password' /var/log/auth.log | wc -l"
    return os.popen(cmd).read().strip()

print("SOC Operator Mode Active")
send_alert("System Monitoring Online (SOC L1 Mode)")

import subprocess

def monitor_log():
    process = subprocess.Popen(['tail', '-F', '/var/log/auth.log'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("👀 Monitoring auth.log in real-time...")

    while True:
        line = process.stdout.readline().decode('utf-8')
        if "Failed password" in line:
            send_alert(f" REAL-TIME ALERT!\nUnauthorized login attempt detected!\nDetails: {line.strip()}")

monitor_log()
