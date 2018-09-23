# https://open.kattis.com/problems/temperatureconfusion


from fractions import Fraction


n, d = map(int, input().split('/'))
f = Fraction(n, d)
f -= 32
f *= Fraction(5, 9)

print('%s/%s' % (f.numerator, f.denominator))
