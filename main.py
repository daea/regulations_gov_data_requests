import requests

# def api key here (locally)
key = 'DIgcyfb87KQN1S6R72385xkxjNWAPAxWpIZcfoTz'

#endpoint address here
endpoint_part1 = 'https://api.data.gov:443/regulations/v3/document.json?api_key='
endpoint_part2 = '&documentId='

#build docketCommentList

#dummylist for testing
docketCommentList = ['APHIS-2018-0034-3984',
    'APHIS-2018-0034-3983',
    'APHIS-2018-0034-1197',
    'APHIS-2018-0034-5475',
    'APHIS-2018-0034-5376',
    'APHIS-2018-0034-1195']

for comment in docketCommentList:
    endpoint = endpoint_part1 + key + endpoint_part2 + comment
    #print(endpoint)
    r = requests.get(url = endpoint)
    #print(r)
    data = r.json()
    #print(data)
