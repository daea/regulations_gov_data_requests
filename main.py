import requests, json

# def api key here (locally)
key = 'DIgcyfb87KQN1S6R72385xkxjNWAPAxWpIZcfoTz'

#endpoint address here
endpoint = 'https://api.data.gov:443/regulations/v3/document.json?api_key=DIgcyfb87KQN1S6R72385xkxjNWAPAxWpIZcfoTz&documentId=APHIS-2018-0034-'

#build docketCommentList, short list for now
commentNum = 6191

# documentId format APHIS-2018-####-####
    # numbers are padded on the left
docketCommentList = [str(number).zfill(4) for number in range(1,commentNum+1)]

# 
for comment in docketCommentList:
    url = ''
    url = endpoint + comment
    #r = requests.get(url = endpoint)
    data = r.json()
    parsed = json.loads(data)
    print(data)
