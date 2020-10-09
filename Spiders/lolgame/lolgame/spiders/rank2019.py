import scrapy
from bs4 import BeautifulSoup
from lolgame.items_rank2019 import Rank2019Item


class Rank2019(scrapy.Spider):
    name = "rank2019"

    custom_settings = {
        'ITEM_PIPELINES' : {'lolgame.pipelines_rank2019.Rank2019Pipeline': 300},
    }

    def start_requests(self):
        urls = [
            'https://lol.gamepedia.com/LCS/2019_Season/Championship_Points',
            'https://lol.gamepedia.com/LEC/2019_Season/Championship_Points',
            'https://lol.gamepedia.com/LCK/2019_Season/Championship_Points',
            'https://lol.gamepedia.com/LPL/2019_Season/Championship_Points',
            'https://lol.gamepedia.com/LMS/2019_Season/Championship_Points',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Rank2019Item()
        html = response.text
        url = response.url
        region = url.split('https://lol.gamepedia.com/')[-1].split('/')[0]
        soup = BeautifulSoup(html, 'html.parser')
        trs = soup.find('table', 'wikitable circuitpoints').find('tbody').find_all(lambda x:x.name=='tr' and x.has_attr('class'))
        for tr in trs:
            teamName = tr.find('span', 'team-object').find('a','catlink-teams')['title']
            rank = tr.find('td').get_text()

            item['teamName'] = teamName
            item['rank'] = rank
            item['region'] = region

            yield item
