import os


PROJECTLIBSTANDARDDIR = "./standard/"
PROJECTLIBSUPPORTDIR = "./support/"
dest = "./"



# ====================================================================
def ls_ext(pathname, ext, give_fullpath=False):
    filelist = os.listdir(pathname)
    output = []
    for filename in filelist:
        fullpath = os.path.join(pathname, filename)
        if os.path.isdir(fullpath):
            continue
        filename_size = len(filename);
        if filename.find(ext, filename_size - len(ext) - 1) != -1:
            if give_fullpath:
                output.append(fullpath)
            else:
                output.append(filename)
    return output


def ProjectToolLibraryHeaderTemplate_1(header, template, script):
    header = header + ".py"
    temp_file = "$PWD/"+PROJECTLIBSTANDARDDIR + template + ".tpl"
    scriptfile = "$PWD/"+PROJECTLIBSUPPORTDIR + script + '_1.awk'

    x = "awk -f " + scriptfile + " "  + ' <' + temp_file + ">" + header
    print(x)



ProjectToolLibraryHeaderTemplate_1(dest + "binval_h", "binval", "binval")
ProjectToolLibraryHeaderTemplate_1(dest + "strval_h", "strval", "strval")
ProjectToolLibraryHeaderTemplate_1(dest + "tagval_h", "tagval", "tagval")
ProjectToolLibraryHeaderTemplate_1(dest + "mesgtext_h", "mesgtext", "mesgtext")
ProjectToolLibraryHeaderTemplate_1(dest + "module_h", "module", "module")
ProjectToolLibraryHeaderTemplate_1(dest + "iodcomp_h", "iodcomp", "iodcomp")
ProjectToolLibraryHeaderTemplate_1(dest + "iodcomp_select_h", "iodcomp", "iodcomps")
ProjectToolLibraryHeaderTemplate_1(dest + "condn_h", "condn", "condn")
ProjectToolLibraryHeaderTemplate_1(dest + "sopclc_h", "sopcl", "sopcl")