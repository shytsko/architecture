from pc_components import Case, PowerSupply, MotherBoard, CPU, RAM, Storage, GPU
from pc_assembly import PCAssembly
from pc_assembly_builder import PCAssemblyBuilder
from pc_service_card_builder import PCServiceCardBuilder

if __name__ == '__main__':
    case = Case("case1", 24, 50)
    power = PowerSupply("power1", 24, 12)
    mother_board = MotherBoard("board1", 12, 55)
    cpu = CPU("cpu1", 12, 100)
    ram1 = RAM("8Gb", 12, 100)
    ram2 = RAM("16Gb", 12, 100)
    storage = Storage("ssd1", 36, 60)

    assembly = (PCAssemblyBuilder().
                reset().
                add_case(case).
                add_power_supply(power).
                add_mother_board(mother_board).
                add_cpu(cpu).
                add_ram(ram1).
                add_ram(ram2).
                add_storage(storage).
                result)

    assembly.run_assembly()

    service_card = (PCServiceCardBuilder().
                    reset().
                    add_case(case).
                    add_power_supply(power).
                    add_mother_board(mother_board).
                    add_ram(ram1).
                    add_ram(ram2).
                    add_storage(storage).
                    result)

    print(service_card.get_components())
