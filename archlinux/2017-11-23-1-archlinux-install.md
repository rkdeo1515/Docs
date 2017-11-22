---
layout: post
title: "1. 아치리눅스 설치하기(UEFI)) "
author: EGOTIRP
category: ARCH LINUX
---
![archlinux-logo](https://rkdeo1515.github.io/assets/2017-10-04-1-install-arch-cli/archlinux-logo.png)

# 아치리눅스 설치하기 ( UEFI )
---

## 1. 설치 준비 단계

### 1-1. 이미지 파일 다운로드
부팅용 이미지 파일을 다운로드한다. 그리고 다운받은 이미지를 이용해 라이브 부팅용 USB를 만들어 준다.

[[아치리눅스 다운로드]](https://www.archlinux.org/download/)

### 1-2. 키보드 레이아웃 설정

키맵은 `/usr/share/kbd/keymaps/` 에서 찾을 수 있다. (기본값은 US)
```
loadkeys us
```
### 1-2 디스크 부팅 모드 확인 하기
디렉토리 내부에 파일들이 존재하는지 확인한다.
```
ls /sys/firmware/efi/efivars
```

### 1-3. 디스크 파티션 설정
gdisk를 이용해서 수동으로 파티션을 잡아준다.
```
gdisk /dev/sda
```

| Mount point | Partition | Partition type (GUID) | Bootable flag | 	Suggested size |
|:---|:---:|:---:|:---:|---:|
| /boot | sdx1 | EFI System | Yes | 260–512 MiB |
| / | sdx2 | Linux | No  | Remainder of the device |
| SWAP  | sdx3 | Linux swap | No  | More than 512 MiB |

### 1-4. 파티션 포맷
`boot`, `/`, `swap` 파티션을 각각 `fat32`, `ext4`, `swap` 으로 포맷 해준다.
```
mkfs.fat -F32 /dev/sda1
mkfs.ext4 /dev/sda2
mkswap /dev/sda3
swapon /dev/sda3
```

### 1-5. 파티션 마운트

`/` 파티션을 `/mnt`에 마운트 하고, `boot` 파티션을 `/mnt/boot`에 마운트 해준다.
```
mount /dev/sda2 /mnt
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot
```

### 1-6. 네트워크 연결하기
유선의 경우 자동으로 연결되지만, 무선 네트워크 사용시  수동 연결
```
wifimenu
```

## 2. 설치하기

### 2-1. 미러 사이트 추가
South Korea 미러리스트를 추가한다. (# 주석 해제 하는거 잊지 말기!)

[[Archlinux Mirrorlist Generator]](https://www.archlinux.org/mirrorlist/)
```
`/etc/pacman.d/mirrorlist
```

### 2-2. 기본 시스템 설치
pacstrap을 이용해 새로 만든 파티션에 시스템을 설치 합니다.

* `base` : 아치 리눅스 기본 시스템
* `base-devel` : 패키지 빌드에 필요한 도구 포함

```
pacstrap /mnt base base-devel
```

### 3-1. fstab 생성

새로 설치한 시스템의 fstab를 생성한다.
```
genfstab -p /mnt >> /mnt/etc/fstab
```

### 3-2. 미러리스트 복사

수정된 pacman 미러리스트를 새로 설치된 시스템에 복사한다.
```
cp /etc/pacman.d/mirrorlist /mnt/etc/pacman.d/mirrorlist
```

### 3-3. 새로 설치한 시스템 진입
새로 설치한 시스템으로 chroot 한다.
```
arch-chroot /mnt
```

### 3-4. 호스트 네임 설정
호스트네임을 설정한다.
```
echo [호스트네임] > /etc/hostname
```

### 3-5. 시간 설정
타임존을 서울로 설정한다.
```
ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

### 3-6. 네트워크 설정(wifi 사용시)
`networkmanager` 설치

```
pacman -S networkmanager
```

 `nm-cli`를 사용하여 네트워크 연결한다.

```
nm-cli dev wifi
nm-cli dev wifi connect [ssid] password [password]
```

DHCP를 활성화 해줍니다.
```
systemctl enable dhcpcd
systemctl start dhcpcd
```

### 3-7. 램디스크 생성
초기 램디스크를 생성한다..
```
mkinitcpio -p linux
```

### 3-8. 루트 비밀번호 재설정
루트 비밀번호 설정.
```
passwd
```

### 3-9. 사용자 계정 생성
```
useradd -m -G wheel -S /bin/bash [유저이름]
passwd [유저이름]
```
sudo를 사용하려면 `visudo`를 통해 wheel 그룹 주석해제
```
visudo
```

### 3-10. 부트로더 설치
`grub`과 `efibootmgr` 설치, 인텔 cpu 사용시 `intel-ucode` 설치
```
pacman -Syu
pacman -S grub efibootmgr intel-ucode

grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub
grub-mkconfig -o /boot/grub/grub.cfg
cp -r /boot/EFI/grub /boot/EFI/boot
mv /boot/EFI/boot/grubx64.efi /boot/EFI/boot/bootx64.efi
```

### 3-11. 재부팅
`exit`를 입력하거나 `Ctrl+D`로 chroot를 해제 한 후 파티션 마운트 해제 하고 재부팅을 한다.
```
umount -R /mnt
reboot
```
