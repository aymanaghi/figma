#!/usr/bin/env python3
"""
auto-rename.py
Rename exported files to match clean naming rules.
"""
import os

for filename in os.listdir("."):
    if filename.endswith(".png"):
        new_name = filename.lower().replace(" ", "_")
        os.rename(filename, new_name)
        print(f"✅ Renamed {filename} → {new_name}")
