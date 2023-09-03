# -*- coding: utf-8 -*-
import tkinter

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

#清空文本
def del_text():
    text_a.delete(0, 'end')
    text_a2.delete(1.0, 'end')
    text_a2.insert(1.0, "举例:   解码字符串:335653056.20480.0000")

#调用解码函数
def decrypt_f5():
    # 获取F5需要解密的cookie
    f5_text = text_a.get().strip()

    #解码函数
    try:
        plaintext = f5decode(f5_text)
    except:
        plaintext="解码失败"

    #清空输出文本
    text_a2.delete(1.0, 'end')
    # 将结果写入输出文本
    text_a2.insert(1.0, plaintext)

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("F5 cookie 解码")
    root.geometry("400x220")

    frame1 = tkinter.Frame(root, width=200, height=200)
    frame2 = tkinter.Frame(root, width=200, height=200)

    lable_a = tkinter.Label(frame1, text='解码字符串:').pack(side="left")
    text_a = tkinter.Entry(frame1, width=30)
    text_a.pack(side="left")

    de_button = tkinter.Button(frame1, text="解码", command=decrypt_f5).pack(side="left")
    del_button = tkinter.Button(frame1, text="清空", command=del_text).pack(side="left")

    lable_4 = tkinter.Label(frame2, text="结果输出").pack()
    text_a2 = tkinter.Text(frame2, width=50, height=10)
    text_a2.insert(1.0, "举例:解码字符串:335653056.20480.0000")
    text_a2.pack()

    frame1.pack()
    frame2.pack()

    root.mainloop()
