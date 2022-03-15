import os
import requests
urlsgot = []

def geturls(a):

    global urlsgot

    linkreplace = "https://google.com/search?q=REPLACE&client=firefox-b-1-e"
    stoppingpoint = 'did not match any documents.'
    linkreplace = linkreplace.replace('REPLACE', a)
    if len(urlsgot) > 0:
        linkreplace = linkreplace + '&start=' + str(len(urlsgot))

    req = requests.get(linkreplace)
    if req.status_code != 200:
        print('Error retrieving...\n')


    ##begin parsing for links
    returndat = req.text
    urlfinder = '/url?q='
    if returndat.find(urlfinder) > -1:
        urlparse = returndat.split(urlfinder)
        for x in urlparse:
            if x.split('&amp')[0].find('google.com') <= 0 and x.split('&amp')[0].find('function(') <= 0:
                urlsgot.append(x.split('&amp')[0])


    if returndat.find(stoppingpoint) <= 0:
        ##spit out urls.
        intstat = 0
        for x in urlsgot:
            intstat += 1
            if intstat > len(urlsgot) - 10:
                print(x + '\n')

        geturls(a)

    elif returndat.find(stoppingpoint) > -1:
        strtotal = ''
        for x in urlsgot:
            strtotal = strtotal + x + '\n'
        a = open (os.getcwd() + '/items.txt', 'w')
        a.write(strtotal)
        a.close()
        print('written to: ' + os.getcwd() + '/items.txt')

if __name__ == '__main__':
    print('G0ogol link finder. Enter a search term...\n')
    a = input('')
    geturls(a)
