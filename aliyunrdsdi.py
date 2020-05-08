# coding = utf-8

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkrds.request.v20140815 import DescribeDBInstancesRequest

# global config
region_id = 'jibei-1'
secret_id = 'lKoKfa7e5Tv9Aq55'
secret_key = 'XsfwEH8irwSZWWTNzseiMMnkfZI1E1'

# product config
product_name = 'Rds'
endpoint = 'rds.jibei-1.res.sgmc.sgcc.com.cn'

# create client
#client.region_provider.modify_point(product_name, region_id,endpoint)
clt = client.AcsClient(secret_id,secret_key,region_id)

# setup request
request = DescribeDBInstancesRequest.DescribeDBInstancesRequest()
request.set_accept_format('JSON')
request.set_endpoint(endpoint)

# get response
response = clt.do_action_with_exception(request)