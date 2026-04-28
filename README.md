**AI / ML Reasoning + Anomaly Detection (Hybrid Approach)**

---

## Overview

This project implements a system to analyze infrastructure-level metrics and:

- Detect anomalies or inefficiencies  
- Explain the reasoning behind decisions  
- Suggest corrective actions  
- Assign confidence scores  

## Approach Chosen

I implemented a **Hybrid Approach** combining:

### 1. Rule-Based System (Core Decision Layer)

- Detects anomalies using predefined thresholds  
- Handles cases like:
  - Over-provisioned resources  
  - Under-provisioned systems  
  - Idle resources  

---

### 2. Heuristic Layer (Signal Intelligence)

- Computes derived metrics such as:
  - CPU spike ratio  
  - Utilization score  
- Improves confidence scoring and reasoning depth  

---

### 3. Reasoning Layer (Explanation Engine)

- Generates human-readable explanations  



## Why This Approach

This problem requires:

> “Making intelligent decisions safely in production systems”

No single method is sufficient:

| Approach   | Limitation                   |
|------------|------------------------------|
| Rule-based | Safe but rigid               |
| ML-only    | Needs data, less explainable |
| LLM-only   | Flexible but unreliable      |

---

### Hybrid Approach Benefits

- **Safety** → Rules ensure deterministic decisions  
- **Intelligence** → Heuristics improve signal understanding  
- **Explainability** → Reasoning layer explains decisions  

---


## Tradeoffs

### Strengths

- Highly explainable decisions  
- Deterministic and safe  
- No training data required  
- Modular and extensible design  

---


## What I Would Improve With More Time

### 1. Adaptive Thresholds
- Use historical data to dynamically adjust thresholds  

---

### 2. Machine Learning Integration
- Apply unsupervised models (e.g., Isolation Forest)  
- Detect anomalies based on learned patterns  

---

### 3. LLM Integration
- Replace template reasoning with real LLM  
- Improve explanation quality and flexibility  

---

### 4. Feedback Loop (Learning System)
- Store past decisions  
- Improve future predictions based on outcomes  

---

### 5. Multi-Agent Architecture
- Separate responsibilities into agents:
  - Optimizer (cost)  
  - Guardian (security)  
  - Executor (actions)  

---

## ▶️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/junaid7535/Assignment-Project-AI-ML-Reasoning-Anomaly-Detection.git

# 2. Check Python version
python3 --version

# 3. Install dependencies
pip3 install -r requirements.txt

# 4. Run the project
python3 -m src.main

# 5. View output
outputs/sample_outputs.json