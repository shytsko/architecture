from harvester import Harvester
from refueling_station import RefuelingStation
from super_car import SuperCar
from color import Color
from washing_station import WashingStation
from service_station import ServiceStation

if __name__ == '__main__':
    refueling_station = RefuelingStation("Заправочная станция 1")
    washing_station = WashingStation("Мойка 1")
    service_station = ServiceStation("Сервисная станция 1")

    super_car = SuperCar("super car", "1", Color.RED)

    super_car.go_to_refueling(refueling_station)
    super_car.refuel()
    super_car.leave_refueling()

    super_car.go_to_washing(washing_station)
    super_car.washing()
    super_car.leave_washing()

    super_car.go_to_refueling(service_station)
    super_car.refuel()
    super_car.leave_refueling()

    super_car.go_to_washing(service_station)
    super_car.washing()
    super_car.leave_washing()

    harvester = Harvester("harvester", "2", Color.BLACK)

    harvester.go_to_refueling(refueling_station)
    harvester.refuel()
    harvester.leave_refueling()

    harvester.go_to_washing(washing_station)
    harvester.washing()
    harvester.leave_washing()

    harvester.go_to_refueling(service_station)
    harvester.refuel()
    harvester.leave_refueling()

    harvester.go_to_washing(service_station)
    harvester.washing()
    harvester.leave_washing()
