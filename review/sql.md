## sql

### 查看创建删除数据库
show databases
create database
drop database

```
create table if not exists `student`.`user`(
	`s_id` int unsigned auto_increment,
	`name` varchar(50) not null,
	`sex` varchar(10) not null,
	primary key (`s_id`)
);

```
---

### 增删改查
```
增
insert into user
(name, sex)
values
("songyi", "f");

删
DELETE FROM table_name [WHERE Clause]
‘’
改
UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]

查
SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[LIMIT N][ OFFSET M]

```
---

### like 模糊查询

不用%的like跟==一样

```
select * from user
where
name like "zhang%";

```

---

### union

默认情况下是distinct, union all包含重复元素
```
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION [ALL | DISTINCT]
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];
```

例子
```
SELECT country FROM Websites
UNION
SELECT country FROM apps
ORDER BY country;

```

---

### 排序 order by

asc升序， desc降序

---

### group by 语句
with rollup (在分组统计的基础上在进行统计)

---

### 链接
三种inner join, left join, right join

```
select a.name, a.s_id, b.times
from user a
inner join times b on a.name=b.name;

```

---

### null值处理
（=null 和 !=null是不起作用的）
* IS NULL: 当列的值是 NULL,此运算符返回 true。
* IS NOT NULL: 当列的值不为 NULL, 运算符返回 true。
* <=>: 比较操作符（不同于 = 运算符），当比较的的两个值相等或者都为 NULL 时返回 true

---

### MySQL 事务
4个条件 ACID
原子性：一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

一致性：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。

隔离性：数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

持久性：事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。

---

### alert
查看表有哪些列：show columns from

###### 删除，添加或修改表字段
删： alter table drop 字段；

添加： alter table add ...;
* 如果需要指定字段位置 first/after 字段

###### 修改字段类型及名称
alter table alter_test change i j bigint; 设置非空 not null default xxxx

修改字段默认值 alter table ... alter i set default 100

重新命名表名：alter table xxx rename to xxx;

取消主键：alter table times drop primary key

---

### 索引


### rank, dense_rank, row_number
* rank 包含并列
* dense_rank 不包含并列
* row_number 无并列
