Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = int(input('Enter a nonnegative integer: '))
Enter a nonnegative integer: 48
>>> while n < 0:
	print('\nThat\'s not a nonnegative integer.')
	n = int(input('Enter a nonnegative integer: '))

	
>>> if n == 0:
	print('\n0! = 1')
else:
	factorial = 1
	for i in range(n,0,-1):
		factorial *= i
	print('\n' + str(n) + '! = ' + str(factorial))

	

48! = 12413915592536072670862289047373375038521486354677760000000000
>>> 