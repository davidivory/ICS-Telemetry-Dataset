import csv, random
from datetime import datetime, timedelta

def next_timestamp(ts): return ts + timedelta(seconds=random.randint(5, 10))
def random_ip(): return f"10.10.0.{random.randint(1, 254)}"
def attacker_ip(): return random.choice(["10.10.99.99", "10.0.0.254"])

def generate_log(log_type):
    rows, ts = [], datetime(2025, 8, 1, 8, 0, 0)
    for _ in range(500):
        row = {
            "timestamp": ts.isoformat() + "Z",
            "device_id": f"LabShock-{random.randint(1, 3):03}",
            "protocol": "LabShock",
            "event_type": random.choice(["latency", "spoofed_io", "anomaly"]),
            "metric": random.choice(["comm_delay", "DO_01", "voltage_spike"]),
            "value": random.choice(["250ms", "350ms", 1, "spike", "fail"]) if log_type != "normal" else "250ms",
            "severity": "warning" if log_type == "normal" else "critical",
            "source_ip": random_ip() if log_type != "attack" else attacker_ip()
        }
        rows.append(row)
        ts = next_timestamp(ts)
    return rows

def save_csv(name, rows):
    with open(name, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

normal = generate_log("normal")
attack = generate_log("attack")
save_csv("labshock_normal.csv", normal)
save_csv("labshock_attack.csv", attack)
save_csv("labshock_mixed.csv", random.sample(normal + attack, len(normal) + len(attack)))
print("✅ LabShock logs generated.")
