from calculadora import Calculator 

calculator = Calculator()

def test_add():
    result = calculator.add(2,3)
    assert result == 5        


def test_sub():
    result = calculator.sub(5,2)
    assert result == 3