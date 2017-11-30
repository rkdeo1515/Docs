---
layout: post
title: 1. 아치리눅스 네트워크 시간 동기화 (systemd-timesyncd)
author: EGOTIRP
category: ARCH LINUX
---
![archlinux-logo](https://rkdeo1515.github.io/assets/2017-10-04-1-install-arch-cli/archlinux-logo.png)

# 아치리눅스 네트워크 시간 동기화 (systemd-timesyncd)
---

## 1. timesyncd 설정 편집
설정 편집
```
sudo nano /etc/systemd/timesyncd.conf
```
```
[Time]
NTP=0.arch.pool.ntp.org 1.arch.pool.ntp.org 2.arch.pool.ntp.org 3.arch.pool.ntp.org
FallbackNTP=0.pool.ntp.org 1.pool.ntp.org 0.fr.pool.ntp.org
```
## 2. NTP 기능 켜기
 ```
 sudo timedatectl set-ntp true
 ```
