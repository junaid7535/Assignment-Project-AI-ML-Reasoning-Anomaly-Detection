def extract_features(resource):
    return {
        "cpu_avg": resource.get("cpu_avg", 0),
        "cpu_p95": resource.get("cpu_p95", 0),
        "memory_avg": resource.get("memory_avg", 0),
        "network_pct": resource.get("network_pct", 0),
        "internet_facing": resource.get("internet_facing", False),
        "identity_attached": resource.get("identity_attached", False)
    }