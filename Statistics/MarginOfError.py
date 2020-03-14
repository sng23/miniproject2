from Calculator import Calculator
from Statistics.zScore import z
from Statistics.standard_Deviation import standard


# me = z (s/ sqrt(n))
def margin_of_error(data, x):
    calc = Calculator.Calculator()
    z_score = abs(z(data, x))
    std_dev = standard(data)
    n = len(data)
    result = calc.multiply(z_score, calc.divide(std_dev, calc.squareroot(n)))
    return round(result, 3)
