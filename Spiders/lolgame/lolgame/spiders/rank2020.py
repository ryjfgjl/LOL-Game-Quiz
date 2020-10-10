import scrapy
from bs4 import BeautifulSoup
from lolgame.items_rank2020 import Rank2020Item


class Rank2020(scrapy.Spider):
    name = "rank2020"

    custom_settings = {
        'ITEM_PIPELINES' : {'lolgame.pipelines_rank2020.Rank2020Pipeline': 300},
    }

    def start_requests(self):
        urls = [
            'https://lol.gamepedia.com/LEC/2020_Season/Championship_Points',
            'https://lol.gamepedia.com/LCK/2020_Season/Championship_Points',
            'https://lol.gamepedia.com/LPL/2020_Season/Championship_Points',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Rank2020Item()
        html = response.text
        url = response.url
        region = url.split('https://lol.gamepedia.com/')[-1].split('/')[0]
        soup = BeautifulSoup(html, 'html.parser')
        trs = soup.find('table', 'wikitable circuitpoints').find('tbody').find_all(lambda x:x.name=='tr' and x.has_attr('class'))
        for tr in trs:
            teamName = tr.find('span', 'team-object').find('a','catlink-teams')['title']
            if url == 'https://lol.gamepedia.com/LEC/2019_Season/Championship_Points':
                rank = tr.find_all('td')[-2].get_text()
            else:
                rank = tr.find('td').get_text()

            item['teamName'] = teamName
            item['rank'] = rank
            item['region'] = region

            yield item
