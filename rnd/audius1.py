from contextlib import nullcontext
from io import FileIO
import json
from typing import Text
import requests
from statusCodes import statusCodes
from audiusgets import GETS
from sys import argv
import time
import datetime
import os
from pathlib import Path
from jprint import jprint
from gethost import getHost

currentTime = datetime.datetime.now()
currentTimeString = "M" + currentTime.strftime("%m") + currentTime.strftime("%d") + currentTime.strftime("%y") + currentTime.strftime("%H") + currentTime.strftime("%M")


#set query argument as the first argument on the command line
query = str(argv[1])


nameofApp = "EXAMPLEAPP"



# default url for debugging
#  url = "https://discovery-us-01.audius.openplayer.org/v1/"
url = getHost() + '/v1'

currentDirectory = os.getcwd()
print(currentDirectory)

def searchForUsers(url, searchQuery, only_downloadable, nameofApp, parameterArg = {}, firstResultOnly =True, followerThreshold = 0):

    parameters = {
    
    "query": searchQuery,
    "only_downloadable": only_downloadable,
    "app_name" : nameofApp
    }


    get =  GETS['Search Users']
    parameters['query'] = searchQuery
    only_downloadable = bool

    url += get
    response = requests.get(url, params= parameters).text
    response_info = json.loads(response)
    data = response_info['data'][0]
    result = data

    followers = result['follower_count']
    name = result['name']
    satisfied = 0

    if firstResultOnly == True:
        result = data[0]
        return result

#work on cycling through results
    else:
        ticker = 0
        def __ask(datain):
            
            satisfiedControl = 0
            if satisfiedControl == 0:
                    followers = datain['follower_count']
                    name = datain['name']
                    
                    satisfied = input(f"name: {name}\nfollowers: {followers} \n are you satisfied? '1' yes and use this result, '0' move onto the next query")
                    
                    if satisfied == 0:
                        
                        ticker = satisfiedControl + ticker
                        result = datain[ticker+1]
                        satisfied = input(f"name: {name}\nfollowers: {followers} \n are you satisfied? '1' yes and use this result, '0' move onto the next query")
                        __ask(datain)
                    
                    elif satisfied ==1:
                        result = datain[ticker]
                        return satisfied

        __ask(result)
        return result
def whereami(num):
    print("We are currently in : ", os.getcwd(),num)



def accumulateData(grabFrom, grabThis, fileName, queryfoldername):

    dirName = queryfoldername
    if os.path.isdir('Mined_Data') == False:
        os.mkdir('Mined_Data')
        os.chdir('Mined_Data')
        whereami(1)
    else:
        os.chdir('Mined_Data')
        whereami(2)

    if os.path.isdir(dirName) != True:
        os.mkdir(dirName)
        os.chdir(dirName)
        whereami(3)
    else:
        os.chdir(dirName)
        whereami(3)

    aggregatedFileName = fileName + '.txt'

    file = open(aggregatedFileName, 'w') 
    for count, item in enumerate(grabThis):
        datapoint = str(grabFrom[grabThis[count]])
        aggregatedData = str(grabThis[count]) + " : " + str(datapoint)
    
        file.write(aggregatedData + "\n")
    file.close()    

result = searchForUsers(url,query, None, "EXAMPLEAPP", firstResultOnly = False)
# data = result['data']

grab = ['bio', 'handle','id','is_verified','location', 'name', 'playlist_count','repost_count','track_count', 'follower_count','followee_count']
accumulateData(result,grab,fileName = query,queryfoldername  = query)


















#




