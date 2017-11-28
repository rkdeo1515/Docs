---
layout: post
title: 1. 아치리눅스 i3 설치 (SAWMS)
description: 2017-11-24-archlinux-i3.md
author: EGOTIRP
category: ARCH LINUX
---
![archlinux-logo](https://rkdeo1515.github.io/assets/2017-10-04-1-install-arch-cli/archlinux-logo.png)

# 아치리눅스 i3 설치

## 1. Xorg 설치하기
```
sudo pacman -S xorg-server xorg-xinit
```
```
cp /etc/X11/xinit/xinitrc .xinitrc
```

## i3-gaps 설치

```
git clone https://aur.archlinux.org/i3-gaps-git.git
```
```
cd i3-gaps-git
makepkg -si
sudo pacman -U i3-gaps
```

```
git clone https://aur.archlinux.org/i3blocks-git.git
```
```
cd i3blocks-gaps-git
makepkg -si
sudo pacman -U i3block-gaps
```

## 터미널
```
sudo pacman -S termite
```
## 배경 화면 설정하기
`feh` 다운로드
```
sudo pacman -S feh
```
배경 화면 설정
```
feh --bg-scale /path/to/image.file
```
자동 실행 스크립트
```
~/.fehbg &
```
