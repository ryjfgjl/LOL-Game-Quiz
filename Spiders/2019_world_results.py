import requests


url = 'https://lol.gamepedia.com/2019_Season_World_Championship/Play-In'
res = requests.get(url)
html = res.text

with open('test.html', 'w', encoding='utf8') as f:
    f.write(html)

print(html)