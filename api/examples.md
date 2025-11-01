# ⚙️ Figma API Examples

Real-world automation snippets to connect, export, and analyze design files.

---

## 📦 Example 1 — Export a Frame as PNG
```python
import requests, os

token = os.getenv("FIGMA_TOKEN")
file_key = "abc123xyz"
node_id = "1:2"  # frame ID

url = f"https://api.figma.com/v1/images/{file_key}?ids={node_id}&format=png"
headers = {"X-Figma-Token": token}

r = requests.get(url, headers=headers)
print(r.json()["images"][node_id])
