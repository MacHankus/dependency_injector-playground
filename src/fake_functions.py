
from fake_db_session import FakeDbSession
from dependency_injector.wiring import inject, Provide


@inject
def fake_function(db_session: FakeDbSession = Provide["db_session"]):
    db_session.do_something()