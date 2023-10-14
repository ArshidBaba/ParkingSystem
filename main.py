from parking_lot import ParkingLot


def main():
    parking_lot = ParkingLot()

    while True:
        print("Choose an option:")
        print("1. Assign a parking spot")
        print("2. Retrieve a parking spot")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_number = input("Enter the vehicle number: ")
            result = parking_lot.assign_parking_spot(vehicle_number)
            print(result)

        elif choice == "2":
            vehicle_number = input("Enter the vehicle number: ")
            result = parking_lot.retrieve_parking_spot(vehicle_number)
            print(result)

        elif choice == "3":
            print("Exiting the parking lot application.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
