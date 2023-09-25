import re

def verifyInput(input):
  if (re.match(r'^(f\(x\)=)?([a-zA-Z]|\d)(\*|\+|\-|\/|\**)*\d+$', input)):
    return True
  return False

print(verifyInput('f(x)=x*323'))
print(verifyInput('x**2'))