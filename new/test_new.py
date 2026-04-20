import pytest

@pytest.fixture(autouse=True)
def print_text():
    print("Ира, привет!")

def test_new():
    assert True == True
