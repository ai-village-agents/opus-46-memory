#!/usr/bin/env python3
"""Cross-agent inventory aggregator — fetches and summarizes inventory.yaml from all known peer repos."""

import yaml
import urllib.request
import json
import sys

REPOS = {
    "GPT-5.4": "gpt-5-4-memory-kit",
    "Claude Sonnet 4.5": "memory-improvement",
    "Claude Opus 4.5": "claude-opus-memory",
    "Claude Opus 4.6": "opus-46-memory",
    "Claude Opus 4.7": "claude-opus-4-7-memory",
    "GPT-5.2": "gpt-5-2-memory-improvement",
    "GPT-5.5": "gpt-5-5-memory-improvement",
    "Gemini 3.1 Pro": "gemini-3.1-pro-memory",
    "DeepSeek-V3.2": "deepseek-v3.2-memory-system",
}

BASE_URL = "https://raw.githubusercontent.com/ai-village-agents/{repo}/main/inventory.yaml"

def fetch_inventory(repo_name):
    url = BASE_URL.format(repo=repo_name)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ai-village-agent"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return yaml.safe_load(resp.read().decode("utf-8"))
    except Exception:
        # Fallback to API (CDN cache may block raw URL for recent files)
        api_url = f"https://api.github.com/repos/ai-village-agents/{repo_name}/contents/inventory.yaml"
        try:
            req2 = urllib.request.Request(api_url, headers={"User-Agent": "ai-village-agent"})
            with urllib.request.urlopen(req2, timeout=10) as resp2:
                data = json.loads(resp2.read().decode("utf-8"))
                if "content" in data:
                    import base64
                    content = base64.b64decode(data["content"]).decode("utf-8")
                    return yaml.safe_load(content)
        except Exception as e2:
            return {"error": str(e2)}
        return {"error": "not found via raw or API"}

def main():
    all_items = []
    agent_stats = []
    
    for agent, repo in sorted(REPOS.items()):
        data = fetch_inventory(repo)
        if isinstance(data, dict) and "error" in data:
            agent_stats.append({"agent": agent, "repo": repo, "status": "ERROR", "count": 0, "error": data["error"]})
            continue
        
        items = data if isinstance(data, list) else data.get("items", data.get("inventory", data.get("entries", [])))
        if not isinstance(items, list):
            agent_stats.append({"agent": agent, "repo": repo, "status": "PARSE_ERROR", "count": 0, "error": "unexpected format"})
            continue
        
        for item in items:
            if isinstance(item, dict):
                item["_agent"] = agent
                item["_repo"] = repo
                all_items.append(item)
        
        kinds = {}
        for item in items:
            if isinstance(item, dict):
                k = item.get("kind", "unknown")
                kinds[k] = kinds.get(k, 0) + 1
        
        agent_stats.append({"agent": agent, "repo": repo, "status": "OK", "count": len(items), "kinds": kinds})
    
    # Print summary
    print("=" * 70)
    print("CROSS-AGENT INVENTORY SCAN")
    print("=" * 70)
    print(f"\nRepos scanned: {len(REPOS)}")
    print(f"Total items indexed: {len(all_items)}")
    print()
    
    # Per-agent table
    print(f"{'Agent':<20} {'Status':<8} {'Items':>5}  {'Kinds'}")
    print("-" * 70)
    for s in agent_stats:
        kinds_str = ", ".join(f"{k}:{v}" for k, v in sorted(s.get("kinds", {}).items())) if s["status"] == "OK" else s.get("error", "")[:40]
        print(f"{s['agent']:<20} {s['status']:<8} {s['count']:>5}  {kinds_str}")
    
    # Kind distribution
    print("\n--- Kind Distribution ---")
    kind_counts = {}
    for item in all_items:
        k = item.get("kind", "unknown")
        kind_counts[k] = kind_counts.get(k, 0) + 1
    for k, v in sorted(kind_counts.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    
    # Status distribution
    print("\n--- Status Distribution ---")
    status_counts = {}
    for item in all_items:
        s = item.get("status", "unknown")
        status_counts[s] = status_counts.get(s, 0) + 1
    for s, v in sorted(status_counts.items(), key=lambda x: -x[1]):
        print(f"  {s}: {v}")
    
    # Common patterns (items appearing in 2+ agents)
    print("\n--- Common Patterns (similar items across agents) ---")
    by_kind = {}
    for item in all_items:
        k = item.get("kind", "unknown")
        if k not in by_kind:
            by_kind[k] = []
        by_kind[k].append(item)
    
    for kind in sorted(by_kind.keys()):
        items = by_kind[kind]
        if len(items) >= 2:
            agents = set(i.get("_agent", "?") for i in items)
            if len(agents) >= 2:
                summaries = [f"  - [{i.get('_agent','?')}] {i.get('id','?')}: {i.get('summary','')[:60]}" for i in items[:8]]
                print(f"\n  {kind} ({len(items)} items across {len(agents)} agents):")
                for s in summaries:
                    print(s)

    # Emit JSON for downstream use
    if "--json" in sys.argv:
        print("\n--- JSON Output ---")
        print(json.dumps(all_items, indent=2, default=str))

if __name__ == "__main__":
    main()
