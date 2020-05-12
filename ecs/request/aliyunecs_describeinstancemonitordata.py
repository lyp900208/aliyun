from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkecs.request.v20140526 import DescribeInstanceMonitorDataRequest
from datetime import datetime, date, timedelta, time
import json
from jsonpath import jsonpath
import set_env
# import sys

# region_id, secret_id, secret_key, product_name, endpoint, api, filename, start_time, last_time = set_env.set_env(sys.argv[1:])

def describeinstancemonitordata(region_id, secret_id, secret_key, product_name, endpoint, filename, start_time, last_time):
    pagesize = 100
    pagenumber = 1

    clt = client.AcsClient(secret_id, secret_key, region_id)

    # start request.
    filename = open("D:\\aliyun\\ecs\\request\\ecsinstanceid")
    instanceid = filename.readlines()
    ino = len(instanceid)
    i = 0
    #print(instanceid)
    for i in range(0,ino):
        newinstanceid = [x.strip() for x in instanceid if x.strip() != '']
        request = DescribeInstanceMonitorDataRequest.DescribeInstanceMonitorDataRequest()
        request.set_accept_format('JSON')
        request.set_InstanceId(newinstanceid[i])
        request.set_StartTime((datetime.today() + timedelta(days = -1)).strftime("%Y-%m-%dT%H:%M:%SZ"))
        request.set_EndTime((datetime.today()).strftime("%Y-%m-%dT%H:%M:%SZ"))
        request.set_Period(3600)
    # selove request.n
        response = clt.do_action_with_exception(request)
        jpath = jsonpath(json.loads(response),"$..InstanceMonitorData.*")
        json_response = json.dumps(jpath,indent=4)
        return json_response

    filename.close()

#if __name__ == "__main__":
#    describeinstancemonitordata(region_id, secret_id, secret_key, product_name, endpoint, filename, start_time, last_time)
#    print(describeinstancemonitordata(region_id, secret_id, secret_key, product_name, endpoint, filename, start_time, last_time))
