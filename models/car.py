class Car:
    def __init__(self, city, manufacture, model, year, fuel,
                 seats, car_class, serial_number, price_per_day,
                 gear="Automatic", wheels_drive="FWD", photo_path=None):
        self.city = city
        self.manufacture = manufacture
        self.model = model
        self.year = year
        self.fuel = fuel
        self.seats = seats
        self.car_class = car_class
        self.serial_number = serial_number
        self.price_per_day = price_per_day
        self.gear = gear
        self.wheels_drive = wheels_drive
        self.photo_path = photo_path