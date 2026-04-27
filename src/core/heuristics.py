def heuristic_signals(resource):
    cpu_avg = resource.get("cpu_avg", 1)
    cpu_p95 = resource.get("cpu_p95", 1)

    return {
        "cpu_spike_ratio": cpu_p95 / max(cpu_avg, 1),
        "utilization_score": (resource.get("cpu_avg", 0) + resource.get("memory_avg", 0)) / 2
    }