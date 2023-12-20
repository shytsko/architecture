from datetime import date


class Note:
    def __init__(self, id_: int, user_id: int, title: str, details: str, creation_date: date, edit_date: date | None):
        self._id: int = id_
        self._user_id: int = user_id
        self._title: str = title
        self._details: str = details
        self._creation_date: date = creation_date
        self._edit_date: date | None = edit_date

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

    def __str__(self):
        return (f"Note <id={self._id}, user_id={self._user_id}, title={self._title},"
                f" creation_date={self._creation_date}, edit_date={self._edit_date}>")
