import pymysql
import time
db = pymysql.connect("127.0.0.1", "root", "root", "testdb",
                     cursorclass=pymysql.cursors.DictCursor)

#表结构


# CREATE TABLE `userinfo` (
#   `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
#   `name` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL COMMENT '姓名',
#   PRIMARY KEY (`id`)
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='用户信息表';


# CREATE TABLE `usermoney` (
#   `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户id',
#   `money` decimal(10,2) DEFAULT NULL COMMENT '用户资产',
#   PRIMARY KEY (`id`)
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='用户资产表';

# CREATE TABLE `userlog` (
#   `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
#   `out_id` int(11) DEFAULT NULL COMMENT '转出id',
#   `in_id` int(11) DEFAULT NULL COMMENT '转入id',
#   `update_time` int(11) DEFAULT NULL COMMENT '操作时间',
#   `money` decimal(10,2) DEFAULT NULL COMMENT '操作金额',
#   PRIMARY KEY (`id`)
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='操作记录表';


with db.cursor() as cursor:
    sql = 'SELECT money FROM usermoney where id=1'
    cursor.execute(sql)
    res = cursor.fetchone()
if(res['money']>=10.00):
    #插入记录表
    with db.cursor() as cursor:
        #获取当前时间戳
        now = int(time.time())
        sql = 'INSERT INTO userlog (out_id,in_id,money,update_time) VALUES (%s,%s,%s,%s)'
        value = (1,2,10.00,now)
        cursor.execute(sql,value)
     #更新资产
        with db.cursor() as cursor:
            sql = 'UPDATE  usermoney SET money=money-10.00 where id=1'
            cursor.execute(sql)
        with db.cursor() as cursor:
            sql = 'UPDATE  usermoney SET money=money+10.00 where id=2'
            cursor.execute(sql)
    print('转账成功')

else:
    print('金额不足')
db.commit()

db.close()