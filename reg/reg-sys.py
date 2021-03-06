def reg_group(itemname,groupName, group):
    # 传入字符串数组！，否则后果自负
    group = '[HKEY_CLASSES_ROOT\Directory\Background\shell\{}]\n"MUIVerb"="{}"\n"SubCommands"="{}"\n\n'.format(itemname,
                                                                                                      groupName, ';'.join(group))
    return group


def create_group(group, paths):
    res = ''
    for i, j in zip(group, paths):
        j = '\\\\'.join(j.split('\\'))+'\\'
        res += '[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\{}]\n@="{}"\n"Icon"="\\"{}", 4"\n[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\{}\Command]\n@="\\"{}""\n\n'.format(
            i, i, j, i, j)

    return res


groupName, group = 'sys', ["regedit","taskmgr"]  # 需要更改
paths = ["C:\\Windows\\regedit.exe",
         "C:\\Windows\\System32\\Taskmgr.exe"]  # 需要更改
# 防火墙 - "C:\\Windows\\System32\\WF.msc" 暂时无法使用
# ["idax64", "idax86", "x64dbg", "ollygdb", "DIE"]



itemname='easySys'
st = 'Windows Registry Editor Version 5.00\n'
with open('temp.reg', 'w') as f:
    f.write(st)
    f.write(reg_group(itemname,groupName, group))
    f.write(create_group(group, paths))
