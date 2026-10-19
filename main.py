import derivative
import pyramid

def show_menu():
    print("  1 — derivate")
    print("  2 — pyramid")
    print("  0 — Exit")

def main():
    show_menu()
    while True:
        choice = input("\nYour choice: ").strip()

        if choice == "1":
            derivative.run()
            input("\nClick Enter for rerturn in menu...")
        elif choice == "2":
            pyramid.run()
            input("\nClick Enter for rerturn in menu...")
        elif choice == "0":
            print("\nGood Bye!")
            break

        else:
            print("\nTry again!")


if __name__ == "__main__":
    main()
