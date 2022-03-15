import os
import requests
import re


def main():
    ##putting everything in one function since it's just a script
    searchfor = input('What to search for\n')
    url = "https://google.com/search?q=" + searchfor
    urlsgot = []

    returndat = '/url?q='
    curpos = 0

    stoppingpoint = 'did not match any documents.'
    urlfinder = '/url?q='
    ##add regex items
    regexlist = []
    b = 'f'
    while b != '':
        b = input('add regex items, hit enter with blank when done \nA useful note is you can simply type a word/phrase and then use . as any character\n')
        if len(b) > 1:
            regexlist.append(b)

    while returndat.find(urlfinder) > -1:
        if curpos == 0:
            req = requests.get(url)
            if req.status_code == 200:
                returndat = req.text
        if curpos > 0:
            req = requests.get(url + '&start=' + str(curpos + 1))
            if req.status_code == 200:
                returndat = req.text

        urlparse = returndat.split(urlfinder)
        for x in urlparse:
            if x.split('&amp')[0].find('google.com') <= 0 and x.split('&amp')[0].find('function(') <= 0:
                urlsgot.append(x.split('&amp')[0])
                curpos = len(urlsgot) + 1
                ##request each page
                try:
                    req2 = requests.get(urlsgot[len(urlsgot) - 1])
                    if req2.ok:
                        ##print out regexs.
                        for regexitems in regexlist:
                            found = re.findall(regexitems, req.text)
                            for printItems in found:
                                print(printItems + '\n')
                                print(urlsgot[len(urlsgot) - 1] + '\n')
                                
                except Exception as e:
                    print(e)

    if returndat == '':
        print('Error getting data\n')
        quit()
if __name__ == '__main__':
    main()
