#!/usr/bin/env python3
"""Weave Explorer Test - Minimal version"""
from pathlib import Path

print("=" * 70)
print("WEAVE EXPLORER TEST")
print("=" * 70)

base = Path(__file__).resolve().parent.parent
current_dir = base

print(f"\nExploring: {current_dir}")
print("-" * 50)

for item in sorted(current_dir.iterdir()):
    if item.is_dir():
        print(f"🕸️  {item.name}/")
    else:
        size = f" ({item.stat().st_size:,} bytes)"
        print(f"🧵 {item.name}{size}")

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
