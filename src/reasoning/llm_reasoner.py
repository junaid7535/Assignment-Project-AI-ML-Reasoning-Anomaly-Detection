def generate_reason(resource, rules):
    anomalies = rules["anomalies"]

    if "over_provisioned" in anomalies:
        return f"Low CPU usage ({resource['cpu_avg']}%) with high memory usage ({resource['memory_avg']}%) indicates inefficient allocation."

    if "under_provisioned" in anomalies:
        return f"CPU peaks at {resource['cpu_p95']}%, suggesting the system is under heavy load and may require scaling."

    if "idle" in anomalies:
        return f"Very low CPU ({resource['cpu_avg']}%) and low network usage indicate an idle resource."

    return "No strong anomaly detected; system appears stable."