from __future__ import annotations
from abc import ABC, abstractmethod
from pc_components import Case, PowerSupply, MotherBoard, CPU, RAM, Storage, GPU


class PCBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def add_case(self, case: Case) -> PCBuilder:
        pass

    @abstractmethod
    def add_power_supply(self, power_supply: PowerSupply) -> PCBuilder:
        pass

    @abstractmethod
    def add_mother_board(self, mother_board: MotherBoard) -> PCBuilder:
        pass

    @abstractmethod
    def add_cpu(self, cpu: CPU) -> PCBuilder:
        pass

    @abstractmethod
    def add_ram(self, ram: RAM) -> PCBuilder:
        pass

    @abstractmethod
    def add_storage(self, storage: Storage) -> PCBuilder:
        pass

    @abstractmethod
    def add_gpu(self, gpu: GPU) -> PCBuilder:
        pass
