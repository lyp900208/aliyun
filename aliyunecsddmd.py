# coding = utf-8

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkecs.request.v20140526 import DescribeDiskMonitorDataRequest
from datetime import datetime, date, timedelta, time
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
clt = client.AcsClient(secret_id, secret_key, region_id)

# start request.
request = DescribeDiskMonitorDataRequest.DescribeDiskMonitorDataRequest()
request.set_accept_format('JSON')
request.set_DiskId("d-8vb6uxf0ykfzisw0eym6")
request.set_StartTime((datetime.today() + timedelta(days = -1)).strftime("%Y-%m-%dT%H:%M:%SZ"))
request.set_EndTime((datetime.today()).strftime("%Y-%m-%dT%H:%M:%SZ"))
request.set_Period(3600)
# selove request.n
response = clt.do_action_with_exception(request).decode().strip('b')
#jresponse = jsonpath(json.loads(response),"$..[InstanceId,TimeStamp,IOPSRead,IntranetBandwidth,IOPSWrite,IntranetTX,CPU,BPSRead,IntranetRX,InternetBandwidth,InternetTX,InternetRX,BPSWrite]")
#n = 13
#for i in range(0,len(jresponse),n):
#    nresponse = jresponse[i:i+n]
#    print(jresponse)
#    print(nresponse)
print(response)
