### 规约

```
from functools import reduce

reduce(fn, arr)

```

### any all
any 一个true就是true， all全部true才为true

### 字符串转意
如果一个字符串前面有r或者R， 后面的\按字符处理

### __doc__
第一个语句出现的字符串是文档字符串

### 格式化字符串
```
intro = f'i am {age} years old'
'{}'.format
```

### is 和 ==
is比较内存地址，==比较对象值
a = [1, 2, 3]
b = a[:]

### 下划线
前单下划线：私有外部可调用

前双下划线： 私有外部不可调用，但是可以通过类名调用

### partial函数
给定部分值
