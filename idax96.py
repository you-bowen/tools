import win32file as w
import sys
import subprocess

def is_64bit_elf(filename):
    with open(filename, "rb") as f:
        return f.read(5)[-1] == 2

def is_64bit_pe(filename):
    return w.GetBinaryType(filename) == 6

filepath = sys.argv[1]
if filepath.endswith('.exe'):
    if is_64bit_pe(filepath):
        subprocess.Popen(r'C:\pwntools\ida75\75ida64.exe '+'"'+filepath+'"')
    else:
        subprocess.Popen(r'C:\pwntools\ida75\75ida.exe '+'"'+filepath+'"')
else:
    if is_64bit_elf(filepath):
        subprocess.Popen(r'C:\pwntools\ida75\75ida64.exe '+'"'+filepath+'"',shell=False)
    else:
        subprocess.Popen(r'C:\pwntools\ida75\75ida.exe '+'"'+filepath+'"')
