# did
Digital Information Display : 학교 복도용 전자게시판 프로그램
<pre>did3.py : Python 3.X 및 별도 클라우드 클라이언트 사용
did2.py : Python 2.X 및 별도 클라우드 클라이언트 사용
* overGrive라는 클라이언트를 구입하여 활용해 보았으나 안정성이 좋지 않음
dbx_did2.py : Python 2.X 및 드롭박스 API v2를 사용하여 통합 설계중이나 아직 연구중인 단계
rclone_did2.py : Python 2.X 및 rclone 클라이언트 사용
* rclone 클라이언트는 안정적으로 동작하며 sudo apt-get install rclone 명령으로 간단하게 설치됨</pre>

# 준비물
<pre>1. Win32DiskImager(https://sourceforge.net/projects/win32diskimager/)</pre>
1. 기본 설정
- 키보드 Asia/Seoul
- SSH, VNC 활성화

2. 네트워크 설정
- sudo nano /etc/dhcpcd.conf
- IP주소 입력

3. 한글폰트 설치
- sudo apt-get install fonts-unfonts-core

4. 파이썬 라이브러리 설치
sudo apt-get install python-imaging-tk

5. rclone 설치 / 설정
- curl https://rclone.org/install.sh | sudo bash
- mkdir did
- rclone config
- rclone sync hongikdid: ~/did

6. 프로그램 테스트
- python ~/did/rclone_did2.py

7. 자동실행 설정
sudo nano ~/did.sh
sudo nano ~/.config/lxsession/LXDE-pi/autostart

8. 화면보호기 설정
- sudo apt-get install xscreensaver
- 실행하여 화면보호기 끄기

9. 자동종료 설정
- sudo crontab -e

10. 암호 바꾸기
- sudo passwd

11. 기타
- 블투, 무선랜, 소리 끄기
