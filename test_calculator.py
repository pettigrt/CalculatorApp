import calculator


class TestCalculator:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_sutract(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self):
        assert 20 == calculator.multiply(5, 4)
