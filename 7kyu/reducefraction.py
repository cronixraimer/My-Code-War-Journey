import math

def reduce_fraction(fraction):
    numerator, deminator = fraction

    #finding the greatest common divisor (gcd) of the numerator and denominator

    gcd = math.gcd(numerator, deminator)

    #reducing the freaction by divinding both numerator and dominator by gcd

    reduce_num = numerator //gcd
    reduce_den = deminator // gcd

    return [reduce_num, reduce_den]

fraction_test = [45, 120]
result = reduce_fraction(fraction_test)
print(result)
