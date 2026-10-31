
import uuid
from faker import Faker
from models.car import Car

faker = Faker()

CITY_OPTIONS = [
    "Tel Aviv", "Jerusalem", "Haifa", "Petah Tikva",
    "Ashdod", "Netanya", "Beersheba", "Bnei Brak"
]

FUEL_OPTIONS = ["Petrol", "Diesel", "Hybrid", "Electric"]
MANUFACTURE_OPTIONS = ["Toyota", "Honda", "Ford", "BMW", "Mazda"]
MODEL_OPTIONS = ["Camry", "Civic", "Focus", "X5", "Premium"]
CAR_CLASS_OPTIONS = ["Economy","Comfort","Business","Premium"]
GEAR_OPTIONS = ["Automatic", "Manual"]
WHEELS_DRIVE_OPTIONS = ["FWD", "RWD", "AWD"]

def create_car(city = None, fuel = None, manufacturer = None, model = None, year = None,
               seats=None, car_class = None, serial_number = None, price = None,
               gear = None, wheels_drive = None, photo_path=None):
    return Car(
        city = city if city is not None else faker.random_element(CITY_OPTIONS),
        manufacture = manufacturer if manufacturer is not None else faker.random_element(MANUFACTURE_OPTIONS),
        model = model if model is not None else faker.random_element(MODEL_OPTIONS),
        year = year if year is not None else faker.random_int(min = 2000, max = 2026),
        fuel = fuel if fuel is not None else faker.random_element(FUEL_OPTIONS),
        seats= seats if seats is not None else faker.random_int(min=2, max=7),
        car_class = car_class if car_class is not None else faker.random_element(CAR_CLASS_OPTIONS),
        serial_number = serial_number if serial_number is not None else "MM"+uuid.uuid4().hex[:8].upper(),
        price_per_day = price if price is not None else faker.random_int(min=20,max=500),
        gear = gear if gear is not None else faker.random_element(GEAR_OPTIONS),
        wheels_drive = wheels_drive if wheels_drive is not None else faker.random_element(WHEELS_DRIVE_OPTIONS),
        photo_path=photo_path
    )