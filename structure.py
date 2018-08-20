import re
from database import Database,CursorFromConnectionFromPool

def read_file():
    #
    with open('properties.txt','r') as p_file:
        filecontent = p_file.readlines()
        for line in filecontent:
            place = line[:-1]

            print(place)

#read_file()

def extraction():
    odd_place = 'K Wellington Point, address available on request $550 per week  House: 4  2  2  Modern Family Home in Wellington Point part of the... Situated in a peaceful tree lined street you will find this beautiful family home within walking distance to public transport....   Photos  View Details  View Wellington Point on realestate.com.au'
    place = 'A 4 Beard Place, Wellington Point, Qld 4160  $680 Per Week  House: 4  2  3 Blue Ribbon Location Re/Max United Vision are very proud to present to the rental market, an opportunity for you to call this luxurious and quality...             1 / 11    Photos  View Details  View 4 Beard Place, Wellington Point on realestate.com.au'
    print(place)
    #https://regex101.com
    match = re.search(r'(House:)(\s+\d)(\s+\d)(\s*\d*)',place)
    if match:
        print(match.group())
        beds = int(match.group(2))
        bath = int(match.group(3))
        car = int(match.group(4))

    print('this places has {} bedrooms, {} bathrooms and {} car spaces'.format(beds,bath,car))
    rent_m = re.search(r'(\s*\$)([0-9]*\s+)(Per)',place)
    if rent_m:
        rent = int(rent_m.group(2))
        print('Renting for {} per week'.format(rent))
    else:
        rent=0
        print('no fertn found')

    location = re.search(r'([\s\w]*),([\s\w]*),(\s*\w*\s*)([0-9]{4})',place)
    if location:
        street = location.group()
        str_no = location.group(1)[2:].strip()
        sub = location.group(2).strip()
        state = location.group(3).strip()
        pcode = location.group(4).strip()
        print('street no {} in {}'.format(str_no,sub))
    else:
        print('no location found')

    odd_loc = re.search(r'(^[\s\w]*), (address available)',odd_place)
    if odd_loc:
        print(odd_loc.group()[2:].strip())
        print(odd_loc.group(1)[2:].strip())


def save_it():
    with CursorFromConnectionFromPool() as cursor:
        cursor.execute('insert into twit_users (screen_name, oauth_token, oauth_token_secret) '
                       'values (%s,%s,%s)',
                       (self.screen_name, self.oauth_token,
                        self.oauth_token_secret))

def read_it():
    with CursorFromConnectionFromPool() as cursor:
        cursor.execute('select * from tblRentals where PK_Rental_ID > %s', (1))
        # need the comma to crete tupple
        #user_data = cursor.fetchone()  # return the first item
        rentals = cursor.fetchall()
        for rent in rentals:
            print(rent)

Database.initialise(database='learning',user='dieterthierry',password='',host='localhost')

