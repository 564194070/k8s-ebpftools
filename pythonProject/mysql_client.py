import pymysql

# 连接 MySQL 数据库
conn = pymysql.connect(
    host='192.168.51.110',      # 主机名
    port=3306,                  # 端口号，MySQL默认为3306
    user='zwt',                 # 用户名
    password='mohican123.',     # 密码
    database='zettest',         # 数据库名称
)

# 创建游标对象
cursor = conn.cursor()

# 执行 SQL 查询语句
cursor.execute("SELECT * FROM users WHERE gender='female'")

# 获取查询结果
result = cursor.fetchall()