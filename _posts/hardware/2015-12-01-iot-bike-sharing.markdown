---
layout: post
title:  "IoT-enabled Bike Sharing"
date:   2015-12-01 00:00:00 -0700
thumbnail: '/img/hardware/Bike_lock_cover_3.jpg'
category: hardware
---
For our CS244r final project we built a smart bike lock and an iPhone app that allowed users to rent out their own bike, or to rent other people's bikes. Our server generated Time-expiring One Time Passwords (TOTP) that were passed to the phone, and then to the lock over BLE if a user has permission to rent the bike. We focused on security / encryption to ensure that malicious users could not unlock a bike when they were not supposed to through replay attacks.