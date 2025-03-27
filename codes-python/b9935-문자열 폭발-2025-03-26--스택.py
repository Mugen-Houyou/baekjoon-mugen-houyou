print(type(range(123)))

exit()
import sys
input = sys.stdin.readline

def explode(inp_str, target_str):
    new_inp = inp_str.replace(target_str, "")
    if inp_str == new_inp: return inp_str
    else: return explode(new_inp,target_str)

def explode_itr(inp_str, target_str):
    old_inp = inp_str
    while True:
        new_inp = old_inp.replace(target_str, "")
        if old_inp == new_inp: return new_inp
        old_inp = new_inp

def explode_stk(inp_str, target_str):
    stk = []
    tglen = len(target_str)
    for c in inp_str:
        stk.append(c)
        
        if len(stk) >= tglen:
            if "".join(stk[-tglen:]) == target_str:
                for _ in range(tglen):
                    stk.pop()
    return stk

orig_str = input().strip()
target_str = input().strip()

#result = explode_itr(orig_str,target_str).strip()
result = "".join(explode_stk(orig_str,target_str))
if result == "":
    print("FRULA")
else:
    print(result)


