# coding = utf-8

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest
from aliyunsdkrds.request.v20140815 import DescribeResourceUsageRequest

# global config
region_id = 'jibei-1'
secret_id = 'lKoKfa7e5Tv9Aq55'
secret_key = 'XsfwEH8irwSZWWTNzseiMMnkfZI1E1'

# product config
product_name = 'Rds'
endpoint = 'rds.jibei-1.res.sgmc.sgcc.com.cn'
dbinstanceid = 'rm-i5x306ar25hjrhgkd'

# create client
#client.region_provider.modify_point(product_name, region_id,endpoint)
clt = client.AcsClient(secret_id,secret_key,region_id)

# setup request
request = DescribeResourceUsageRequest.DescribeResourceUsageRequest()
request.set_accept_format('JSON')
request.set_endpoint(endpoint)
request.set_DBInstanceId(dbinstanceid)

# get response
response = clt.do_action_with_exception(request)
print(response)