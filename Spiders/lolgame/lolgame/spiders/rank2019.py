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
            'https://lol.gamepedia.com/NA_LCS/2018_Season/Championship_Points',
            'https://lol.gamepedia.com/EU_LCS/2018_Season/Championship_Points',
            'https://lol.gamepedia.com/LCK/2018_Season/Championship_Points',
            'https://lol.gamepedia.com/LPL/2018_Season/Championship_Points',
            'https://lol.gamepedia.com/LMS/2018_Season/Championship_Points',
            
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
        print(trs[0])
        for tr in trs:
            teamName = tr.find('span', 'team-object').find('a','catlink-teams').get_text()
            rank = tr.find('td').get_text()

            item['teamName'] = teamName
            item['rank'] = rank
            item['region'] = region

            yield item
