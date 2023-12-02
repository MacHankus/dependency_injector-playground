from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector import providers

from fake_db_session import get_fake_db_session
from fake_repositories import FakeRepository, FakeRepositoryForInject


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=["fake_db_session", "fake_repositories", "fake_function"]
    )

    db_session = providers.Factory(get_fake_db_session)

    repository = providers.Factory(FakeRepository, db_session=db_session)

    repository_for_inject = providers.Factory(FakeRepositoryForInject)
