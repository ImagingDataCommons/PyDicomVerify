version 1.0

task query_series
{
    input
    {
        String json_file_name
        String json_var_name
        Int series_chunk_size = -1
        Int max_series_to_query = -1
    }
    command
    <<<
    cd /fix/
    git pull origin master
    cd -
    python3 <<CODE
    print('before adding the fix to path')
    import sys
    sys.path.insert(1, '/fix/')
    print('added fix to path')
    from query_fix_convert_inputs import query_all
    query_all(
        '~{json_file_name}',
        '~{json_var_name}',
        ~{series_chunk_size},
        ~{max_series_to_query})  
    CODE
    >>>
    runtime
    {
        docker: "afshinmha/dicom-multiframe-conversion:latest"
        memory: "4GB"
    }
    output{
        Array[File] json = glob(json_file_name + '*.json')
    }
}
task create_datasets
{
    input
    {
        String dataset_name
    }
    command
    <<<
    cd /fix/
    git pull origin master
    cd -
    python3 <<CODE
    print('before adding the fix to path')
    import sys
    sys.path.insert(1, '/fix/')
    print('added fix to path and before import create_bucket_tables')
    from pipeline_fix_convert_locally import create_bucket_tables
    print('after import create_bucket_tables before call')
    create_bucket_tables('~{dataset_name}')
    print('aftetr call')
    CODE
    gsutil cp -r Logs/* gs://~{dataset_name}/Logs/create_datasets
    >>>
    runtime
    {
        docker: "afshinmha/dicom-multiframe-conversion:latest"
        memory: "4GB"
    }
    output{
        String created_dataset = dataset_name
    }
}
task create_dicomstores
{
    input
    {
        String dataset_name
    }
    command
    <<<
    cd /fix/
    git pull origin master
    cd -
    python3 <<CODE
    import sys
    sys.path.insert(1, '/fix/')
    from pipeline_fix_convert_locally import create_dicomstores
    create_dicomstores('~{dataset_name}')
    CODE
    gsutil cp -r Logs/* gs://~{dataset_name}/Logs/create_dicomstores
    >>>
    runtime
    {
        docker: "afshinmha/dicom-multiframe-conversion:latest"
        memory: "4GB"
    }
    output{
        Array[File] logs = glob('Logs/' + '*.log')
    }
}
