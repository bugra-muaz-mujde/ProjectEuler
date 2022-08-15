import os
import sched, time
import keyboard


class Bike:
    def __init__(self, bike, name, brand, cranckset, cassette):
        self.bike = self.set_bike_list(bike)
        self.cadence = 0
        self.speed = 0
        self.name = name
        self.brand = brand
        self.cranckset = cranckset
        self.cassette = cassette
        self.stamina = 100

    @staticmethod
    def set_bike_list(bike):
        row_list = []
        for row in bike.split("0"):
            row_list.append(list(row))
        return row_list

    def move_bike(self):
        wheel_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for row in range(len(self.bike)):
            for col in range(len(self.bike[row])):
                if self.bike[row][col] in wheel_list:
                    if int(self.bike[row][col]) == 9:
                        self.bike[row][col] = str(1)
                    else:
                        self.bike[row][col] = str(int(self.bike[row][col]) + 1)

    def increase_cadence(self):
        if self.cadence < 80:
            self.cadence += 20
            self.speed += 5
        elif 100 <= self.cadence <= 106:
            self.stamina += 2
            self.cadence += 1
        elif 80 <= self.cadence < 100:
            self.cadence += 1
            self.speed += 1
        else:
            self.stamina -= 30
            self.cadence = 80
            self.speed -= 5
        if self.speed > 30:
            self.stamina -= 1

    def get_bike_data(self):
        print("Cadence :", self.cadence, "Speed :", self.speed, end="")


bike_ascii = """
                                          $'   **.0
              d$$$$$$$P'                  $    J0
                  ^$.                     $r  '0
                  d'b                    .db0
                 P   $                  e' $0
       12345678       *                *    123456780
     9 12345678 9      *             .*   9 12345678 90
   8  5        9  1     *         .$'   8  5        9  10
 7  4            1  2    c  7    d'   7  4            1  20
6  3              2  3     OOO**     6  3              2  30
5  2              3  4    OOOOO      5  2              3  40
4  1              4  5     OOO       4  1              4  50
3  9              5  6      j        3  9              5  60
 2  8            6  7                 2  8            6  70
   1  7        7  8                     1  7        7  80
     9 65432198 9                         9 65432198 90
       87654321                             876543210
"""


bike1 = Bike(bike_ascii, "Bugra", "Cube", 2, 11)
for bike_row in bike1.bike:
    for bike_col in bike_row:
        print(bike_col, end="")
while True:
    if keyboard.is_pressed("w"):
        bike1.increase_cadence()
        time.sleep(60/(bike1.speed ** 2))
        os.system("cls")
        bike1.move_bike()
        bike1.get_bike_data()
        for bike in bike1.bike:
            for col in bike:
                print(col, end="")


