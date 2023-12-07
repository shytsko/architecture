from dealer_provider import DealerProvider
from factory_provider import FactoryProvider
from component_info import ComponentInfo
from payment_provider import PaymentProvider

if __name__ == '__main__':
    factory_provider = FactoryProvider(PaymentProvider())
    dealer_provider = DealerProvider(factory_provider)

    component = dealer_provider.get_component(900020)
    if component is not None:
        print(component)
