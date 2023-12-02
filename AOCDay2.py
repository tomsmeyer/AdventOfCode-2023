''' AOCDay2.py
tmeyer
12/2/23
'''


def readInput(filename):
    """ Read file and strip eol chars. Return list of lines.
    """
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print("File not found, check your filename and path and try again.")
        exit()
    fileList = f.readlines()

    for i in range(len(fileList)):
        fileList[i] = fileList[i].rstrip()
    return fileList


def isGameValid(game):
    """ Check each number against the limits and return True if good, False otherwise.
    """
    cubes = {"red": 12, "green": 13, "blue": 14}
    line = game.split(':')[1]
    turns = line.split(';')
    for i in turns:
        turnCubes = i.split(',')
        for j in turnCubes:
            #if j[0] == " ":
            #    j=j[0:]
            rgb = j.split(' ')
            num = int(rgb[1])
            color = rgb[2]
            limit = cubes.get(color)
            if type(limit) == None:
                if color == "red":
                    limit = 12
                elif color == "green":
                    limit = 13
                else:
                    limit = 14

            if num > limit:
                return False

    return True


def findMaxCubes(game):
    """ simple max find solution. Uses same parsing as function above.
    """
    rMax = 0
    gMax = 0
    bMax = 0

    line = game.split(':')[1]
    turns = line.split(';')
    for i in turns:
        turnCubes = i.split(',')
        for j in turnCubes:
            rgb = j.split(' ')
            num = int(rgb[1])
            color = rgb[2]
            if color == "red":
                if num > rMax:
                    rMax = num
            if color == "green":
                if num > gMax:
                    gMax = num
            if color == "blue":
                if num > bMax:
                    bMax = num

    return rMax * gMax * bMax


def main():
    """ main: calls functions and output results
    """
    fileList = readInput("Day2Input.txt")
    print("Start of Game")

    #Part 1
    total = 0
    for i in range(len(fileList)):
        if isGameValid(fileList[i]):
            total += i+1

    print("Total value = ",total)

    #Part2
    power = 0
    for i in fileList:
        power += findMaxCubes(i)

    print("Power = ", power)

main()
