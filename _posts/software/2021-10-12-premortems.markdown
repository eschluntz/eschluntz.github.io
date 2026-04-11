---
layout: post
title:  "Premortems Will Keep Your Code Alive"
date:   2021-10-12 12:00:00 -0700
thumbnail: '/img/software/premortem/thumb.jpg'
background: '/img/software/premortem/inconceivable.png'
category: software
---
<h1>Premortems and Postmortems</h1>
_Two crucial tools for writing code when the stakes are high, like managing our fleet of over 100 robots at <a href="https://www.cobaltrobotics.com/">Cobalt Robotics</a>. This is part 2 of a 2 part series on High Stakes Code. See <a href="https://www.cobaltrobotics.com/writing-high-stakes-code-at-a-startup/">Part 1.</a>_
<h3>Premortems</h3>
<a href="https://en.wikipedia.org/wiki/Pre-mortem#:~:text=A%20pre%2Dmortem%2C%20or%20premortem,of%20the%20project%20or%20organization.">Premortems</a> are remarkably quick, and have saved my team from making bad mistakes many times. What’s a premortem? Before deploying new code, ask yourself and at least one other person "If this is going to cause a major issue, what would it be?" Then, ask yourselves what you could do to protect yourself better. That could include doing additional testing or adding safeguards before deploying the code.

No one intentionally releases code that they think is going to cause major problems, so the author of code about to go out will think that it's safe. The benefit of the premortem is to stretch your mind outside of the mental box you've created where your code is safe, and then look around from that perspective.

We've found premortems particularly good at discovering "unknown unknowns" and issues that occur when moving from a test environment to a production environment. Will that database upgrade be just as quick when the database is under load? Will that new safety feature have disruptive false positives? Is every robot starting from the same state for this update?

Part of the magic of a premortem is it gets the team to discuss worst case scenarios, <a href="https://www.mckinsey.com/business-functions/strategy-and-corporate-finance/our-insights/bias-busters-premortems-being-smart-at-the-start">despite any over-optimism or the planning fallacy</a> about the feature itself. It creates a safe space to bring up issues, without being seen as negative, obstructionist, or not committed to the goal.

<img src="/img/software/premortem/inconceivable_10-10-21-1024x354.jpg" alt="The Princess Bride meme" width="100%"/>
_Fig 1. Vizzini never did premortems and look what happened to him_
<h3>Postmortems</h3>
Postmortems are the sadder, but even more useful, version of premortems. The idea here is that when you do have a failure, you want to learn absolutely as much from it as you can. Think about how much you'll need to learn about your situation to truly write a failure proof system - if you learn twice as much from each failure, then you'll need half as many failures to get there!

Huge amounts have been written about good postmortems, <a href="https://sre.google/workbook/postmortem-culture/">most notably Google's SRE book.</a> I won't go through the details of how to write a postmortem, but instead focus on what makes a good postmortem.
<h4>BLAMELESS</h4>
Humans are going to make mistakes. At the end of the day, what matters is setting up a process to catch and prevent those errors, not which human made the mistake. This takes a strong culture to do well, but there are little tactical things you can do that help. For instance, never name names in postmortems. Instead of "at 1am <strong>Erik</strong> rebooted the database" write "at 1am <strong>an engineer</strong> rebooted the database". If you don't make your postmortems blameless, people will hide details and try to cover up their mistakes in the future. If people cover up mistakes, your team isn't going to learn from them and someone is going to make the same mistake again.
<h4>ACTION ITEMS</h4>
Action items (AIs) are the silver lining of your incident—and the entire point of the postmortem—so make sure you mine as many valuable ones out of the wreckage of your code while they're fresh. Ask "why" 5 times for any problem to go down into not just the immediate problem, but how it came to exist in the root cause. The deeper you mine, the more valuable the action items become. For instance, the top level AI might be "fix this bug on line 237", but 4 levels down the AI might be "we could have caught this by adding a stress test to our CI". Any one "problem" can help you uncover a number of valuable action items for your team to work on.
<table>
<tbody style="background-color: #f5f5f5;">
<tr>
<td style="padding: 12px; border: 1px solid #000000; text-align: center;"><strong>Level</strong></td>
<td style="padding: 12px; border: 1px solid #000000; text-align: center;"><strong>"Why?" to row above</strong></td>
<td style="padding: 12px; border: 1px solid #000000; text-align: center;"><strong>Action Item</strong></td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #000000; text-align: center;">1</td>
<td style="padding: 12px; border: 1px solid #000000;">System ran out of memory</td>
<td style="padding: 12px; border: 1px solid #000000;">Add memory monitor</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #000000; text-align: center;">2</td>
<td style="padding: 12px; border: 1px solid #000000;">Bug on line 237</td>
<td style="padding: 12px; border: 1px solid #000000;">Fix memory leak bug</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #000000; text-align: center;">3</td>
<td style="padding: 12px; border: 1px solid #000000;">Easy to make this kind of bug</td>
<td style="padding: 12px; border: 1px solid #000000;">Refactor library</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #000000; text-align: center;">4</td>
<td style="padding: 12px; border: 1px solid #000000;">Difficult to review for this kind of bug</td>
<td style="padding: 12px; border: 1px solid #000000;">Add stress tests to CI</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #000000; text-align: center;">5</td>
<td style="padding: 12px; border: 1px solid #000000;">Little known topic</td>
<td style="padding: 12px; border: 1px solid #000000;">Lunch 'n Learn on memory</td>
</tr>
</tbody>
</table>
_Fig 2. Example of "5 Whys" digging into the root cause of a problem_

<h4>LOOK BROADLY</h4>
Don't just brainstorm around the specific bug that hurt you - look more broadly for "things that went poorly" and "things that went well". Even if something wasn't directly responsible for the incident, such as "it took us too long to find the logs for this issue" you can still find valuable action items there. Noting "things that went well" can help you identify strengths that you can double down on as a team.

<img src="/img/software/premortem/miners_10-10-21-500x404.jpg" alt="Miners" width="100%"/>
_Fig 3. Engineers mining for action items in the aftermath of an incident_

<h3>Premortems and Postmortems at Cobalt Robotics</h3>
At Cobalt, we build autonomous indoor security guard robots that patrol through office buildings and warehouses looking for anything out of the ordinary. We write code that controls a 120lb robot navigating around people - basically an indoor self driving car, and our customers are relying on us to keep their most sensitive areas secure and protected. We're committed to keeping a great engineering culture, moving fast, and NOT breaking things. To do that <a href="https://www.cobaltrobotics.com/culture-careers/">we need great engineers like you!</a>

<img src="/img/software/high-stakes/cobalt.gif" width="100%"/>
_Fig 4. A Cobalt Robot patrolling an office space_

([Cross post from Cobalt's Blog](https://www.cobaltrobotics.com/blog/))