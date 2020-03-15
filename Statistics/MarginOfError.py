from Calculator import Calculator
from Statistics.zScore import z, z_given_p
from Statistics.standard_Deviation import standard


# me = z (s/ sqrt(n))
def margin_of_error(data, p, ddof=0):
    calc = Calculator.Calculator()
    z_score = abs(z_given_p(p))
    s = standard(data, ddof)
    n = len(data)
    result = calc.multiply(z_score, calc.divide(s, calc.squareroot(n)))
    return round(result, 3)
