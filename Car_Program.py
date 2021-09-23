import Car_Class as xx

def main():


    car = xx.Car("2014","Buick")
    print("Accelerating the car...")

    for v in range(5):
        car.accelerate()
        print("Current speed:",car.get_speed())

    print("Decelerating the car...")


    for v in range(5):
        car.brake()
        print("Current speed:",car.get_speed())

main()
