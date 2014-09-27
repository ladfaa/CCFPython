import math
import random
class Node():
    def __init__(self, name, news, time, visit):
        self.name = name
        self.news = news
        self.time = time
        self.visit = visit
    
def getNum(follow, leader, log):
    count = 0
    for i in range(len(log[follow])):
        for j in range(len(log[leader])):
            if log[leader][j].news == log[follow][i].news:
                count = count + 1
    return count


def getNum2(follow, leader, log):
    vis1 = []
    vis2 = []
    for i in range(len(log[follow])):
        vis1.append(log[follow][i].news)
    for i in range(len(log[leader])):
        vis2.append(log[leader][i].news)
    count = 0
    for i in range(len(vis2)):
        if vis2[i] not in vis1:
            count = count + 1
    return count


def sim(follow, leader, log):
    t1 = getNum(follow, leader, log)-getNum2(follow, leader, log)
    t2 = len(log[leader])
    t3 = 1-1/math.sqrt(len(log[leader]))
    res = t1/t2*t3
    return res
    
def recommendation(user, news, log, net):
    visited = []
    res = 0
    for i in range(len(log[user])):
        visited.append(log[user][i].news)
    for i in range(len(net[user])):
        for j in range(len(log[net[user][i]])):
            if log[net[user][i]][j].news not in visited:
                res = res + sim(user, log[net[user][i]][j].name, log)
    return res


def replace(user, log, net):
    min = 1000
    minI = -1
    for i in range(len(net[user])):
        tmp = sim(user, net[user][i], log)
        if min > tmp:
            min = tmp
            k = net[user][i]
            minI = i
    max = -1000
    for key in log.keys():
        if key in net[user]:
            continue
        tmp = sim(user, key, log)
        if max < tmp:
            max = tmp
            kk = key
    if min<max:
        net[user][minI] = kk
    
def init(log, net):
    user = {}
    f = open('in', 'r')
    ff = f.read();
    f.close()
    k = 0;
    for line in ff.split('\n'):
        tmp = line.split(',')
        if not log.has_key(tmp[0]):
            log[tmp[0]] = []
            user[k] = tmp[0]
            k = k+1
        log[tmp[0]].append(Node(tmp[0], tmp[1], int(tmp[2]), tmp[3]))
    for key in log.keys():
        net[key] = []
        for i in range(5):
            ran = random.randint(0, 9999)
            net[key].append(user[ran])
    



log = {}
usernet = {}
init(log, usernet)
tmp = []
for key in log.keys():
    tmp.append((sim('52550', key, log), key))
tmp.sort(cmp=None, key=None, reverse=True)
print sim('5218791', '52550', log)
k = 0
for key in log.keys():
    k = k + 1
    print k
    for i in range(5):
        replace(key, log, usernet)
for i in range(5):
    print sim('52550', usernet['52550'][i], log)
t = recommendation('5218791', '100643277', log, usernet)
print t

f = open('res', 'w')
for key in log.keys():
    f.write(key+' ')
    for i in range(len(usernet[key])):
        f.write(usernet[key][i]+' ')
    f.write('\n')
f.close()





















