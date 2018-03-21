# -*- coding: utf-8 -*-
import json

from scrapy import Spider, Request

from zhihuuser.items import UserItem


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_user = 'excited-vczh'  # 初始从轮子哥开始

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'url_token,name,headline,is_advertiser,is_org,badge,url,gender,educations,locations,description,employments,business,user_type,follower_count,following_count,question_count,commercial_question_count,answer_count,articles_count,included_answers_count,included_articles_count,thanked_count,voteup_count,hosted_live_count,participated_live_count,pins_count,columns_count,following_columns_count,following_favlists_count,following_question_count,following_topic_count,favorited_count,favorite_count,logs_count[?(type=best_answerer)].topics'  # 使用知乎的接口，可以随意增减，参考Item中的各项

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].url_token[?(type=best_answerer)].topics'  # 此处因为只用到url_token，所以只请求这一个信息

    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].url_token[?(type=best_answerer)].topics'

    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20),
                      callback=self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20),
                      callback=self.parse_follows)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()

        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield Request(
            self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0),
            self.parse_follows)
        yield Request(
            self.followers_url.format(user=result.get('url_token'), include=self.followers_query, limit=20, offset=0),
            self.parse_followers)

    def parse_follows(self, response):
        results = json.loads(response.text)

        if "data" in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_follows)

    def parse_followers(self, response):
        results = json.loads(response.text)

        if "data" in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_followers)
