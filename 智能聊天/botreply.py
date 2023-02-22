def bot(a):
    import json
    import requests
    url = "https://api.ownthink.com/bot?appid=58359cabc0841824bcf8a088a45a1611&spoken={}".format(a)
    sess = requests.get(url)
    answer = json.loads(sess.text)
    return answer['data']['info']['text']
