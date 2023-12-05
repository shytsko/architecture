from wiping import Wiping


class WashingStation(Wiping):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def wip_mirrors(self):
        print("Помыли зеркала")

    def wip_windshield(self):
        print("Помыли лобовое стекло")

    def wip_head_lights(self):
        print("Помыли фары")
