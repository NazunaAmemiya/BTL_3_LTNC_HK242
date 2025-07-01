from StaticError import *
from Symbol import *
from functools import *

#--------------------------HELPER FUNCTION-----------------------------------

def find_name(x,n):
    if(len(list(filter(lambda y: y.name == n, x))) != 0):
        return True
    else:
        return False
    
def find_type(x,n):
    if(len(list(filter(lambda y: y.typ == n, x))) != 0):
        return True
    else:
        return False

def find(x,n,t):
    if(len(list(filter(lambda y: y.name == n and y.typ == t, x))) != 0):
        return True
    else:
        return False

def check_word(char):
    if(not ((char >='a' and char <= 'z')or(char >='A' and char <= 'Z')or(char >= '0' and char <= '9')or char == '_')):
        return False
    return True

def check_chuoi(chuoi):
    
    if(len(chuoi)<2):
        return False
    if (chuoi[len(chuoi)-1] != "\'"):
        return False
    if (chuoi[0] != "\'"):
        return False

    new_chuoi = list(filter(lambda x: x!= "\'", chuoi))
    if (len(list(filter(lambda x: check_word(x),new_chuoi ))) != len(new_chuoi)):
        return False
    if (len(list(filter(lambda x: x == '_',new_chuoi)))!=0):
        return False

    return True

def isNUM(num):
    c = len(list(filter(lambda x: ((x>='0' and x<='9')or x=="."),num)))
    if(c==len(num)):
        return True
    return False

def check_name(name):
    if(len(name)==0):
        return False

    if (len(list(filter(lambda x: check_word(x),name ))) != len(name)):
        return False

    if(not(name[0]>='a' and name[0]<="z")):
        return False
    return True

def find_block(idx,name, symbol_table):
    block = symbol_table[idx]
    if (idx < 0):
        return -1
    if (find_name(block,name)):
        return idx
    return find_block(idx-1,name,symbol_table)

#-------------------------------------------------------------
def insert(name, type, symbol_table,instruction,output):
    symbol = Symbol(name, type)

    #tìm kiếm tên trong block hiện tại
    if (find_name(symbol_table[-1],name) != 0):
        raise Redeclared(instruction)
        
    # có thể bỏ vì đề không yêu cầu
    if (type != "number" and type != "string"):
        raise InvalidInstruction(instruction)
      
    return symbol_table[:-1] + [symbol_table[-1] +[symbol]],output+["success"]
    # [:-1] lấy tất cả các phần tử trừ phần tử cuối
    # [-1] lấy phần tử cuối cùng
    # [symbol_table[-1] + [symbol]] thêm phần tử vào cuối
    # thêm cái list mới vào cuối

#-------------------------------------------------------------
def assign(name, value, symbol_table,instruction,output):
    #check Valid
    #value = number
    
    if(isNUM(value)):
        try:
            int(value)
        except ValueError:
            raise InvalidInstruction(instruction)
    #value = string
    elif (value[0] == "\'" or value[len(value)-1] == "\'"):
        if(not check_chuoi(value)):
            raise InvalidInstruction(instruction)
    else:
        if(not check_name(value)):
            raise InvalidInstruction(instruction)
    
    #Tìm name
    if (len(list(filter(lambda x: find_name(x,name), symbol_table[::-1]))) == 0):
        raise Undeclared(instruction)
    
    idx_name = find_block(len(symbol_table)-1,name,symbol_table)#block chua name
    block_name = symbol_table[idx_name]

    #value = number
    if (isNUM(value)):
        if (not find(block_name,name,"number")):
            raise TypeMismatch(instruction)
    #value = string
    elif (value[0] == "\'" or value[len(value)-1] == "\'"):    
        if (not find(block_name,name,"string")):
            raise TypeMismatch(instruction)
    #value = variable
    else:  
        #check exist value
        if(len(list(filter(lambda x: find_name(x,value), symbol_table[::-1]))) == 0):
            raise Undeclared(instruction)

        idx_value = find_block(len(symbol_table)-1,value,symbol_table)#block chua value
        block_value = symbol_table[idx_value]
        # check type giữa name và value
        # nếu name là number
        if (find(block_name,name,"number")):
            if (not find(block_value,value,"number")):
                raise TypeMismatch(instruction)
        # nếu name là string
        if (find(block_name,name,"string")):
            if (not find(block_value,value,"string")):
                raise TypeMismatch(instruction)

    return symbol_table,output+["success"]
    
#------------------------------\------------------------------
def lookup(name, symbol_table,instruction,output):
    #tìm name
    if(len(list(filter(lambda x: find_name(x,name), symbol_table[::-1]))) == 0):
        raise Undeclared(instruction)

    return symbol_table,output+[find_block(len(symbol_table)-1,name,symbol_table)]

