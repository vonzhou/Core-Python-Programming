#P347

x = 3 + 0.14j
print x.__class__
print dir(x)

print x.real
print x.imag
print x.conjugate()

# Error
print x.__dict__