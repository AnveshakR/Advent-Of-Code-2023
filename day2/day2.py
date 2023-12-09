import math

max_cubes = {
    'red':12,
    'green':13,
    'blue':14
}

gamelist = []
gamesum = 0
with open('day2/day2.txt') as f:
    for line in f:
        gamelist.append(line.strip())

# part 1
for gamenum, game in enumerate(gamelist):
    game = game.split(':')[1]
    game = game.split(';')
    gametrue = True
    for balls in game:
        ball_count = {}
        balls = balls.split(',')
        balls = [ball.strip() for ball in balls]
  
        for ball in balls:
            ball_count[ball.split(' ')[1].strip()] = int(ball.split(' ')[0].strip())
        
        for color in ball_count.keys():
            if ball_count[color] > max_cubes[color]:
                gametrue = False
                break

        if not gametrue:
            break

    if gametrue:
        gamesum += gamenum+1

print("part 1: ", gamesum)


# part 2
gamesum = 0
for gamenum, game in enumerate(gamelist):
    game = game.split(':')[1]
    game = game.split(';')
    ball_count = {}
    for balls in game:
        
        balls = balls.split(',')
        balls = [ball.strip() for ball in balls]
  
        for ball in balls:
            if ball.split(' ')[1].strip() not in ball_count.keys():
                ball_count[ball.split(' ')[1].strip()] = int(ball.split(' ')[0].strip())
            elif ball_count[ball.split(' ')[1].strip()] < int(ball.split(' ')[0].strip()):
                ball_count[ball.split(' ')[1].strip()] = int(ball.split(' ')[0].strip())
        
    gamesum += math.prod(ball_count.values())

print("part 2: ", gamesum)