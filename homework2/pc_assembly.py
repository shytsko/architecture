from pc_components import Case, PowerSupply, MotherBoard, CPU, RAM, Storage, GPU


class PCAssembly:

    def __init__(self):
        self._case: Case | None = None
        self._power_supply: PowerSupply | None = None
        self._mother_board: MotherBoard | None = None
        self._cpu: list[CPU] = []
        self._ram: list[RAM] = []
        self._storage: list[Storage] = []
        self._gpu: list[GPU] = []

    def set_case(self, case: Case):
        self._case = case

    def set_power_supply(self, power_supply: PowerSupply):
        self._power_supply = power_supply

    def set_mother_board(self, mother_board: MotherBoard):
        self._mother_board = mother_board

    def add_cpu(self, cpu: CPU):
        self._cpu.append(cpu)

    def add_ram(self, ram: RAM):
        self._ram.append(ram)

    def add_storage(self, storage: Storage):
        self._storage.append(storage)

    def add_gpu(self, gpu: GPU):
        self._gpu.append(gpu)

    def run_assembly(self):
        cpu_str = "; ".join(map(str, self._cpu))
        ram_str = "; ".join(map(str, self._ram))
        storage_str = "; ".join(map(str, self._storage))
        gpu_str = "; ".join(map(str, self._gpu))
        print(f"In case {self._case}:\n"
              f"install power supply: {self._power_supply}\n"
              f"install mother_board: {self._mother_board}\n"
              f"install cpu: [{cpu_str}]\n"
              f"install ram: [{ram_str}]\n"
              f"install storages: [{storage_str}]\n"
              f"install gpu: [{gpu_str}]")
