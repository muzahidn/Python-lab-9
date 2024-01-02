class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

    def accelerate(self, change_of_speed):
        if change_of_speed < 0:
            if self.current_speed + change_of_speed < 0:
                self.current_speed = 0 # The car stops
            else:
                self.current_speed = self.current_speed - change_of_speed
        elif change_of_speed > 0:
            if self.current_speed + change_of_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            else:
                self.current_speed = self.current_speed + change_of_speed


def main():
    car1 = Car('ABC-123', 142)
    car1.accelerate(30)
    car1.accelerate(70)
    car1.accelerate(50)
    car1.accelerate(-200)
    print(f'The current speed is {car1.current_speed} km/h')


main()