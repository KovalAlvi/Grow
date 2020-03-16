import requests
import time
from tqdm import tqdm

#Возмоности прогресс бара. Прикольно получается. Можно отслеживать прогреес

a = []
for i in tqdm(range(100)):
    a.append(i**2)

HOST = 'https://api.vk.com/method/'
VERSION = '5.74'
access_token = '501e6ee0501e6ee0501e6ee0a15072d48f5501e501e6ee00d6c5a19bf3986830c8502e8'
r = requests.get(HOST + 'users.get', params = {'user_ids': ' 70408624,1',
                                                'access_token': access_token,
                                                'v': VERSION})

for i in range(2):
    print(r.json()['response'][i])

# Ищем расстояние между пользователями. Между мной и Дуровым
id_start = 70408624
id_ens = 1

def get_friends_list(id_user):
    r = requests.get(HOST + 'friends.get', params = {'user_ids': id_user,
                                                    'access_token': access_token,
                                                    'v': VERSION})
    if 'response' in r.json():
        return r.json()['response']['items']
    return []

print(get_friends_list(70408624))

from collections import deque

queue = deque
