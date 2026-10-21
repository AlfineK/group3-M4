# Fleet Management CLI

A command-line application for managing cars, drivers and customers. It is a group project built with Python.

## The Problem

Car hijacking is a big problem. This system keeps a record of every vehicle, its driver, and the customer who bought it, so cars can be tracked back to a registered person.

## Features

- Customers with a name, driver ID and payments
- Drivers with a name, mileage and driver ID
- Vehicles linked to drivers
- Data saved in JSON files

## Project Structure

```
main.py        the program you run
models/
  customer.py  Customer class
  driver.py    Driver class
  vehicle.py   Vehicle class
```

## How to Set Up

1. Clone the project:

```
git clone https://github.com/AlfineK/group3-M4.git
cd group3-M4
```

2. Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the packages, if the project has a requirements.txt file:

```
pip install -r requirements.txt
```

## How to Run

```
python main.py
```

## How the Classes Work Together

- A **Driver** gets a driver ID, like `Driver 10002`.
- A **Customer** stores that driver ID, so a customer is linked to a driver.
- A **Vehicle** is linked to a driver.



## Team

- Hope Kathomi
- Kinya Alfine
- Sandra Wanjiru
- Bradley Chacha