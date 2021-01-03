#АПИ не работал, проверял через repl.it
import requests

HEROES_NAMES = ['Hulk', 'Captain America', 'Thanos']
TOKEN = 'https://superheroapi.com/api/2619421814940190/'

if __name__ == '__main__':
    intelligence = 0
    intel_hero_name = ''

    fname = 'search/name'

    for hname in HEROES_NAMES:
        geturl = TOKEN + fname.replace('name', hname)
        print(geturl)
        response = requests.get(geturl)

        print(response.status_code)
        data = response.json()
        intel = int(data['results'][0]['powerstats']['intelligence'])

        if intel > intelligence:
            intelligence = intel
            intel_hero_name = hname

    print(f'Самый умный супергерой {intel_hero_name} с интеллектом {intelligence}')