#!/usr/bin/env python3

import math
import time
import sys

def rotate_around_axis(ascii_art, angle):
    # Split the art into lines and pad them so all lines have equal width.
    lines = ascii_art.splitlines()
    if not lines:
        return ""
    height = len(lines)
    width = max(len(line) for line in lines)
    art = [line.ljust(width) for line in lines]
    
    # Determine the vertical axis (the line splitting the art in half).
    # We use the center of the width.
    axis_x = width / 2

    # Create a canvas using the original art dimensions.
    canvas = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Compute cosine of the angle (the only factor needed for this transformation).
    cos_angle = math.cos(angle)
    
    # Iterate over each character in the original art.
    for y in range(height):
        for x in range(width):
            char = art[y][x]
            if char == ' ':
                continue  # Skip blank spaces.
            
            # Compute horizontal distance from the vertical axis.
            dx = x - axis_x
            
            # Transform the x coordinate. When angle=0, cos(0)=1 so new_x == x.
            # When angle increases, positions away from the axis are scaled.
            new_x_float = axis_x + dx * cos_angle
            new_x = int(round(new_x_float))
            new_y = y  # y remains unchanged.
            
            # Place the character on the canvas if it falls within bounds.
            if 0 <= new_x < width and 0 <= new_y < height:
                canvas[new_y][new_x] = char

    # Join the canvas rows into a single string.
    return "\n".join("".join(row) for row in canvas)

