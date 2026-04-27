from src.config import thresholds as t

def rule_engine(f):
    anomalies = []
    severity = "low"

    if f["cpu_avg"] < t.CPU_IDLE and f["memory_avg"] > t.HIGH_MEMORY:
        anomalies.append("over_provisioned")

    if f["cpu_p95"] > t.CPU_HIGH_P95:
        anomalies.append("under_provisioned")
        severity = "high"

    if f["cpu_avg"] < t.CPU_VERY_LOW and f["network_pct"] < t.LOW_NETWORK:
        anomalies.append("idle")

    return {
        "anomalies": anomalies,
        "severity": severity
    }