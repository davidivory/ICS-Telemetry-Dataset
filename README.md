# ICS Telemetry Dataset
## Overview
This repository provides structured telemetry data from simulated industrial control systems (ICS), including SCADA and PLC event logs. It is designed to support research, testing, and development of cybersecurity tools, anomaly detection models, and log ingestion pipelines.

## 📦 Contents
datasets/: CSV and JSON files containing timestamped ICS events

schemas/: Field definitions and formatting standards

generators/: Scripts for producing synthetic telemetry

docs/: Documentation and usage examples

## 📦 Dataset Overview

The dataset includes telemetry samples from various ICS protocols and components, such as:

- **Modbus** and **DNP3** traffic logs
- **SCADA/PLC event traces**
- **Sensor and actuator telemetry**
- **LabShock-generated synthetic anomalies**
- **Time-series logs** with timestamps, event types, and system states

Each log file is structured for easy ingestion into tools like **Splunk**, **ELK**, or **custom AI pipelines**.

## 🧠 Use Cases

This dataset is ideal for:

- 🔍 ICS vulnerability testing and red team simulations  
- 🧪 AI model training for anomaly detection  
- 📊 Splunk dashboard development and telemetry visualization  
- 🛡️ Cybersecurity research in OT environments  
- 🧬 RAG (Retrieval-Augmented Generation) systems for ICS diagnostics

## 📁 Repository Structure

ICS-telemetry-dataset/
├── modbus/
│   ├── normal/
│   │   └── modbus_normal.csv
│   ├── attack/
│   │   └── modbus_attack_stuxnet_sim.csv
│   └── hybrid/
│       └── modbus_hybrid_mixed.csv
├── dnp3/
│   ├── normal/
│   │   └── dnp3_normal.json
│   ├── attack/
│   │   └── dnp3_attack_crashoverride.json
│   └── hybrid/
│       └── dnp3_hybrid_mixed.json
├── scada/
│   ├── normal/
│   │   └── scada_normal_log.csv
│   ├── attack/
│   │   └── scada_attack_trisis.csv
│   └── hybrid/
│       └── scada_hybrid_mixed.csv
├── openplc/
│   ├── normal/
│   │   └── openplc_runtime_log.csv
│   ├── attack/
│   │   └── openplc_labshock_injected.csv
│   └── hybrid/
│       └── openplc_hybrid_mixed.csv
├── labshock/
│   ├── normal/
│   │   └── labshock_synthetic_anomalies.csv
│   ├── attack/
│   │   └── labshock_openplc_injection.csv
│   └── hybrid/
│       └── labshock_hybrid_mixed.csv
├── generators/
│   ├── generate_modbus.py
│   ├── generate_dnp3.py
│   ├── generate_scada.py
│   ├── generate_openplc.py
│   ├── generate_labshock.py
│   └── generate_ics_logs.py  # Unified generator for all telemetry types
├── README.md
└── LICENSE


## ⚔️ Normal vs. Attack Logs

To support anomaly detection and cybersecurity testing, this dataset is organized into **normal** and **attack** telemetry samples across multiple ICS protocols.

### 🔹 Normal Logs
These represent baseline operations under expected conditions:
- Standard Modbus and DNP3 traffic
- OpenPLC runtime logs from ladder logic execution
- SCADA event traces without malicious interference

### 🔺 Attack Logs
These simulate or replicate known ICS attack patterns:
- **Stuxnet-style Modbus manipulation** (e.g., false feedback loops)
- **CrashOverride DNP3 disruptions** (e.g., command flooding)
- **TRISIS SCADA tampering** (e.g., safety logic overwrite)
- **LabShock-injected anomalies** into OpenPLC telemetry

### 🧠 How to Use

#### 🔍 Anomaly Detection
- Train ML models on `normal/` logs
- Validate detection on `attack/` logs
- Use time-series comparisons to highlight deviations

#### 📊 Splunk Dashboards
- Ingest both normal and attack logs
- Build dashboards to visualize telemetry shifts
- Create alerts based on known attack signatures


**Tip:** Each protocol folder contains both `normal/` and `attack/` subfolders for easy comparison and ingestion.

## 🚀 Getting Started
Clone the repository:
git clone https://github.com/davidivory/ICS-telemetry-dataset.git

## 📜 License
This dataset is released under the Creative Commons Zero v1.0 Universal (CC0 1.0) license.

You are free to copy, modify, distribute, and use the dataset — even for commercial purposes — without asking for permission.

See the LICENSE file for full details.

## 🤝 Contributing
Contributions are welcome! If you have telemetry samples, improvements, or suggestions:

Fork the repository
Create a new branch (feature/my-enhancement)
Submit a pull request

Please ensure your data is anonymized and safe for public sharing.

📬 Contact
For questions, feedback, or collaboration ideas, feel free to reach out via GitHub Issues.
