# coding = utf-8
import sys
import set_env
import request.aliyunecs_describeinstances,request.aliyunecs_describeinstancemonitordata

region_id, secret_id, secret_key, endpoint, product_name, api, filename, start_time, last_time = set_env.set_env(sys.argv[1:])

if api == "describeinstances" :
    jsoninfo = request.aliyunecs_describeinstances.describeinstances(region_id, secret_id, secret_key, endpoint, product_name)
elif api == "describeinstancemonitordata" :
    jsoninfo = request.aliyunecs_describeinstancemonitordata.describeinstancemonitordata(region_id, secret_id, secret_key, 
                                                                                         product_name, endpoint, filename, start_time, last_time)
else:
    print("exit")
    pass
print(jsoninfo)