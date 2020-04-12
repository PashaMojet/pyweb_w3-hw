#%%
import random

def gen_hor(cnt=4):
    date_time = ["Утром","Вечером","Днем"]
    verbs = ["остерегайтесь","ожидайте","предвкушайте"]
    other = ["котов","собак","еду"]
    rsl = []
    for i in range(0,cnt):
        rsl.append(random.choice(date_time)+' '+ random.choice(verbs)+' '+random.choice(other))
    return rsl
# %%
