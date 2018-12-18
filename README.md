# did
Digital Information Display : 학교 복도용 전자게시판 프로그램
<pre>did3.py : Python 3.X 및 별도 클라우드 클라이언트 사용
did2.py : Python 2.X 및 별도 클라우드 클라이언트 사용
* overGrive라는 클라이언트를 구입하여 활용해 보았으나 안정성이 좋지 않음
dbx_did2.py : Python 2.X 및 드롭박스 API v2를 사용하여 통합 설계중이나 아직 연구중인 단계
rclone_did2.py : Python 2.X 및 rclone 클라이언트 사용
did2_off_omx.py : Python 2.X 및 omxplayer 프로그램으로 동영상 재생, 오프라인
did2_rclone_omx : Python 2.X 및 rclone 클라이언트 사용, omxplayer 프로그램으로 동영상 재생
did_rclone_omx_time : Python 2.X 및 3.X에서 동작하며 하단에 시간과 날짜가 표시됨
did_core : Python 3.X에서 동작하는 수업용 핵심 코드</pre>

# hardware
<pre>1. 라즈베리파이
2. SDHC 메모리카드(8GB 이상)
3. HDMI 케이블
4. Micro USB 케이블
5. 키보드와 마우스</pre>

# software
<pre>1. Raspbian with Desktop(https://www.raspberrypi.org/downloads/raspbian/)
2. Etcher(https://etcher.io/)
3. VNC Viewer(https://www.realvnc.com/en/connect/download/viewer/)</pre>

# install
1. 기본 설정
<pre>키보드 Asia/Seoul
SSH, VNC 활성화</pre>

2. 네트워크 설정
<pre>sudo nano /etc/dhcpcd.conf
IP주소 입력</pre>

3. 한글폰트 설치
<pre>sudo apt-get install fonts-unfonts-core</pre>

4. 파이썬 라이브러리 설치
<pre>sudo apt-get install python-imaging-tk</pre>

5. rclone 설치 / 설정
<pre>sudo apt-get install rclone
mkdir did
cd did
rclone config
rclone sync hongikdid: .</pre>

6. 프로그램 테스트
<pre>python did_xxxx.py</pre>

7. 자동실행 설정(http://www.ktman.pe.kr/RaspberryPi/60640)
<pre>cd ..
nano did.sh
##########
cd ~/did
rclone sync hongikdid: .
python did_xxxx.py
##########
chmod +x did.sh
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
##########
@/home/pi/did.sh
(xscreensaver 전에)
##########
</pre>

8. 화면보호기 설정
<pre>sudo apt-get install xscreensaver
실행하여 화면보호기 끄기</pre>

9. 자동종료 설정
<pre>sudo crontab -e
@reboot /sbin/shutdown -h 16:00</pre>

10. 암호 바꾸기
<pre>sudo passwd</pre>

11. 기타
<pre>블루투스, 무선랜, 소리 끄기</pre>
