#! /usr/bin/env

import os

def main():
    """Sets the basic variables!"""
    
    year = raw_input('Year? ')
    client = raw_input('Client? ')
    path = raw_input('Path? ')

    createDir(year, client, path)

def createDir (year, client, path = '/'):
    months = ('Janurary', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

    monthCount = 1

    try:
        for i in months:
            os.mkdir((path + client + ' ' + year + ' ' + str(monthCount).zfill(2) + ' ' + i))
            monthCount += 1
    except:
        print("Cannot create these directories because I said so!!!")


if __name__ == '__main__':
    main()
