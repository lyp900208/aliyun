# coding = utf-8

import sys
import json
from jsonpath import jsonpath
from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
import set_env

# 初始化参数
product_name = 'ecs'
pagesize = 100
pagenumber = 1

# 调取参数信息
region_id, secret_id, secret_key, endpoint = set_env.set_env(sys.argv[1:])

# 配置请求
clt = client.AcsClient(secret_id, secret_key, region_id)
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_accept_format('JSON')
request.set_PageSize(pagesize)
request.set_PageNumber(pagenumber)
#request.set_endpoint(endpoint)

# 处理请求
response = clt.do_action_with_exception(request).decode().strip('b')
jresponse = json.loads(response)
jpath = jsonpath(json.loads(response),"$..Instance.*")
json_response = json.dumps(jpath,indent=4)
print(json_response)