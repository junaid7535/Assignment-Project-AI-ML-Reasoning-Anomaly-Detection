import json
from src.pipeline import run_pipeline

def main():
    with open("data/input_samples.json") as f:
        data = json.load(f)

    results = [run_pipeline(r) for r in data]

    with open("outputs/sample_outputs.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Analysis complete. Check outputs/sample_outputs.json")

if __name__ == "__main__":
    main()