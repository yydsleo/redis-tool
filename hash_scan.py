#!/bin/python

import redis

if __name__ == "__main__":

    key = "__fine_state_key_5e19050ac2__TemplateCacheManager"
    # r = redis.Redis(host='localhost', port=6379, db=0, password='empty')
    r = redis.Redis(host='localhost', port=6379, db=0)

    allkey = r.hkeys(key)
    allsize = 0
    for k in allkey:
        print(k)
        hashkeylen = r.hstrlen(key, k)
        allsize = allsize + hashkeylen
        print("key: %d, valuelen: %d", k, hashkeylen)

    print("allsize: %d" % (allsize))