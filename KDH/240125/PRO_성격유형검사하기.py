def solution(survey, choices):
    R,T,C,F,J,M,A,N = 0,0,0,0,0,0,0,0
    n = len(survey)
    answer = ''
    for i in range(n):
        point = choices[i]
        if survey[i] == "RT":
            if point < 4:
                R += 4 - point
            elif point > 4:
                T += point - 4
        elif survey[i] == "TR":
            if point < 4:
                T += 4 - point
            elif point > 4:
                R += point - 4
        elif survey[i] == "CF":
            if point < 4:
                C += 4 - point
            elif point > 4:
                F += point - 4
        elif survey[i] == "FC":
            if point < 4:
                F += 4 - point
            elif point > 4:
                C += point - 4
        elif survey[i] == "JM":
            if point < 4:
                J += 4 - point
            elif point > 4:
                M += point - 4
        elif survey[i] == "MJ":
            if point < 4:
                M += 4 - point
            elif point > 4:
                J += point - 4
        elif survey[i] == "AN":
            if point < 4:
                A += 4 - point
            elif point > 4:
                N += point - 4
        elif survey[i] == "NA":
            if point < 4:
                N += 4 - point
            elif point > 4:
                A += point - 4
    if R < T:
        answer += "T"
    else:
        answer += "R"
    if C < F:
        answer += "F"
    else:
        answer += "C"
    if J < M:
        answer += "M"
    else:
        answer += "J"
    if A < N:
        answer += "N"
    else:
        answer += "A"

    return answer