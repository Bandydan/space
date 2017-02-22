import math
fuelMass = 100000 # kg 1 000 000
dryMass = 5500 # kg
burnTime = 150 # s
iEngineFuelUsage = 450 # kg/s
iEngineThrust = 3800000 # N
m0 = dryMass + fuelMass
result = 0
for time in xrange(0, burnTime):
    m1 = m0 - iEngineFuelUsage
    if (m1 <= dryMass):
        break
    ms = ((m0 + m1)/2)
    Fy = (1-math.pow(result/7900,2))*9.81*ms
    if Fy < 0:
        Fy = 0
    Fx = math.sqrt(math.pow(iEngineThrust, 2)-math.pow(Fy, 2))
    if (Fx < 0):
        Fx = 0
    result = (result + Fx / ms)
    if (result >= 7900):
        print "Success: ", time
        print "Result speed: ", result
        break
    m0 = m1
