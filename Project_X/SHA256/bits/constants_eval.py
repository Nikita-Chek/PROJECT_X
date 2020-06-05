import math
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

def to_hex(num):
	i = 8
	hx = '0x'
	while i:
		d = math.modf(num * 16)
		hx += hex_digits.get(d[1])
		num = d[0]
		i -= 1
	return hx

hex_digits = {0.0:'0',1.0:'1', 2.0:'2', 3.0:'3',
				4.0:'4',5.0:'5', 6.0:'6', 7.0:'7',
				8.0:'8',9.0:'9', 10.0:'a', 11.0:'b',
				12.0:'c',13.0:'d', 14.0:'e', 15.0:'f'}

session = WolframLanguageSession('C:/Program Files/Wolfram Research/Mathematica/12.1/MathKernel.exe')
primes1 = list( session.evaluate(wl.Map(wlexpr('Prime@#&'), wl.Range(8))) )
primes2 = list( session.evaluate(wl.Map(wlexpr('Prime@#&'), wl.Range(64))) )
session.terminate()

h1 = [math.modf(math.sqrt(_))[0] for _ in primes1]
h2 = [math.modf(_ ** (1/3))[0] for _ in primes2]

with open('square_roots.txt', 'w') as f:
	for _ in h1:
		f.write(to_hex(_) + ' ')

with open('cube_roots.txt', 'w') as f:
	for _ in h2:
		f.write(to_hex(_) + ' ')