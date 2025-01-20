from car import Car


class CombustionCar(Car):

    def __init__(self, gas_capacity: float, gas_per_100km: float):

        if not isinstance(gas_capacity, float):
            raise Warning("Has to be float")

        if not isinstance(gas_per_100km, float):
            raise Warning("Has to be float")

        if gas_capacity < 0:
            raise Warning("Negative gas capacity")
        if gas_per_100km < 0:
            raise Warning("Invalid gas per 100km")

        self.gas_per_100km = gas_per_100km
        self.c_current = gas_capacity
        self.c_max = gas_capacity

    def fuel(self, f):
        # adds f liters of fuel to the gas tank. The method should raise a Warning, if the gas tank gets overfilled
        if f <= 0:
            raise Warning("No fuel being tanked")
        if (self.c_current + f) > self.c_max:
            raise Warning("Gas tank is overflowing!")
        else:
            self.c_current += f

    def get_gas_tank_status(self):
        # call to get_gas_tank_status returns the c_current gas tank capacity c and the maximum capacity c_max as a tuple (c, c_max). It must always be that 0 <= c <= c_max

        return (self.c_current, self.c_max)

    def get_remaining_range(self):

        return (self.c_current * 100) / self.gas_per_100km

    def drive(self, dist):
        # drive should remove the correct amount of gas from the gas tank and it should raise a Warning if the gas tank is fully depleted through driving.

        if not isinstance(dist, float):
            raise Warning("Has to be a float")

        if dist < 0:
            raise Warning("Cant drive negative distance")

        gas_per_dist = (dist/100) * self.gas_per_100km

        if self.c_current - gas_per_dist <= 0:
            self.c_current = 0
            raise Warning("Gas is depleted!")
        else:
            self.c_current -= gas_per_dist


c = CombustionCar(40.0, 8.0)
print(c.get_remaining_range())  # 500
c.drive(25.0)
print(c.get_gas_tank_status())  # (38.0, 40.0)
c.drive(1000.0)  # fuel is depleted, Warning raised
