import redis

redis_conn = redis.Redis(
    host='192.168.51.110',
    port=6379,
    password='mohican123.',
    db=0,
    decode_responses=True
)


redis_conn.set('Key','000000')
redis_conn.set('Key1','11111')
redis_conn.set('Key2','22222')
redis_conn.set('Key3','33333')

# -------------------------------------------------------通用操作-----------------------------------------------------
key_list = redis_conn.keys('*')
print(key_list)

# 转换列表为字符串
for key in key_list:
    print(key)

# 查看Key类型
print("Key的类型为:",redis_conn.type("Key"))
# 查看返回值
print("Key3是否存在",redis_conn.exists("Key3"))
print("Key4是否存在",redis_conn.exists("Key4"))
# 删除Key
redis_conn.delete('Key3')
print("Key3是否存在",redis_conn.exists("Key3"))
test = redis_conn.get('Key')
print(test)


# -------------------------------------------------------字符串操作-----------------------------------------------------


