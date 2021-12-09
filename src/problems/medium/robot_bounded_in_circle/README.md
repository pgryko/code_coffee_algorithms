On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.

Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...


1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}
The solution in Java
First it is important to validate our inputs.

Then we can create some variables to store the x, y (for coordinates) and a further dir to store the direction we are travelling in.

Looping through the list of instructions and checking for which coordinate we need to adjust as well as turning left or right allows for a simple complete block of code.

We can determine a successful robotic circle if x and y are both 0, or if dir is not 0.


```java
class Solution {
    public boolean isRobotBounded(String instructions) {
        // perform some initial sanity checks
        if (instructions.length()>=1 && instructions.length()<=100) {
            
            // create `x`, `y` and `dir` variables
            // for the coordinate system, as well as the direction
            int x = 0;
            int y = 0;
            int dir = 0;
            
            // loop through all instructions
            for (int i=0; i<instructions.length(); i++) {
                // get the current instruction
                char ch = instructions.charAt(i);
                
                if (ch=='G') {
                    // if Going Forward
                    //  _____
                    // |  0  |
                    // |3 + 1|
                    // |__2__|
                    // 
                    // works like a clock:
                    // 0==up (y++)
                    // 1==right (x++)
                    // 2==down (y--)
                    // 3==left (x--)
                    
                    if (dir==0) y++;
                    if (dir==3) x--;
                    if (dir==2) y--;
                    if (dir==1) x++;
                    
                } else if (ch=='L') {
                    // change direction if left
                    dir = (dir+5)%4;
                } else if (ch=='R') {
                    // change direction if right
                    dir = (dir+3)%4;
                }
                
            }
            
            return (x==0 && y==0) ? true : (dir!=0);
            
            
        } else return false;
    }
}
```

To resolve this problem, you must notice a couple of facts:
If after the set of operations, the robot is still at the position (0, 0), then it is bounded
If the robot doesn’t point North after the set of instructions, it will return to the point (0, 0) after 4 sets of instructions, pointing North, and repeat. Therefore, if the robot doesn’t point North after the set of operations, it is bounded.
In all other cases, the robot is unbounded.
Then, in code, I executed the set of operations, tracking position and orientation of the robot. The end position and orientation tell me if the robot is bounded.
This can be done the following way, although tracking position with N, S, E, W symbols is a bit awkward, it should be easily understandable.
func isRobotBounded(instructions string) bool {
    // robot is bounded if:
    // end position is 0,0
    // OR
    // end direction is not North
    direction := 'N'
    x := 0
    y := 0
    for _, c := range instructions {
        if c == 'G' {
            if direction == 'N' {
                y++
            } else if direction == 'S' {
                y--
            } else if direction == 'W' {
                x--
            } else {
                x++
            }
        } else if c == 'L' {
            if direction == 'N' {
                direction = 'W'
            } else if direction == 'S' {
                direction = 'E'
            } else if direction == 'W' {
                direction = 'S'
            } else {
                direction = 'N'
            }            
        } else {
            if direction == 'N' {
                direction = 'E'
            } else if direction == 'S' {
                direction = 'W'
            } else if direction == 'W' {
                direction = 'N'
            } else {
                direction = 'S'
            }            
        }
    }
    return (x == 0 && y == 0) || (direction != 'N')
}
A follow up would be, what is the position of the robot after p repetitions of the instructions?
