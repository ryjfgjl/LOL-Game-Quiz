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
            'https://lol.gamepedia.com/2019_Season_World_Championship/Play-In',
            'https://lol.gamepedia.com/2019_Season_World_Championship/Main_Event',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Rank2019Item()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        pools = soup.find_all('div', 'pool-participants')
        for pool in pools:
            contents = pool.find_all('div', 'inline-content')
            for content in contents:
                region_rank = content.find('a').get_text()
                region = content.find('div', 'region-icon').get_text()
                if '#' in region_rank:
                    rank = region_rank.split('#')[-1]
                else:
                    rank = '1'

                team_info = content.find('tbody').find('a')
                teamName = team_info['title']
                link = team_info['href']

                item['teamName'] = teamName
                item['rank'] = rank
                item['region'] = region
                item['link'] = link

                yield item
