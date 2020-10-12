# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from lolgame.sql import Sql


class Rank2020Pipeline:
    def process_item(self, item, spider):

        teamName = item['teamName']
        rank = item['rank']
        region = item['region']
        link = item['link']

        self.Sql = Sql()
        db_conn = self.Sql.conn_db('lolgamequiz')
        sql = 'insert into rank2020(teamName, rank, region,link) values ("{}", "{}", "{}", "{}")'.format(teamName, rank, region,link)
        self.Sql.exec_sql(db_conn, sql)

        return item
