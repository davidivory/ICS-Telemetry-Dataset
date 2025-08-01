import json
import random
from datetime import datetime, timedelta

def generate_dnp3_entry(log_type, timestamp):
    device_id = f"RTU-{random.randint(1, 20):03}"
    index = random.randint(0, 99)
    source_ip = f"10.0.0.{random.randint(1, 254)}"
    entry = {
        "timestamp": timestamp.isoformat() + "Z",
        "device_id": device_id,
        "protocol": "DNP3",
        "index": index,
        "source_ip": source_ip
    }

    if log_type == "normal":
        event_type = random.choice(["analog_input", "digital_input", "status", "counter"])
        entry["event_type"] = event_type
        if event_type == "analog_input":
            entry["value"] = round(random.uniform(0, 250), 1)
        elif event_type == "digital_input":
            entry["value"] = random.choice([0, 1])
        elif event_type == "status":
            entry["value"] = random.choice(["OK", "WARN", "FAIL"])
        elif event_type == "counter":
            entry["value"] = random.randint(0, 100)
        entry["severity"] = "info" if entry["value"] in ["OK", 0, 1] else "warning"

    elif log_type == "attack":
        entry["event_type"] = random.choice(["malformed_command", "unauthorized_control", "flood", "spoofed_status"])
        entry["value"] = random.choice([None, "trip", "override", "burst", "FAIL"])
        entry["severity"] = "critical"
        entry["source_ip"] = random.choice(["10.0.0.99", "10.0.0.254"])

    return entry

def generate_dnp3_log(log_type, count):
    entries = []
    timestamp = datetime(2025, 8, 1, 8, 0, 0)
    for _ in range(count):
        if log_type == "mixed":
            subtype = random.choice(["normal", "attack"])
            entry = generate_dnp3_entry(subtype, timestamp)
        else:
            entry = generate_dnp3_entry(log_type, timestamp)
        entries.append(entry)
        timestamp += timedelta(seconds=random.randint(5, 10))
    return entries

def save_log(log_type, entries):
    filename = f"dnp3_{log_type}.json"
    with open(filename, "w") as f:
        json.dump(entries, f, indent=2)
    print(f"✅ Saved {filename} with {len(entries)} entries.")

# Generate and save all three logs
for log_type in ["normal", "attack", "mixed"]:
    log_entries = generate_dnp3_log(log_type, 500)
    save_log(log_type, log_entries)
