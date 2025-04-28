from abc import abstractmethod, ABC


class Vehicle(ABC):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str):
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str):
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str):
        car = Car(make, model)
        print(f"Створено {car.make} {car.model} (US Spec)")
        return car

    def create_motorcycle(self, make: str, model: str):
        moto = Motorcycle(make, model)
        print(f"Створено {moto.make} {moto.model} (US Spec)")
        return moto


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str):
        car = Car(make, model)
        print(f"Створено {car.make} {car.model} (EU Spec)")
        return car

    def create_motorcycle(self, make: str, model: str):
        moto = Motorcycle(make, model)
        print(f"Створено {moto.make} {moto.model} (EU Spec)")
        return moto


# Використання
us_vehicle = USVehicleFactory()
eu_vehicle = EUVehicleFactory()

car1 = us_vehicle.create_car("Lincoln", "Continental")
car1.start_engine()
car2 = eu_vehicle.create_car("Reliant", "Regal Supervan")
car2.start_engine()

moto1 = us_vehicle.create_motorcycle("Harley-Davidson", "Fat Boy")
moto1.start_engine()
moto2 = eu_vehicle.create_motorcycle("Ducati", "996")
moto2.start_engine()
