#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
int main(int argc, int **argv)
{
    if (argv[1])
    {
        char command[] = "pyinstaller -F --noupx ";
        strcat(command, (char *)argv[1]);
        system(command);
    }
    else
    {
        printf("usage: pyexe test.py");
    }
}