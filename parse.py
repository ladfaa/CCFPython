#coding:utf-8


def user(ff):
    f2 = open('out', 'w')
    max = -1
    for line in ff.split('\n'):
        tmp = line.split()
        try:
            username = tmp[0]
            if max < int(username):
                max = username
            news = tmp[1]
            time = tmp[2]
            f2.write(username+','+news+','+time+','+tmp[5]+'\n')
        except:
            print tmp
    f2.close()
    print max

def news(ff):
    news = {}
    f2 = open('outNews', 'w')
    for line in ff.split('\n'):
        tmp = line.split()
        try:
            newsId = tmp[1]
            newsTitle = tmp[3]
            newsMain = tmp[4]
            newsTime = tmp[5]
            if not news.has_key(newsId):
                news[newsId] = 1
                f2.write(newsId+','+newsTitle+','+newsMain+','+newsTime+'\n')
            else:
                continue
        except:
            print tmp
    f2.close()

    pass
f = open('train_data.txt')
ff = f.read()
f.close()
user(ff)
#news(ff)

