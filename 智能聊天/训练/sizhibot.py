def sizhi(a):
    import json
    import requests

    sess = requests.get('https://api.ownthink.com/bot?spoken={}'.format(a))

    answer = sess.text

    answer = json.loads(answer)

    return answer['data']['info']['text']