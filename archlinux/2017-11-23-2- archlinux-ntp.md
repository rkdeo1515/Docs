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
NTP 서버 리스트 주석 해제
```
sudo nano /etc/systemd/timesyncd.conl
```

## 2. NTP 기능 켜기
 ```
 sudo timedatectl set-ntp true
 ```
