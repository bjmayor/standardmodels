#coding=UTF-8
import crypt
import random, string
def getsalt(chars = string.letters + string.digits):
    # generate a random 2-character 'salt'
    # 生成随机的 2 字符 'salt'
    return random.choice(chars) + random.choice(chars)
print crypt.crypt("bananas", getsalt())