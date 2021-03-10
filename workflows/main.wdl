version 1.0
import "tasks/query_series.wdl" as sub_
workflow  main{
    input {
        Int number_of_series_in_chunk = -1
        Int whole_number_of_series_to_qurey = -1
        String input_bgq_table_name
        String dest_bucket_name
    }
    String json_file = 'sereies_info'
    String json_var = 'data'
    call sub_.query_series as input_series{
        input: json_file_name=json_file,
        json_var_name=json_var,
        series_chunk_size=number_of_series_in_chunk,
        max_series_to_query=whole_number_of_series_to_qurey
    }

    scatter(j in range(length(input_series.json)))
    {
        Object tmp = read_json(input_series.json[j])
        Array[Object] inputs = tmp[json_var]

    }
    call sub_.create_datasets as first_task{
        input: dataset_name=dest_bucket_name
    }
    
    scatter (i in range(length(inputs)))
    {
        File json_file = input_series.json[i]
        scatter (j in range(length(inputs[i])))
        {
            Array[File] series_files= inputs[i][j].SERIES_PATH 
            File series_file_firstsample = series_files[0]
        }
        
        call convert_all_series
        { 
            input: series_file_list=series_files,
            sereise_file_firstsamples=series_file_firstsample,
            json_file=json_file,
            source_bgq_table_name=input_bgq_table_name,
            destination_bucket_name=first_task.created_dataset

        }
        # Object OutputSt = { 
            
        # } 
    }
    call sub_.create_dicomstores as third_task{
        input: dataset_name = convert_all_series.filled_bucket_name[0]
    }
    
    output {
        Array[File] firsttask =  first_task.logs
        Array[File] conversion = flatten(convert_all_series.logs)
        Array[File] thirdttask =  third_task.logs
    }
    meta {
    allowNestedInputs: true
    }
}
task convert_all_series
{
    input { 
        Array[Array[File]] series_file_list
        Array[File] sereise_file_firstsamples
        File json_file
        String source_bgq_table_name
        String destination_bucket_name
    }
    String fx_study_local_folder = 'data_fx'
    String mf_study_local_folder = 'data_mf'
    command
    <<<
    cd /fix/
    git pull origin master
    cd -
    python3 <<CODE
    import sys
    sys.path.insert(1, '/fix/')
    from pipeline_fix_convert_locally import main_fix_multiframe_convert
    import os
    print('~{json_file}')
    folders = [ os.path.dirname(f) for f in ['~{sep = "\', \'"  sereise_file_firstsamples}']]
    for f in folders:
        ff = os.listdir(f)
        print('----->',f)
        for i, fff in enumerate(ff):
            print(i, ')', fff)
    main_fix_multiframe_convert(
        '~{json_file}',
        folders, 
        '~{source_bgq_table_name}',
        '~{destination_bucket_name}',
        '~{fx_study_local_folder}',
        '~{mf_study_local_folder}'
        )
    CODE
    gsutil -m cp -r ~{fx_study_local_folder}/dicom gs://~{destination_bucket_name}/FIXED
    gsutil -m cp -r ~{mf_study_local_folder}/dicom gs://~{destination_bucket_name}/MULTIFRAME
    >>>
    runtime {
        docker: "afshinmha/dicom-multiframe-conversion:latest"
        memory: "8GB"
    }
    output{
        Array[File] logs = glob('Logs/' + '*.log')
        String filled_bucket_name = destination_bucket_name
    }
    meta {
        author: "Afshin"
        email: "akbarzadehm@gmail.com"
        description: "deep prognosis pipeline task."
    }
    


}
