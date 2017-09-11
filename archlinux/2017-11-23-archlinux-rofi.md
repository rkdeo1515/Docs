---
layout: post
title: 1. 아치리눅스 i3 설치 (SAWMS)
description: 2017-11-24-archlinux-i3.md
author: EGOTIRP
category: ARCH LINUX
---
![archlinux-logo](https://rkdeo1515.github.io/assets/2017-10-04-1-install-arch-cli/archlinux-logo.png)

# 아치리눅스 rofi 설치

## rofi 설치

```
sudo pacman -S rofi
```
## rofi 설정

설정 샘플 파일 생성 및 편집
```
rofi -dump-xresources > ~/.config/rofi/config
```

```
! "Window width" Set from: Default
rofi.width:                          950
! "Number of lines" Set from: Default
rofi.lines:                          8
! "Number of columns" Set from: Default
rofi.columns:                        1
! "Font to use" Set from: Default
rofi.font:                           NotoMono 11
! "Border width" Set from: Default
rofi.bw:                             3
! "Location on screen" Set from: Default
rofi.location:                       0
! "Padding" Set from: Default
rofi.padding:                        15
! "Whether to load and show icons" Set from: Default
rofi.show-icons:                     true
! "Margin between rows *DEPRECATED*" Set from: Default
rofi.line-margin:                    1
! "Padding within rows *DEPRECATED*" Set from: Default
rofi.line-padding:                   10
! "Separator style (none, dash, solid) *DEPRECATED*" Set from: Default
rofi.separator-style:                solid
! "Hide scroll-bar *DEPRECATED*" Set from: Default
rofi.hide-scrollbar:                 true
! "Fullscreen" Set from: Default
rofi.fullscreen:                     false
! "Click outside the window to exit" Set from: Default
rofi.click-to-exit:                  true
! bg    fg    bg-alt    hl-bg    hl-fg
rofi.color-normal: #282828, #ebdbb2, #282828, #665c54, #fbf1c7
rofi.color-urgent: #cc241d, #282828, #cc241d, #fb4934, #282828
rofi.color-active: #d79921, #282828, #d79921, #fabd2f, #282828
! bg    border    separator
rofi.color-window: #282828, #a89984, #a89984
```

## dmenu와 교체 하기
i3 설정파일 편집
```
nano .config/i3/config
```
```
# bindsym $mod+d exec dmenu_run
bindsym $mod+d exec rofi -show drun
```
