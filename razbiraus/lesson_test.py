from razbiraus.calculator import Calculator

calculator=Calculator()

res = calculator.sum(4,5)
assert res==9

numbers = [1,2,3,4,5,6,7,8,9,5]
res = calculator.avg(numbers)
assert res == 5

res = calculator.pow(4,4)
assert res == 256

res = calculator.mult(5,6)
assert res == 30