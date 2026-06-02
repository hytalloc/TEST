import pytest


@pytest.fixture
def usuario_fake():
    return {
        "nome": "João",
        "email": "teste@email.com"
    }