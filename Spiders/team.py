from bs4 import BeautifulSoup
from sql import Sql

Sql = Sql()
db_conn = Sql.conn_db('lolgamequiz')
url = 'https://lpl.qq.com/es/worlds/2020/'
html = """
<div class="swiper-wrapper" id="team_list" style="transform: translate3d(0px, 0px, 0px);"><a href="//lpl.qq.com/es/team_detail.shtml?tid=29" target="_blank" class="swiper-slide swiper-slide-active" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20190523093050/f63d37cbc3810f2f9e8fb5688dd40254/0" alt="">
                                    </div>
                                    <p>LPL赛区：<span>JDG</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=41" target="_blank" class="swiper-slide swiper-slide-next" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20190523093521/b753e24c05cc53123ce5fa3f3a19162f/0" alt="">
                                    </div>
                                    <p>LPL赛区：<span>SN</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=4" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20190523093621/b1721b1e247c18bab54a548775a887a5/0" alt="">
                                    </div>
                                    <p>LPL赛区：<span>LGD</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=117" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20190919151523/2a9931322ed5750213ab6204adadaec1/0" alt="">
                                    </div>
                                    <p>LEC赛区：<span>G2</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=42" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//game.gtimg.cn/images/lpl/act/a20200901worlds/c6-team2.png" alt="">
                                    </div>
                                    <p>LPL赛区：<span>TES</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=17" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200911165810/b11c4520120dac7eff2706d1d02cdfbf/0" alt="">
                                    </div>
                                    <p>LEC赛区：<span>FNC</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=697" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200910152954/768ec5351974e4fa8066319640aacb47/0" alt="">
                                    </div>
                                    <p>LEC赛区：<span>RGE</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=696" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200915170213/6db2e472296273e5f52e4786d3a8ea12/0" alt="">
                                    </div>
                                    <p>LEC赛区：<span>MAD</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=591" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20190627103251/4ebf7bfc74547c63e3950f7f9374ed82/0" alt="">
                                    </div>
                                    <p>LCK赛区：<span>DWG</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=691" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200520170805/785f39559b7bf83a2e5d9e43c73af899/0" alt="">
                                    </div>
                                    <p>LCK赛区：<span>DRX</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=137" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200917075421/4f419363a55504bbd24aa5d286ce289e/0" alt="">
                                    </div>
                                    <p>LCK赛区：<span>GEN</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=25" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200910152249/e055683f081be13ff1d93a9ac0ff9448/0" alt="">
                                    </div>
                                    <p>LCS赛区：<span>TSM</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=695" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200910152014/53e518b0400a196628e062f97e8cc54a/0" alt="">
                                    </div>
                                    <p>LCS赛区：<span>FLY</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=476" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200917080213/cea2153521d7c5d4bad9bb54f861a21d/0" alt="">
                                    </div>
                                    <p>LCS赛区：<span>TL</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=701" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200917074554/50e3eca989c7f2da37aa628e19342717/0" alt="">
                                    </div>
                                    <p>PCS赛区：<span>MCX</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=702" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200914204817/6c5bc6ed779210fb32ccb79dba55beb5/0" alt="">
                                    </div>
                                    <p>PCS赛区：<span>PSG</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=623" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20190919150531/ec6d78c2cd2d78318d2a7f9f2fe49d07/0" alt="">
                                    </div>
                                    <p>LCL赛区：<span>UOL</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=699" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200910162358/237b7c76fe9de75eab93c76ba112287b/0" alt="">
                                    </div>
                                    <p>LLA赛区：<span>R7</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=703" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200917080328/203c7d2119a63285e7279f95169c10e5/0" alt="">
                                    </div>
                                    <p>TCL赛区：<span>SUP</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=136" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200910164309/6eeafadef5d75cd2c6faa786d6c32ce6/0" alt="">
                                    </div>
                                    <p>CBLOL赛区：<span>ITZ</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=698" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200910153240/3bad37b8654827d4eb18ecdf434cc6b9/0" alt="">
                                    </div>
                                    <p>LJL赛区：<span>V3</span></p>
                                    </a><a href="//lpl.qq.com/es/team_detail.shtml?tid=700" target="_blank" class="swiper-slide" onclick="PTTSendClick('btn','btn-team1','队伍');">
                                    <div>
                                        <img src="//img.crawler.qq.com/lolwebvideo/20200910163353/27deba54af0ca94c3d2642affd0cd31b/0" alt="">
                                    </div>
                                    <p>OPL赛区：<span>LGC</span></p>
                                    </a></div>
"""
import re


soup = BeautifulSoup(html, 'html.parser')
a_list = soup.find(id="team_list").find_all('a')
for a in a_list:
    href = a['href']
    tid = href.split('tid=')[-1]
    area = a.find(text=re.compile('赛区')).strip('：')
    name = a.find('span').get_text()
    data = [tid, name, area]
    sql = 'insert into team(tid, name, area) values("{}", "{}", "{}")'.format(tid, name, area)
    Sql.exec_sql(db_conn,sql)
db_conn.close()




