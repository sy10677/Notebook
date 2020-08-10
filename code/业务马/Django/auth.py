from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

err_message = {
    'err_exists': '用户名不存在',
    'wrong_password': '密码错误',
    'is_not_superuser': '无权登陆'
}


# 验证用户存在并验证用户合法
def exists_check_user(username, password, check_admin):
    ret = {'err': '', 'status': True, 'user': None, 'admin': 0}
    exists = User.objects.filter(username = username).exists()

    if not exists:
        ret['status'] = False
        ret['err'] = err_message['err_exists']
    else:
        user = authenticate(username=username, password=password)
        if not user:
            ret['status'] = False
            ret['err'] = err_message['wrong_password']
        elif check_admin:
            if user.is_superuser:
                ret['admin'] = 1
            else:
                ret['err'] = err_message['is_not_superuser']
                ret['status'] = False
        ret['user'] = user
    return ret
