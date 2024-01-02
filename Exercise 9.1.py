class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed


def main():
    car1 = Car('ABC-123', 142)
    print(car1.registration_number)
    print(f'{car1.maximum_speed} km/h')
    print(car1.current_speed)
    print(car1.travelled_distance)


main()
