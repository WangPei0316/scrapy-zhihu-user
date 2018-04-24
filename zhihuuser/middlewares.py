# import base64  # 阿布云(使用时取消注释)

import random  # 其他代理提取(用到随机获取)
import requests  # 其他代理提取(获取文本)

from fake_useragent import UserAgent  # 随机UA

from scrapy import signals


#  自带middleware(可删除)
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


#  自定义UA中间件
class RandomUserAgentMiddleware(object):
    # 使用fake_useragent动态更换UA，详见https://github.com/hellysmile/fake-useragent
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        request.headers.setdefault('User-Agent', get_ua())
        request.headers.setdefault('authorization', 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20')


# #  自定义代理中间件(阿布云)
# class ProxyMiddleware(object):
#     def __init__(self):
#         # 代理服务器
#         self.proxyServer = "http-dyn.abuyun.com:9020"
#         # 代理隧道验证信息
#         self.proxyUser = ""  # User
#         self.proxyPass = ""  # Pass
#         self.proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((self.proxyUser + ":" + self.proxyPass), "ascii")).decode("utf8")
#
#     def process_request(self, request, spider):
#         request.meta["proxy"] = self.proxyServer
#         request.headers["Proxy-Authorization"] = self.proxyAuth

#  自定义代理中间件(此处使用蘑菇代理，可以自己修改和匹配)
class ProxyMiddleware(object):

    def __init__(self):
        self.url = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=91a4450c3b98477bcfead8c060db8d&count=7&expiryDate=5&format=2"
        self.proxy = requests.get(self.url).text.split("\n")[0:-1]
        self.counts = 0

    def process_request(self, request, spider):
        #  这里作一个计数器,在访问次数超过1000次之后就切换一批(10个)高匿代理,使得代理一直保持最新的状态
        if self.counts < 500:
            pre_proxy = random.choice(self.proxy)
            request.meta['proxy'] = 'https://{}'.format(pre_proxy)
            self.counts += 1
        else:
            # 进入到这里的这一次就不设定代理了,直接使用本机ip访问
            self.counts = 0
            self.proxy = requests.get(self.url).text.split("\n")[0:-1]
