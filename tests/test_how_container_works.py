import pytest
from fake_functions import fake_function

from fake_repositories import FakeRepository, FakeRepositoryForInject
from unittest.mock import Mock
from dependency_injector import providers


def test_should_return_repository_instance(container):
    # Act
    repository = container.repository()

    # Assert
    assert isinstance(repository, FakeRepository)


def test_should_call_dependency_inside_repository(container):
    # Arrange
    mock_dependency = Mock()
    mock_dependency.do_something = Mock()
    # Act
    with container.db_session.override(providers.Factory(lambda: mock_dependency)):
        repository = container.repository()
        repository.get_data()
    # Assert
    mock_dependency.do_something.assert_called_once()


def test_should_call_dependency_inside_fake_function(container):
    # Arrange
    mock_dependency = Mock()
    mock_dependency.do_something = Mock()
    # Act
    with container.db_session.override(providers.Factory(lambda: mock_dependency)):
        fake_function()
    # Assert
    mock_dependency.do_something.assert_called_once()


def test_should_call_dependency_inside_fake_repository_for_inject(container):
    # Arrange
    mock_dependency = Mock()
    mock_dependency.do_something = Mock()
    # Act
    with container.db_session.override(providers.Factory(lambda: mock_dependency)):
        repository = container.repository_for_inject()
        repository.get_data()
    # Assert
    mock_dependency.do_something.assert_called_once()
