---
layout: post
title:  "Path Planning with Trajectory Libraries"
date:   2015-12-12 00:00:00 -0700
thumbnail: '/img/software/traj/traj_libraries.png'
background: '/img/software/traj/traj3.png'
category: software
---

Traditional path planning techniques such as RRT or A* do not do a good job expressing physical constraints like maximum acceleration or turning radius. Even if they are smoothed to find the *shortest* path, it might not be the *quickest* path.

<iframe width="100%" height="400px" src="https://www.youtube.com/embed/9BBTKllZ-eA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<img src="/img/software/traj/rrt.png" alt="rrt" width="100%"/>
_Fig 1. An example path found by RRT_

Trajectory Optimization will find the *fastest* path, taking into account physical constraints, but takes a long time to compute, making it difficult to run in real time.

<img src="/img/software/traj/opt.png" alt="opt" width="100%"/>
_Fig 2. The process of Trajectory Optimization_

Trajectory Libraries combine the best of both worlds - optimal results in super fast runtimes. The idea is to _discretize all possible initial states_, and for each possibility build a "library" of possible paths. At runtime, select the fastest path without collisions from the closest library.

<img src="/img/software/traj/picking.png" alt="opt" width="100%"/>
_Fig 3. Picking the fastest valid path from a Library_

Building a library for **every** initial condition sounds crazy, but there's lots of symmetries that can be exploited to compress the space to just a few dimensions. The 7 dimensions of the problem space `start_x, start_y, start_theta, start_velocity_x, start_velocity_y, goal_x, goal_y` can be compressed to just 3 with `start_velocity_x, start_velocity_y, goal_dist`.

<img src="/img/software/traj/symmetry.png" alt="opt" width="100%"/>
_Fig 4. Exploiting symmetry to reduce the storage space_

Against random obstacle scenarios, Trajectory Libraries found a solution 98% of the time, runs in just `1.8ms`, and only 4% slower than the path found by running a full Trajectory Optimization.

<img src="/img/software/traj/results.png" alt="opt" width="100%"/>
_Fig 5. Results_

[github repo](https://github.com/eschluntz/traj)