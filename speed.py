def speed(i):

 V1= 'Increase a speed!!!'
 V2 = 'You are trying to set off the Earth!!!'
 V3 = 'You are trying to set off the Solar system!!!'
 V4 = 'Attention! Your are trying to set off the Galaxy!!!'

 if (i == 0):
    print 'Activate the speed!!!'
 elif i>0 and i <= 7.9:
    i = V1
 elif i > 7.9 and i <= 11.2:
    i = V2
 elif i > 11.2 and i <= 16.7:
    i = V3
 else:
    i = V4
 return i   
i = float(raw_input("Enter your speed:  "))
print speed(i)
