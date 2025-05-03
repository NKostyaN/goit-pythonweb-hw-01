from abc import abstractmethod, ABC
import logging


logging.basicConfig(
    format="%(message)s", level=logging.INFO, handlers=[logging.StreamHandler()]
)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        car = Car(make, model)
        logging.info(f"Створено {car.make} {car.model} (US Spec)")
        return car

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        moto = Motorcycle(make, model)
        logging.info(f"Створено {moto.make} {moto.model} (US Spec)")
        return moto


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        car = Car(make, model)
        logging.info(f"Створено {car.make} {car.model} (EU Spec)")
        return car

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        moto = Motorcycle(make, model)
        logging.info(f"Створено {moto.make} {moto.model} (EU Spec)")
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
