# CyberSentinel EDR

A lightweight Endpoint Detection and Response (EDR) platform designed to provide real-time endpoint visibility, threat detection, system monitoring, and security event management. CyberSentinel EDR demonstrates core EDR capabilities through process analysis, network monitoring, file integrity verification, and centralized alerting.

## Overview

CyberSentinel EDR is a Python-based security monitoring solution built to help security practitioners understand the fundamentals of endpoint detection and response technologies. The platform continuously monitors endpoint activity, analyzes system behavior, detects suspicious events, and generates actionable security alerts through a centralized dashboard.

## Key Features

### Endpoint Monitoring

* Real-time process monitoring
* CPU and memory utilization tracking
* Network connection monitoring
* System resource visibility

### Threat Detection

* Blacklisted process detection
* Suspicious activity identification
* High resource usage detection
* Rule-based detection engine

### File Integrity Monitoring

* SHA-256 file hashing
* Integrity verification
* File change detection
* Baseline comparison support

### Alert Management

* Severity-based alert classification
* Centralized alert logging
* Security event tracking
* Historical alert records

### Reporting & Analytics

* Automated report generation
* Security event summaries
* Alert statistics and insights
* Incident documentation support

### Dashboard

* Web-based monitoring interface
* Live endpoint visibility
* Active alert management
* Security monitoring overview

---

## Technology Stack

| Component         | Technology            |
| ----------------- | --------------------- |
| Backend           | Python                |
| Web Framework     | Flask                 |
| Database          | SQLite                |
| ORM               | SQLAlchemy            |
| Authentication    | Flask-Login           |
| System Monitoring | Psutil                |
| Frontend          | HTML, CSS, JavaScript |

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/username/CyberSentinel-EDR.git
cd CyberSentinel-EDR
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch the Application

```bash
python run.py
```

Access the dashboard:

```text
http://127.0.0.1:5000
```

---

## Project Structure

```text
CyberSentinel-EDR/
│
├── app/               # Web application and dashboard
├── agent/             # Monitoring and detection engine
├── database/          # Database schemas and configuration
├── reports/           # Security report generation
├── tests/             # Unit and integration tests
├── docs/              # Project documentation
│
├── requirements.txt   # Project dependencies
├── config.py          # Application configuration
├── run.py             # Application entry point
└── README.md
```

---

## Detection Modules

| Module                 | Description                                  |
| ---------------------- | -------------------------------------------- |
| Process Detector       | Detects suspicious and blacklisted processes |
| CPU Detector           | Identifies abnormal CPU utilization          |
| Network Detector       | Monitors unusual network activity            |
| File Integrity Monitor | Detects unauthorized file modifications      |

---

## Security Capabilities

* Endpoint Activity Monitoring
* Process Enumeration
* Security Event Logging
* Threat Detection Engine
* File Integrity Verification
* Alert Generation and Management
* Security Reporting

---

## Future Enhancements

* VirusTotal Integration
* YARA Rule Scanning
* MITRE ATT&CK Mapping
* PostgreSQL Support
* Email & Telegram Notifications
* Docker Deployment
* JWT Authentication
* Real-Time WebSocket Alerts
* Threat Intelligence Integration
* SIEM Connectivity

---

## Testing

Run the test suite:

```bash
python -m unittest discover tests
```

---

## Disclaimer

CyberSentinel EDR is intended for educational, research, and portfolio purposes. It is designed to demonstrate endpoint security concepts and should not be considered a replacement for enterprise-grade EDR solutions.

---

## Author

**Hero**

Cybersecurity Analyst | Blue Team Enthusiast | Threat Detection & Endpoint Security

IBM Cybersecurity Analyst Certified
