import math

volume = lambda h, s1, s2: (h / 3) * (s1 + s2 + math.sqrt(s1 * s2))

def main():
     h = float(input("\nEnter height (h): "))
     s1 = float(input("Enter square lower base (S1): "))
     s2 = float(input("Enter square upper base (S2): "))
     res = volume(h, s1, s2)
     print(f"Square of truncated pyramid: {res}")


if __name__ == "__main__":
 main()