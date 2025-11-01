#!/usr/bin/env python3
"""
export-assets.py
Export Figma assets (frames/components) as PNGs.
"""
import requests, os, json

FIGMA_TOKEN = os.getenv("FIGMA_TOKEN")
FILE_KEY = input("Enter Figma File Key: ")
NODE_IDS = input("Enter comma-separated Node IDs: ")

url = f"https://api.figma.com/v1/images/{FILE_KEY}?ids={NODE_IDS}&format=png"
headers = {"X-Figma-Token": FIGMA_TOKEN}

r = requests.get(url, headers=headers)
data = r.json().get("images", {})

for node_id, link in data.items():
    print(f"🧩 {node_id} → {link}")
