#This file is part of CQIM.
#CQIM is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#CQIM is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with CQIM. If not, see <https://www.gnu.org/licenses/>. 

import os

#Creating directories
if not os.path.exists("drives"):
	os.mkdir("drives")
if not os.path.exists("maschines"):
	os.mkdir("maschines")
	
if os.path.exists("./qemu-path"):
    os.system("python3 ./cqim.py")

else:
	qemu_path = input("Path to qemu binaries\n>>")
	qemu_path_file = open("qemu-path","w+")
	qemu_path_file.write(qemu_path)
	qemu_path_file.close

os.system("python3 ./main.py")
