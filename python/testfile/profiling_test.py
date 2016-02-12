def calcuate(x):
    res = (x * x / 3 * x ** x + 10000) * x
    print res
    return res


# import profile
# profile.run('calcuate(32167)')
import cProfile
num = 32167
cProfile.run('calcuate(num)', '/tmp/output')
