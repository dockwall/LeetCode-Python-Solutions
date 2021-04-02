"""
Problem:
Design a parking system for a parking lot.
The parking lot has three kinds of parking spaces: big, medium, and small,
with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small):
Initializes object of the ParkingSystem class.
The number of slots for each parking space are given as part of the constructor.

bool addCar(int carType):
Checks whether there is a parking space of carType
for the car that wants to get into the parking lot.
carType can be of three kinds: big, medium, or small,
which are represented by 1, 2, and 3 respectively.
A car can only park in a parking space of its carType.
If there is no space available, return false, else park the car in that size space and return true.

Example 1:
Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]
Explanation:
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1);
// return true because there is 1 available slot for a big car
parkingSystem.addCar(2);
// return true because there is 1 available slot for a medium car
parkingSystem.addCar(3);
// return false because there is no available slot for a small car
parkingSystem.addCar(1);
// return false because there is no available slot for a big car. It is already occupied.

Constraints:
1)0 <= big, medium, small <= 1000
2)carType is 1, 2, or 3
3)At most 1000 calls will be made to addCar
"""


class ParkingSystem:
    def __init__(self, big, medium, small):  # class Constructor
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):  # class Method
        if carType == 1:  # if carType - big(1):
            if self.big == 0:  # if there is no place for a car:
                return False
            else:  # if there is a place for a car:
                self.big -= 1  # take one big place
                return True
        elif carType == 2:  # if carType - medium(2):
            if self.medium == 0:  # if there is no place for a car:
                return False
            else:  # if there is a place for a car:
                self.medium -= 1  # take one medium place
                return True
        elif carType == 3:  # if carType - small(3):
            if self.small == 0:  # if there is no place for a car:
                return False
            else:  # if there is a place for a car:
                self.small -= 1  # take one small place
                return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


output_list = []  # our bool List

obj = ParkingSystem(1, 1, 0)  # Example parking lot
output_list.append(None)

param1 = obj.addCar(1)  # Example first car
output_list.append(param1)

param2 = obj.addCar(2)  # Example second car
output_list.append(param2)

param3 = obj.addCar(3)  # Example third car
output_list.append(param3)

param4 = obj.addCar(1)  # Example fourth car
output_list.append(param4)

print(output_list)
