---
layout: post
title:  "Robotic Drawing"
date:   2014-11-05 00:00:00 -0700
thumbnail: '/img/hardware/robot-arm.png'
category: hardware
---
My final project for Advanced Robotics was to <a href="https://www.youtube.com/watch?v=Y-VPsfdT8Fc">draw pictures</a> from an <a href="https://www.youtube.com/watch?v=nNL7_r4sgOY">input photo</a> using a Catalyst-5 robot arm. Standard edge detection algorithms were just the beginning of my processing pipeline, the real challenge was to connect these edgelets into continuous pencil strokes for the arm to draw in the most efficient manner. <br><br>

To find the best pencil strokes I transform the image into a graph, where edge pixels are nodes and adjacent pixels are connected by edges. I then repeatedly selected and removed the longest shortest path from the graph, which I found to be the fastest and most accurate heuristic for human-like drawings.