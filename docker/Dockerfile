# adapted from https://hub.docker.com/r/jupyter/base-notebook/ AKA https://github.com/jupyter/docker-stacks/tree/master/base-notebook

# FROM marketplace.gcr.io/google/ubuntu1804:latest
FROM gcr.io/gcp-runtimes/ubuntu_18_0_4:latest
USER root
WORKDIR '/'

#######################
# Prerequisites
#######################
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -yq --no-install-recommends \

    # gnupg requirement
    dirmngr \
    gnupg \

    # curl requirement
    ca-certificates \
    curl \

    # google-cloud-sdk requirement
    lsb-release \
    gcc-6 \
    gcc-8 \

    # useful utilities for debugging within the docker
    unzip \
    nano \
    vim \
    procps \

    # python requirements
    checkinstall \
    build-essential \
    zlib1g-dev \

    # pip requirements
    libssl1.0-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python-openssl \

    # install script requirements
    sudo \
    wget \
    locales \
    git \
    jq \

    # for ssh-agent and ssh-add
    keychain \



 # Uncomment en_US.UTF-8 for inclusion in generation
 && sed -i 's/^# *\(en_US.UTF-8\)/\1/' /etc/locale.gen \
 # Generate locale
 && locale-gen \

 # google-cloud-sdk separately because it need lsb-release and other prereqs installed above
 && export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \
 && echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list \
 && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
 && apt-get update \
 && apt-get install -yq --no-install-recommends \
    google-cloud-sdk \

 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# # Python3, kernel, and pip
RUN apt update \
   && apt install -yq software-properties-common \
   && add-apt-repository ppa:deadsnakes/ppa \
   && apt install -yq python3.8 \
   && update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.8 1 \
   && apt-get -yq install python3-pip \
   && /usr/local/bin/python3 -m pip install --upgrade pip


# gcloud stuff -----------
RUN pip install google-cloud-storage \
&& pip install google-cloud-bigquery \
&& pip install dicomweb-client \
&& pip install google-auth-oauthlib \
&& pip install google-api-core  \
&& pip install google-api-python-client  \
&& pip install google-auth  \
&& pip install google-auth-httplib2  \
&& pip install google-cloud-core  \
&& pip install google-cloud-datastore  \
&& pip install google-crc32c  \
&& pip install google-resumable-media  \
&& pip install googleapis-common-protos 

ENV  FIXCODE_DIR 'fix'
ENV  HIDICOM_DIR 'highdicom'
RUN mkdir "${FIXCODE_DIR}" \
&& cd "${FIXCODE_DIR}" \
&& git init \
&& git remote add -f origin https://github.com/afshinmessiah/highdicom.git \
&& git pull origin dev_pixelmed_converstion_00 \
&& cd high_dicom \
&& pip install -e . \
&& cd -
RUN mkdir "${FIXCODE_DIR}" \
&& cd "${FIXCODE_DIR}" \
&& git init \
&& git remote add -f origin https://github.com/afshinmessiah/PyDicomVerify.git \
&& git pull origin master \
&& cd - \
&& pip3 install -r "/${FIXCODE_DIR}/requirements.txt" \
&& pip3 install google-cloud-bigquery


RUN apt install xutils-dev
ENV dicom3_folder "/dicom3tools"
RUN rm -rfv $dicom3_folder \
&& dicom3_address="http://dclunie.com/dicom3tools/workinprogress/dicom3tools_1.00.snapshot.20201208085311.tar.bz2" \
&& file_name=${dicom3_address##*/} \
&& ws_name=$(echo $dicom3_address | grep -o '[0-9]\{8,\}') \
&& dl_folder="$dicom3_folder/$ws_name/downloaded" \
&& mkdir -p $dl_folder \
&& wget -P $dl_folder $dicom3_address \
&& src_folder="$dicom3_folder/$ws_name/src" \
&& tar -C $dicom3_folder/$ws_name/ -xf $dl_folder/$file_name  \
&& extracted_folder=${file_name%.*} \
&& extracted_folder=${extracted_folder%.*} \
&& mv -f $dicom3_folder/$ws_name/$extracted_folder $src_folder \
&& cd $src_folder \
&& ./Configure \
&& imake -I./config \
&& make World \
&& make install \
&& sudo cp appsrc/dcfile/dciodvfy /bin/ \
&& cd -
USER $USER


