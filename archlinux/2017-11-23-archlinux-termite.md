---
layout: post
title: 아치리눅스 터미널 에뮬레이터 설치 ( termite )
author: EGOTIRP
category: ARCH LINUX
---
![archlinux-logo](https://rkdeo1515.github.io/assets/2017-10-04-1-install-arch-cli/archlinux-logo.png)

# 아치리눅스 터미널 에뮬레이터 설치 ( termite )
---

## termite 설치

설치
```
sudo pacman -S termite
```

## termite 설치

설정 파일 복사
```
 cp -r /etc/xdg/termite .config/
```

폰트 설정
```
[options]
font = Noto Mono 10
```

컬러 설정
```
[colors]
#cursor = #dcdccc
#cursor_foreground = #dcdccc
foreground = #dcdccc
foreground_bold = #ffffff
background = #3f3f3f

# 20% background transparency (requires a compositor)
#background = rgba(63, 63, 63, 0.8)

# if unset, will reverse foreground and background
highlight = #2f2f2f

# colors from color0 to color254 can be set
color0 = #3f3f3f
color1 = #705050
color2 = #60b48a
color3 = #dfaf8f
color4 = #506070
color5 = #dc8cc3
color6 = #8cd0d3
color7 = #dcdccc
color8 = #709080
color9 = #dca3a3
color10 = #c3bf9f
color11 = #f0dfaf
color12 = #94bff3
color13 = #ec93d3
color14 = #93e0e3
color15 = #ffffff
```
