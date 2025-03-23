import sys

for _ in range(int(sys.stdin.readline())):
    test_count = 0
    # test_stack = []
    result = False
    for ch in sys.stdin.readline():
        try:
            if ch == "(":
                # test_stack.append("(")
                test_count += 1
            elif ch == ")":
                # test_stack.pop()
                if test_count <= 0:
                    result=False
                    break
                test_count -= 1
        except:
            result = False
            break;

        # if ch == "(":
        #     test_stack.append("(")
        # if ch == ")":
        #     try:
        #         test_stack.pop()
        #     except:
        #         result = False
        #         break;

        result = True
    # if len(test_stack)==0 and result:
    #     print("YES")
    if test_count == 0 and result:
        print("YES")
    else: 
        print("NO")