---
layout: post
title:  "Refinance your Tech Debt"
date:   2021-12-07 12:00:00 -0700
thumbnail: '/img/software/refinance/thumb.jpg'
background: '/img/software/refinance/thumb.jpg'
category: software
---

<h3>Credit Card Tech Debt vs Mortgage Tech Debt</h3>
_People online talk about "tech debt" as a universal evil that heroic engineers must fight against Product to prevent, but just like real debt, the story is more complicated._
<h3>Tech Debt</h3>
Technical Debt is the idea of reducing work now to finish a project sooner, in a way that will create more total work later. This can occur in many different flavors — cutting quality corners, not writing any tests, or solving only a subset of the problem you know you'll eventually need to solve. Creating tech debt comes with a few different dimensions that need to be compared:
<ol>
 	<li>The benefit. What will we gain by finishing this project earlier? Does an important customer deal hang in the balance? Will we learn more about product market fit months earlier? Will we just increase our short term velocity?</li>
 	<li>The payback. What work does this create for us in the future, and how much bigger is the total work vs just doing it properly the first time?
<p style="font-family: Courier New,monospace; background-color: #eeeeee; padding: 5px; display: inline-block; font-size: 16px;">cost(shortcut) + cost(later fix) - benefit(shortcut) &gt; cost(doing it right)?</p>
</li>
 	<li>The Interest Rate. Just like real debt, technical debt has an interest rate that makes it grow until you pay it back, and if you're unlucky, the interest payments will MASSIVELY outweigh the original debt.</li>
</ol>
Benefit and Payback are the easiest to think about, but actually it's the Interest Rate that is the greatest risk of tech debt.

<img src="/img/software/refinance/einstein.png" alt="" width="100%" />
_Fig 1. Einstein's thoughts on Tech Debt_

<h3>Credit Card Debt vs Mortgages</h3>
There's a massive difference between having $500k of credit card debt and having a $500k mortgage, because of how much interest you'll need to pay. Credit cards can have interest rates as high as 20%, and the worst pieces of tech debt will be just as bad.

Let's say you built a brittle product with no tests to get it out the door, and plan to rewrite it a year later when the team has bandwidth. Your cost isn't JUST
<span style="font-family: Courier New,monospace; background-color: #eeeeee; padding: 5px; display: inline-block; font-size: 16px;">initial_work + fixup</span>
Instead, it's:

<span style="font-family: Courier New,monospace; background-color: #eeeeee; padding: 5px; display: inline-block; font-size: 16px;">initial_work + <strong>bugs_and_friction_from_tech_debt</strong> + fixup</span>

In the year until you fix the original tech debt, every new bug caused by the brittle solution and all the extra manual testing that engineers will do because there are no automated tests is part of the true cost of that tech debt. Pretty soon you'll find that each sprint a big chunk of your engineering velocity is just going into "interest payments" caused by that initial tech debt, and over the year your total work may end up being 2-10x more than doing it right the first time. This is "Credit Card Tech Debt".

<img src="/img/software/refinance/TDblog-Escalator2.gif" alt="" width="100%" />
_Fig 2. Trying to pay back high-interest tech debt_

Now, not all tech debt has to be like that, just like not all debt is credit card debt. Let's say your product eventually needs to support millions of users, but to start you build a solution that will only support thousands. You build your solution in ½ the time the full solution would take, but you'll need to fully rewrite it a few years later when your business scales. This IS still tech debt — your total work will be 1.5x higher than if you built the full solution from the beginning. But as long as the "interest rate" on this is low, it won't balloon out of control. This is "Mortgage Tech Debt".

<img src="/img/software/refinance/TDblog-Remax-394x500.jpg" alt="" width="100%" />
_Fig 3. Finding low interest tech debt_
<h3>When to choose Tech Debt?</h3>
Now you might be wondering why you should ever choose to create tech debt, when even the good example still created 1.5x more work than "doing it right the first time". The answer is that work is more valuable today than will be tomorrow.
<ol>
 	<li>Disappearing opportunity. This could be a big deal that's hinging on a new feature, or demonstrating a milestone before the next fundraise. This is the most common reason to choose tech debt, but you need to be careful that the tradeoff is real. False Urgency is common in sales, and product teams need to be careful of the line where motivation for speed starts to create unnecessary tech debt.</li>
 	<li>Uncertainty. Especially for startups, the first version of a product is inherently an experiment with high uncertainty. You may want to take the extra time to build a backend that can support millions from day 1, but if you need to pivot before getting to millions of users, you'll be throwing out your work anyway. This is the argument that the first version of your product should always be a prototype, because you don't actually know what your real "requirements" will be until it's in the hands of your users.</li>
 	<li>Time discounting. An hour of time today is worth way more than an hour a few years from now. If your company is growing in size, you'll have more resources to throw at the problem. Even if your team size isn't going to change, it will be more experienced, and will better understand the problem. This is especially true in VC backed startups — as valuations grow, every dollar becomes exponentially "cheaper" in terms of how much equity was bought for it.</li>
 	<li>Live in your house while paying for it. A mortgage lets you live in your house while you pay for it over 20-30 years — much more pleasant than staying in that tiny studio in SF for another 20-30 years before you can buy a house. Low interest tech debt can let you do the same thing — be in the market learning about your customers months or years earlier than you could have otherwise, while slowly paying back the debt.</li>
</ol>
<h3>Paying back Tech Debt</h3>
It's important to make time in engineering sprints to pay back tech debt before it spirals out of control. When deciding how much to pay back which parts to pay back, focus on the Interest Rate. Mortgage Tech Debt might be ugly and get complaints from the team, but dig in to really understand if it's adding cost each sprint.
<ul>
 	<li>That one ugly service that works, but is written in PHP? If no one's had to touch it in a year it can probably wait another year.</li>
 	<li>That part of the code that breaks almost every release? That's Credit Card Tech Debt. Pay it back soon, or you're going to be paying more and more interest.</li>
 	<li>Part of the code with only manual tests? If engineers are working on it frequently and spending an hour each week DOING those manual tests, it's probably worth automating.</li>
 	<li>Part of the code that's slow or won't scale? Work with product to decide WHEN that will become a bottleneck to your company.</li>
</ul>
With careful design, choosing the right kinds of tech debt to take on can help your engineering team gain a meaningful headstart without creating an ongoing cost. Tech debt needs to be carefully watched and paid down, to keep engineering velocity high. If you want to join a team that takes tech debt seriously and cares about its engineers, <a href="https://www.cobaltrobotics.com/culture-careers/">Cobalt Robotics is hiring!</a>

<img src="/img/software/high-stakes/cobalt.gif" width="100%"/>

([Cross post from Cobalt's Blog](https://www.cobaltrobotics.com/blog/))