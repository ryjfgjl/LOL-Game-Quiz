# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from lolgame.sql import Sql


class LolgamePipeline:
    def process_item(self, item, spider):

        date = item['date']
        teamA = item['teamA']
        teamB = item['teamB']
        scoreA = item['scoreA']
        scoreB = item['scoreB']

        self.Sql = Sql()
        db_conn = self.Sql.conn_db('lolgamequiz')
        sql = 'insert into world2019(date, teamA, teamB, scoreA, scoreB) values ("{}", "{}", "{}", "{}", "{}")'.format(date, teamA, teamB, scoreA, scoreB)
        self.Sql.exec_sql(db_conn, sql)

        return item
