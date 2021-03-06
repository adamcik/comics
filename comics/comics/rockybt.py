from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.comics.rocky import Meta as RockyMeta

class Meta(RockyMeta):
    name = 'Rocky (bt.no)'
    url = 'http://www.bt.no/tegneserier/rocky/'

class Crawler(CrawlerBase):
    history_capable_days = 162
    schedule = 'Mo,Tu,We,Th,Fr,Sa'
    time_zone = 1

    def crawl(self, pub_date):
        url = 'http://images.bt.no/gfx/cartoons/rocky/%s.gif' % (
            pub_date.strftime('%d%m%y'),)
        return CrawlerImage(url)
