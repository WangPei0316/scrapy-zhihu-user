# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from random import random
import requests

from fake_useragent import UserAgent
from scrapy import signals


class ZhihuuserSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class RandomUserAgentMiddleware(object):
    def __init__(self,crawler):
        super(RandomUserAgentMiddleware,self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.setting.get('RANDOM_UA_TYPE','random')

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self,request,spider):
        def get_ua():
            return getattr(self.ua,self.ua_type)
        request.headers.setdefault('User-Agent',get_ua())

class ProxyMiddleware(object):
    def __init__(self):
        self.url = "http://0.0.0.1:8000/?types=0&count=10&country=%E5%9B%BD%E5%86%85"
        self.proxy = eval(requests.get(self.url).content)
        self.counts = 0
        def process_request(self,request,spider):
        #这里作一个计数器,在访问次数超过1000次之后就切换一批(10个)高匿代理,使得代理一直保持最新的状态
            if self.counts < 500:
                pre_proxy = random.choice(self.proxy)
                request.meta['proxy'] = 'http://{}'.format(str(pre_proxy[0])+":"+str(pre_proxy[1]))
                self.counts += 1
            else:
                #进入到这里的这一次就不设定代理了,直接使用本机ip访问
                self.counts = 0
                self.proxy = eval(requests.get(self.url).content)