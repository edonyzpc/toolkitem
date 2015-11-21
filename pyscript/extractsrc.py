import re
import sys
if sys.version.startswith('3.'):
    from urllib.request import urlopen
else:
    from urllib import urlopen


link_src = []
with open('tmp.html') as fbuf:
    for line in fbuf.readlines():
        line = line.rstrip()
        pattern = '^<img .* src=\"(.+)\">$'
        proc = re.compile(pattern)
        mat = proc.match(line)
        if mat: link_src.append(mat.group(1))
# TODO(edony): use shell command to download
for item in link_src:
    response = urlopen(item)
    save_file = open('./img/' + item.split('/')[-1], 'wb')
    save_file.write(response.read())
    save_file.close()

