from collections import deque
from collections import OrderedDict
from datetime import datetime
import time
import math
def time_minus(time):
    all_time = 0
    all_time += int(time[:2])*60
    all_time += int(time[3:5])
    return all_time


def solution(fees, records):
    temp_answer = []
    answer = []
    temp_list = []
    dict = {}
    IN_dict = {}
    time_dict = {}
    dict = OrderedDict()
    IN_dict = OrderedDict()
    time_dict = OrderedDict()

    for i in range(len(records)):
        temp = records[i].split(' ')
        temp_list.append(temp)

    for i in range(len(temp_list)):
        total_time = 0
        if (temp_list[i][1] not in dict) and temp_list[i][2] =='OUT':
            total_time = time_minus(temp_list[i][0]) - IN_dict[temp_list[i][1]]
            dict[temp_list[i][1]] = total_time
            dict.move_to_end(temp_list[i][1])
            del IN_dict[temp_list[i][1]]
        elif (temp_list[i][1] in dict) and temp_list[i][2] =='OUT':
            total_time = time_minus(temp_list[i][0]) - IN_dict[temp_list[i][1]]
            dict[temp_list[i][1]] += total_time
            dict.move_to_end(temp_list[i][1])
            del IN_dict[temp_list[i][1]]
        elif temp_list[i][2] =='IN':
            IN_dict[temp_list[i][1]] = time_minus(temp_list[i][0])
        else:
            dict[temp_list[i][1]] = time_minus(temp_list[i][0])
        #print('indict = ',IN_dict)
        #print('temp_list = ',temp_list[i])
        #if temp_list[i][1] not in time_dict:
        #    time_dict[temp_list[i][1]] =  total_time
        #else:
        #   time_dict[temp_list[i][1]] +=  total_time

    print(dict)

    for i in IN_dict:
        IN_dict[i] = 1439 - IN_dict[i]
        if i in dict:

            dict[i] += IN_dict[i]
        else:
            dict[i] = IN_dict[i]



    dict2 = OrderedDict(sorted(dict.items()))
    print('dict2 = ',dict2)
    for i in dict2:
        #print(i)
        temp_answer.append(dict[i])
    print('temp_answer', temp_answer)   
    for i in temp_answer:
        i = int(i)
        if i<=fees[0]:
            answer.append(fees[1])
        else:
            if i-fees[0]%fees[2] != 0:
                l = int(fees[1] + (math.ceil((i-fees[0])/fees[2])*fees[3]))
                answer.append(l)
            else:
                l = int(fees[1] + (((i-fees[0])/fees[2])*fees[3]))
                answer.append(l)
    print(answer)
    return answer