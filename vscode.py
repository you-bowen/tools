import json
import os
import sys

filename = sys.argv[1]
snipName, suffix = filename.split('.')
langDict = {'py': 'python',
            'c': 'c',
            'cpp': 'cpp',
            'html': 'html',
            'js': 'javascript',
            'vue': 'vue',
            'css': 'css'}

if suffix in langDict.keys():
    lang = langDict[suffix]
else:
    print('{} is not included in your vscode snippets'.format(suffix))
    exit()

path = r'C:\Users\{}\AppData\Roaming\Code\User\snippets\{}.json'.format(
    os.getlogin(), lang)
with open(path) as f:
    data = json.load(f)

with open(filename) as f:
    content = f.read()
    new = {}
    new['prefix'] = snipName
    new['body'] = content.split('\n')
    new['description'] = 'template for {}'.format(snipName)

data[snipName] = new
if content == 'DEL\n':  # 删除对应snippet就在文件中输入'DEL\n'
    data.pop(snipName)

with open(path, 'w') as f:
    f.write(json.dumps(data, indent=4))
