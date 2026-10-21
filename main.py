import random

from models.vehicle import Vehicle
from models.driver import Driver
from models.customer import Customer
from services.dispatch import dispatch, print_summary

drivers_list = ["Samuel", "Naledi", "Tendai", "Aisha",
                "Kwame", "Lerato", "Mpho", "Farai"]
customers_list = ["Bradley", "Amara", "Chen Wei", "Diego",
                  "Fatima", "Grace", "Hiroshi", "Imani"]
brands = ["Toyota Hilux", "Toyota Prado", "Ford Ranger", "Nissan Navara",
          "Mazda BT-50", "Isuzu D-Max"]


def make_vehicles(n):
    for i in range(n):
        Vehicle.create(random.randint(5000, 80000), brands[i % len(brands)])


def make_drivers(n):
    for i in range(n):
        Driver.create(drivers_list[i % len(drivers_list)], random.randint(500, 5000))


def make_customers(n):
    for i in range(n):
        Customer(customers_list[i % len(customers_list)],
                 payment=random.randint(0, 2500))


def link(drivers, vehicles):
    for i, c in enumerate(Customer.all()):
        c.driver_id = drivers[i % len(drivers)].driver_id
    for i, d in enumerate(drivers):
        d.vehicle = vehicles[i % len(vehicles)]


def show_all():
    print("\n--- vehicles ---")
    for v in Vehicle.all():
        print(" ", v)
    print("\n--- drivers ---")
    for d in Driver.all():
        print(" ", d)
    print("\n--- customers ---")
    for c in Customer.all():
        print(" ", c)


def ask(prompt):
    while True:
        v = input(prompt).strip()
        if v:
            return v


def main():
    make_drivers(4)
    make_vehicles(4)
    make_customers(4)

    link(Driver.all(), Vehicle.all())

    show_all()
    print_summary()

    while True:
        choice = input("\n1 add vehicle  2 dispatch  3 summary  4 show all  q quit\n> ").strip().lower()
        if choice == "q":
            break
        if choice == "1":
            v = Vehicle.create(int(ask("mileage: ")), ask("brand: "))
            print("added", v)
        elif choice == "2":
            vs = Vehicle.all()
            for i, v in enumerate(vs, 1):
                print(i, "-", v.vehicle_id, v.brand)
            sel = vs[int(ask("pick: ")) - 1]
            cust, drv, veh = dispatch(sel.vehicle_id, ask("driver: "), ask("customer: "))
            print(cust.name, "->", drv.driver_name, "->", veh.vehicle_id)
        elif choice == "3":
            print_summary()
        elif choice == "4":
            show_all()
        else:
            print("?")


if __name__ == "__main__":
    main()