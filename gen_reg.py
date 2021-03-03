def reg_group(groupName, group):
    # 传入字符串数组！，否则后果自负
    group = '[HKEY_CLASSES_ROOT\{}\shell\Managerment]\n"MUIVerb"="{}"\n"SubCommands"="{}"\n\n'.format(Range,
                                                                                                      groupName, ';'.join(group))
    return group


def create_group(group, paths):
    res = ''
    for i, j in zip(group, paths):
        j = '\\\\'.join(j.split('\\'))+'\\'
        res += '[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\{}]\n@="{}"\n"Icon"="\\"{}", 4"\n[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\{}\Command]\n@="\\"{}" \\"%1\\""\n\n'.format(
            i, i, j, i, j)

    return res


groupName, group = 'pwn', ["idax96","x96dbg",
                           "52od", "DIE"]  # 需要更改
paths = ["C:\\pwntools\\ida75\\idax96.exe",
         "C:\\pwntools\\x64dbg\\release\\x96dbg.exe",
         "C:\\pwntools\\wuaiOD\\52od.exe",
         "C:\\pwntools\\die\\die.exe"]  # 需要更改
# ["idax64", "idax86", "x64dbg", "ollygdb", "DIE"]

Range = "*"  # ['exefile', ...]


st = 'Windows Registry Editor Version 5.00\n'
with open('temp.reg', 'w') as f:
    f.write(st)
    f.write(reg_group(groupName, group))
    f.write(create_group(group, paths))
