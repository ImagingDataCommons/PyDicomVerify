import importlib
import keyword
import re
import os
from common import common_tools as ctools


def edit_code(code: str):
    operators1 = r'==|!=|>=|<=|\+=|-=|\*=|->|//|\*\*'
    operators2 = r'\+|\*|=|>|<'
    patterns = [
       (r'\s*;*\s*\n',r'\n'),
       (r'(,|,)([^\s\n])', r'\g<1> \g<2>'), #space after , and :
       (r'([\w]+)\s+(,|,|\(|\))', r'\g<1>\g<2>'),
       (r'(,|,)(\s\n)', r'\g<1>\n'),
       (r'(.*)(\n\s*){1,}(\n\s*)', r'\g<1>\g<2>'),
       (r'(.*)\n(def|class)',r'\g<1>\n\n\n\g<2>'),
       (r'(.*)\n(\s{4})(def|class)',r'\g<1>\n\n\g<2>\g<3>'),
       (r'({})([^\s\n-])'.format(operators1), r'\g<1> \g<2>'),
       (r'([^\s\n-])({})'.format(operators1), r'\g<1> \g<2>'),
       (r'({})([^\s\n-])'.format(operators2), r'\g<1> \g<2>'),
       (r'([^\s\n-])({})'.format(operators2), r'\g<1> \g<2>'),
       (r'= =',r'=='),
       (r'\+ =',r'+='),
       (r'- =',r'-='),
       (r'\* =',r'*='),
       (r'! =',r'!='),
       (r'> =',r'>='),
       (r'< =',r'<='),
       (r'- >',r'->'),
       (r'> >',r'>>'),
       (r'< <',r'<<'),
       (r'\* \*',r'**'),
       (r'/ /',r'//'),
       (r"([.*])\s{2,}([.*])", r'\g<1> \g<2>'),
       (r'([_\w]*\([^()]*)\s{1,}=\s{1,}([^()]*\))',r'\g<1>=\g<2>')
        ]
    n = 0
    out = ''
    for is_included, txt in code:
        if not is_included:
            out += txt
            continue
        for pt, rpl in patterns:
            txt = re.sub(pt, rpl, txt)
        out += txt
    return out


def LabelStrings(text):
    text = re.sub(r'#([^\s])', r'# \g<1>', text)
    reg_quoted =r'(\'. * \'|".*|#.*")'
    m = re.finditer(reg_quoted, text)
    prev_end = 0
    out = []
    for i in m:
        out.append((0, text[prev_end:i.start()]))
        out.append((1, text[i.start():i.end()]))
        prev_end = i.end()
    if prev_end < len(text):
        out.append((0, text[prev_end:len(text)]))
    return out


def label_python_code_string(text: str):
    tt = text
    out = []
    while tt != '':
        p, tt = breakdown_text(tt)
        out.extend(p)
    return out


def breakdown_text(text: str):
    prev_end = 0
    out = []
    marks = {
        r'(#)': [r'(.)\n'],
        r"[^'](')[^']": [r"[^'](')[^']", r'(.)\n'],
        r'[^"](")[^"]': [r'[^"](")[^"]', r'(.)\n'],
        r"(''')": [r"(''')"],
        r'(""")': [r'(""")'],
    }
    ptrn = r'([^\\]|^){{1}}{}'
    starts = ''
    first_pos = (len(text) + 1, len(text) + 1, '', [], '')
    for start, end in marks.items():
        pp = ptrn.format(start)
        m = re.search(pp, text, flags=re.MULTILINE)
        if m is not None:
            s, e = m.span(2)
            if first_pos[0] > s:
                first_pos = (s, e, start, end, m.group(2))
    if first_pos[2] == '':
        out = [(1, text)]
        return(out, '')
    if first_pos[0] == 0:
        pre_txt = ''
    else:
        pre_txt = text[:first_pos[0]]
    post_txt = text [first_pos[1]:]
    end_pos = (len(post_txt),  len(post_txt), '', '')
    for end_m in first_pos[3]:
        if end_m == r'(.)\n':
            p = r'(.)\n'
            m = re.search(p, post_txt)
            if m is not None:
                s, e = m.span(1)
                if e < end_pos[0]:
                    end_pos = (s, e, end_m, m.group(1))
        else:
            p = ptrn.format(end_m)
            m = re.search(p, post_txt)
            if m is not None:
                s, e = m.span(2)
                if e < end_pos[0]:
                    end_pos = (s, e, end_m, m.group(2))
    if end_pos[2] == '':
        if pre_txt != '':
            out.append((1, pre_txt))
        out.append((0, first_pos[-1] + post_txt))
        return(out, '')
    excluded_txt = first_pos[-1] + post_txt[:end_pos[1]]
    unknown_txt = post_txt[end_pos[1]:]
    if pre_txt != '':
        out.append((1, pre_txt))
    out.append((0, excluded_txt))
    return(out, unknown_txt)


