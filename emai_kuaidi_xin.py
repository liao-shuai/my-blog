#  _*_  coding:utf-8  _*_

# import time
#
# words = raw_input('Please input the words you want to say!:')
# for item in words.split():
#     print('\n'.join([''.join([(item[(x-y) % len(item)]
#     if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')
#     for x in range(-30, 30)])
#     for y in range(30, -30, -1)]))
#     time.sleep(1.5)


# import sys
# import json,requests
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
# print sys.getdefaultencoding()
# def searchPackage():
#     #输入运单号码，注意，只有正在途中的快递才可以查到！
#     packageNum = raw_input('请输入运单号码：')
#     url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum
#     #用url1查询运单号对应的快递公司，如中通，返回：zhongtong。
#     companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
#     # 在用url2查询和运单号、快递公司来查询快递详情，结果是一个json文件，用dict保存在resultdict中。
#     url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum
#     #还有个temp字段加不加都可以。如：'&temp=0.9829438147420106'
#     print('时间↓                             地点和跟踪进度↓\n')
#     for item in json.loads(requests.get(url2).text)['data']:
#         print(item['time'],item['context'].decode('unicode-escape'))
# searchPackage()


#  授权码为  ezhtexsopcqycbab

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.encoders import encode_base64

sender = '525659323@qq.com'
password = 'ezhtexsopcqycbab'
mail_host = 'smtp.qq.com'
receivers = ['2040307504@qq.com']

msg = MIMEMultipart()
msg['Subject'] = raw_input(u'请输入邮件主题: ')
msg['From'] = sender
msg_content = raw_input(u'请输入邮件内容: ')
text = MIMEText(msg_content, 'plain', 'utf-8')
#   添加正文
msg.attach(text)
with open('D:/360Downloads/1.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='pig.png')
    mime.add_header('Content-Disposition', 'attachment', filename='pig.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-attachment-Id', '0')
    mime.set_payload(f.read())
    encode_base64(mime)
    msg.as_string(mime)

try:
    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.set_debuglevel(1)
    s.login(sender, password)
    for i in range(len(receivers)):
        to = receivers[i]
        msg['To'] = to
        s.sendmail(sender, to, msg.as_string())
        print 'END'

    s.quit()
    print 'all email have been send over!'

except smtplib.SMTPException as e:
    print 'failed: %s' % e

#  https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb4931821
#  03fac9270762a000/001408244819215430d726128bf4fa78afe2890bec57736000

