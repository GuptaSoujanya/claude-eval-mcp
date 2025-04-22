import sys
import json
from .tools import evaluate_model, profile_latency

TOOLS = [
    {"name": "benchmark_model", "description": "Run standard evaluation probe on local/open-source LLMs."},
    {"name": "profile_latency", "description": "Profile TTFT and ITL token streaming latency."}
]

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--list-tools":
        print(json.dumps(TOOLS, indent=2))
        return
    print("[claude-eval-mcp] Model Context Protocol Server active.", file=sys.stderr)

if __name__ == "__main__":
    main()
