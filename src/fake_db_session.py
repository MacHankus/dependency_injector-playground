from typing import Generator


class FakeDbSession:
    def do_something(self) -> None:
        print("Done something")


def get_fake_db_session() -> FakeDbSession:
    return FakeDbSession()
