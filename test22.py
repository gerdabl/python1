# #01S1#01S2#02SrS4S5 oder #01S6
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
    c = ""

    for i in cmd_id_list:
        if i != "":
            a = a + i
            if len(a) < maxlength:
             b = a
            else:
                c = c + i
    cmd_list[id] = c

    return(b)


print(tx_que)
a = prep_cmd(id, tx_que, cmd_list)

print(a)
print(cmd_list)