def main():
    # Input ASCII art (as provided).
    ascii_art = r"""
                                                                                                                                          
                                                                                   rOOOOO^    UOOOOv                  `11{11'                         
                                                                                   0$$$$$"    #$$$$p                  ;$$$$$"                         
                                                                                   0$$$$$"    #$$$$p                  ;$$$$$"                         
                                                                                                                      ;$$$$$"                         
                         ^]?]]-  :)0aowtI    >ud*kJ}"          '!)Xqa*opU1!.       <?]]?]'    -?]]?+        ^?Xb*kJ[^ ;$$$$$"                         
                         l$$$$M"a$$$$$$$$M!_%$$$$$$$$*!      '0$$$$$$$$$$$$$0"     0$$$$$"    #$$$$p      :h$$$$$$$$$pI$$$$$"                         
                         l$$$$@$$$B@$$$$$$$$$$@@$$$$$$B,    ;$$$$$$%oa#@$$$$$#`    0$$$$$"    #$$$$p     /$$$$$$$$$$$$$$$$$$"                         
                         l$$$$$%l   `w$$$$$$\   .v@$$$$q    X$$$$#,     {$$$$$[    0$$$$$"    #$$$$p    1$$$$$Bj    ;q$$$$$$"                         
                         l$$$$$+      8$$$$Q      h$$$$#    ~____;      )$$$$$1    0$$$$$"    #$$$$p    d$$$$$~       m$$$$$"                         
                         l$$$$$"      M$$$$r      p$$$$*       l{vOa@$$$$$$$$${    0$$$$$"    #$$$$p    W$$$$k        '@$$$$"                         
                         l$$$$$"      W$$$$r      p$$$$#    ^J$$$$$$$$$@o$$$$${    0$$$$$"    #$$$$p    8$$$$C         W$$$$"                         
                         l$$$$$"      M$$$$r      p$$$$#   ^M$$$$%U?"   i$$$$$1    0$$$$$"    *$$$$p    *$$$$#.       'B$$$$"                         
                         l$$$$$"      W$$$$r      p$$$$#   u$$$$$!      +$$$$${    0$$$$$"    #$$$$p    O$$$$$[      'p$$$$$"                         
                         l$$$$$"      W$$$$r      p$$$$#   z$$$$$+     )B$$$$${    0$$$$$"    #$$$$p    I%$$$$$X"  .]o$$$$$$"                         
                         l$$$$$"      M$$$$r      p$$$$#   IB$$$$$%ko@$$$$$$$$|    0$$$$$"    #$$$$p     <@$$$$$$$$$$$B$$$$$"                         
                         l$$$$$"      W$$$$r      p$$$$#    ;d$$$$$$$$$C,#$$$$a;   0$$$$$"    #$$$$p       vB$$$$$$$$J B$$$$"                         
                                                               i|nxt-`             0$$$$$"                   `?fnr):                                  
                                                                                   O$$$$$"                                                            
                                                                                lCm@$$$$W.                                                            
                                                                                +$$$$$$%I                                                             
                                                                                +$$@Wqt^                                                              
                                                                                                                                                      
                                                jOO0Oc                                                                  `OO0OOr                       
                                                0$$$$b                                                                  ^$$$$$O                       
                                                0$$$$b                                                                  ^$$$$$O                       
                                                0$$$$b                                                                  ^$$$$$O                       
         .LCLCL1 'jhW8_      :np*&8&*px,        0$$$$b  )q#&8*q(             ~Ub#88Wow/`        ICLCLC]       xLCLCX    ^$$$$$O `xbM8&*w1'            
         .$$$$$v\B$$$$?    /@$$$$$$$$$$$%1      0$$$$bj$$$$$$$$$$Z`       ;p$$$$$$$$$$$$8(      >$$$$$t       p$$$$#    ^$$$$$mp$$$$$$$$$@c           
         .$$$$$&$$$$$$?   b$$$$$$MbW$$$$$$q     0$$$$$$$$$$$$$$$$$&,     Y$$$$$$$B&$$$$$$$o'    >$$$$$t       p$$$$#    ^$$$$$$$$$8%$$$$$$$C          
         .$$$$$$$h1>ll^ '*$$$$Wl    .-B$$$$O    0$$$$$Mi.   ^X$$$$$@:   x$$$$$m^    '-B$$$$B;   >$$$$$t       p$$$$#    ^$$$$$$b"    ,M$$$$$;         
         .$$$$$@i       ?$$$$$]       r$$$$$i   0$$$$@;       X$$$$$1  ;$$$$$Q        [$$$$$r   >$$$$$t       p$$$$#    ^$$$$$k       z$$$$$!         
         .$$$$$p        x$$$$$@@B@@B@@@$$$$$}   0$$$$C        I$$$$$z  /$$$$$]         *$$$$d   >$$$$$t       p$$$$*    ^$$$$$O       u$$$$$l         
         .$$$$$m        X$$$$$$$$$$$$$$$$$$$|   0$$$$u        `$$$$$Y  j$$$$$-         d$$$$a   >$$$$$t       p$$$$#    ^$$$$$O       n$$$$$!         
         .$$$$$w        f$$$$B'.'.'.'.'.'.'..   0$$$$0        _$$$$$t  [$$$$$|        `@$$$$Q   >$$$$$t       b$$$$#    ^$$$$$O       u$$$$$l         
         .$$$$$m        <$$$$$z       :>>>>>^   0$$$$$)       b$$$$$<  .a$$$$%I       0$$$$$]   i$$$$$C      i@$$$$#    ^$$$$$O       u$$$$$!         
         .$$$$$w         r$$$$$#-   ^U@$$$$Z.   0$$$$$$a+  'jB$$$$$n    i$$$$$@d+  ,n8$$$$$z.   ^@$$$$$b<  +d$$$$$$#    ^$$$$$O       n$$$$$l         
         .$$$$$m          )$$$$$$$$$$$$$$$c     0$$$$8$$$$$$$$$$$$u      `d$$$$$$$$$$$$$$@}      ;B$$$$$$$$$$$o$$$$#    ^$$$$$O       u$$$$$!         
         .$$$$$w           '[W$$$$$$$$$Bj^      0$$$$Q,k$$$$$$$$m,         ,Y@$$$$$$$$$*~'        "O$$$$$$$$Q`Y$$$$*    ^$$$$$O       u$$$$$l         
                               ^;l!!I,'                 ."l!lI^               ',Il!l;`               "I!!I^                                           
                        
"""
    # Remove any leading newline from the triple-quoted string.
    ascii_art = ascii_art.lstrip("\n")
    
    angle = 0.0
    try:
        while True:
            # Compute the current frame by swinging the art about the vertical axis.
            frame = rotate_around_axis(ascii_art, angle)
            
            # Clear the terminal screen (ANSI escape codes).
            print("\033[H\033[J" + frame)
            
            # Pause briefly to control the animation speed.
            time.sleep(0.1)
            
            # Increment the angle.
            angle += 0.1
    except KeyboardInterrupt:
        # Graceful exit when the user presses Ctrl+C.
        sys.exit(0)

if __name__ == '__main__':
    main()
