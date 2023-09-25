import re

def verifyInput(input):
  if (re.match(r'^(f\(x\)\s?=\s?)?([a-zA-Z]|\d)\s?(\*|\+|\-|\/|\**)*\s?\d+', input)):
    return True
  return False

print(verifyInput('f(x) = x * 323'))
print(verifyInput('x**2'))