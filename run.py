# uncompyle6 version 3.3.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Apr 25 2019, 21:47:43) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: <Secret>
import sys, os, time
G = '\x1b[092m'
K = '\x1b[093m'
H = '\x1b[091m'
P = '\x1b[0m'
try:
    from tqdm import *
    import fbchat
    from fbchat.models import *
except ImportError:
    print H + 'Memeriksa Module'
    time.sleep(2)
    print K + 'Installing Module\n'
    os.system('pip2 install tqdm')
    os.system('pip2 install fbchat')
    print G + 'Installing Sukses\nSilahkan Jalankan Ulang run.py'
    sys.exit()

print H + '\n=================================================='
print K + 'AUTHOR :' + G + ' AGIL DIMAS FERGIANSYAH'
print K + 'BOOM   :' + G + ' MESSENGER'
print K + 'GITHUB :' + G + ' https://github.com/F3R614N5N0OB'
print H + '=================================================='
print H + '--------------------------------------------------'
user_name = raw_input(H + '{' + G + '+' + H + '} ' + K + 'Username:' + P + ' ')
password = raw_input(H + '{' + G + '+' + H + '} ' + K + 'Password:' + P + ' ')
print 'Sedang Login Ke Facebook'
print H + '--------------------------------------------------', P
client = fbchat.Client(user_name, password)
friend_name = raw_input(H + '{' + G + '+' + H + '} ' + K + 'Nama Fb Target :' + P + ' ')
friends = client.searchForUsers(friend_name)
friend = friends[0]
message = raw_input(H + '{' + G + '+' + H + '} ' + K + 'Pesan To Target:' + P + ' ')
times = raw_input(H + '{' + G + '+' + H + '} ' + K + 'Jumlah Pesan   : ')
print H + '--------------------------------------------------'
for i in tqdm(range(int(times))):
    message_id = client.sendMessage(message, thread_id=friend.uid, thread_type=ThreadType.USER)

print G + ' BOOM CHAT BERHASIL DI KIRIM!'
print G + ' THANKS UDAH PAKAI TOOLS INI '

