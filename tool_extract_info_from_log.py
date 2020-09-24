import re
import common_tools as ctools

def FindThreads(content):
    ptrn = 'with <([0-9]+)>'
    all_output = []
    for m in re.finditer(ptrn, content):
        selected = str(m.group(1))
        all_output.append(int(selected))
    return all_output

def FindAll(patrn, content, g):
    all_output = []
    for m in re.finditer(patrn, content):
        selected = str(m.group(g))
        elems = GetElements(selected)
        # print('--->{}'.format(selected))
        all_output.append(elems)
    return all_output

def GetElements(selected):
    ptrn = '([0-9.:]+) (.*) in ([0-9.:]+) \(([0-9.:]+) (.*)\) \[([0-9.:]+)%\]'
    m = re.search(ptrn, selected)
    xxx = ' 234.32 MB in 0:00:43 (5.37 MB/sec) [15.9%]\t'
    if m is None:
        print(m)
    out = {'size': m.group(1), 'unit': m.group(2), 'time': m.group(3), 'rate': m.group(4), 'r_unit': m.group(5), 'percent': m.group(6)}
    return out




file = '/home/akbarzadehm/verify_dicom/Logs/log[24-09-2020][19-55-47].log'
kw = ['download', 'upload', 'fix', 'frameset extraction', 'conversion', 'big query', '\n']
xx = ' 475.17 (inst) in 0:00:41 (11.37 (inst)/sec) [15.2%]\t'
content = ctools.Txt2StrList(file)
pattern = '{} ->(.*){}'
outs = {}
th = FindThreads(content)
for i in range(1, len(kw)):
    kw1 = kw[i-1]
    kw2 = kw[i]
    out = FindAll(pattern.format(kw1, kw2), content, 1)
    outs[kw1] = out

for kw, rate in outs.items():
    print(kw)
    for t, r in zip(th, rate):
        print('{}\t\t{}\t\t{}\t\t{}\t\t{}'.format(t, r['size'], r['time'], r['rate'], r['percent']))



