## CQIM by ro0fy
CQIM is console interface manager for Qemu with the ability to easily and quickly manage virtual machines

## REQUIREMENTS<br>
* Qemu<br>
* Any *nix system<br>
* python3<br>

## INSTALLATION & RUNNING<br>
Install Qemu:<br>
For debian/ubuntu `sudo apt install qemu qemu-system`<br>
For fedora/RHEL `sudo dnf install qemu qemu-system`<br>
For Arch `sudo pacman -S qemu qemu-system`<br>
<br>
Clone the repository<br>
`git clone https://github.com/ro0fy/CQIM`<br>
Changedir to repository<br>
`cd CQIM`<br>
Run the script<br>
`python3 main.py`<br>
<br>
Or download the binary file (by pyinstaller) in releases & run it.<br>
`./cqim`<br>
<br>
Enter the path to the Qemu binaries (default - /usr/bin/)<br>
 `Path to qemu binaries >>` 

## LICENSE<br>
GNU GPLv3<br>
You are free to redistribute and modify the code, provided it is open source.<br>
More in COPYING file
