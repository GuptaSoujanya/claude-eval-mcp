# claude-eval-mcp

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Protocol: MCP](https://img.shields.io/badge/Protocol-Anthropic%20MCP-black.svg)](https://modelcontextprotocol.io/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

An official **Model Context Protocol (MCP)** server engineered to connect **Claude** (Claude Desktop, Claude Code CLI, and autonomous agents) directly to AI/ML evaluation harnesses, token latency profilers, and prompt security red-teaming tools.

---

## Sequence Architecture

```mermaid
sequenceDiagram
    autonumber
    actor User as Engineer
    participant Claude as Claude Desktop / Claude Code
    participant MCP as claude-eval-mcp Server
    participant Engine as Local Evaluation Engine

    User->>Claude: "Evaluate Qwen-2.5-7B on GSM8K and profile TTFT"
    Claude->>MCP: Call tool `benchmark_model(model='qwen-2.5-7b', task='gsm8k')`
    MCP->>Engine: Run reasoning suite
    Engine-->>MCP: Accuracy 82.4%
    MCP-->>Claude: JSON Tool Result
    Claude-->>User: Format detailed benchmark summary table
```

---

## Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "ai-evaluator": {
      "command": "python3",
      "args": ["-m", "claude_eval.server"]
    }
  }
}
```

---

## License

MIT License (c) 2024 Soujanya Gupta.

<!-- PR #4: docs: clarify benchmark metric configuration options -->

<!-- PR #17: perf: optimize memory buffer reuse during batch evaluation -->

<!-- PR #30: test: expand edge case coverage for empty input strings -->

<!-- PR #43: refactor: clean up typing annotations across core modules -->
