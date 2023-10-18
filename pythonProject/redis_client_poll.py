import redis

#创建连接池并连接到redis，并设置最大连接数量;
conn_pool = redis.ConnectionPool(host='127.0.0.1',port=6379,max_connections=10)
# 第一个客户端访问
re_pool = redis.Redis(connection_pool=conn_pool)
# 第二个客户端访问
re_pool2 = redis.Redis(connection_pool=conn_pool)