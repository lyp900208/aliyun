import json
import itertools
from operator import itemgetter

raw = r'[{"name": "24-tiankong","value": "填空回答内容1"},{"name": "19-tiankong","value": "填空回答内容2"},{"name": "7-duoxuan","value": "A"},{"name": "7-duoxuan","value": "B"},{"name": "7-duoxuan","value": "C"}]'
jdata = json.loads(raw)
sorted_jdata = sorted(jdata, key=itemgetter('name'))	# 先进行排序
#for key, group in itertools.groupby(sorted_jdata, key=lambda x:x['name']):	# 使用匿名函数将name传给key
#    print(key)
#    print(list(group))
