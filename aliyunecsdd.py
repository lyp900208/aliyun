# coding = utf-8

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkecs.request.v20140526 import DescribeDisksFullStatusRequest
import json
from jsonpath import jsonpath

# globle setting.
region_id = 'cn-zhangjiakou'
secret_id = 'LTAI4FvMXJPscDq5w5JaYX3m'
secret_key = 'TaiqXvNj6lXJjUooRdbRypizuVbNjv'

# production setting.
product_name = 'ecs'
endpoint = 'ecs.console.aliyun.com'
pagesize = 100
pagenumber = 1

# create conn.
#client.region_provider.modify_point(product_name, region_id, endpoint)
clt = client.AcsClient(secret_id, secret_key, region_id)

# start request.
#while pagenumber <= 1000:
request = DescribeDisksFullStatusRequest.DescribeDisksFullStatusRequest()
request.set_accept_format('JSON')
request.set_PageSize(pagesize)
#    request.get_PageNumber()
request.set_PageNumber(pagenumber)
#request.set_endpoint(endpoint)

# selove request.n
response = clt.do_action_with_exception(request).decode().strip('b')
jresponse = json.loads(response)

jpath = jsonpath(json.loads(response),"$..DiskFullStatusType")
json_response = json.dumps(jpath,indent=4)
#    if jresponse != False:
#        n = 4
#        for i in range(0,len(jresponse),n):
#            nresponse = jresponse[i:i+n]
#            print(jresponse)
#            print(nresponse)
print(json_response)
print(jpath)
#            pagenumber += 1
#    else:
#        break
#    jresponse[0].split(',')
#    print(response)