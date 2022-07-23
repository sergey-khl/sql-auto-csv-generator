import mysql.connector
from datetime import datetime, timedelta, date
import sys
import csv

stamp = datetime.today().strftime("%Y%m%d")

file_install = "location\of\install.csv\data{}.csv".format(stamp) # set this to where you want your download to be made. The csv need not exist yet.
showConsole = True # make this false if you do not want to see the terminal pop up with the values.

if __name__ == '__main__':
    conn = mysql.connector.connect(user='user', password='pass',
                             host='127.0.0.1',
                             database='')
    cursor = conn.cursor()

    query = ('enter your sql query here where parameter=%s')
    
    param = 5
    cursor.execute(query, (param))

    with open(file_install, 'w', encoding='UTF8', newline='') as f:
        f.write('')
        writer = csv.writer(f)

        header = ['some', 'header', 'names']
        writer.writerow(header)

        for (some, head, params) in cursor:
            row = [some, head, params]
            writer.writerow(row)
            if showConsole:
                print(row)
            
        f.close()
    cursor.close()
    conn.close()

