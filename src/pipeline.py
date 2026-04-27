from src.core.feature_engineering import extract_features
from src.core.rule_engine import rule_engine
from src.core.heuristics import heuristic_signals
from src.core.decision_engine import decide_action
from src.core.confidence import compute_confidence
from src.core.security import security_check
from src.reasoning.llm_reasoner import generate_reason

def run_pipeline(resource):
    features = extract_features(resource)
    rules = rule_engine(features)
    heuristics = heuristic_signals(resource)

    reason = generate_reason(resource, rules)
    action = decide_action(rules)
    confidence = compute_confidence(rules, heuristics)
    security = security_check(resource)

    return {
        "resource_id": resource.get("resource_id"),
        "is_anomalous": len(rules["anomalies"]) > 0,
        "anomaly_type": rules["anomalies"][0] if rules["anomalies"] else None,
        "reason": reason,
        "suggested_action": action,
        "confidence": round(confidence, 2),
        "security_note": security
    }