# GruntPy
Introduction: 
A basic grunt work project for new coming penetration testing students to learn about the in and outs of the first stage of hacking and networking.
This is from a basic view, a TCP, UDP and Ping scanner. The scanners are scripted from the very powerfull tool 'Scapy'
I have made this project (My first ever python project) keeping in mind about the new comers in this field by crafting almost everything from scratch.
Like IPv4 Validation, IPv4 subnet and available host calculation are written from scratch instead of just using IPaddress and Netaddr modules.
This would help new comers to understand about the in and outs of common scanning methods, Subnetting for the network guys, and coding one's way in a real world project for coding guys.
I have intentionally kept this project interactive unlike CLI Arugumentative like NMAP. This will help new comers to learn the How things, instead of remembering exact sequnce of letters in argumentative instructions.
I have separated the IPv4 validation and Subnet calculation codes in modules, for understanding purposes and also can be imported into other python apps as modules or using it as stand alone application.
New scanner codes can be written to the scanners.py file and the function name can be easily added by just adding the name into a dictionary in the main() function.

Upcoming:
-> Banner Grabbing

current bugs:
-> Loopback or 127.0.0.1 doesn't work. Looking to fix it soon enough.

Requirments: 
-> Latest versions of npcap or winpcap, Python 2.x, scapy 2.4.0, termcolor

installation: 
-> pip install scapy==2.4.0, pip install termcolor

usage:
-> Basically nothing to explicitly mention. As easy as answering questions.

P.S: You are free to use it, change it, learn from it.etc. But, if you are planning to change and re upload it elsewhere or GitHub, Do not forget to mention the original author's name and link

Thank You ...



