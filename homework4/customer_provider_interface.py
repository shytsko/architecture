from abc import ABC, abstractmethod

from customer import Customer


class ICustomerProvider(ABC):

    @abstractmethod
    def registration(self, login: str, password: str):
        """
        Регистрация пользователя.
        :param login: Логин нового пользователя. Должен быть уникальным. Если пользователь с таким логином существует,
         должно возбуждаться исключение.
        :param password: Пароль нового пользователя. Длина пароля должна быть не менее 8 символов
        :return:
        """
        pass

    @abstractmethod
    def get_customer(self, login: str, password: str) -> Customer:
        """
        Получить пользователя с указанным логином и паролем. Если пользователь не существует или логин или пароль не
         верные, должно возбуждаться исключение
        :param login:
        :param password:
        :return:
        """
        pass
