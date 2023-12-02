from typing import Generator
import pytest 
from container import Container

@pytest.fixture
def container() -> Generator[Container, None, None]:
    yield Container()