'''
Created on Mar 17, 2019

@author: H304464
'''


import random
from notif_telegram import tdpbot_sendtext

actual = ["201","500","400","403","","<Response [200]>"]
expected = "<Response [200]>"

for i in range(50):
    
    if actual[random.randrange(0,len(actual))] == expected:
        print(i,"PASS")
        #tdpbot_sendtext(str(i) + " - PASSED")
    else:
        print(i,"FAIL")
        tdpbot_sendtext(str(i) + " - FAILED")







    