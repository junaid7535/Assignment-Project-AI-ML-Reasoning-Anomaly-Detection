def compute_confidence(rules, heuristics):
    score = 0.5

    if rules["anomalies"]:
        score += 0.2

    if heuristics["cpu_spike_ratio"] > 3:
        score += 0.2

    if rules["severity"] == "high":
        score += 0.1

    return min(score, 1.0)