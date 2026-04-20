import pytest

@pytest.fixture(autouse=True)
def print_text_new_new():
    print("Ира, мяу!")