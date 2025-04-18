# Assignment 1: Smartphone Class

class Smartphone:
    def _init_(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"

# Inherited class
class SmartCameraPhone(Smartphone):
    def _init_(self, brand, model, storage, camera_megapixels):
        super()._init_(brand, model, storage)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"Taking photo with {self.camera_megapixels}MP camera"

# Test the classes
phone1 = Smartphone("OPPO", "A76",128)
phone2 = SmartCameraPhone("iPhone", "14 Pro", 128, 48)

print(phone1.info())
print(phone1.call("07123456780"))

print(phone2.info())
print(phone2.take_photo())


# ============================
# Activity 2: Polymorphism
# ============================

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈"

# Polymorphism in action
vehicles = [Car(), Plane()]

for v in vehicles:
    print(v.move())