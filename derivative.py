def derivative(n):
 polynomial = [
    (23, 10),
    (18, 8),
    (-15, 6),
    (10, 15)
 ]

 current = polynomial[:]
    
 for step in range(n):
        new_poly = []
        for coef, degree in current:
            if degree == 0:
                continue   
            new_poly.append((coef * degree, degree - 1))
        current = new_poly
    
 print(f"\n Derivate {n} oreder:")
    
 if not current:
        print("f^(n)(x) = 0")
 else:
        parts = []
        for coef, degree in current:
            parts.append(f"{coef}x^{degree}")
        print("f^(n)(x) = " + " + ".join(parts))


def main():
 n  = int(input("Enter order of the derivative (0 < n ≤ 10): "))
 derivative(n)


if __name__ == "__main__":
  main()