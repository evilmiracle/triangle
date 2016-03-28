import math
def angel(small,middle):
	#tall = (small*small)+(middle*middle)
	tall = math.sqrt((small*small)+(middle*middle))
	return "the right triangle third side's length"+str(tall)
A = angel(3,4)
print A
