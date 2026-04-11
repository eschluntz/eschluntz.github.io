---
layout: post
title:  "Replacing my Right Hand with AI"
date:   2024-07-30 12:00:00 -0700
thumbnail: '/img/software/code-with-ai/square-thumb.jpg'
background: '/img/software/code-with-ai/background.jpg'
category: software
excerpt: "Breaking my hand forced me to write all my code with AI for 2 months. I'm never going back."
---

Breaking my hand forced me to write all my code with AI for 2 months. I'm never going back.

<img src="/img/software/code-with-ai/cast.png" width="100%">
*Fig 1. "Thumbs Up" to coding with AI*

*(All opinions are my own, not my employer's)*

A few months ago, I broke my hand while biking to work in San Francisco and could only type with my left hand. By using a combination of voice-to-text and Claude, I was still able to write a tremendous amount of code at my job, including one week when I wrote over 3,000 lines of (admittedly, boilerplate-heavy) code!

The silver lining of all this is that it forced me to live in the future where we humans write very little of our own code. Honestly, I loved it.

## My Setup

I had previously used AI code generation with tools like Copilot, but still was largely writing my own code before the accident. I had also used voice-to-text, but mainly for text messages on my phone, and had never done it on my computer.

Fortunately, the built-in Voice Control for Mac was very good for natural language, but sadly was terrible at anything code-related; the symbols and vocabulary were just too out of distribution. "Eval"? You must have meant "Evil".

<img src="/img/software/code-with-ai/evil.png" width="100%">
*Fig 2. A typical slack message from me using Voice Control.*

There are great code-specific voice-to-text systems like [Talon](https://talonvoice.com), but being very excited about code generation, I saw this as an excuse to dog food our own product!

Copilot Autocomplete was too slow for me now, because it required me to write out half a line of code. My overall goal was much easier to express in English than by starting to write the code itself.

I copy and pasted large chunks of the codebase into Claude AI and gave voice commands to transform it. For instance, I would say "refactor ABC function to take input XYZ" or "write unit tests for these new functions ABC, and look at example tests for XYZ".

It wouldn't always succeed on the first try, but Claude was receptive to follow up instructions and tweaks. I felt like I was pair programming while somebody else was driving the keyboard! 

## How to Claude

Being forced to code like this, I very quickly figured out what worked and what didn't. Sometimes it was magical, but other times I wanted to throw my computer out the window. I had to constantly copy-paste between my IDE and Claude, and manually stitch together code snippets that were truncated by Claude's output length limits. Several times I raised my voice at Claude for forgetting my earlier instructions. 

<img src="/img/software/code-with-ai/angry.png" width="100%">
*Fig 3. Being angry at your computer is much more satisfying when using voice control.*

### Be specific and give examples

If you give a basic request, LLMs will give you a middle-of-the-road generic answer which probably won't work for your specific codebase.

You get much better results giving very explicit instructions of what input and output you expect, what libraries to use, etc. I had the best luck putting my instructions at the beginning AND end of my input data and context.

Even better is giving examples from your codebase to emulate. This worked tremendously well for boilerplate code such as writing unit tests or anything that is templatized, but also helped show the model how to use internal utility functions from our codebase.

Migrations and refactors were perfect cases for this. I would migrate one instance manually and then use that as an example for Claude to transform the rest of my inputs. By following this format, I was able to refactor about 3,000 lines of code pretty quickly.

### Put Claude in the Driver's Seat

<img src="/img/software/code-with-ai/robot.png" width="100%">
*Fig 4. A remote control robot built by my friend!*

Most people use LLMs as StackOverflow replacements: they ask for directions, but they are still driving. I flipped that around. If you can give Claude the right building blocks, it can often "single-shot" the full thing in one try.

On a [weekend robotics project](https://medium.com/@sarvagya.vaish/robomagellan-building-an-outdoor-robot-powered-by-cell-phone-sensors-fcf36722636e) with my friend [Survy](https://www.linkedin.com/in/sarvagyavaish/), we gave Claude code snippets to control a single motor and read our Bluetooth joystick. With these building blocks, Claude was able to write all the code to remote control the robot in a single try, saving us a ton of time and tedious data plumbing!

Surprisingly, this is the opposite of common advice to prompt LLMs for one thing at a time! In contexts unfamiliar to me, Claude often excels at task breakdown. Overly specific requests will work, but much like restricting human advice to a narrow question without giving the overall context and goal, can lead you down a rabbit hole!

### RTFM == Read This For Me

<img src="/img/software/code-with-ai/datasheet.png" width="100%">
*Fig 5. 100 pages of datasheets and user manuals...*

Our motor controller had a 100 page datasheet that was overwhelming and dense - but uploading it to Claude and then asking questions let us quickly resolve one of our issues! Previously that could have been an hour of careful reading and looking up related terms and tutorials.

## Mechanical Sympathy

> "You don't have to be an engineer to be a racing driver, but you do have to have Mechanical Sympathy" 
> 
> Jackie Stewart, 3x Formula One world champion

I started to build up a very good intuition of what kinds of things Claude could get right, and what I should still do myself. Knowing this distinction saved me lots of frustration in both directions.

I learned where I could cut corners: 
- "I'm using a Python library called pygame and ...." becomes just "in pygame..."
- "When I ran your code I got this error message ... what do you think I should do now" becomes just copying in the stack trace.

I learned that transforming or refactoring large chunks of code works great; for instance, adding timing instrumentation between every line. 

On the other hand, I learned that if an LLM can't fix a bug in two tries, it's never going to. It's time to dig in yourself.

I also developed a very good sense of what kinds of mistakes Claude will make. At one point Claude gave us code that looped over `motor1, motor2, motor2, motor4`, missing `motor3`. My friend noticed this and said "oh, this must be a hallucination!" but I could just feel "no way would claude make that mistake" and sure enough when we checked the input, that bug was present in the original code we put into Claude as well.

## Build throw-away tools for yourself

After taking our robot for a spin around the backyard, it spat out a CSV file of GPS coordinates and other data. We wanted to check how accurate this was against ground truth, but I didn't have a great way to view or inspect it.

Previously, figuring out how to view and analyze these GPS coordinates could have taken an hour. We might have even resorted to manual inspection of the GPS coordinates on our phone and trying to compare the numbers by eye.

Instead, I gave Claude the first two rows of the CSV and it generated a web app for us to render an uploaded CSV of GPS coordinates on top of Satellite images!

<img src="/img/software/code-with-ai/gps.png" width="100%">
*Fig 6. The GPS Visualization web app that Claude created for us in a single prompt.*

Having the perfect debugging tools just as I need them instead of relying on print statements or pre-built visualization tools is a total game changer. Software is becoming so cheap that it's disposable!

Overall, these lessons and experience have made me much faster at writing code with AI! Going back to non-AI tools would feel like giving up compilers and writing Assembly by hand.

## Where is this going?

<img src="/img/software/code-with-ai/diagram.png" width="100%">
*Fig 7. Where is this all going?*

Over the last few years, AI's biggest uses in software engineering were Github Copilot for autocomplete within IDEs, and ChatGPT for answering programming questions that used to go to StackOverflow. There were early demos of "Agents" that could operate many steps at a time without human oversight, but nothing that was practical.

This year, all three domains are transforming. IDEs like [Zed](https://zed.dev/), [Cursor](https://cursor.com), and various VSCode extensions have integrated LLMs more deeply to provide better context and tackle larger chunks of code generation. Claude's Artifacts and ChatGPT's Data Analyst have become my go-to solution for quick prototypes and single-use code, instead of Jupyter notebooks. Lastly, a swarm of Agent startups like [Cognition](https://cognition.ai), [Factory](https://factory.ai), and [CodeGen](https://codegen.com) are automating certain slices of the engineering workflow end-to-end.

Personally, I think these three surface areas could converge into a single product - the "AI Engineer''. This will be a single system that can work in a continuum between autonomous and synchronous modes:

1. **Autonomous mode for well-scoped tasks:** The AI will work fully independently, with the ability to write and run code, use external tools, search the web for information, access internal docs, and learn from past mistakes. It will continue iterating on a task until it's done or gets stuck. This will be done for 80% of work.

2. **Pair programming mode for the hardest tasks:** Humans will guide the AI at a high level while it handles the low-level implementation details. Interactions will be highly multimodal, with humans and AIs switching fluidly between text descriptions, visual diagrams, verbal discussions, and directly manipulating each other's code. You might share your screen and have the AI follow along and give you advice and suggestions, or it might share its screen while you give guidance as it drives!

The AI Engineer will have full access to all of the context and knowledge that you have as an employee: it will be hooked up to company knowledge bases, have access to your design files and your customer interview notes, and will seamlessly pull in this information as needed to make decisions, whether operating autonomously or pairing with a human. It will be proactive instead of obsequious: if you suggest a design, it might surface a user interview transcript that suggests a better idea.

The autonomous employee will dispatch cheaper sub-agents for simple and predictable parts of its work, mainly as a way to lower computational cost and latency, in the same way you can skim through a log file without actually reading every word.

While it's hard to predict how future models will perform, I think the AI Engineer will be smarter than most human engineers at specific things, but occasionally lacks common sense or needs to be refocused and guided. Honestly, this isn't too different from how managers and PMs work with engineers today!

## Will we still need engineers?

Before the calculator was invented, accountants spent most of their time literally doing computations. The calculator didn't put them out of jobs, it just elevated them to think at a higher level of abstraction. Accountants still need to know how to do math and understand the computations, but tools like calculators and spreadsheets allow them to provide tremendously more value than they could before!

I do think that AI will lower the bar for anyone to be able to create software, just like anyone can use Excel to do their own personal accounting. This is a good thing! Students will launch full apps and businesses from their dorm rooms; Mom and Pop businesses will create software tools tailored just for them. I want to live in a world where people's creativity is the only bottleneck to what they can create.

<img src="/img/software/code-with-ai/culture.png" width="100%">
*Fig 8. What I hope the future feels like*

Human engineers won't go away. We'll still be needed to drive high-level prioritization, understand the overall architecture and scope of the problem, and review the AI's work, especially as systems get bigger. But we'll spend much more of our time thinking about what to build, and much less on the repetitive "how" of building it. We will finally reach our dream of dealing only with the ["inherent complexity"](https://pressupinc.com/blog/2014/05/root-causes-software-complexity/) of the problem, not the "incidental complexity" of the system's implementation. 

I'm out of my cast and typing with both hands again, but Claude is still writing most of my code. Overall, I've figured out how to get the most out of these new AI tools, and I'm incredibly optimistic about where the industry is going!