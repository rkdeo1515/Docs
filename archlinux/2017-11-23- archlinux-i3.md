---
layout: post
title: 1. 아치리눅스 독립형 윈도우 매니저 시스템 설치 (i3-gaps)
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

aur 패키지 다운로드
```
git clone https://aur.archlinux.org/i3-gaps-git.git
```
패키지 설치
```
cd i3-gaps-git
makepkg -si
sudo pacman -U i3-gaps
```

## i3-gaps 설정

설정 파일 복사
```
cp /etc/i3/config .config/i3/config
```
config 파일 내용 추가
```
# ==============================
# settings for i3-gaps - https://github.com/Airblader/i3
# ==============================

# Disable window titlebars entirely
for_window [class="^.*"] border pixel 3

# Set inner/outer gaps
gaps inner 10
gaps outer 5

# Additionally, you can issue commands with the following syntax. This is useful to bind keys to changing the gap size.
# gaps inner|outer current|all set|plus|minus <px>
# gaps inner all set 10
# gaps outer all plus 5

# Smart gaps (gaps used if only more than one container on the workspace)
# smart_gaps on

# Smart borders (draw borders around container only if it is not the only container on this workspace)
# on|no_gaps (on=always activate and no_gaps=only activate if the gap size to the edge of the screen is 0)
smart_borders on

# Press $mod+Shift+g to enter the gap mode. Choose o or i for modifying outer/inner gaps. Press one of + / - (in-/decrement for current workspace) or 0 (remove gaps for current workspace). If you also press Shift with these keys, the change will be global for all workspaces.
set $mode_gaps Gaps: (o) outer, (i) inner
set $mode_gaps_outer Outer Gaps: +|-|0 (local), Shift + +|-|0 (global)
set $mode_gaps_inner Inner Gaps: +|-|0 (local), Shift + +|-|0 (global)
bindsym $mod+Shift+g mode "$mode_gaps"
mode "$mode_gaps" {
        bindsym o      mode "$mode_gaps_outer"
        bindsym i      mode "$mode_gaps_inner"
        bindsym Return mode "default"
        bindsym Escape mode "default"
}

mode "$mode_gaps_inner" {
        bindsym plus  gaps inner current plus 5
        bindsym minus gaps inner current minus 5
        bindsym 0     gaps inner current set 0

        bindsym Shift+plus  gaps inner all plus 5
        bindsym Shift+minus gaps inner all minus 5
        bindsym Shift+0     gaps inner all set 0

        bindsym Return mode "default"
        bindsym Escape mode "default"
}
mode "$mode_gaps_outer" {
        bindsym plus  gaps outer current plus 5
        bindsym minus gaps outer current minus 5
        bindsym 0     gaps outer current set 0

        bindsym Shift+plus  gaps outer all plus 5
        bindsym Shift+minus gaps outer all minus 5
        bindsym Shift+0     gaps outer all set 0

        bindsym Return mode "default"
        bindsym Escape mode "default"
}
```
## i3blocks-gaps 설치
aur 패키지 다운로드
```
git clone https://aur.archlinux.org/i3blocks-git.git
```
패키지 설치
```
cd i3blocks-gaps-git
makepkg -si
sudo pacman -U i3block-gaps
```
## i3blocks-gaps 설정
설정 파일 복사
```
cp /etc/i3blocks.conf ~/.config/i3/i3blocks.config
```
i3 config파일 수정
```
bar {
        # status_command i3status
        status_command i3blocks
}
```
## i3 컬러 설정

기본값
```
# class                 border  backgr. text    indicator child_border
client.focused          #4c7899 #285577 #ffffff #2e9ef4   #285577
client.focused_inactive #333333 #5f676a #ffffff #484e50   #5f676a
client.unfocused        #333333 #222222 #888888 #292d2e   #222222
client.urgent           #2f343a #900000 #ffffff #900000   #900000
client.placeholder      #000000 #0c0c0c #ffffff #000000   #0c0c0c

client.background       #ffffff
```

## i3bar

기본값
```
bar {
    colors {
        background #000000
        statusline #ffffff
        separator #666666

        # <colorclass> <border> <background> <text>
        focused_workspace  #4c7899 #285577 #ffffff
        active_workspace   #333333 #5f676a #ffffff
        inactive_workspace #333333 #222222 #888888
        urgent_workspace   #2f343a #900000 #ffffff
        binding_mode       #2f343a #900000 #ffffff
        }
}
```
