from dependency_injector.wiring import inject, Provide
from fake_db_session import FakeDbSession


class FakeRepository:
    def __init__(self, db_session: FakeDbSession):
        self.db_session = db_session

    def get_data(self) -> None:
        self.db_session.do_something()
