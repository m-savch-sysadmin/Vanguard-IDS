import os
import requests
import subprocess
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TOKEN = "8989165610:AAHlSf-9CV4xmLWDRNV91jUlOk-RqEd45-A"
CHAT_ID = "1721410650"
SPLUNK_TOKEN = "3651f4bb-1351-4059-b0d8-e83094be0873"
SPLUNK_URL = "https://192.168.56.1:8088/services/collector/event"

def send_alerts(alert_text):
    try:
        telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(telegram_url, json={"chat_id": CHAT_ID, "text": alert_text, "parse_mode": "Markdown"}, timeout=5)
    except Exception as e:
        print(f"Telegram alert route failed: {e}")

    headers = {"Authorization": f"Splunk {SPLUNK_TOKEN}"}
    payload = {"event": alert_text}
    try:
        requests.post(SPLUNK_URL, headers=headers, json=payload, verify=False, timeout=5)
    except Exception as e:
        print(f"Splunk SIEM route failed: {e}")

def monitor_log():
    print("Vanguard Monitoring Engine is liveee")
    process = subprocess.Popen(['tail', '-F', '/var/log/auth.log'], stdout=subprocess.PIPE)
    
    while True:
        line = process.stdout.readline().decode('utf-8')
        if not line:
            break
        
        if "Failed password" in line:
            clean_log = line.strip()
            msg = f" *BRUTE FORCE DETECTED* \nLog: `{clean_log}`"
            send_alerts(msg)

if __name__ == "__main__":
    monitor_log()
