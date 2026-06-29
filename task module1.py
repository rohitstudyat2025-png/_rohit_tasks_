import math as m
#1) Constants function
print("1) Constants function ")
print(m.pi)
print(m.e)
print(m.tau)
print(m.inf)
print(m.nan)
print("\n")

#2) Basic functions
print("2) Basic functions")
print(m.sqrt(625))
print(m.pow(4,2))
print(m.factorial(4))
print(m.fabs(-8))
print(m.gcd(3,18))
print(m.lcm(4,16))
print('\n')

#3) Rounding function
print("3) Rounding function")
print(m.ceil(7.6))
print(m.floor(4.5))
print(m.trunc(4.5))
print(round(4.5384723894789,5))
print('\n')

#4) Trigonometic functions(angles in radians)
print("4) Trigonometic functions(angles in radians)")
print(m.sin(m.pi))
print(m.cos(m.pi))
print(m.tan(m.pi))
print(m.asin(1))
print(m.acos(1))
print(m.atan(1))
print('\n')

#5) Convert between degrees and radians
print("5) Convert between degrees and radians")
print(m.radians(180))
print(m.degrees(m.pi))
print('\n')

#6) Logarithmic and exponential function
print("6) Logarithmic and exponential function")
print(m.log(100,10))
print(m.log10(100))
print(m.log2(2))
print(m.exp(3))
print(m.expm1(1))
print('\n')

#7) Hyperbolic functions
print("7) Hyperbolic functions")
print(m.sinh(1))
print(m.cosh(1))
print(m.tanh(1))
print("\n")

#8) Other useful function
print("8) Other useful function")
print(m.isqrt(37))
print(m.perm(5,2))
print(m.comb(5,2))
print(m.fmod(10.4,3))
print(m.remainder(10,3))
print(m.copysign(3,-1))
