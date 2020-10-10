import scrapy
from bs4 import BeautifulSoup
from lolgame.items_world2020 import LolgameItem


class World2020(scrapy.Spider):
    name = "world2020"

    custom_settings = {
        'ITEM_PIPELINES' : {'lolgame.pipelines_world2020.LolgamePipeline': 300},
    }

    def start_requests(self):
        urls = [
            'https://lol.gamepedia.com/2020_Season_World_Championship/Play-In',
            'https://lol.gamepedia.com/2020_Season_World_Championship/Main_Event',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = LolgameItem()
        html = response.text
        processor = response.url.split('/')[-1]
        soup = BeautifulSoup(html, 'html.parser')
        days = soup.find_all('div', 'matchlist-tab-wrapper')
        for day in days:
            matches = day.find('tbody').find_all('tr', 'ml-row')
            dayNum = day.find('tbody').find('tr').find('th').get_text().split(']')[-1]
            for match in matches:
                date = match['data-date']
                teamnames = match.find_all('span', 'teamname')
                teamA = teamnames[0].get_text()
                teamB = teamnames[1].get_text()
                scores = match.find_all('td', 'matchlist-score')
                if scores:
                    scoreA = scores[0].get_text()
                    scoreB = scores[1].get_text()
                else:
                    scoreA = 0
                    scoreB = 0
                    

                fullTeamA = match.find('td', 'matchlist-team1')['data-teamhighlight']
                fullTeamB = match.find('td', 'matchlist-team2')['data-teamhighlight']

                dayOrder = match['data-initial-order']

                
                item['date'] = date
                item['teamA'] = teamA
                item['teamB'] = teamB
                item['scoreA'] = scoreA
                item['scoreB'] = scoreB
                item['fullTeamA'] = fullTeamA
                item['fullTeamB'] = fullTeamB
                item['dayNum'] = dayNum
                item['dayOrder'] = dayOrder
                item['processor'] = processor
                

                yield item

