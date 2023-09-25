import re

def verifyInput(input):
  if (re.match(r'^([a-zA-Z]\([a-zA-Z]\)\s?=\s?)?((([a-zA-Z]|\d)\s?(\*|\+|\-|\/|\**)*\s?\d+)|[a-zA-Z])', input)):
    return True
  return False

print(verifyInput('f(x) = x * 323'))
print(verifyInput('x**2'))