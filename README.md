## async duckduckgo-api


```
duckduckgo-api

异步

```


```
install python pkg  cmd pip install -r requirements.txt
run server cmd  python check_server.py

```

```
可定时任务来检查服务是否运行, 没有运行将自启

crontab

# * * * * * cd /home/ubuntu/work/duckgo_api;/home/ubuntu/.pyenv/shims/python check_server.py # check_server

```


```

docs

http://localhost:9400/docs
http://localhost:9400/redoc

/chat
/search
/search/answers
/search/images
/search/videos
/search/news


chat 

模型选择,gpt-3.5,claude-3-haiku,llama-3-70b,mixtral-8x7b

http://127.0.0.1:9400/api/v1/ddgo/chat?q=你可以做什么&m=lama-3-70b


"我可以回答问题、提供建议、讲故事、玩游戏，还可以和你聊天。有什么我可以帮助你的吗？"


http://localhost:9400/api/v1/ddgo/search/news?q=麒麟9010&max_results=6



[
        {
            "date": "2024-04-29T01:01:00+00:00",
            "title": "权威机构探秘华为麒麟9010：中国自己的第二代7nm!",
            "body": "快科技4月28日消息，华为Pura 70系列搭载了最新的麒麟9010处理器，和几位前辈一样蒙着神秘的面纱，而权威机构TechInsights经过初步研究，有了惊喜发现。 麒麟9010 CPU配置规格和麒麟9000S是一样的， 依然包括一个超高性能的泰山架构大核心、三个高性能的泰山架构大核心、四个低功耗的A510小核心。",
            "url": "https://finance.sina.com.cn/tech/discovery/2024-04-29/doc-inatkzsr3755971.shtml",
            "image": "https://n.sinaimg.cn/spider20240428/205/w600h405/20240428/7baa-fba86f305d8d91cbac57a447522f65ff.jpg",
            "source": "新浪网"
        },
        {
            "date": "2024-04-29T00:51:06+00:00",
            "title": "麒麟9010处理器揭秘，华为Pura 70性能再升级!",
            "body": "【ITBEAR科技资讯】4月29日消息，近日，华为旗下的新款旗舰手机Pura 70系列正式亮相，其最大的亮点无疑是搭载了全新的麒麟9010处理器。然而，与华为的前几款处理器一样，这款新品也带着一丝神秘。权威技术机构TechInsights在对麒麟9010进行初步研究后，揭露了一些令人振奋的细节。 据TechInsights分析，麒麟9010处理器很可能是由中芯国际采用第二代7nm工艺，即N+2技术",
            "url": "https://www.msn.com/zh-cn/news/other/麒麟9010处理器揭秘-华为pura-70性能再升级/ar-AA1nPqYR",
            "image": "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1nPjTl.img?w=600&h=405&m=4&q=99",
            "source": "ITBEAR科技资讯 on MSN.com"
        },
        {
            "date": "2024-04-29T00:26:00+00:00",
            "title": "华为麒麟9010 vs 苹果A17 Pro vs 高通骁龙8Gen3：顶级手机芯片性能大比拼",
            "body": "随着科技的不断进步，手机芯片作为手机性能的核心驱动力，日益受到消费者和业界的关注。近日，华为Pura70的上市再次点燃了市场对手机芯片的讨论热情。其中，华为自研的麒麟9010芯片，作为华为海思旗下的最新力作，自然成为了焦点。然而，在当前的手机芯片市场中，苹果A17",
            "url": "https://www.kejixun.com/article/651351.html",
            "image": "https://img.kejixun.com/2024/04/2024042809303838.jpg",
            "source": "科技讯"
        },
        {
            "date": "2024-04-28T17:18:31+00:00",
            "title": "极客湾、麒麟9010，测评汇总：IPC性能，巨幅提升!",
            "body": "◇ 注释：以下性能解析数据均来自极客湾频道。 一、基础架构 【麒麟9000S】 ◇ CPU：1×泰山大核（2.62GHz）+3×泰山中核（2.15GHz）+4× A510小核（1.5GHz），8核心12线程； ——L3缓存：4 MB。 ◇ GPU：Maleoon 910•750MHz； 【麒麟9010】 ◇",
            "url": "https://www.msn.com/zh-cn/news/other/极客湾-麒麟9010-测评汇总-ipc性能-巨幅提升/ar-AA1nPcOd",
            "image": "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1nPcN2.img?w=850&h=481&m=4&q=100",
            "source": "小黑盒数码硬件 on MSN.com"
        },
        {
            "date": "2024-04-28T23:33:00+00:00",
            "title": "麒麟9010或为中芯国际制造：采用第二代7nm工艺",
            "body": "权威机构TechInsights经过初步研究认为，华为Pura 70搭载的麒麟9010是中芯国际制造的，所用工艺是第二代7nm，也就是N+2。此前华为Mate 60 Pro中搭载的麒麟9000S，也是同样的制造工艺。",
            "url": "https://new.qq.com/rain/a/20240429A00R2Q00",
            "image": "",
            "source": "腾讯网"
        },
        {
            "date": "2024-04-19T21:04:00+00:00",
            "title": "疑似麒麟9010超大核频率低于麒麟9000S，但跑分成绩更高",
            "body": "不过值得注意的是，从CPU配置来看，其实麒麟9000S同样是2+6+4的架构设计，2颗超大核频率有2.62GHz，大核与小核的频率分别是2.15GHz和1.53GHz，因此其实麒麟9000S的超大核频率比麒麟9010高出不少，只是大核和小核的频率略微低了点，但跑分成绩的提升表明麒麟9010可以被看做是麒麟9000S的优化版本。 那么，麒麟9010这个跑分成绩对比高通是什么样的档次呢，综合来看，其单核成绩稍逊于骁龙888，多核成绩则更接近于骁龙7+ Gen 2，虽说还没有追上高通的旗舰芯片，但自研SoC的进步还是相当明显的，步步为营稳扎稳打，麒麟的未来依然前途光明。",
            "url": "https://new.qq.com/rain/a/20240418A0543500",
            "image": "https://inews.gtimg.com/news_bt/OWZXloCz9fAEMQ7hOGR5hTkIMpKhPu0VCrVbulM8dmt9kAA/1000",
            "source": "腾讯网"
        }
]

```
