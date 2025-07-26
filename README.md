# Euclidean Algorithm

This Python script calculates the greatest common divisor (GCD) between two numbers using the Euclidean Algorithm.

## How the Algorithm Works

The Euclidean Algorithm states:

> **gcd(a, b) = gcd(b, r)**

Where:
- **a > b**
- **a** and **b** are positive integers
- **r** is the remainder when **a** is divided by **b**  
  (i.e., **a = q × b + r**)

The algorithm repeats the process, replacing **a** with **b** and **b** with **r**, until **r = 0**.  
At that point, **gcd(b, 0) = b**, which is the greatest common divisor.

---

 
