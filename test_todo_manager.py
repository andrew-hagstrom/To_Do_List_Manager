# def test_helloworldfunction():
#     assert practice(1, 2)==3

from todolist import user_input
from todolist import add_answer


def test_user_input():
    assert type(user_input("What's up?")) ==str

def test_add_answer():
    assert add_answer("Walk the dog") == ["Walk the dog"]