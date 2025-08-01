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
To support anomaly detection, ICS threat modeling, and cybersecurity research, this dataset is organized into normal, attack, and hybrid telemetry samples across multiple industrial protocols. All logs are generated using purpose-built Python scripts located in the generators/ directory, including the unified generate_ics_logs.py script for full-batch generation.

### 🔹 Normal Logs
These represent baseline operations under expected conditions, useful for training models and establishing behavioral baselines:

Standard Modbus and DNP3 traffic with valid coil/register operations

OpenPLC runtime logs from ladder logic execution without interference

SCADA event traces reflecting routine control and monitoring activity

### 🔺 Attack Logs
These simulate or replicate known ICS attack patterns and adversarial behaviors:

Stuxnet-style Modbus manipulation — false feedback loops, unauthorized coil writes

CrashOverride DNP3 disruptions — command flooding, malformed packets

TRISIS SCADA tampering — safety logic overwrite, unauthorized state changes

LabShock-injected anomalies — synthetic fault injection into OpenPLC telemetry

### ⚫ Hybrid Logs
These combine normal and attack events to reflect real-world conditions where malicious activity is interleaved with legitimate operations. Useful for testing detection thresholds and model robustness.

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
