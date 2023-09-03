# F5 cookie泄露内部ip问题
当我们使用f5负载均衡设备时，会需要使用会话保持，如果会话保持使用cookie进行绘画保持时，如果配置不注意就会存在内部真实ip地址泄露。判断方法也很简单，只要在cookie中发现有BIGipxxx极有可能使用了F5的负责均衡设备（例子：BIGipServerapp-enterprise-ebank-pool=2588125376.31523.0000）。

## 1. F5 cookie 解码代码
> f5 cookie解码参考地址为：https://my.f5.com/manage/s/article/K6917

 
### f5decode 使用方法
python f5decode.py 335653056.20480.0000

### f5decodegui
> 使用python3 +thinker 编写的GUI解码程序,
打包好的路径再f5decodegui.zip

#### f5decodegui 程序打包方法
pip install pyinstaller
pyinstaller -F -w  f5decodegui.py


## 2. 内部地址泄露解决方法
请参考以下链接配置F5设备
https://packetpushers.net/encrypted-cookie-persistence/
