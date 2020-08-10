### User

检查用户是否存在
```
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# 用户是否存在
exists = User.objects.filter(username=username).exists()

```

判断用户是否登陆
```
if request.user.is_authenticated:
    return redirect(reverse('dsindex'))
```

用户注销
```
from django.contrib.auth import logout

```
