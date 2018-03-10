# scrapy-zhihu-user  
毕业设计练习项目，使用scrapy，scrapyd，scrapy_redis，gerapy等实现分布式爬取知乎用户信息。  
master为普通爬虫，未添加任何防反爬，主要修改在distributed分支  
整体框架为scrapy，防反爬措施为动态修改useragent(使用fake_useragent),使用IPProxyPool辅助爬取的免费代理，借助random动态更换IP(可使用率极低，推荐收费代理，待完善。)。  
在阿里云Ubuntu14.04测试通过。
