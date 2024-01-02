from random import randint


class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

    def accelerate(self, change_of_speed):
        if change_of_speed < 0:
            if self.current_speed + change_of_speed < 0:
                self.current_speed = 0  # The car stops
            else:
                self.current_speed = self.current_speed - change_of_speed
        elif change_of_speed > 0:
            if self.current_speed + change_of_speed > self.maximum_speed:
                self.current_speed = self.maximum_speed
            else:
                self.current_speed = self.current_speed + change_of_speed

    def drive(self, number_of_hours_drove):
        self.travelled_distance += (self.current_speed * number_of_hours_drove)


def main():
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        maximum_speed = randint(100, 200)
        car = Car(registration_number, maximum_speed)
        cars.append(car)

    total_race_distance = 10000
    is_over = False

    while True:
        if is_over:
            break
        for each_car in cars:
            speed_increase = randint(-10, 15)
            each_car.accelerate(speed_increase)
            each_car.drive(1)
            if each_car.travelled_distance >= total_race_distance:
                is_over = True
                break

    print(f"Reg-Number | Max-Speed (km/h) | Distance (km)")
    for car in cars:
        if car.travelled_distance >= 10000:
            distance = f'{car.travelled_distance} -> ( Winner )'
        else:
            distance = car.travelled_distance
        print(f"{car.registration_number}     |     {car.maximum_speed:}     |     {distance}")


main()
