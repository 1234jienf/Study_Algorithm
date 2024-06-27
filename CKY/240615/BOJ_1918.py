words = input()

ans = ""
left_list = []
right_list = []
bracket_list = []
bracket = 0

for word in words:
    if word == "+" or word == "-":
        if bracket == 0:
            left_list.append(word)
        else:
            bracket_list.append(word)
    elif word == "*" or word == "/":
        if bracket == 0:
            while left_list:
                if left_list[-1] == "+" or left_list[-1] == "-":
                    right_list.append(left_list.pop())
            left_list.append(word)
            while right_list:
                left_list.append(right_list.pop())
        else:
            check = 0
            while check < bracket:
                if bracket_list[-1]
    elif word == "(":
        bracket += 1
    elif word == ")":
        bracket -= 1
    else:
        ans += word
