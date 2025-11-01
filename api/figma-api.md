# 🧩 Figma API — Developer Entry Point

The Figma REST API lets you **fetch, inspect, and update** your design files using code.  
Perfect for automation, analytics, or version control.

---

## 🔐 Authentication
Every request needs a **Personal Access Token (PAT)**.

Generate one:
1. Log in to [Figma](https://www.figma.com)
2. Go to **Settings → Personal Access Tokens**
3. Create token → copy it

Then export it:
```bash
export FIGMA_TOKEN="your_token_here"
