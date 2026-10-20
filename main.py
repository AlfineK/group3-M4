from models.vehicle import Vehicle
# v = Vehicle.create(20000,"toyota")


while True:
    choice = input(
        "1. To add a new vehicle, press 1.\n"
        "2. To send out a vehicle, press 2.\n"
        "3. To exit, press Q: "
    )
    if choice.lower() == "q":
        break
    if choice == "1":
        current_mileage = int(input("Enter current mileage: "))
        brand = input("Enter brand and model (eg.Toyota Hilux): ")
        v = Vehicle.create(current_mileage, brand)
        print(v.vehicles)
    if choice == "2":
        customer = input("Enter customer name: ")
        
