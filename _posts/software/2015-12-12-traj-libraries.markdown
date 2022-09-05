---
layout: post
title:  "Path Planning with Trajectory Libraries"
date:   2015-12-12 00:00:00 -0700
thumbnail: '/img/software/traj_libraries.png'
category: software
---
Traditional path planning techniques such as RRT or A* do not do a good job expressing physical constraints like maximum acceleration or turning radius. <a href="https://youtu.be/9BBTKllZ-eA">My algorithm builds libraries of dynamically correct trajectories</a> offline that cover all possible initial conditions, and then at runtime selects the fastest path that doesn't collide with any obstacles.<br><br>

Over a sample of 1000 runs, my algorithm runs in 1.8ms, is only 4% slower than the optimal path, and can find a feasible path 98.4% of the time.  