def refine_code(finle_name: str):
    content = ctools.Txt2StrList(finle_name)
    l_str = label_python_code_string(content)
    return edit_code(l_str)


def get_rid_of_str(content: str):
    labeled = label_python_code_string(content)
    out = ''
    for is_code, st in labeled:
        if is_code:
            out += st
    return out


def module_content_2str(module_name: str, contents: dict):
    import_str = 'from {} import (\n{})'
    name_str = ''
    for cont_label, cont_val in contents.items():
        if len(cont_val) == 0:
            continue
        cont_val.sort()
        name_str += '    # {}\n'.format(cont_label)
        for name in cont_val:
            name_str += ('    {},\n'.format(name))
    return import_str.format(module_name, name_str)


def refine_imports(filename):
    stripped_content, import_, from_, as_= find_imports(filename)
    imp_modules = []
    header = ''
    header_imports = []
    for line, modules in import_:
        for mod in modules:
            if mod in imp_modules:
                continue
            if contains_word_with_dot(mod, stripped_content):
                header_imports.append('import {}'.format(mod))
                imp_modules.append(mod)
    header_imports.sort()
    for hl in header_imports:
        header += hl + '\n' 
    # ---------------------------------------------
    header_as = []
    # as_modules = []
    for line, module in as_:
        if module in imp_modules:
            continue
        imp_modules.append(module)
        if contains_word_with_dot(module, stripped_content):
            header_as.append(line)
    header_as.sort()
    for hl in header_as:
        header += hl + '\n' 
    # ---------------------------------------------
    header_from = ''
    from_modules = []
    for module_str in from_:
        if module_str not in from_modules:
            from_modules.append(module_str)
    from_modules.sort()
    for line, module_str in from_modules:
        module = importlib.import_module(module_str)
        header_from += '\n' + import_all_from_file(
            module, destination_file_content = stripped_content,
            already_imported=imp_modules,
            print_ = False)
    header += header_from
    header = re.sub(r'\n{2,}', r'\n', header)

    print(header)


def import_all_from_file(module: str, module_name: str = '',
                         destination_file_content: str = '',
                         already_imported: list = [],
                         print_: bool=True):
    if type(module) == str:
        # if the input is file name
        filename = module
        if module_name == '':
            base = os.path.basename(filename)
            module_name = base[:-3]
    else:
        module_name = module.__name__
        filename = module.__file__
    check_if_used_in_file = False
    if destination_file_content != '':
        check_if_used_in_file = True
    module_file = os.path.basename(filename)
    if module_file == '__init__.py':
        try:
            all_sub_modules = module.__all__
            sub_modules = {'SUBMODULES':[]}
            for sm in all_sub_modules:
                if check_if_used_in_file:
                    if not contains_wholeword(
                        sm, destination_file_content):
                        continue
                if sm not in sub_modules['SUBMODULES'] and \
                        sm not in already_imported:
                    sub_modules['SUBMODULES'].append(sm)
            sub_modules['SUBMODULES'].sort
            mod_str = module_content_2str(module_name, sub_modules)
            if print_:
                print(mod_str)
            return mod_str
        except:
            pass
    content = ctools.Txt2StrList(filename)
    content = get_rid_of_str(content)
    #ctools.WriteStringToFile('/Users/afshin/Documents/work/VerifyDicom/gitexcluded_text_test.py', content)            
    reg_ptrn = {'CLASSES':r'^\bclass\b\s+([\w]+)',
                'FUNCTIONS':r'^\bdef\b\s+([\w]+)',
                'VARIABLES':r'^(?!def|class|import|from)(\b\w+\b)'}
    # rmove all imports from file conents:
    mod_content = {}
    all_sub_modules = already_imported
    for label, ptrn in reg_ptrn.items():
        ms = re.finditer(ptrn, content, flags=re.MULTILINE)
        for m in ms:
            name = m.group(1)
            if keyword.iskeyword(name):
                continue
            if check_if_used_in_file:
                if not contains_wholeword(
                    name, destination_file_content):
                    continue
            if name not in all_sub_modules:
                all_sub_modules.append(name)
                if label in mod_content:
                    if name not in mod_content[label]:
                        mod_content[label].append(name)
                else:
                    mod_content[label] = [name]
    if len(mod_content) != 0:
        mod_str = module_content_2str(module_name, mod_content)
    else:
        mod_str = ''
    if print_:
        print(mod_str)
    return mod_str


