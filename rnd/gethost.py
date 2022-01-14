import requests
import json
from jprint import jprint
hostlist = 'https://api.audius.co'

def getHost(printcode = False):
    makeRequest = requests.get(hostlist)
    checkForHost = makeRequest.text
    response = json.loads(checkForHost)
    checkStatus = makeRequest.status_code
    usableHosts = response['data']

    if checkStatus == 200:
        # print("The request was a success!")
        # Code here will only run if the request is successful
        url = usableHosts[0]
        # print(f'the url is {url}')
        return url

    elif checkStatus == 200 and print == True:
        print("The request was a success!")
        # Code here will only run if the request is successful
        url = usableHosts[0]
        # print(f'the url is {url}')
        return url

    
    elif checkStatus== 404:
        print("Result not found! trying to find another host")
        
        for count, i in enumerate(usableHosts):
            url = usableHosts[count]
            if checkStatus== 200:
                print("The request was a success!")
                # Code here will only run if the request is successful
                url = usableHosts[count]
                print(url)
                return url
                break


            elif checkStatus.status_code == 404:
                print("Result not found! trying to find another host")
                inputResponse = input("do you want to try again? Y or N")
                if inputResponse == "Y":
                    gethost()
                else:
                    exit()
            else:
                print('better press cntrl z at this point')
            
url = getHost()

