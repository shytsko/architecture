from __future__ import annotations
from pc_components import Case, PowerSupply, MotherBoard, CPU, RAM, Storage, GPU
from pc_buider import PCBuilder
from pc_service_card import PCServiceCard


class PCServiceCardBuilder(PCBuilder):
    def __init__(self):
        self._result: PCServiceCard | None = None

    def reset(self):
        self._result = PCServiceCard()
        return self

    def add_case(self, case: Case) -> PCServiceCardBuilder:
        self._result.add_component(case)
        return self

    def add_power_supply(self, power_supply: PowerSupply) -> PCServiceCardBuilder:
        self._result.add_component(power_supply)
        return self

    def add_mother_board(self, mother_board: MotherBoard) -> PCServiceCardBuilder:
        self._result.add_component(mother_board)
        return self

    def add_cpu(self, cpu: CPU) -> PCServiceCardBuilder:
        self._result.add_component(cpu)
        return self

    def add_ram(self, ram: RAM) -> PCServiceCardBuilder:
        self._result.add_component(ram)
        return self

    def add_storage(self, storage: Storage) -> PCServiceCardBuilder:
        self._result.add_component(storage)
        return self

    def add_gpu(self, gpu: GPU) -> PCServiceCardBuilder:
        self._result.add_component(gpu)
        return self

    @property
    def result(self):
        return self._result