#------------------------------\------------------------------
def unique_var(table,idxname,used):
    name = table[idxname]
    if idxname <0:
        return used
    if(name not in used):
        return unique_var(table,idxname-1,[name]+used)
    return unique_var(table,idxname-1,used )

def format(index,name_table,block_table):
    size = len(name_table)-1

    mess = f'{name_table[size - index]}//{block_table[size - index]}'
    return mess

def print_symbol_table(symbol_table,instruction,output):
    # m là danh sách các tên biến
    m = list(map(lambda x: list(map(lambda y: y.name,x )), symbol_table))
    lst_name = [item for sublist in m for item in sublist]# chỉnh từ list của list thành list

    if(len(lst_name)<1):
        return symbol_table,output+[""]
    unique_queue = unique_var(lst_name, len(lst_name)-1, [])#tên không trùng
    # tìm kiếm block
    block = list(map(lambda x: find_block(len(symbol_table)-1,x,symbol_table),unique_queue))

    # chuyển từ list sang string
    list_mess = [format(i,unique_queue,block) for i in range(len(unique_queue))]
    str_mess = " ".join(list(reversed(list_mess)))

    return symbol_table,output+[str_mess]

#------------------------------\------------------------------
def Rprint_symbol_table(symbol_table,instruction,output):
    # m là danh sách các tên biến
    m = list(map(lambda x: list(map(lambda y: y.name,x )), symbol_table))
    lst_name = [item for sublist in m for item in sublist]# chỉnh từ list của list thành list

    if(len(lst_name)<1):
        return symbol_table,output+[""]

    unique_queue = unique_var(lst_name, len(lst_name)-1, [])#tên không trùng

    # tìm kiếm block
    block = list(map(lambda x: find_block(len(symbol_table)-1,x,symbol_table),unique_queue))
    
    # chuyển từ list sang string
    list_mess = [format(i,unique_queue,block) for i in range(len(unique_queue))]
    str_mess = " ".join(list_mess)

    return symbol_table,output + [str_mess]
#------------------------------\------------------------------
def check(arg):

    if(arg[0] not in ["INSERT", "BEGIN", "END", "ASSIGN", "LOOKUP", "PRINT", "RPRINT"]):
        raise InvalidInstruction("Invalid command")

    if(arg[0] in ["INSERT","ASSIGN"] and len(arg)!= 3):
        return 0
    elif(arg[0] in ["LOOKUP"] and len(arg)!= 2):
        return 0
    elif(arg[0] in ["BEGIN","END","PRINT","RPRINT"] and len(arg)!= 1):
        return 0

    if(arg[0]=="INSERT" or arg[0]=="ASSIGN" or arg[0]=="LOOKUP" ):
        if(not check_name(arg[1])):
            return 0
    

    return 1

def run(instruction,symbol_table):
    # tách lệnh
    arg = instruction.split(" ")
    if(check(arg) ==0):
        raise InvalidInstruction(instruction)
    if (arg[0] == "INSERT"):
        return insert(arg[1], arg[2],symbol_table[0],instruction,symbol_table[1])
    elif(arg[0] == "ASSIGN"):
        return assign(arg[1], arg[2],symbol_table[0],instruction,symbol_table[1])
    elif(arg[0] == "BEGIN"):
        return symbol_table[0]+[[]],symbol_table[1]
    elif(arg[0] == "END"):
        # check xem có block nào chưa đóng không
        if (len(symbol_table[0]) <= 1 ):
            raise UnknownBlock()
        else:
            removed_sym = symbol_table[0]
            return removed_sym[:-1],symbol_table[1]
    elif(arg[0] == "LOOKUP"):
        return lookup(arg[1],symbol_table[0],instruction,symbol_table[1])
    elif(arg[0] == "PRINT"):
        return print_symbol_table(symbol_table[0],instruction,symbol_table[1])
    elif(arg[0] == "RPRINT"):
        return Rprint_symbol_table(symbol_table[0],instruction,symbol_table[1])
    return symbol_table
#-------------------------------------------------------------
def simulate(list_of_commands):
    """
    Executes a list of commands and processes them sequentially.
    
    Args:
        list_of_commands (list[str]): A list of commands to be executed.

    Returns:
        list[str]: A list of return messages corresponding to each command.
    """

    prio_symbol = [[]]
    # chạy lệnh
    try:
        sym,output = reduce(lambda acc,com: run( com,acc ),list_of_commands, ([[]],[]))
        
        #print("res: ", res)
    except StaticError as e:        
        return [str(e)]
    # kiểm tra xem có block nào chưa đóng không
    try:
        if(len(sym) > 1):
            raise UnclosedBlock(len(sym)-1)
    except StaticError as e:
        return [str(e)]

    # return
    return list(map(str,output))

