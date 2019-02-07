from math import sqrt
#返回一个有关 personl 与 person2 的基于距离的相似Jt伴价 def sim distance(prefs,personl,person2):
# 得到 shared items 的列在
def sim_distance(prefs,person1,person2):
# 得到 shared items 的列在
    si ={ }
    for item in prefs[person1] :
        if item in prefs [person2]: si[item]=1
# 如果两者没有共同之处 . 则返回 O if len(si)==O: return 0
#计算所有差值的平方和
        Sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
        return 1/(1+sqrt(Sum_of_squares))