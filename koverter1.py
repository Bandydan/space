def konv(a, b, c):
	p={'m':1, 'km':1000, 'au':149597870700, 'ly':9460730472580800, 'pc':30856776000000000}
	return a* p[b]/ p[c]

print 'Please enter value'
x = float(raw_input())
print 'First unit of measurement (m, km, au, ly, pc )'
p1= raw_input()
print 'Second unit of measurement (m, km, au, ly, pc )'
p2= raw_input()
print str(x)+p1+ ' = '+ str( konv(x,p1,p2))+p2
