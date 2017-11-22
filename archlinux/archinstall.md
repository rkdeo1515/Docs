---
layout: post
title: "1. ARCH LINUX 설치하기 "
author: EGOTIRP
category: ARCH LINUX
---

![archlinux-logo](https://rkdeo1515.github.io/assets/2017-10-04-1-install-arch-cli/archlinux-logo.png)

## 1. 설치 준비 단계
### 1-1. 이미지 파일 다운로드
아래의 링크에서 ArchLinux 이미지 파일을 다운로드합니다. 그리고 다운받은 이미지를 이용해 부팅 USB를 만들어 줍니다.

[[아치리눅스 다운로드]](https://www.archlinux.org/download/)
### 1-2. 키보드 레이아웃 설정
드
`loadkeys` 명령으로 설정합니다. 기본값은 US로 설정되어 있습니다. `/usr/share/kbd/keymaps/` 목록에서 필요한 키맵을 찾아 쓸 수 있지만, ARCH는 한국어를 공식적으로 지원하지 않기 때문에 디폴트 상태로 두고 건너 뜁니다.

### 1-3. 디스크 파티션 설정
`/sys/firmware/efi/efivars` 디렉토리 내부에 파일들이 존재한다면 UEFI/GPT, 없다면 BIOS/MBR 방식으로 작업을 합니다.

UEFI/GPT 파티션 레이아웃 예제

| Mount point | Partition | Partition type (GUID) | Bootable flag | 	Suggested size |
|:---|:---:|:---:|:---:|---:|
| /boot | sdx1 | EFI System | Yes | 260–512 MiB |
| / | sdx2 | Linux | No  | Remainder of the device |
| SWAP  | sdx3 | Linux swap | No  | More than 512 MiB |

BIOS/MBR 파티션 레이아웃 예제

| Mount point | Partition | Partition type (GUID) | Bootable flag | 	Suggested size |
|:---|:---:|:---:|:---:|---:|
| / | sdx1 | Linux | No  | Remainder of the device |
| SWAP  | sdx2 | Linux swap | No  | More than 512 MiB |

### 1-4. 파티션 포맷
부트 영역은 FAT32로 포맷 해주시고, 루트 영역은 ext4, 그리고 SWAP 영역은 SWAP으로 설정해 주시면 됩니다.

```
mkfs.fat -F32 /dev/sda1
mkfs.ext4 /dev/sda2
mkswap /dev/sda3
swapon /dev/sda3
```

### 1-5. 파티션 마운트
루트 파티션을 `/mnt`에 마운트 합니다.
```
mount /dev/sda2 /mnt
```

부트 파티션을 `/mnt/boot`에 마운트 합니다.
```
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot
```

### 1-6. 네트워크 연결하기
유선 인터넷의 경우 자동으로 연결되지만, 무선 인터넷의 경우 `wifi_menu`를 이용해서 와이파이에 연결 해줍니다.

## 2. 설치하기

### 2-1. 미러 사이트 추가
South Korea 미러 서버 목록을  `/etc/pacman.d/mirrorlist`파일의 내용에 추가합니다. (# 주석 해제 하는거 잊지 말기!)

[[Archlinux Mirrorlist Generator]](https://www.archlinux.org/mirrorlist/)

### 2-2. 기본 시스템 설치
pacstrap을 이용해 새로 만든 파티션에 시스템을 설치 합니다.

* `base` : Arch Linux 기본 시스템
* `base-devel` : 패키지 빌드에 필요한 도구 포함
* `networkmanager` : 네트워크 연결 관리자

```
pacstrap /mnt base base-devel networkmanager
```

## 3. 시스템 세팅

### 3-1. fstab 생성

새로 설치한 시스템의 fstab를 생성합니다.
```
genfstab -p /mnt >> /mnt/etc/fstab
```

### 3-2. 미러리스트 복사

수정된 pacman 미러리스트를 새로 설치된 시스템에 복사합니다.
```
cp /etc/pacman.d/mirrorlist /mnt/etc/pacman.d/mirrorlist
```

### 3-3. 새로 설치한 시스템 진입
새로 설치한 시스템에 chroot로 진입 합니다.
```
arch-chroot /mnt
```

### 3-4. 호스트 네임 설정
컴퓨터의 호스트네임을 설정합니다.
```
echo [호스트네임] > /etc/hostname
```

### 3-5. 시간 설정
타임존을 서울로 설정합니다.
```
ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

### 3-6. 네트워크 설정
무선 네트워크 사용시, `nm-cli`를 사용하여 네트워크 연결합니다.

* 검색 : `nm-cli dev wifi`
* 연결 : `nm-cli dev wifi connect [ssid] password [password]`

그리고 DHCP를 활성화 해줍니다.
```
systemctl enable dhcpcd
systemctl start dhcpcd
```

### 3-7. 램디스크 생성
초기 램 디스크를 만듭니다.
```
mkinitcpio -p linux
```

### 3-8. 루트 비밀번호 재설정
`passwd`로 루트 비밀번호를 재설정해주세요.

### 3-9. 사용자 계정 생성
```
useradd -m -G wheel -S /bin/bash [유저이름]    # 유저 생성
passwd [유저이름]    # 유저 암호 설정
visudo    # wheel 그룹 주석 해제
```

### 3-10. 부트로더 설치
pacman을 이용해 부트로더 grub과 UEFI 펌웨어 변수를 수정하는 도구인 efibootmgr 그리고 인텔 CPU를 사용한다면 intel-ucode를 설치 합니다.
```
pacman -Syu
pacman -S grub efibootmgr intel-ucode
```
새로 설치한 시스템에 grub 부트로더를 설치합니다.
```
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub
grub-mkconfig -o /boot/grub/grub.cfg
cp -r /boot/EFI/grub /boot/EFI/boot
mv /boot/EFI/boot/grubx64.efi /boot/EFI/boot/bootx64.efi
```

### 3-11. 재부팅
`exit`를 입력하거나 `Ctrl+D`로 chroot를 해제 해줍니다.

마운트된 파티션을 전부 해제 해줍니다.
```
umount -R /mnt
```

재부팅을 해줍니다.
