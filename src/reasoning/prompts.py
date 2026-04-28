def build_prompt(resource, anomalies):
    return f"""
Resource Metrics:
CPU avg: {resource.get('cpu_avg')}%
CPU p95: {resource.get('cpu_p95')}%
Memory avg: {resource.get('memory_avg')}%
Network: {resource.get('network_pct')}%

Detected anomalies: {anomalies}

