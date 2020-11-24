import reliability_3
import reliability_4
import reliability_5
import ch17pp_1
import ch17pp_2

if __name__ == "__main__":
    while True:
        print("1 - reliability_3")
        print("2 - reliability_4")
        print("3 - reliability_5")
        print("4 - ch17pp_1")
        print("5 - ch17pp_2")
        print("0 - exit")
        choice = input("Select excercise to solve: ")
        print()
        if choice == "1":
            reliability_3.run()
        elif choice == "2":
            reliability_4.run()
        elif choice == "3":
            reliability_5.run()
        elif choice == "4":
            ch17pp_1.run()
        elif choice == "5":
            ch17pp_2.run()
        elif choice == "0":
            break