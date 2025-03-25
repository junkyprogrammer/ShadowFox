#Creating a class MobilePhone
class MobilePhone:
    def __init__(self, screen_type="Touch Screen", network_type="4G/5G", dual_sim=False,
                 front_camera="5MP", rear_camera="8MP", ram="2GB", storage="16GB"):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, number):
        print(f"Receiving call from {number}...")

    def take_a_picture(self):
        print(f"Taking a picture with {self.front_camera} front camera...")

#creating a class Apple
class Apple(MobilePhone):
    def __init__(self, model, storage, ram, dual_sim=False):
        super().__init__(dual_sim=dual_sim, ram=ram, storage=storage)
        self.brand = "Apple"
        self.model = model

    def get_info(self):
        return (f"{self.brand} {self.model}: {self.screen_type}, {self.network_type}, "
                f"Dual SIM: {self.dual_sim}, Front Camera: {self.front_camera}, "
                f"Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}")

#creating a class Samsung
class Samsung(MobilePhone):
    def __init__(self, model, storage, ram, dual_sim=False):
        super().__init__(dual_sim=dual_sim, ram=ram, storage=storage)
        self.brand = "Samsung"
        self.model = model

    def get_info(self):
        return (f"{self.brand} {self.model}: {self.screen_type}, {self.network_type}, "
                f"Dual SIM: {self.dual_sim}, Front Camera: {self.front_camera}, "
                f"Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}")


# Create some objects of Apple class with different properties
iphone_14 = Apple(model="iPhone 14", storage="128GB", ram="4GB", dual_sim=True)
iphone_12 = Apple(model="iPhone 12", storage="64GB", ram="3GB", dual_sim=False)

# Create some objects of Samsung class with different properties
galaxy_s21 = Samsung(model="Galaxy S21", storage="256GB", ram="8GB", dual_sim=True)
galaxy_a52 = Samsung(model="Galaxy A52", storage="128GB", ram="6GB", dual_sim=False)

# Show details of the phones
for phone in [iphone_14, iphone_12, galaxy_s21, galaxy_a52]:
    print(phone.get_info())
    
