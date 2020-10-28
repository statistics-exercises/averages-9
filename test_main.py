import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_second_moment(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        samples = np.zeros(100)
        for j in range(100) :
          sss = np.random.uniform( size=len(this_y) )
          mean = sum(sss) / len(sss)
          for k in range(len(this_y)) : 
            myvar = sss[k] - mean 
            samples[j] = samples[j] + myvar*myvar
          samples[j] = samples[j] / len(this_y)
        self.assertTrue( this_y[-1]>np.percentile(samples,1) and this_y[-1]<np.percentile(samples,99), "the second central moment is not correct" )
        
    def test_third_moment(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        samples = np.zeros(100)
        for j in range(100) :
          sss = np.random.uniform( size=len(this_y) )
          mean = sum(sss) / len(sss)
          for k in range(len(this_y)) : 
            myvar = sss[k] - mean 
            samples[j] = samples[j] + myvar*myvar*myvar
          samples[j] = samples[j] / len(this_y)
        self.assertTrue( this_y[-1]>np.percentile(samples,1) and this_y[-1]<np.percentile(samples,99), "the third central moment is not correct" )
        
    def test_third_moment(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[2].get_xydata()
        this_x, this_y = zip(*figdat)
        samples = np.zeros(100)
        for j in range(100) :
          sss = np.random.uniform( size=len(this_y) )
          mean = sum(sss) / len(sss)
          for k in range(len(this_y)) : 
            myvar = sss[k] - mean 
            samples[j] = samples[j] + myvar*myvar*myvar*myvar
          samples[j] = samples[j] / len(this_y)
        self.assertTrue( this_y[-1]>np.percentile(samples,1) and this_y[-1]<np.percentile(samples,99), "the fourth central moment is not correct" )
