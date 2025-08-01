import csv, random
from datetime import datetime, timedelta

def next_timestamp(ts): return ts + timedelta(seconds=random.randint(5, 10))
def random_ip(): return f"192.168.2.{random.randint(1, 254)}"
def attacker_ip(): return random.choice(["192.168.99.99", "10.0.0.254"])

def generate_log(log_type):
    rows, ts = [], datetime(2025, 8, 1, 8, 0, 0)
    for _ in range(500):
        row = {
            "timestamp": ts.isoformat() + "Z",
            "device_id": f"OpenPLC-{random.randint(1, 5):03}",
            "protocol": "OpenPLC",
            "event_type": random.choice(["cycle_start", "cycle_end", "logic_injection"]),
            "cycle": random.randint(1, 100),
            "value": random.choice(["ok", "fail", "injected"]) if log_type != "normal" else "ok",
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
save_csv("openplc_normal.csv", normal)
save_csv("openplc_attack.csv", attack)
save_csv("openplc_mixed.csv", random.sample(normal + attack, len(normal) + len(attack)))
print("✅ OpenPLC logs generated.")
