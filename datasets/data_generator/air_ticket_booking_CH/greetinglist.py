# -*- coding: utf8 -*-
__author__ = 'shin'
import jieba

greetinglist_server = []
greetinglist_server.append('您好，机票预订中心，需要我为您做些什么？')
greetinglist_server.append('您好，这里是机票预订中心，需要什么服务？')
greetinglist_server.append('您好，我是机票预订服务代理，需要什么服务？')
greetinglist_server.append('您好，这里是机票预订服务代理中心。')
greetinglist_server.append('您好，这里是机票预订服务代理中心，需要我为您做些什么？')
greetinglist_server.append('您好，这里是机票预订服务中心，需要什么帮助？')

greetinglist_server.append('上午好，机票预订中心，需要我为您做些什么？')
greetinglist_server.append('上午好，这里是机票预订中心，需要什么服务？')
greetinglist_server.append('上午好，我是机票预订服务代理，需要什么服务？')
greetinglist_server.append('上午好，这里是机票预订服务代理中心。')
greetinglist_server.append('上午好，这里是机票预订服务代理中心，需要我为您做些什么？')
greetinglist_server.append('上午好，这里是机票预订服务中心，需要什么帮助？')

greetinglist_server.append('下午好，机票预订中心，需要我为您做些什么？')
greetinglist_server.append('下午好，这里是机票预订中心，需要什么服务？')
greetinglist_server.append('下午好，我是机票预订服务代理，需要什么服务？')
greetinglist_server.append('下午好，这里是机票预订服务代理中心。')
greetinglist_server.append('下午好，这里是机票预订服务代理中心，需要我为您做些什么？')
greetinglist_server.append('下午好，这里是机票预订服务中心，需要什么帮助？')

greetinglist_client = []
greetinglist_client.append('我想预订机票')
greetinglist_client.append('我要预订一张机票。')
greetinglist_client.append('请帮我预订一张机票')
greetinglist_client.append('请您帮我预订一下机票。')
greetinglist_client.append('我需要预订机票。')
greetinglist_client.append('您好，我需要预订机票')
greetinglist_client.append('您好，我想预订机票')
greetinglist_client.append('您好，我要预订一张机票。')
greetinglist_client.append('您好，请帮我预订一张机票')
greetinglist_client.append('您好，请您帮我预订一下机票。')
greetinglist_client.append('您好，我需要预订机票。')

greetinglist_server_split = []
for ans in greetinglist_server:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    greetinglist_server_split.append(w_sent)

greetinglist_client_split = []
for ans in greetinglist_client:
    w_sent = ''
    sent = jieba._lcut(ans)
    for word in sent:
        w_sent += ' '
        w_sent += word
    w_sent += '\n'
    greetinglist_client_split.append(w_sent)
pass
