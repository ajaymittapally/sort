# 📦 Package Sorting System

This Python project simulates the logic used by Thoughtful's robotic automation factory to dispatch packages to the correct stack based on their **volume** and **mass**.

## 🚀 Objective

Implement a function that classifies packages into one of three categories:

- **STANDARD**: Packages that are neither bulky nor heavy.
- **SPECIAL**: Packages that are either bulky or heavy.
- **REJECTED**: Packages that are both bulky and heavy.

## 📐 Classification Rules

A package is classified based on:

- **Volume** = `width × height × length` (in cm³)
- **Bulky**: If volume ≥ 1,000,000 cm³ **OR** any one dimension ≥ 150 cm
- **Heavy**: If mass ≥ 20 kg

### 📦 Stack Criteria

| Bulky | Heavy | Category   |
|-------|--------|------------|
| No    | No     | STANDARD   |
| Yes   | No     | SPECIAL    |
| No    | Yes    | SPECIAL    |
| Yes   | Yes    | REJECTED   |

---

## 🧠 Function Definition

```python
def sort(width, height, length, mass):
    ...
Parameters:

width (int): Width in cm

height (int): Height in cm

length (int): Length in cm

mass (float): Mass in kg

Returns: A string — one of "STANDARD", "SPECIAL", or "REJECTED"

Running the Script:
python sort.py
