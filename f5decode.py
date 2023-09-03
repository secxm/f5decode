# -*- coding: utf-8 -*-
import sys

#python3

#f5解码方法
def f5decode(f5_text):
    (host, port, end) = f5_text.split('.')

    # 解码f5 cookie 主机ip
    host=hex(int(host))
    host=str(host)[2:]

    #不足8位，在前面加0
    for i in range(0,8-len(host)):
        host="0"+host

    #将16进制倒序
    host_l1=list()
    for i1 in range(0,4):
        temp=host[2*i1:2*i1+2]
        #将16进制转为10进制
        host_l1.insert(0,int(temp,base=16))

    #获得解码的ip地址
    f5_host_ip="{0}.{1}.{2}.{3}".format(host_l1[0],host_l1[1],host_l1[2],host_l1[3])

    #解码f5 cookie端口
    port=hex(int(port))
    port=str(port)[2:]

    #不足4位，在前面加0
    if len(port)%2!=0:
        port="0"+port

    # 将16进制倒序
    port_l1=list()
    for i2 in range(0,int(len(port)/2)):
        temp1=port[2*i2:2*i2+2]
        port_l1.insert(0,temp1)

    #获得解码的端口号
    f5_port=int("".join(port_l1),base=16)
    f5_cookie="{0}:{1}".format(f5_host_ip,f5_port)

    return "{0}-->{1}".format(f5_text,f5_cookie)


if __name__ == '__main__':
    try:
        f5_text=sys.argv[1]
        print(f5decode(f5_text))
    except:
        print("使用举例:")
        print("python f5decode.py 335653056.20480.0000")
