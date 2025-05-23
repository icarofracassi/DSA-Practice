# Problem

Your colleague Nathália has a training scheduled to take place in person at SAP Labs and needs your help finding the room for her appointment. She received a code with 4 characters (GE02) that represents the location of the room.

You know that there are 4 possible floors, which are: (B=basement, G=ground, 1=first, 2=second). In addition, there are 10 sectors represented by letters of the alphabet from A to J. Finally, the rooms numbers are integers ranging from 01 to 20.

Therefore, help your colleague by creating a program that receives the room code and prints its location in the pattern “Room < room_number > on the < floor > floor of sector < sector >”.

## Inputs

The input contains 4 characters, where the first character represents the floor, the second represents the sector of the building and the last two represent the room number.

## Outputs

For each input test case, your program must print a single line containing the location of the room in text format.

## Examples

| Sample Input 1    | Sample Output 1                           |
| ----------------- | ----------------------------------------- |
| GE02              | Room 02 on the ground floor of sector E   |

| Sample Input 2    | Sample Output 2                           |
| ----------------- | ----------------------------------------- |
| 2F06              | Room 06 on the second floor of sector F   |

## Code

[Go to code](../codes/A.py)
