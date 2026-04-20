import pytest

@pytest.fixture(autouse=True)
def print_text_new():
    print("Ира, пока!")