"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 22:35:53 2017
Number of code lines: 
34
"""
""" Based on lecture of MIT 6.00 Opencourseware """ 

""" A problem that pascal and fermat try to solve is if we have a fair dice, you roll 24 times, 
    is it worth betting on not getting 2 <6,6> ? 

    What is the probability of getting 6 is 1/6 in the first dice and 1/6 in the other
    so the probability of getting <6,6> in the first try is 1/36 
    So the probability of not getting <6,6> is 1 - 1/36 = 35/36 

    Then if we want to know for 24 for times we use the and operator in probability that is 
    multiplying the probabilities 

    35/36 x 35/36 x 35/36 .... 24 times 

    what leades to (35/36) ^ 24
""" 
probability = (35/36) ** 24
print("Probability of not getting <6,6> : {:.5f} %".format(probability*100))

""" And now, how can one build a simulation for testing if the result is right ? """ 
import random
def testTheory(numTrials = 2000000):
    yes = 0.0
    for i in range(numTrials):
        """ roll dice 24 times for numTrials """
        for j in range(24):
            d1 = random.choice([1,2,3,4,5,6])
            d2 = random.choice([1,2,3,4,5,6])
            if d1 == 6 and d2 == 6:
                yes += 1
                break
    print("Probability of losing : {:.5f} ".format(float(1.0 - yes/numTrials)*100))

testTheory()
