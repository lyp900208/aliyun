# coding = utf-8
import sys
import set_env
import aliyunecs_describeinstances

region_id, secret_id, secret_key, endpoint, product_name, api = set_env.set_env(sys.argv[1:])

if api == "describeinstances" :
    jsoninfo = aliyunecs_describeinstances.describeinstances(region_id, secret_id, secret_key, endpoint, product_name)
    print(jsoninfo)
    
else:
    print("exit")