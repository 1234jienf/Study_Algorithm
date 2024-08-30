data = input()
rounds = 1
shots = 0
score = 0

def scoreAdder(depth: int, index: int, lastShot: int):
    global score
    if depth == 0:
        return
    tmp = data[index]
    if tmp == '-':
        tmp = 0
    elif tmp == 'S':
        tmp = 10
    elif tmp == 'P':
        tmp = 10 - lastShot
    else:
        tmp = int(tmp)
    score += tmp
    scoreAdder(depth - 1, index + 1, tmp)
    

lastShotScore = 0
for i in range(len(data)):
    if rounds > 10:
        break
    if data[i] == 'S':
        score += 10
        scoreAdder(2, i + 1, 0)
        rounds += 1
        shots = 0
    elif data[i] == 'P':
        score += 10 - lastShotScore
        scoreAdder(1, i + 1, 0)
        rounds += 1
        shots = 0
    else:
        shot = data[i]
        if shot == '-':
            shot = 0
        else:
            shot = int(shot)
        lastShotScore = shot
        score += shot
        shots += 1
        if shots == 2:
            rounds += 1
            shots = 0

print(score)