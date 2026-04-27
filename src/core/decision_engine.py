def decide_action(rules):
    anomalies = rules["anomalies"]

    if "over_provisioned" in anomalies:
        return "Downsize instance"

    if "under_provisioned" in anomalies:
        return "Scale up resources"

    if "idle" in anomalies:
        return "Terminate or stop instance"

    return "Monitor system"