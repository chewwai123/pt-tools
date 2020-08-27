from config import SESSION, URL
from function import now
import re


# 完整url
thanksUrl = URL + '/thanks.php'

i = 17700
invalid_time = 0

for id in range(i, i+100):

    with SESSION.post(thanksUrl, data={'id': id}) as res:

        if not res.text:
            tips = '感谢成功'
        else:
            r = re.compile(r'<tr><td class="text">(.+?)</td></tr>')
            tips = r.search(res.text).group(1)

            if tips == 'Invalid torrent id!':
                invalid_time += 1

                if invalid_time > 2:
                    print(now(), '种子连续不存在，任务终止')
                    break

        print(now(), 'id:', id, tips)
