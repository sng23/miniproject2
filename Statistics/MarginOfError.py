from Calculator import Calculator
from Statistics.zScore import z, z_given_confidence
from Statistics.standard_Deviation import standard


# me = z (s/ sqrt(n))
def margin_of_error(data, p, ddof=0):
    calc = Calculator.Calculator()
    z_score = z_given_confidence(p)
    s = standard(data, ddof)
    n = len(data)
    result = calc.multiply(z_score, calc.divide(s, calc.squareroot(n)))
    return round(result, 3)
