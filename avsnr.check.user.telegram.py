import requests
import random
kn = 0
nk = 0

print('  Tool Check user telegram :\n  programmer ⇨ avsnr \n  Have Fun ')
print('- - - - -')
k = input(' - PLEASE ENTER ID : ')
t = input(' - PLEASE ENTER TOKEN : ')
message = requests.get("https://api.telegram.org/bot"+str(t)+"/sendMessage?chat_id="+str(k)+"&text= ⌔ New Start! ").json()
id_msg = str(message['result']["message_id"])
print('- '*9)
oh = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
op = '0987654321KKKOOOOPPPSBSVVSJSHJSSISSHSSBSSJSS'
while True :
    ok = str("".join(random.choice(oh)for i in range(1)))
    on = str("".join(random.choice(op)for i in range(1)))
    os = ok+ok+'_'+ok+on+ok
    oa = requests.get(f'https://t.me/{os}').text
    if 'tgme_username_link' in oa:
        print(f'\r [{kn}] : done  ')
        kn+=1
        tb = f'https://api.telegram.org/bot{t}/sendMessage?chat_id={k}&text= ⌔ unavailable avsnr user ⇨ 💀👾 < @{os} >'
        i = requests.post(tb)
    else:
        print(f'\r [{nk}] : error  ')
        nk+=1
        requests.post(f"""https://api.telegram.org/bot{t}/editmessagetext?chat_id={k}&message_id={id_msg}&text= ⌔ Checking in progress .
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⌔ user : {os} :
⌔️ available {kn} :
⌔ unavailable {nk} :
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉.""")

