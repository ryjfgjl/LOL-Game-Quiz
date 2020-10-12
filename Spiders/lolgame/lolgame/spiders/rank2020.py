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
            'https://lol.gamepedia.com/2020_Season_World_Championship/Play-In',
            'https://lol.gamepedia.com/2020_Season_World_Championship/Main_Event',
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = Rank2020Item()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        pools = soup.find_all('div', 'pool-participants')
        for pool in pools:
            contents = pool.find_all('div', 'inline-content')
            for content in contents:
                region_rank = content.find('a')
                if region_rank:
                    region_rank = region_rank.get_text()
                    region = region_rank.split('#')[0]
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
