# #01S1#01S2#02SrS4S5 oder #01S6
import numpy as np
maxid = 10
cmd_list = ["" for x in range(maxid+1)]
id = 1
maxlength = 10
tx_que = "#01xxxxx#01S1#01S2#01S1dgdr#01S1dgdr#01S1dgdr#01S1dgdr#01S2#05SrS4S5"

def prep_cmd(id, tx_que, cmd_list):

    s_list = tx_que.split("#")

    for i in s_list:
        if i != "":
            cmd_list[int(i[1:2])] = cmd_list[int(i[1:2])] + "#" + i[2:]

    cmd_id_list = cmd_list[id].split("#")

    a = ""
    b = ""


    for i in cmd_id_list:
        if i != "":
            a = a + i
            if len(a) < maxlength:
             b = a
            else:
                b = b + i
    cmd_list[id] = b
    
    return(b)


print(tx_que)
a = prep_cmd(id, tx_que, cmd_list)

print(a)
print(cmd_list)

#  1   2    3    4      5      6       7
# R,S  T,U  Edg  quick  qick2  quick3  long

dig_arr = np.zeros((64,100) ,dtype=np.int8)

dig_arr[0,0] = 1
print(dig_arr)

print(dig_arr.__sizeof__())

import configparser
config = configparser.ConfigParser()
config.sections()
config.read('file.ini')
print(config.sections())
for k in config['LOGIC_MODULE_CALC']:
    #print(k)
    print(k,"=",config['LOGIC_MODULE_CALC'][k])





