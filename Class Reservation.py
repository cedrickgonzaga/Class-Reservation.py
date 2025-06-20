class CarReservation:
    def availableCars(self):
        try:
            with open("availableCars.txt", "r") as file:
                print("\n\t=== Our Current Available Cars ===\n")
                content = file.read()
                if content.strip():
                    print(content)
                else:
                    print("No cars currently available.")
        except FileNotFoundError:
            print("Available cars file not found. Creating a sample file...")
            self.createSampleCarsFile()
            self.availableCars()

    def createSampleCarsFile(self):
        """Create a sample available cars file if it doesn't exist"""
        sample_cars = """1. Toyota Camry - $50/day
2. Honda Civic - $45/day
3. Ford Mustang - $80/day
4. BMW 3 Series - $120/day
5. Chevrolet Malibu - $55/day
6. Nissan Altima - $48/day"""
        
        with open("availableCars.txt", "w") as file:
            file.write(sample_cars)

    def createSampleCarsFile(self):
        """Create a sample available cars file if it doesn't exist"""
        sample_cars = """1. Toyota Camry - $50/day
2. Honda Civic - $45/day
3. Ford Mustang - $80/day
4. BMW 3 Series - $120/day
5. Chevrolet Malibu - $55/day
6. Nissan Altima - $48/day"""
        
        with open("availableCars.txt", "w") as file:
            file.write(sample_cars)

    def currentReservations(self):
        try:
            with open("reservations.txt", "r") as file:
                print("\n\t=== Current Reservations ===\n")
                content = file.read()
                if content.strip():
                    print(content)
                else:
                    print("No reservations found.")
        except FileNotFoundError:
            print("No reservations file found. No reservations have been made yet.")

    def reservationForm(self):
        print("\n\t=== Reservation Form ===\n")
        
        # Get customer information
        name = input("Enter Full Name: ").title()
        
        while True:
            try:
                phone = int(input("Enter Phone Number: "))
                break
            except ValueError:
                print("Enter a valid phone number!")
        
        vehicle_type = input("Enter Vehicle Type (e.g., Sedan, SUV, Coupe): ").title()
        vehicle_model = input("Enter Vehicle Model: ").title()
        pickup_date = input("Enter Pick-up Date (MM/DD/YYYY): ")
        return_date = input("Enter Return Date (MM/DD/YYYY): ")

        # Save reservation to file in formatted columns
        with open("reservations.txt", "a") as file:
            # Check if file is empty to add header
            try:
                with open("reservations.txt", "r") as read_file:
                    if not read_file.read().strip():
                        # File is empty, add header
                        file.write(f"{'Name':>19} {'Phone':>19} {'Vehicle Type':>19} {'Model':>19} {'Pick-up Date':>19} {'Return Date':>19}\n")
                        file.write("-" * 114 + "\n")
            except FileNotFoundError:
                # File doesn't exist, add header
                file.write(f"{'Name':>19} {'Phone':>19} {'Vehicle Type':>19} {'Model':>19} {'Pick-up Date':>19} {'Return Date':>19}\n")
                file.write("-" * 114 + "\n")
            
            # Write reservation data in formatted columns
            file.write(f"{name:>19} {phone:>19} {vehicle_type:>19} {vehicle_model:>19} {pickup_date:>19} {return_date:>19}\n")
        
        print(f"\nReservation confirmed for {name}!")
        print(f"Vehicle: {vehicle_type} - {vehicle_model}")
        print(f"Pick-up: {pickup_date}")
        print(f"Return: {return_date}")

    def displayMenu(self):
        """Display the main menu options"""
        print("\n" + "="*50)
        print("\t CAR RESERVATION SYSTEM ")
        print("="*50)
        print("1. View Available Cars")
        print("2. Make a Reservation")
        print("3. View Current Reservations")
        print("4. Exit")
        print("="*50)

    def runSystem(self):
        """Main system loop with menu options"""
        while True:
            self.displayMenu()
            
            try:
                choice = int(input("Enter your choice (1-4): "))
                
                if choice == 1:
                    self.availableCars()
                elif choice == 2:
                    self.reservationForm()
                elif choice == 3:
                    self.currentReservations()
                elif choice == 4:
                    print("\nThank you for using Car Reservation System!")
                    print("Have a great day!")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1-4.")
                    
            except ValueError:
                print("Invalid input! Please enter a valid number.")
            
            # Pause before showing menu again
            if choice != 4:
                input("\nPress Enter to continue...")

def main(): 
    car_reservation = CarReservation()
    car_reservation.runSystem()

if __name__ == "__main__":
    main()
