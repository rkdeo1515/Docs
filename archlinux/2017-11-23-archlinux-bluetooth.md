---
layout: post
title: 1. 아치리눅스 블루투스 마우스 사용하기  (Bluez)
description: 2017-11-24-archlinux-bluetooth.md
author: EGOTIRP
category: ARCH LINUX
---
![archlinux-logo](https://rkdeo1515.github.io/assets/2017-10-04-1-install-arch-cli/archlinux-logo.png)

# 아치리눅스 Bluetooth 설치 (Bluez)
---
## 1. Bluez 설치하기
```
sudo pacman -S bluez bluez-utils
```

블루투스 드라이버 로드
```
modprobe btusb
```

## 2. 연결 하기

```
sudo systemctl start bluetooth.service
```

```
bluetoothctl
```

```
# bluetoothctl
[bluetooth]# list
Controller <controller mac> BlueZ 5.5 [default]
[bluetooth]# select <controller mac>
[bluetooth]# power on
[bluetooth]# scan on
[bluetooth]# agent on
[bluetooth]# devices
Device <mouse mac> Name: Bluetooth Mouse
[bluetooth]# pair <mouse mac>
[bluetooth]# trust <mouse mac>
[bluetooth]# connect <mouse mac>
```

## 3. 자동 설정

```
sudo systemctl enable bluetooth.service
```

```
/etc/bluetooth/main.conf

[Policy]
AutoEnable=true
```
