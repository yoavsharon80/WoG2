import Utils


def readf():
    #checking if file exsist, if not create and set value to 0 avoid null
    try:
        my_file = open(Utils.SCORES_FILE_NAME(),'r', encoding='utf-8')
    except IOError:
        print('File not found, open new file')
        my_file = open(Utils.SCORES_FILE_NAME(), 'w', encoding='utf-8')
        handler = my_file.write('0')
        my_file.close()
    #read value from file
    my_file = open(Utils.SCORES_FILE_NAME(), 'r', encoding='utf-8')
    handler = my_file.read()
    points = int(handler)
    my_file.close()
    return points

def writef(value):
    points = str(value)
    try:
        my_file = open(Utils.SCORES_FILE_NAME(), 'w',encoding='utf-8')
        handler = my_file.write(points)
        #handling txt file to number
    except IOError:
        print('File can not be opened / created')
    finally:
        print('File created and closed')
        my_file.close()

def add_score(str_points):
    points = int(str_points)
    tmp=readf()
    points = tmp + points
    writef((points))
    print('Current Score is:',readf())


