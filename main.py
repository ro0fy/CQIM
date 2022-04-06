# -*- coding: utf-8 -*-

#This file is part of CQIM.
#CQIM is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#CQIM is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with CQIM. If not, see <https://www.gnu.org/licenses/>. 


import os
import colorama

from colorama import init, Fore, Back, Style

qemu_path_file = open("qemu-path")
qemu_path = qemu_path_file.read()
init()

print(Fore.GREEN + """
Welcome to 
╔══╗╔═══╗╔══╗╔╗  ╔╗
║╔═╝║╔═╗║╚╗╔╝║║  ║║
║║  ║║ ║║ ║║ ║╚╗╔╝║
║║  ║║╔╝║ ║║ ║╔╗╔╗║
║╚═╗║╚╝─║╔╝╚╗║║╚╝║║
╚══╝╚═══╝╚══╝╚╝  ╚╝
Version 0.1.2
By TheRo0fy
""")
print(Style.RESET_ALL)

#Mode
while True:
    ask1 = input("1 - Add\n2 - Load \n3 - Create_disk\n4 - Create a custom maschine\n>> ")

    #Adding machine
    if ask1 == "1":
        #Architecture
        aask1 = input("Architecture:\n1 - x86\n2 - x86_64\n3 - PowerPC\n4 - DEC Alpha\n5 - SPARC(32)\n6 - ARM\n7 - S390\n>> ")
        if aask1 == "1":
            aout = "x86"
        elif aask1 == "2":
            aout = "x86_64"
        elif aask1 == "3":
            aout == "PowerPC"
        elif aask1 == "4":
            aout == "DEC-Alpha"
        elif aask1 == "5":
            aout == "SPARC"
        elif aask1 == "6":
            aout == "ARM"  
        elif aask1 == "7":
            aout == "S390"
        else:
            print(Fore.RED + "\nERROR 2:INVALID OPTION\n")
            print(Style.RESET_ALL)
            continue
        #Drive path    
        aask2 = input(str(os.listdir("./drives")) + "Disk path >> ") + " "
        aout2 = " -hda " + "./drives/" + aask2

        #RAM
        aask3 = input("RAM (mb) >> ") + " "
        aout3 = "-m " + aask3

        #CDROM path
        aask4 = input('CDROM path("n" if not use) >> ')
        if aask4 == "n":
            aout4 = " "
        else:
            aout4 = " -cdrom " + aask4

        #Boot 
        aask5 = input("Boot from:\n1 - Floppy\n2 - Hard drive\n3 - CDROM\n4 - From net\n>> ")
        if aask5 == "1":
            aout5 = " -boot a"
        elif aask5 == "2":
            aout5 = " -boot c"
        elif aask5 == "3":
            aout5 = " -boot d"
        elif aask5 == "4":
            aout5 = " -boot n"
        else:
            print(Fore.RED + "\nERROR 2:INVALID OPTION\n")
            print(Style.RESET_ALL)
            continue

        #Enabling KVM    
        aask6 = input("KVM (y/n) >> ")
        if aask6 == "y":
            aout6 = " -enable-kvm"
        elif aask6 == "n":
            aout6 = " "
        else:
            print(Fore.RED + "\nERROR 2:INVALID OPTION\n")
            print(Style.RESET_ALL)
            continue

        #Enabling graphics    
        aask7 = input("Graphical (y/n) >> ")
        if aask7 == "n":
            aout7 = " -nographic"
        elif aask7 == "y":
            aout7 = " "
        else:
            print(Fore.RED + "\nERROR 2:INVALID OPTION\n")
            print(Style.RESET_ALL)
            continue

        #Pre-final command for write to file
        command = qemu_path + "qemu-system-" + aout + aout2 + aout3 + aout4 + aout5 + aout6  + aout7

        #Name of  machine        
        name = input("Name of machine >> ")

        #Final writing
        final = open("./machines/" + name,"w+")
        final.write(command)
        final.close()

    #Loading machine            
    if ask1 == "2":
        #Machine path
        lask1 = input(str(os.listdir("./machines")) + "\nChoose the machine >> ")
        if os.path.exists("./machines/" + lask1):
            lout1 = lask1
        else:
            print(Fore.RED + "\nERROR 3:FILE DOES NOT EXIST\n")
            print(Style.RESET_ALL)
            continue

        #Final machine load    
        machine = open("./machines/" + lout1)
        final2 = machine.read()
        os.system(final2)   
        machine.close()

    #Creating drive
    if ask1 == "3":
        #Drive name
        dname = input("Drive name >> ") + ".qcow2 "
        #Drvie path
        dpath = "./drives/" + dname
        #Drive size
        dsize = input("Drive size (mb) >> ") + "M"
        #Final drive command
        dcommand = qemu_path + "qemu-img create -f qcow2 " + dpath + dsize
        os.system(dcommand)

    
    #Creating custom machine
    if ask1 == "4":
        ccommand = input("Enter a custom command\n>> ")
        name = input("Name of machine >> ")
        cfinal = open("./machines/" + name,"w+")
        cfinal.write(ccommand)
        cfinal.close()        
