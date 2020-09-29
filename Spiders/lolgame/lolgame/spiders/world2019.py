import scrapy
from bs4 import BeautifulSoup
from lolgame.items import LolgameItem


class World2019(scrapy.Spider):
    name = "world2019"

    custom_settings = {
        'ITEM_PIPELINES' : {'lolgame.pipelines.LolgamePipeline': 300},
    }

    def start_requests(self):
        urls = [
            'https://lol.gamepedia.com/2019_Season_World_Championship/Play-In',
            'https://lol.gamepedia.com/2019_Season_World_Championship/Main_Event',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = LolgameItem()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        days = soup.find_all('div', 'matchlist-tab-wrapper')
        for day in days:
            matches = day.find('tbody').find_all('tr', 'ml-row')
            for match in matches:
                date = match['data-date']
                teamnames = match.find_all('span', 'teamname')
                teamA = teamnames[0].get_text()
                teamB = teamnames[1].get_text()
                scores = match.find_all('td', 'matchlist-score')
                scoreA = scores[0].get_text()
                scoreB = scores[1].get_text()

                fullTeamA = match.find('td', 'matchlist-team1')['data-teamhighlight']
                fullTeamB = match.find('td', 'matchlist-team2')['data-teamhighlight']
                
                item['date'] = date
                item['teamA'] = teamA
                item['teamB'] = teamB
                item['scoreA'] = scoreA
                item['scoreB'] = scoreB
                item['fullTeamA'] = fullTeamA
                item['fullTeamB'] = fullTeamB
                

                yield item

