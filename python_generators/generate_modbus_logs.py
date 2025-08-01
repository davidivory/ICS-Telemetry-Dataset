import csv, random
from datetime import datetime, timedelta

def next_timestamp(ts): return ts + timedelta(seconds=random.randint(5, 10))
def random_ip(): return f"192.168.1.{random.randint(1, 254)}"
def attacker_ip(): return random.choice(["192.168.99.99", "10.0.0.254"])

def generate_log(log_type):
    rows, ts = [], datetime(2025, 8, 1, 8, 0, 0)
    for _ in range(500):
        row = {
            "timestamp": ts.isoformat() + "Z",
            "device_id": f"PLC-{random.randint(1, 20):03}",
            "protocol": "Modbus",
            "event_type": random.choice(["read", "write", "status"]),
            "register": random.randint(40001, 40099),
            "value": round(random.uniform(60, 80), 1) if log_type != "attack" else random.choice([0, 1]),
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
save_csv("modbus_normal.csv", normal)
save_csv("modbus_attack.csv", attack)
save_csv("modbus_mixed.csv", random.sample(normal + attack, len(normal) + len(attack)))
print("✅ Modbus logs generated.")
