import json
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

# 🔧 Configuration
LOG_COUNT = 500
START_TIME = datetime(2025, 8, 1, 8, 0, 0)
OUTPUT_DIR = Path("generated_logs")
OUTPUT_DIR.mkdir(exist_ok=True)

# 🧠 Utility Functions
def random_ip():
    return f"192.168.{random.randint(0, 5)}.{random.randint(1, 254)}"

def attacker_ip():
    return random.choice(["192.168.99.99", "10.0.0.254"])

def next_timestamp(ts):
    return ts + timedelta(seconds=random.randint(5, 10))

# 📄 CSV Writer
def save_csv(filename, rows, headers):
    with open(OUTPUT_DIR / filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    print(f"✅ Saved {filename} with {len(rows)} entries.")

# 📄 JSON Writer
def save_json(filename, entries):
    with open(OUTPUT_DIR / filename, "w") as f:
        json.dump(entries, f, indent=2)
    print(f"✅ Saved {filename} with {len(entries)} entries.")

# 🔌 Modbus Generator
def generate_modbus(log_type):
    rows = []
    ts = START_TIME
    for _ in range(LOG_COUNT):
        device = f"PLC-{random.randint(1, 20):03}"
        row = {
            "timestamp": ts.isoformat() + "Z",
            "device_id": device,
            "protocol": "Modbus",
            "event_type": random.choice(["read", "write", "status"]),
            "register": random.randint(40001, 40099),
            "value": round(random.uniform(60, 80), 1) if log_type != "attack" else random.choice([0, 1]),
            "severity": "info" if log_type == "normal" else "critical",
            "source_ip": random_ip() if log_type != "attack" else attacker_ip()
        }
        rows.append(row)
        ts = next_timestamp(ts)
    save_csv(f"modbus_{log_type}.csv", rows, list(rows[0].keys()))

# 🏭 SCADA Generator
def generate_scada(log_type):
    rows = []
    ts = START_TIME
    for _ in range(LOG_COUNT):
        device = f"SCADA-{random.randint(1, 10):03}"
        row = {
            "timestamp": ts.isoformat() + "Z",
            "device_id": device,
            "protocol": "SCADA",
            "event_type": random.choice(["valve_status", "sensor_reading", "logic_change"]),
            "tag": f"T{random.randint(100,199)}",
            "value": random.choice(["open", "closed", round(random.uniform(20, 100), 1), "override"]) if log_type != "attack" else "override",
            "severity": "info" if log_type == "normal" else "critical",
            "source_ip": random_ip() if log_type != "attack" else attacker_ip()
        }
        rows.append(row)
        ts = next_timestamp(ts)
    save_csv(f"scada_{log_type}.csv", rows, list(rows[0].keys()))

# ⚙️ OpenPLC Generator
def generate_openplc(log_type):
    rows = []
    ts = START_TIME
    for _ in range(LOG_COUNT):
        device = f"OpenPLC-{random.randint(1, 5):03}"
        row = {
            "timestamp": ts.isoformat() + "Z",
            "device_id": device,
            "protocol": "OpenPLC",
            "event_type": random.choice(["cycle_start", "cycle_end", "logic_injection"]),
            "cycle": random.randint(1, 100),
            "value": random.choice(["ok", "fail", "injected"]) if log_type != "normal" else "ok",
            "severity": "info" if log_type == "normal" else "critical",
            "source_ip": random_ip() if log_type != "attack" else attacker_ip()
        }
        rows.append(row)
        ts = next_timestamp(ts)
    save_csv(f"openplc_{log_type}.csv", rows, list(rows[0].keys()))

# 🧪 LabShock Generator
def generate_labshock(log_type):
    rows = []
    ts = START_TIME
    for _ in range(LOG_COUNT):
        device = f"LabShock-{random.randint(1, 3):03}"
        row = {
            "timestamp": ts.isoformat() + "Z",
            "device_id": device,
            "protocol": "LabShock",
            "event_type": random.choice(["latency", "spoofed_io", "anomaly"]),
            "metric": random.choice(["comm_delay", "DO_01", "voltage_spike"]),
            "value": random.choice(["350ms", 1, "spike", "fail"]) if log_type != "normal" else "250ms",
            "severity": "warning" if log_type == "normal" else "critical",
            "source_ip": random_ip() if log_type != "attack" else attacker_ip()
        }
        rows.append(row)
        ts = next_timestamp(ts)
    save_csv(f"labshock_{log_type}.csv", rows, list(rows[0].keys()))

# 🔁 Mixed Generator (calls normal + attack)
def generate_mixed(generator_fn, name):
    print(f"🔀 Generating mixed log for {name}...")
    generator_fn("normal")
    generator_fn("attack")
    # Combine both files
    normal_file = OUTPUT_DIR / f"{name}_normal.csv"
    attack_file = OUTPUT_DIR / f"{name}_attack.csv"
    mixed_file = OUTPUT_DIR / f"{name}_mixed.csv"
    with open(normal_file) as f1, open(attack_file) as f2:
        lines = f1.readlines()[1:] + f2.readlines()[1:]
        random.shuffle(lines)
    with open(mixed_file, "w") as f:
        f.write(','.join(lines[0].strip().split(',')) + '\n')  # header
        f.writelines(lines)
    print(f"✅ Saved {name}_mixed.csv with {len(lines)} entries.")

# 🚀 Generate All Logs
generate_modbus("normal")
generate_modbus("attack")
generate_mixed(generate_modbus, "modbus")

generate_scada("normal")
generate_scada("attack")
generate_mixed(generate_scada, "scada")

generate_openplc("normal")
generate_openplc("attack")
generate_mixed(generate_openplc, "openplc")

generate_labshock("normal")
generate_labshock("attack")
generate_mixed(generate_labshock, "labshock")
