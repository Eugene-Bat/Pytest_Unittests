import pytest

from Pytest_Unittests.main import calculator


def test_plus():
    assert calculator('2+2') == 4


def test_minus():
    assert calculator('3-2') == 1


def test_multiply():
    assert calculator('2*2') == 4


def test_divide():
    assert calculator('6/2') == 3


def test_no_sigbs():
    with pytest.raises(ValueError) as error:
        calculator('qwerty')
    assert ('Must contain at least one of the allowed signs', error.value.args[0])


def test_many_sigbs():
    with pytest.raises(ValueError) as error:
        calculator('3+3+7*2/3')
    assert ('The expression must contain two integers and one sign', error.value.args[0])


def test_no_ints():
    with pytest.raises(ValueError) as error:
        calculator('3+3+7')
    assert ('The expression must contain two integers and one sign', error.value.args[0])


def test_strings():
    with pytest.raises(ValueError) as error:
        calculator('a+f')
    assert ('The expression must contain two integers and one sign', error.value.args[0])


if __name__ == '__main__':
    pytest.main()
