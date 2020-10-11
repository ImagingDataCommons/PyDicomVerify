import re
import common.common_tools as ctools

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

def extract_lines(contents):
    ptrn1 = 'For this chunk of studies.*\]'
    ptrn2 = 'For for all studies so far.*\]'
    vec1 = []
    vec2 = []
    for m in re.finditer(ptrn1, content):
        vec1.append(str(m.group(0)))
    
    for m in re.finditer(ptrn2, content):
        vec2.append(str(m.group(0)))
    return (vec1, vec2)




file = '/home/akbarzadehm/verify_dicom/Logs/log[24-09-2020][23-48-23].log'
kw = ['download', 'upload', 'fix', 'frameset extraction', 'conversion', 'big query', '\n']
xx = ' 475.17 (inst) in 0:00:41 (11.37 (inst)/sec) [15.2%]\t'
content = ctools.Txt2StrList(file)
pattern = '{} ->(.*){}'
outs = {}
th = FindThreads(content)
v1, v2 = extract_lines(content)
for l1, l2 in zip(v1, v2):
    print('---->'+l1)
    print('---->'+l2)
for i in range(1, len(kw)):
    kw1 = kw[i-1]
    kw2 = kw[i]
    out = FindAll(pattern.format(kw1, kw2), content, 1)
    outs[kw1] = out

for kw, rate in outs.items():
    print(kw)
    for t, r in zip(th, rate):
        print('{:03d}\t{:8.8s}\t{:8.8s}\t{:16.16s}\t{:8.8s}\t{:8.8s}\t{:8.8s}'.format(t, r['size'], r['unit'], r['time'], r['rate'], r['r_unit'], r['percent']))



