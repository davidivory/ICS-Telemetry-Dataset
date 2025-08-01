import csv, random
from datetime import datetime, timedelta

def next_timestamp(ts): return ts + timedelta(seconds=random.randint(5, 10))
def random_ip(): return f"172.16.0.{random.randint(1, 254)}"
def attacker_ip(): return random.choice(["172.16.99.99", "10.0.0.254"])

def generate_log(log_type):
    rows, ts = [], datetime(2025, 8, 1, 8, 0, 0)
    for _ in range(500):
        row = {
            "timestamp": ts.isoformat() + "Z",
            "device_id": f"SCADA-{random.randint(1, 10):03}",
            "protocol": "SCADA",
            "event_type": random.choice(["valve_status", "sensor_reading", "logic_change"]),
            "tag": f"T{random.randint(100,199)}",
            "value": random.choice(["open", "closed", round(random.uniform(20, 100), 1), "override"]) if log_type != "attack" else "override",
            "severity": "info" if log_type == "normal" else "critical",
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
save_csv("scada_normal.csv", normal)
save_csv("scada_attack.csv", attack)
save_csv("scada_mixed.csv", random.sample(normal + attack, len(normal) + len(attack)))
print("✅ SCADA logs generated.")
