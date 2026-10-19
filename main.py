import derivative
import pyramid

def main():
    while True:
        # show_menu()
        choice = input("\nYour choice: ").strip()

        if choice == "1":
            derivative.run()
        elif choice == "2":
            pyramid.run()
        elif choice == "0":
            print("\nGood Bye!")
            break
        else:
            print("\nTry again!")


if __name__ == "__main__":
    main()