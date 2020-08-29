
#### NoSql
为什么需要NoSQL
* 高并发读写
* 海量数据的高效率存储和访问
* 高可扩展行和高可用性

#### nosql 四大分类
* 键值对存储
* 列存储

#### nosql 特点
* 易扩展
* 灵活数据模型
* 大量数据，高性能
* 高可用

---

#### Redis

#### 数据类型
字符串，列表，有序集合，哈希，集合

* key 不要过长 也不要过短， 统一命名规范
* 字符串：以二进制方式进行操作，最大可存512M
  * 赋值：set
  * 删除：del
  * 取值：get
  * 数据增减：incr， decr，incrby，decrby
  * 扩展命令：getset（先获取在赋值）， append（追加）

* 哈希
  * 赋值：hset， hmset，
  * 取值：hget， hmget， hgetall
  * 删除：del, hdel
  * 增加数字：hincrby
  * 自学命令：hexists（判断某个属性是否存在），hlen（查看几个属性），hkeys（获得所有属性），hvalues（获得所有值）

* list
  * 两端添加：lpush, rpush
  * 查看列表：lrange
  * 两端弹出：lpop，rpop
  * 获取列表元素个数：llen
  * 扩展命令：lpushx（如果存在，插入）
  * 删除：lrem, lset index value, linsert before/after, rpoplpush xx(尾部弹出) xx（头部压入）

* set
  * 添加：sadd
  * 删除：srem
  * 获得：smembers, sismember(是否存在)
  * 集合运算: sdiff a b(差集), sinter(交集), sunion(并集)
  * 其他：scard（数量），srandmember(获得随机成员)， sdiffstore a b c(b和c的差存入a)

* sorted set
  * 添加：zadd x score para
  * 获得：zscore x para, zcard(数量)， 范围查找zrange/zrevrange (withscores(带分数))
  * 删除：zremrangebyrank
  * 查找：zrangebyscore x lb hb limit(显示哪几个)， zscore, zincrby xx num para, zcount xx 区间（区间个数）


#### 应用场景
* 缓存
* 任务队列
* 网站访问统计
* 数据过期处理
* 应用排行榜
* 分布式集群架构中的session分离

#### 相关操作
* 启动： redis-server, 关闭 redis-cli, shutdown
* 查看key对应所有 keys *
* 删除键值：del
* 存在：exists
* 重命名：rename
* 过期时间：expire xxx --s
* ttl查看过期时间
* 查看类型：type

#### 特性
* 多数据库
  * 最多16个
  * 切换 select
  * 移动：mv xxx num  

* 事务
  * multi, exec, discard
    * multi 创建一个事务
    * exec
    * discard

#### 持久化
* RDB：在指定时间间隔内将数据快照写入磁盘
* AOF：日志的形式，存储每一个操作
* 不持久化：缓存
* 同时使用RDB AOF

##### RDB
* 优势：
* 缺点：来不及写就宕机
* 配置

#### AOF
* 优势：数据安全
* 劣势：
* 配置
  * redis-cli config set appendonly yes
  * redis-cli config set save ""