def contains_wholeword(substr: str, string: str):
    ptrn = r'\b{}\b'.format(substr)
    return re.search(ptrn, string) is not None


def contains_word_with_dot(substr: str, string: str):
    ptrn = r'\b{}\.'.format(substr)
    return re.search(ptrn, string) is not None


def find_imports(filename):
    all_ = r'[\n\s]*(\bimport\b|\bfrom\b)(.*\([^\)]*\)|([^\(\)\\\n)]*(\\[\s\n]*))*[^\(\)\\\n)]*[\s\n]*)'
    content = get_rid_of_str(ctools.Txt2StrList(filename))
    content = get_rid_of_str(content)
    stripped_content = re.sub(all_, '', content)
    ms = re.finditer(all_,content)
    header = ''
    for m in ms:
        header += m.group(0)
    # rmove extra returns:
    ptrn = r'\s*\n[\s\n]*'
    header = re.sub(ptrn, '\n', header)
    # rmove extra spaces:
    ptrn = r'\s{2,}'
    header = re.sub(ptrn, ' ', header)
    # rmove backslashes:
    ptrn = r'(.*)(\\\s*\n\s*)'
    rpl_txt = r'\g<1>'
    header = re.sub(ptrn, rpl_txt, header)
    # make all brackets on line:
    ptrn = r'(\([^\)]*)\n+'
    rpl_txt = r'\g<1>'
    header1 = ''
    while header1 != header:
        header1 = header
        header = re.sub(ptrn, rpl_txt, header)
    # rmove prethesis:
    header = re.sub('[\(\)]*', '', header)
    # find all import as :
    ptrn = r'.*import.*(\bas\b)\s+(\w*)'
    ms = re.finditer(ptrn, header)
    as_lines = []
    modules = []
    for m in ms:
        line = m.group(0)
        as_word = m.group(2)
        if as_word in modules:
            continue
        modules.append(as_word)
        as_lines.append((line, as_word))
    header = re.sub(ptrn, '', header)
    header = re.sub(r'\n{2,}','\n', header ) 
    # find all from:
    ptrn = r'from\s+(\b[\w.]*\b)\s+[^\n]*'
    ms = re.finditer(ptrn, header)
    from_lines = []
    modules = []
    for m in ms:
        line = m.group(0)
        from_word = m.group(1)
        if from_word in modules:
            continue
        modules.append(from_word)
        from_lines.append((line, from_word))
    header = re.sub(ptrn, '', header)
    header = re.sub(r'\n{2,}','\n', header )
    # find imports:
    ptrn = r'import\s+([^\n]*)'
    ms = re.finditer(ptrn, header)
    imp_lines = []
    for m in ms:
        x = m.group(1)
        x = re.sub('\s+', '', x)
        mods = re.split(',', x)
        imp_lines.append((m.group(0), mods))
    header = re.sub(ptrn, '', header)
    return (stripped_content, imp_lines, from_lines, as_lines)


