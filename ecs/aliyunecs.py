# coding = utf-8
import sys
import set_env
import request.aliyunecs_describeinstances
import request.aliyunecs_describeinstancemonitordata
import request.aliyunecs_describediskfullstatus

region_id, secret_id, secret_key, endpoint, product_name, api, filename, start_time, last_time = set_env.set_env(sys.argv[1:])

if api == "describeinstances" :
    jsoninfo = request.aliyunecs_describeinstances.describeinstances(region_id, secret_id, secret_key, endpoint, product_name)
elif api == "describeinstancemonitordata" :
    jsoninfo = request.aliyunecs_describeinstancemonitordata.describeinstancemonitordata(region_id, secret_id, secret_key, 
                                                                                         product_name, endpoint, filename, start_time, last_time)
elif api == "describediskfullstatus" :
    jsoninfo = request.aliyunecs_describediskfullstatus.describedisksfullstatus(region_id, secret_id, secret_key, product_name)
else:
    print("exit")
    pass
print(jsoninfo)