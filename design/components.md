# 🧩 Components — The Building Blocks

Every design lives off re-usable parts.  
In code or visuals, **components = consistency**.

---

## 🧠 Core Components

| Component | Purpose | Example |
|------------|----------|----------|
| Button | trigger actions | “Add to cart”, “Sign in” |
| Input Field | user data entry | text, email, password |
| Card | compact info container | product preview, post snippet |
| Nav Bar | main navigation | top / side menus |
| Modal | focused overlay | alerts, confirmations |

---

## ⚙️ Naming System (Atomic Design Logic)

| Level | Prefix | Example |
|-------|---------|---------|
| Atom | a- | `a-button` |
| Molecule | m- | `m-card` |
| Organism | o- | `o-navbar` |
| Template | t- | `t-homepage` |
| Page | p- | `p-shop` |

> This helps screen readers and codebases stay organized.

---

## 🔊 For Blind / Low-Vision Devs

Imagine each component as **an instrument** in a band:
- Button → drum (hit & response)  
- Input → melody (interactive flow)  
- Card → bass (support rhythm)  
- Navbar → beat pattern (guides direction)  

---

## 🧩 Re-use Example (HTML)

```html
<button class="a-button m-primary">Buy Now</button>
<div class="m-card">
  <h2>Honey Jar</h2>
  <p>Pure Lebanese honey 500 ml</p>
</div>
