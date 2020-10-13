import os
PROJECTLIBSTANDARDDIR = "./standard/"
PROJECTLIBSUPPORTDIR = "./support/"
dest = "./"
# after partial building of david clunie's dicom3tools: 
# cp dicom3tools/libsrc/src/locale/mesgtext.tpl ./standard
# cp dicom3tools/libsrc/standard/*.tpl ./standard
#     cp dicom3tools/libsrc/standard/binval.tpl ./standard
#     cp dicom3tools/libsrc/standard/condn.tpl ./standard
#     cp dicom3tools/libsrc/standard/elmdict.tpl ./standard
#     cp dicom3tools/libsrc/standard/iodcomp.tpl ./standard
#     cp dicom3tools/libsrc/standard/module.tpl ./standard
#     cp dicom3tools/libsrc/standard/sopcl.tpl ./standard
#     cp dicom3tools/libsrc/standard/strval.tpl ./standard
#     cp dicom3tools/libsrc/standard/tagval.tpl ./standard
#     cp dicom3tools/libsrc/standard/transyn.tpl ./standard
# ============================================================
def ls_ext(pathname, ext, give_fullpath=False):
    filelist = os.listdir(pathname)
    output = []
    for filename in filelist:
        fullpath = os.path.join(pathname, filename)
        if os.path.isdir(fullpath):
            continue
        filename_size = len(filename)
        if filename.find(ext, filename_size - len(ext) - 1) != -1:
            if give_fullpath:
                output.append(fullpath)
            else:
                output.append(filename)
    return output


def ProjectToolLibraryHeaderTemplate_1(header, template, script):
    header = header + ".py"
    temp_file = "$PWD/" + PROJECTLIBSTANDARDDIR + template + ".tpl"
    scriptfile = "$PWD/" + PROJECTLIBSUPPORTDIR + script + '_1.awk'
    x = "awk -f " + scriptfile + " " + '<' + temp_file + ">" + header
    print(x)
ProjectToolLibraryHeaderTemplate_1(dest + "binval_h", "binval", "binval")
ProjectToolLibraryHeaderTemplate_1(dest + "strval_h", "strval", "strval")
ProjectToolLibraryHeaderTemplate_1(dest + "tagval_h", "tagval", "tagval")
ProjectToolLibraryHeaderTemplate_1(dest + "mesgtext_h", "mesgtext", "mesgtext")
ProjectToolLibraryHeaderTemplate_1(dest + "module_h", "module", "module")
ProjectToolLibraryHeaderTemplate_1(dest + "iodcomp_h", "iodcomp", "iodcomp")
ProjectToolLibraryHeaderTemplate_1(
    dest + "iodcomp_select_h", "iodcomp", "iodcomps")
ProjectToolLibraryHeaderTemplate_1(dest + "condn_h", "condn", "condn")
ProjectToolLibraryHeaderTemplate_1(dest + "sopclc_h", "sopcl", "sopcl")