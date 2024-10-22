import pytest


@pytest.fixture
def fixture():
    print("hihihi")

def test_fixture(fixture):
    assert 1 == 1