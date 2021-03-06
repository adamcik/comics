from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Apokalips Web Comic'
    language = 'en'
    url = 'http://www.myapokalips.com/'
    start_date = '2009-02-13'
    rights = 'Mike Gioia, CC BY-NC 2.5'

class Crawler(CrawlerBase):
    history_capable_days = 30
    schedule = 'Mo,Th'
    time_zone = -5

    def crawl(self, pub_date):
        feed = self.parse_feed('http://feeds2.feedburner.com/Apokalips')
        for entry in feed.for_date(pub_date):
            url = entry.summary.src('img[src*="/cartoons/"]')
            title = entry.title
            text = entry.summary.alt('img[src*="/cartoons/"]')
            return CrawlerImage(url, title, text)
