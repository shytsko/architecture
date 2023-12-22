from datetime import datetime, date


class NoteRecord:
    _id_generator = iter(range(1000, 2000))

    def __init__(self, title: str, details: str):
        self._id: int = self._next_id()
        self._user_id: int = 20001
        self._title: str = title
        self._details: str = details
        self._creation_date: date = datetime.date(datetime.now())
        self._edit_date: date | None = None

    def _next_id(self):
        return next(self._id_generator)

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def edit_date(self):
        return self._edit_date

    @edit_date.setter
    def edit_date(self, value):
        self._edit_date = value
