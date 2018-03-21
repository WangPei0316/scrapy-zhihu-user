# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    #  个人感觉有用的信息
    url_token = Field()  # 唯一ID
    name = Field()  # 昵称
    headline = Field()  # 个人主页标签
    is_advertiser = Field()  # 是否是广告用户
    is_org = Field()  # 是否是机构号
    badge = Field()  # 机构信息
    url = Field()  # 网址
    gender = Field()  # 性别
    educations = Field()  # 教育背景
    locations = Field()  # 居住信息
    description = Field()  # 个人描述
    employments = Field()  # 工作信息
    business = Field()  # 公司或者商业信息
    user_type = Field()  # 账户类型
    follower_count = Field()  # 关注ta的人数量
    following_count = Field()  # ta关注的人数量
    question_count = Field()  # 提问数
    commercial_question_count = Field()  # 商业问题数
    answer_count = Field()  # 答案数量
    articles_count = Field()  # 文章数
    included_answers_count = Field()  # 知乎收录答案数量
    included_articles_count = Field()  # 知乎收录文章数
    thanked_count = Field()  # 被感谢数量
    voteup_count = Field()  # 被赞同数量
    hosted_live_count = Field()  # 举办live数量
    participated_live_count = Field()  # 参与live数量
    pins_count = Field()  # 想法数
    columns_count = Field()  # 创建专栏数
    following_columns_count = Field()  # 关注的专栏数
    following_favlists_count = Field()  # 关注的收藏夹数
    following_question_count = Field()  # 关注问题数
    following_topic_count = Field()  # 关注的话题数
    favorited_count = Field()  # 回答被收藏数
    favorite_count = Field()  # 收藏数
    logs_count = Field()  # 参与公共编辑数

    # # 个人觉得无用信息
    # is_active = Field()
    # is_blocked = Field()
    # is_blocking = Field()
    # is_force_renamed = Field()
    # is_privacy_protected = Field()
    # marked_answers_text = Field()
    # message_thread_token = Field()
    # mutual_followees_count = Field()  # 我关注的人有多少关注他
    # cover_url = Field()
    # id = Field()   # id
    # is_bind_sina = Field()
    # show_sina_weibo = Field()
    # type = Field()
    # is_followed = Field()
    # is_following = Field()
    # thank_from_count = Field()
    # thank_to_count = Field()
    # vote_from_count = Field()
    # vote_to_count = Field()
    # account_status = Field()  # 账户状态
    # allow_message= Field()  # 是否允许发送消息
    # avatar_hue = Field()  # 头像色调
    # avatar_url = Field()  # 头像链接
    # avatar_url_template = Field()  # 头像链接模板
