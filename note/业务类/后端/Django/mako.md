### mako配置

```
# coding: utf-8

from mako.lookup import TemplateLookup
from django.template import RequestContext
from django.conf import settings
from django.template.context import Context
from django.http import HttpResponse
from django.middleware.csrf import get_token

def render_to_response(request, template, data={}):
    context_instance = RequestContext(request)
    path = settings.TEMPLATES[0]['DIRS'][0]
    lookup = TemplateLookup(directories=[path],
                            output_encoding='utf-8',
                            input_encoding='utf-8')
    mako_tmp = lookup.get_template(template)

    if context_instance:
        context_instance.update(data)
    else:
        context_instance = Context(data)

    res = {}
    for items in context_instance:
        res.update(items)

    request.META["CSRF_COOKIE"] = get_token(request)
    res['csrf_token'] = ('<div style="display:none">'
                            '<input type="hidden" '
                            'name="csrfmiddlewaretoken" '
                            'value="{0}"/>'
                            '</div>'.format(request.META["CSRF_COOKIE"]))

    return HttpResponse(mako_tmp.render(**res))

```

---

### mako语法

嵌入函数：
```
${self.func()}
<%def name="func()"></%def>
```

body中嵌入file
```
<%include file="./nav.html"></%include>
```


继承模版html
```
<%inherit file="base.html"></%inherit>
```

嵌入py语句
```
<%! from django.shortcuts import reverse %>

```

插入循环语句
```
% for user in users:
<tr>${user.username}</tr>
% endfor

```
