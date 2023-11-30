from __future__ import annotations
from pc_components import Case, PowerSupply, MotherBoard, CPU, RAM, Storage, GPU
from pc_buider import PCBuilder
from pc_assembly import PCAssembly


class PCAssemblyBuilder(PCBuilder):
    def __init__(self):
        self._result: PCAssembly | None = None

    def reset(self):
        self._result = PCAssembly()
        return self

    def add_case(self, case: Case) -> PCAssemblyBuilder:
        self._result.set_case(case)
        return self

    def add_power_supply(self, power_supply: PowerSupply) -> PCAssemblyBuilder:
        self._result.set_power_supply(power_supply)
        return self

    def add_mother_board(self, mother_board: MotherBoard) -> PCAssemblyBuilder:
        self._result.set_mother_board(mother_board)
        return self

    def add_cpu(self, cpu: CPU) -> PCAssemblyBuilder:
        self._result.add_cpu(cpu)
        return self

    def add_ram(self, ram: RAM) -> PCAssemblyBuilder:
        self._result.add_ram(ram)
        return self

    def add_storage(self, storage: Storage) -> PCAssemblyBuilder:
        self._result.add_storage(storage)
        return self

    def add_gpu(self, gpu: GPU) -> PCAssemblyBuilder:
        self._result.add_gpu(gpu)
        return self

    @property
    def result(self):
        return self._result
