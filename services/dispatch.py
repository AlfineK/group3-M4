from models.vehicle import Vehicle
from models.driver import Driver
from models.customer import Customer


def dispatch(vehicle_id, driver_name, customer_name, payment=0):
    vehicle = Vehicle.get(vehicle_id)
    if not vehicle:
        raise ValueError("No vehicle with that ID")

    driver = None
    for d in Driver.all():
        if d.driver_name.lower() == driver_name.strip().lower():
            driver = d
            break
    if not driver:
        driver = Driver.create(driver_name, mileage=vehicle.mileage)
    driver.vehicle = vehicle

    customer = None
    for c in Customer.all():
        if c.name.lower() == customer_name.strip().lower():
            customer = c
            break
    if not customer:
        customer = Customer(customer_name)
    customer.driver_id = driver.driver_id
    customer.payment = payment

    return customer, driver, vehicle


def print_summary():
    customers = Customer.all()
    if not customers:
        print("no customers yet")
        return
    print(f"{'Cust ID':<8} {'Customer':<12} {'Driver ID':<12} {'Driver':<10} {'Vehicle':<12} {'Brand':<15} Paid")
    print("-" * 88)
    for c in customers:
        driver = Driver.get(c.driver_id) if c.driver_id else None
        vehicle = driver.vehicle if driver else None
        did = driver.driver_id if driver else "-"
        dname = driver.driver_name if driver else "-"
        vid = vehicle.vehicle_id if vehicle else "-"
        brand = vehicle.brand if vehicle else "-"
        print(f"{c.customer_id:<8} {c.name:<12} {did:<12} {dname:<10} {vid:<12} {brand:<15} {c.payment:.2f}")
