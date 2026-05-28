# Vanguard-IDS: Real-Time Brute Force Monitor with Telegram & Splunk Alerts

A lightweight Python project that turns a Linux server into a basic Host Intrusion Detection System (HIDS). The script monitors system authentication logs in real-time, detects SSH brute force attempts, and automatically sends alerts to a Telegram chat and a central Splunk SIEM instance.

## Why I Built This

I built this project in my homelab to understand how SOC analysts collect and analyze log data. It covers several important cybersecurity requirements:
* **Log Analysis:** Tracking live system telemetry via Linux logs.
* **Network Infrastructure:** Bridging data across different network layers (VirtualBox VM to Host OS).
* **SIEM Ingestion:** Authenticating and sending structured payloads to Splunk over a secure HTTPS port.

## Infrastructure Setup

* **Attacked Machine:** Ubuntu Server running inside VirtualBox.
* **SIEM Monitoring:** Splunk Enterprise installed on the Windows Host machine.
* **Alert Channel:** Telegram Bot API.

## Project Files

* `app.py` - The main Python script that tails logs, parses alerts, and handles API calls.
* `requirements.txt` - Python dependencies (`requests` and `urllib3`).

## How It Works

1. The script reads the `/var/log/auth.log` file continuously using a subprocess execution of the `tail -F` command.
2. It screens every line looking for the `"Failed password"` string signature.
3. When a match is found, it extracts the raw log and builds an alert message.
4. The script triggers a double HTTP POST request:
   * **Telegram:** Delivers a real-time message to a private group channel.
   * **Splunk:** Sends a JSON event structure to Splunk's HTTP Event Collector (HEC) on port 8088.

<img width="1280" height="139" alt="splunk" src="https://github.com/user-attachments/assets/4e1789a6-c962-40d1-bb3e-a7374aec0743" />
<img width="1836" height="755" alt="Screenshot 2026-05-25 191400" src="https://github.com/user-attachments/assets/d8bcdbe3-8e81-4424-b4db-84580afc937c" />
<img width="594" height="326" alt="Screenshot 2026-05-25 191227" src="https://github.com/user-attachments/assets/400ea3ee-28ed-41d7-85c9-bfc05b7914f9" />

