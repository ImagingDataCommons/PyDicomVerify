import os
import conversion as conv
import common_tools as ctools
import time
import shutil
def pixelMed(input_folder:str, output_folder:str, 
output_file_pattern="{:03d}.dcm",log=[]):
    pixelmed_exe = "/Users/afshin/Documents/work/pixelmedjavadico"\
    "m_binaryrelease.20191218/pixelmed.jar"
    pixelmed_lib = "/Users/afshin/Documents/work/pixelmedjavadicom_"\
    "dependencyrelease.20191218/lib/additional/vecmath1.2-1.14.jar"
    pixelemed_jars = '{}:{}'.format(pixelmed_exe,pixelmed_lib)
    conv.ConvertByPixelMed(pixelemed_jars,input_folder, output_folder,'','',log)
    if len(output_file_pattern)>0:
        files = ctools.Find(output_folder, 1, ctools.is_dicom, sort_key=os.path.getsize)
        for n, f in enumerate(files,0):
            new_name = os.path.join(os.path.dirname(f), output_file_pattern.format(n))
            os.rename(f, new_name)

def Convert(in_folder, pixelmed_folder, highdicom_folder, log=[]):
    folders = ctools.Find(in_folder, cond_function=ctools.is_dicom, find_parent_folder=True)
    start = time.time()
    last_time_point_for_progress_update = 0
    time_interval_for_progress_update = 1
    deslash = lambda x: x if not x.endswith('/') else x[:-1]
    in_folder = deslash(in_folder)
    highdicom_folder = deslash(highdicom_folder)
    pixelmed_folder = deslash (pixelmed_folder)


    for i, folder in enumerate(folders,1):
        progress = float(i) / float(len(folders))
        time_point = time.time()
        time_elapsed = round(time_point - start)
        time_left = round(float(len(folders)-i)* time_elapsed/float(i))
        time_elapsed_since_last_show = time_point - last_time_point_for_progress_update
        if time_elapsed_since_last_show > time_interval_for_progress_update:
            ctools.ShowProgress(progress,time_elapsed, time_left, 80, 'CONVERSION:')
            if i == len(folders):
                print("\n")
        pm_folder = folder.replace(in_folder, pixelmed_folder)
        if not os.path.exists(pm_folder):
            os.makedirs(pm_folder)
        pixelMed(folder, pm_folder, log=log)
        hd_folder = folder.replace(in_folder, highdicom_folder)
        if not os.path.exists(hd_folder):
            os.makedirs(hd_folder)
        try:
            conv.ConvertByHighDicom(folder, hd_folder, log)
        except(BaseException) as err:
            log.append(str(err))

