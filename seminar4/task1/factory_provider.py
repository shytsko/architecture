from component_info import ComponentInfo
from payment_provider import PaymentProvider
from factory import Factory


class FactoryProvider(Factory):
    def __init__(self, payment_provider: PaymentProvider):
        self._payment_provider: PaymentProvider = payment_provider
        self._components: dict[int, ComponentInfo] = {i: ComponentInfo(i, f"component {i}")
                                                      for i in range(900000, 900010)}
        self._components.update({i: ComponentInfo(i, f"component {i}") for i in range(1000, 1005)})

    def get_component(self, id_component: int) -> ComponentInfo:
        if id_component < 0:
            raise RuntimeError("Некорректный номер детали.")
        if id_component < 100000:
            raise RuntimeError("Эта деталь устаревшая")

        component = self._components.get(id_component)

        if component is None:
            raise RuntimeError("Деталь не найдена")

        price = self._payment_provider.get_price(id_component)

        if price < 10:
            raise RuntimeError("Цена слишком низкая")

        component.price = price
        if component.price != price:
            raise RuntimeError("Цена установлена неправильно")

        return component
