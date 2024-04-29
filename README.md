## async duckduckgo-api


```
duckduckgo-api

```


```
install python pkg  cmd pip install -r requirements.txt
run server cmd  python check_server.py

```

```
crontab


# * * * * * cd /home/ubuntu/work/duckgo_api;/home/ubuntu/.pyenv/shims/python check_server.py # check_server

```


```

docs

http://localhost:9400/docs
http://localhost:9400/redoc


!!! 注意请求时  headers 里添加 cid  用来校验用户 可在配置文件里添加


http://localhost:9400/api/v1/ddgo/search?keywords=啊对对对是什么梗&max_results=6


{
    "code": 1,
    "data": [
        {
            "title": "啊对对对网络梗词含义及解释-台词课",
            "href": "https://www.taicike.com/baike/17770.html",
            "body": "你说啊对对对，开摆就完了呗，对不对？在单位里头人家问：哎怎么不干活？你说啊对对对，桥洞里你盖小被儿，你说啊对对对，对就完了呗。\"于是，\"啊对对对\"就成为了一种敷衍的回答方式，是王喜顺用来调侃自己或者别人的摆烂的手段。"
        },
        {
            "title": "啊对对对什么意思网络用语 啊对对对是谁说的→Maigoo知识",
            "href": "https://m.maigoo.com/goomai/5zAMMzk2.html",
            "body": "啊对对对什么意思网络用语. 1、\"啊对对对\"这个梗是敷衍和摆烂的意思，也是一种承认自己破罐子破摔的无赖态度。 2、\"啊对对对\"这个梗在短视频上爆火后，常用于摆烂后的一种调侃，碰到一些不想进行争辩的事情时，就可以发\"啊对对对，你说得对\"来 ..."
        },
        {
            "title": "\"啊对对对\"是什么梗，出自哪里？ - 知行乐集",
            "href": "https://www.zhixinglj.cn/article/details/20230914210830166231",
            "body": "这个梗实际上是一种漫不经心和无所谓的态度表达，当遇到无理取闹或摆烂的人时，可以使用这句话。它通常用于对付那些喜欢争辩和挖苦别人的人，表达自己不愿合作和不屑于与对方争论的情绪。 ... \"啊对对对\"是什么梗，出自哪里？ ..."
        },
        {
            "title": "对对对什么梗 - 百度知道",
            "href": "https://zhidao.baidu.com/question/2086048323494944748.html",
            "body": "关注. \"对对对\"这个梗就是敷衍和摆烂的意思，也是一种承认自己破罐子破摔的无赖态度。. \"对对对\"这个梗的正确写法是\"啊对对对\"，这个梗出自一个游戏主播csgo久菜合子的经典梗，在他的某一局游戏中，遇到了几个比较坑的队友，在一番\"礼貌交谈 ..."
        },
        {
            "title": "\"啊对对对\"中的叹词\"啊\"起到了什么作用？它的功能可以用\"嗯\"\"哦\"代替吗？ - 知乎",
            "href": "https://www.zhihu.com/question/626811698?write",
            "body": "以前有类似问题，其中\"啊\"的表现如\"今天我遇到小王了，你猜他说什么了？啊我们平时吃饭不叫他了，我们最近对他关心又不够了\"。\"啊\"之后的命题内容虽然是对\"小王\"说的话的引用，但整体上还是表达了说话人对这些命题的消极评价。"
        },
        {
            "title": "对对对是什么梗-抖音",
            "href": "https://www.douyin.com/shipin/7266241040603203645",
            "body": "十万个梗百科：啊对对对。他都这样了，你为什么不顺从他呢。#王喜顺 #敷衍 十万个割麦克之啊对对对是一种十分敷衍且百烂的回复方式，出自 cs go 韭菜盒子，也就是王喜顺。在某局游戏中，他遇到了三个十分离谱的队友。经过一番友好交流后，王喜顺"
        }
    ]
}


```
