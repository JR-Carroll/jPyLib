import os

def initvars():
    """Sets the basic variables!"""
    
    year = raw_input('Year? ')
    client = raw_input('Client? ')
    path = raw_input('Path? ')

    main(year, client, path)

def main (year, client, path = '/'):
    months = ('Janurary', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

    monthCount = 1

    try:
        for i in months:
        os.mkdir((path + client + ' ' + year + ' ' + str(monthCount).zfill(2) + ' ' + i))
        monthCount += 1
    except:
        print("Cannot create these directorirs!")


if __name__ == '__main__':
    initvars()


