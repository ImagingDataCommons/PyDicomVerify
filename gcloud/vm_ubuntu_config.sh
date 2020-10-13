#!bin/bash
git_make()
{
    folder=./$1
    git_address=$2
    branch=$3
    if [ ! -d $folder ]
    then
        mkdir -p $folder
    fi
    tmp=$PWD
    cd $folder
    git init
    git remote add remote_$1 $git_address
    git pull remote_$1 $branch
    cd $tmp

}
apt update
apt install python3.8
apt install git
apt install python3.8-distutils
python3.8 -m pip install --upgrade pip setuptools wheel
pip install GitPython
pip install pydicom
pip install XlsxWriter

# gcloud stuff -----------
pip install google-cloud-storage
pip install google-cloud-bigquery
pip install dicomweb-client
pip install google-auth-oauthlib
pip install google-api-core 
pip install google-api-python-client 
pip install google-auth 
pip install google-auth-httplib2 
pip install google-cloud-core 
pip install google-cloud-datastore 
pip install google-crc32c 
pip install google-resumable-media 
pip install googleapis-common-protos 
#----------------------------------------
git_make verify_dicom https://github.com/afshinmessiah/PyDicomVerify.git master
git_make high_dicom https://github.com/afshinmessiah/highdicom.git dev_pixelmed_converstion_00
cd high_dicom
pip install -e .
cd -

Key_file=$(realpath ~/.config/gcloud/service_account_key.json) 
Service_account=207848281915-compute@developer.gserviceaccount.com
gcloud iam service-accounts keys create $Key_file --iam-account $Service_account 
export GOOGLE_APPLICATION_CREDENTIALS=$Key_file
echo export GOOGLE_APPLICATION_CREDENTIALS=$Key_file >> "$(realpath ~/.bashrc)"
#---------------------------------------------------
sudo apt install xutils-dev
dicom3_folder="$HOME/dicom3tools"
rm -rfv $dicom3_folder
dicom3_address="https://www.dclunie.com/dicom3tools/workinprogress/dicom3tools_1.00.snapshot.20200806153050.tar.bz2"
file_name=${dicom3_address##*/}
ws_name=$(echo $dicom3_address | grep -o '[0-9]\{8,\}')
dl_folder="$dicom3_folder/$ws_name/downloaded"
if [ ! -d $dl_folder ]
then
    mkdir -p $dl_folder
fi
wget -P $dl_folder $dicom3_address
src_folder="$dicom3_folder/$ws_name/src"
tar -C $dicom3_folder/$ws_name/ -xf $dl_folder/$file_name 
extracted_folder=${file_name%.*}
extracted_folder=${extracted_folder%.*}
mv -f $dicom3_folder/$ws_name/$extracted_folder $src_folder
cd $src_folder
./Configure
imake -I./config
make World
make install
sudo cp appsrc/dcfile/dciodvfy /bin/
cd -