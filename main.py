from models.vehicle import Vehicle
from models.customer import Customer

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
        # print("cars ",Vehicle.vehicles)
        customer = Customer("Bradley", "DL001")
        list_of_Vehicles = [key for key in Vehicle.vehicles.keys()]

        print(f"Customer name: {customer.name}")
        print("Available vehicles: ")

        for index, vehicle in enumerate(list_of_Vehicles, start=1):
            print(f"{index} - {vehicle}")
        choice = input("Select a vehicle")

        
