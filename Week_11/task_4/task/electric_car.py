from car import Car


class ElectricCar(Car):

    def __init__(self, battery_size: float, battery_range_km: float):

        if not isinstance(battery_size, float):
            raise Warning("Has to be float")

        if not isinstance(battery_range_km, float):
            raise Warning("Has to be float")

        if battery_size < 0:
            raise Warning("Negative battery capacity")
        if battery_range_km < 0:
            raise Warning("Invalid amount of electricity per km")

        self.battery_range_km = battery_range_km
        self.battery_current = battery_size
        self.battery_max = battery_size

    def charge(self, kwh):
        # over-charging should raise a Warning

        if kwh < 0:
            raise Warning("Cant negatively charge")
        if (kwh + self.battery_current) > self.battery_max:
            raise Warning("Dont overcharge the battery")
        else:
            self.battery_current += kwh

    def get_battery_status(self):
        # current and the maximum capacity in a tuple (c, c_max)

        return (self.battery_current, self.battery_max)

    def get_remaining_range(self):

        return self.battery_current * self.battery_range_km

    def drive(self, dist):

        if not isinstance(dist, float):
            raise Warning("Has to be a float")

        if dist < 0:
            raise Warning("Cant drive negative distance")

        battery_required = self.battery_range_km / dist

        if self.battery_current < battery_required:
            self.battery_current = 0
            raise Warning("Battery is depleted!")
        else:
            self.battery_current -= battery_required


e = ElectricCar(25.0, 500.0)
e.drive(100.0)
e.charge(2.0)
print(e.get_battery_status())  # (22.0, 25)
