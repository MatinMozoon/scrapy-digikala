import json
from collections import Counter

with open('2.json') as json_file:
    data = json.load(json_file)

sellers = data[0]


id = []
sr = []
satisfaction_ratio = []
ri = []
ready_in = []
price = []
provider = []
color = []


for i in sellers:
    seller = sellers[i]
    sr.append(seller['sr'])
    ri.append(seller['leadTime'])
    price.append(seller['price_list']['selling_price'])
    provider.append(seller['provider'])
    if seller['color']:
        color.append(seller['color']['title'])
    id.append(seller['id'])


for i in sr:
    if i is None:
        satisfaction_ratio.append(0)
    else:
        satisfaction_ratio.append(i)

for i in ri:
    if i is None:
        ready_in.append(0)
    else:
        ready_in.append(i)

color_set = sorted(set(color))


if len(color_set) == 0:
    sellers_list = zip(id, satisfaction_ratio, ready_in, price, provider)
    sellers_list = list(sellers_list)

    complete_sorted_list = []

    for i in sellers_list:
        print(i)
        complete_sorted_list.append(i)
        
        
    

    c_satisfaction_ratio = []
    c_ready_in = []
    c_price = []
    for i in complete_sorted_list:
        c_satisfaction_ratio.append(i[1])
        c_ready_in.append(i[2])
        c_price.append(i[3])


    if len(c_satisfaction_ratio) > 1:
        ratio_sub = []
        ratio_sub_bb = []
        add_price_sr = []
        add_price_sr_bb = []
        ratio_sub_bb.append(c_satisfaction_ratio[1] - c_satisfaction_ratio[0])
        add_price_sr_bb.append((ratio_sub_bb[0]/100) * price[0])
    for i in range(len(c_satisfaction_ratio)):
        subt = c_satisfaction_ratio[0] - c_satisfaction_ratio[i]
        ratio_sub.append(subt)
        add_price_sr.append(((ratio_sub[i]/100) * price[i]))

    print()
    print('ratio_sub_bb', ratio_sub_bb)
    print('add_price_sr_bb', add_price_sr_bb)
    print('--------------------------------------------------------')
    print('ratio_sub: ', ratio_sub)
    print('add_price_sr: ', add_price_sr)


    if len(c_ready_in) > 1:
        ready_sub = []
        ready_sub_bb = []
        add_price_ready_in_bb = []
        add_price_ready_in = []
        ready_sub_bb.append(c_ready_in[1] - c_ready_in[0])
        add_price_ready_in_bb.append((ready_sub_bb[0]*5/100) * price[0])
    for i in range(len(c_ready_in)):
        rsub = c_ready_in[0] - c_ready_in[i]
        ready_sub.append(rsub)
        add_price_ready_in.append((ready_sub[i]*5/100) * price[i])

    print()
    print('ready_sub_bb', ready_sub_bb)
    print('add_price_ready_in_bb', add_price_ready_in_bb)
    print('--------------------------------------------------------')
    print('ready_sub: ', ready_sub)
    print('add_price_ready_in: ', add_price_ready_in)


else:
    sellers_list = zip(id, satisfaction_ratio, ready_in, price, provider, color)
    sellers_list = list(sellers_list)

    complete_sorted_list = []

    for i in color_set:
        for j in sellers_list:
            if i == j[5]:
                print(j)
                complete_sorted_list.append(j)

    color_counter = Counter(elem[5] for elem in complete_sorted_list)
    color_counter = list(color_counter.values())
    print()
    print('number of each color',color_counter)


    
    c_satisfaction_ratio = []
    c_ready_in = []
    c_price = []
    for i in complete_sorted_list:
        c_satisfaction_ratio.append(i[1])
        c_ready_in.append(i[2])
        c_price.append(i[3])

        
    ratio_sub = []
    ratio_sub_bb = []
    add_price_sr = []
    add_price_sr_bb = []
    for c in color_counter:
        c_s = c_satisfaction_ratio[0:c:]
        for i in range(len(c_s)):
            ratio_sub.append(c_s[0] - c_s[i])
        if len(c_s) > 1:
            ratio_sub_bb.append(c_s[1] - c_s[0])

        c_satisfaction_ratio = c_satisfaction_ratio[c::]
        add_price_sr = []
        for i in range(len(ratio_sub)):
            add_price_sr.append(((ratio_sub[i]/100) * price[i]))

    
    for i in range(len(ratio_sub_bb)):
        add_price_sr_bb.append((ratio_sub_bb[i]/100) * price[0])

    print()
    print('ratio_sub_bb', ratio_sub_bb)
    print('add_price_sr_bb', add_price_sr_bb)
    print('--------------------------------------------------------')
    print('ratio_sub: ', ratio_sub)
    print('add_price_sr: ', add_price_sr)



    
    


    ready_sub = []
    ready_sub_bb = []
    add_price_ready_in_bb = []
    add_price_ready_in = []
    for c in color_counter:
        c_s = c_ready_in[0:c:]
        for i in range(len(c_s)):
            ready_sub.append(c_s[0] - c_s[i])
        if len(c_s) > 1:
            ready_sub_bb.append(c_s[1] - c_s[0])
            
        c_ready_in = c_ready_in[c::]
        add_price_ready_in = []
        for i in range(len(ready_sub)):
            add_price_ready_in.append(((ready_sub[i]*5/100) * price[i]))


    for i in range(len(ready_sub_bb)):
        add_price_ready_in_bb.append((ready_sub_bb[i]*5/100) * price[0])
    
    print()
    print('ready_sub_bb', ready_sub_bb)
    print('add_price_ready_in_bb', add_price_ready_in_bb)
    print('--------------------------------------------------------')
    print('ready_sub: ', ready_sub)
    print('add_price_ready_in: ', add_price_ready_in)
    


print('===========================================================================================================================')

zipped_add_price = zip(add_price_sr, add_price_ready_in)
zipped_add_price_bb = zip(add_price_sr_bb, add_price_ready_in_bb)
sum = [x + y for (x, y) in zipped_add_price]
sum_bb = [x + y for (x, y) in zipped_add_price_bb]
zipped_finale_price = zip(c_price, sum)
zipped_finale_price_bb = zip(c_price, sum_bb)
sum_f = [x + y for (x, y) in zipped_finale_price]
sum_f_bb = [x + y for (x, y) in zipped_finale_price_bb]
# zipped_finale_price_bb = zip()
# print(sum_bb)
# print(sum)
print(sum_f)
# print(sum_f_bb)