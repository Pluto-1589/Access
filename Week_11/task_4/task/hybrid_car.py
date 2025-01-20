from combustion_car import CombustionCar
from electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.default_mode = "electric"

    # the two methods switch_to_combustion and switch_to_electric can be used to change the operation mode. Should the car run out of fuel or battery during a tour, it should automatically switch the mode. If both modes are fully depleted, the car should raise a Warning.
    def switch_to_combustion(self):
        self.default_mode = "combustion"

    def switch_to_electric(self):
        self.default_mode = "electric"

    def get_remaining_range(self):
        CombustionCar.get_remaining_range(
            self) + ElectricCar.get_remaining_range(self)

    def drive(self, dist):

        if not isinstance(dist, float):
            raise Warning("Has to be a float")

        if dist < 0:
            raise Warning("Can't drive negative distance")

        if dist > self.get_remaining_range:
            raise Warning("Can't drive that far!")
        if self.default_mode:
            electric_range = ElectricCar.get_remaining_range(self)

            if dist > electric_range:
                ElectricCar.drive(self, electric_range)
                self.switch_to_combustion()
                CombustionCar.drive(self, dist - electric_range)
            else:
                ElectricCar.drive(self, dist)

            combustion_range = CombustionCar.get_remaining_range(self)
            if dist > combustion_range:
                CombustionCar.drive(self, combustion_range)
                self.switch_to_electric()
                ElectricCar.drive(self, dist - combustion_range)
            else:
                CombustionCar.drive(self, dist)


h = HybridCar(40.0, 8.0, 25.0, 500.0)
h.switch_to_combustion()
h.drive(600.0)  # depletes fuel, auto-switch
print(h.get_gas_tank_status())  # (0.0, 40.0)
print(h.get_battery_status())  # (20.0, 25.0)
