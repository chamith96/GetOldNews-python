import requests
import json

query = 'query'
page_size = '200'
apiKey = 'api_key'
from_date = '2020-01-1'
to_date = '2020-01-31'

url = "https://content.guardianapis.com/search?q=" + query + "&show-blocks=all&from-date=" + from_date + "&api-key=" + apiKey + "&page-size=" + page_size + "&to-date=" + to_date

r = requests.get(url)

data = {}
data['news'] = {}

if int(page_size) <= 200 & r.json()['response']['total'] <= 200:
    print("Total collected data: " + str(r.json()['response']['total']))
    f = open(query + "." + from_date + "to" + to_date + ".json", "w")
    f.write('[')
    i = 0

    while i < r.json()['response']['total']:

        data['news'].update({
            'date': r.json()['response']['results'][i]['webPublicationDate'],
            'body': r.json()['response']['results'][i]['blocks']['body'][0]['bodyHtml']
        })

        jsonVal = json.dumps(data['news'])
        print(jsonVal)

        if r.json()['response']['total'] - 1 == i:
            f.write(jsonVal)
            break
        else:
            f.write(jsonVal + ',')
            i += 1

    f.write(']')
    f.close()

else:
    print("page count and total count cannot more than 200")
