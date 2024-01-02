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

    def drive(self, number_of_hours_drove):
        self.travelled_distance += self.current_speed * number_of_hours_drove


def main():
    car1 = Car('ABC-123', 142)
    car1.travelled_distance = 2000
    car1.current_speed = 60
    car1.drive(1.5)


    print(f'The total travel distance is {round(car1.travelled_distance)} km.')


main()
