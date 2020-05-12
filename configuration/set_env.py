import sys,getopt

def set_env(argv):

    # 初始化参数
    region_id = ''
    secret_id = ''
    secret_key = ''
    endpoint = ''

    # 配置选项
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:i:k:e:",["region_id=","secret_id=","secret_key=","endpoint="])

    # 处理异常
    except getopt.GetoptError:
        print("script.py -r <region_id> -i <secret_id> -k <secret_key> -e <endpoint>")
        sys.exit(2)

    # 传递参数
    for opt, arg in opts:
        if opt == "-h":
            print("this.py -r <region_id> -i <secret_id> -k <secret_key> -e <endpoint>")
            sys.exit(2)
        elif opt in ("-r", "--region_id"):
            region_id = arg
        elif opt in ("-i", "--secret_id"):
            secret_id = arg
        elif opt in ("-k", "--secret_key"):
            secret_key = arg
        elif opt in ("-e", "--endpoint"):
            endpoint = arg
    return (region_id, secret_id, secret_key, endpoint)

if __name__ == "__main__":
    set_env(sys.argv[1:])