class Customer:
    counter = 1
    _customers = {}

    def __init__(self, name, driver_id=None, payment=0, customer_id=None):
        self.name = name
        self.payment = payment
        self.customer_id = customer_id if customer_id else self._next()
        self.driver_id = driver_id
        Customer._customers[self.customer_id] = self

    @classmethod
    def _next(cls):
        cid = Customer.counter
        Customer.counter += 1
        return cid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip().title()

    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, value):
        if value is not None and not str(value).strip():
            raise ValueError("Driver ID cannot be blank")
        self._driver_id = str(value).strip() if value is not None else None

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, value):
        if float(value) < 0:
            raise ValueError("Payment cannot be negative")
        self._payment = float(value)

    def add_payment(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be more than 0")
        self.payment = self.payment + amount

    @classmethod
    def get(cls, customer_id):
        return cls._customers.get(customer_id)

    @classmethod
    def all(cls):
        return list(cls._customers.values())

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "driver_id": self.driver_id,
            "payment": self.payment,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            driver_id=data.get("driver_id"),
            payment=data.get("payment", 0),
            customer_id=data.get("customer_id"),
        )

    def __str__(self):
        return f"{self.customer_id} | {self.name} | driver={self.driver_id or '-'} | paid={self.payment}"
