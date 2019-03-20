'''
Created on Mar 15, 2019

@author: H304464
'''

import requests

def tdpbot_sendtext(bot_message):
    
    #"https://api.telegram.org/bot%TOKEN%/sendMessage?chat_id=%CHAT_ID%&text=%TEXT%"
    
    ### Send text message
    bot_token = '801962032:AAFMesoRDSux3Q6sF5OjjRVr77NheWlCDLE'
    bot_chatID = '-341511753'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)

#bot_sendtext("Test1 PASSSED/FAILED.....")



