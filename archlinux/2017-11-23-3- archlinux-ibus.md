---
layout: post
title: 1. 아치리눅스 커스텀 셋업
author: EGOTIRP
category: ARCH LINUX
---
![archlinux-logo](https://rkdeo1515.github.io/assets/2017-10-04-1-install-arch-cli/archlinux-logo.png)

# 아치리눅스 ibus 설치 (한글 사용하기)
---

## 1. ibus 설치하기

```
sudo pacman -S ibus ibus-hangul
```

## 2. 초기 설정
아래의 내용을  `.bashrc`에 추가
```
export GTK_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_IM_MODULE=ibus
```
아래의 내용을 `.xinitrc`에 추가
```
ibus-daemon -drx
```
## 3. 언어 설정

터미널에서 `ibus-setup` 을 실행 한 후 `Input Mathod` 탭에서 `English`를 제거 하고 `korean-hangul` 를 추가해 준다.
