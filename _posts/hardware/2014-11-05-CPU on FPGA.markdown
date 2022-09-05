---
layout: post
title:  "CPU on FPGA"
date:   2014-11-05 00:00:00 -0700
thumbnail: '/img/hardware/cpu.jpg'
category: hardware
---
As part of a class on computing hardware, I designed and implemented a multicycle MIPS RISC architecture CPU on a Xilinx FPGA using Verilog. I started by creating the Arithmetic and Logic Unit (ALU) that is the heart of any CPU using combinational logic. I then created the datapath and control structure that loads instructions from memory, decodes them, and forwards the correct data between registers, external memory, and the ALU. My teammate and I also wrote an assembler to translate MIPS assembly language into the native machine code understood by the processor. <br><br> 

The class also covered pipelining, memory cache performance, branch prediction, and compiler optimizations.