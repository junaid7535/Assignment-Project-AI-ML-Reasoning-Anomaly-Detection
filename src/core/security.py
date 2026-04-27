def security_check(resource):
    if resource.get("internet_facing") and resource.get("identity_attached"):
        return "High risk: public resource with attached identity may be exploited"
    return None