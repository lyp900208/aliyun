from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkecs.request.v20140526 import DescribeDisksFullStatusRequest
import json
from jsonpath import jsonpath
import set_env

#region_id, secret_id, secret_key, product_name, endpoint, api, filename, start_time, last_time = set_env.set_env(sys.argv[1:])

def describedisksfullstatus(region_id,secret_id,secret_key,product_name):
    pagesize = 10
    pagenumber = 1
    clt = client.AcsClient(secret_id, secret_key, region_id)
    request = DescribeDisksFullStatusRequest.DescribeDisksFullStatusRequest()
    request.set_accept_format('JSON')
    request.set_PageSize(pagesize)
    request.set_PageNumber(pagenumber)
    response = clt.do_action_with_exception(request).decode().strip('b')
    jpath = jsonpath(json.loads(response),"$..DiskFullStatusType")
    json_response = json.dumps(jpath,indent=4)
    return json_response

#if __name__ == "__main__":
#    describedisksfullstatus(region_id,secret_id,secret_key,product_name)
#    print(describedisksfullstatus(region_id,secret_id,secret_key,product_name))