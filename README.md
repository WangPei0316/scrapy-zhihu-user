# scrapy-zhihu-user  
## 介绍
毕业设计练习项目，在Python3环境下，使用scrapy借助scrapyd，scrapy_redis，gerapy等实现分布式爬取知乎用户信息，然后将信息存储在mongodb中。  
在本地Ubuntu16.04和阿里云Ubuntu14.04测试通过。
## 使用的库&&反爬
整体框架为scrapy,官网和使用方法见[scrapy.org](https://scrapy.org/).    
分布式和存储去重使用scrapy_redis[查看使用文档](http://scrapy-redis.readthedocs.io/en/stable/).  
部署使用[scrapyd](https://github.com/scrapy/scrapyd)和[gerapy](https://github.com/Gerapy/Gerapy),scrapyd安装和使用办法查看[scrapyd文档](http://scrapyd.readthedocs.io/en/stable/),gerapy是免去命令行操作远程部署和查看，是崔庆才大大的作品，本项目也是基于他的视频来做的，gerapy介绍和使用方法在这里[跟繁琐的命令行说拜拜！Gerapy分布式爬虫管理框架来袭！](https://cuiqingcai.com/4959.html).  
防反爬措施1:动态修改useragent(使用fake_useragent库),安装和使用看这里[hellysmile/fake-useragent](https://github.com/hellysmile/fake-useragent)  
防反爬措施2:使用IPProxyPool辅助爬取的免费代理，借助random动态更换IP(可使用率极低，推荐收费代理)。安装和使用看这里[qiyeboy/IPProxyPool](https://github.com/qiyeboy/IPProxyPool)  
防反爬措施3:使用收费代理，这里推荐[阿布云](https://www.abuyun.com/)或者[蘑菇代理](http://www.mogumiao.com)  
## 能爬到什么
这个爬虫是从一个大V开始，爬取其关注人和粉丝的信息，再继续爬取关注人和粉丝的关注人和粉丝，理论上可以爬取所有关注和粉丝非0的所有知乎用户。  
这个爬虫主要是通过接口爬取知乎用户几乎所有的信息，包括    唯一ID、昵称、个人主页标签、是否是广告用户、是否是机构号、机构信息、网址、性别、教育背景、居住信息、个人描述、工作信息、公司或者商业信息、 账户类型、 关注ta的人数量、关注的人数量、提问数、商业问题数、答案数量、文章数、知乎收录答案数量、知乎收录文章数、被感谢数量、被赞同数量、举办live数量、参与live数量、 想法数、创建专栏数、关注的专栏数、关注的收藏夹数、 关注问题数、关注的话题数、回答被收藏数、收藏数 等等，因为部分信息无大作用，所以只保存可以分析的数据(详见items.py)。  
## 缺点(待完善)
爬虫整体效率低下  
优化代码  
增加截图说明  
增加自动化操作