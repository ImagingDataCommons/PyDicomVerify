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

    call sub_.create_datasets as first_task{
        input: dataset_name=dest_bucket_name
    }
    
    scatter (i in range(length(input_series.json)))
    {
        File j_file = input_series.json[i]
        Object tmp = read_json(j_file)
        Array[Object] inputs = tmp[json_var]
        scatter (j in range(length(inputs)))
        {
            Array[File] series_files= inputs[j].SERIES_PATH 
            File series_file_firstsample = series_files[0]
        }
        
        call convert_all_series
        { 
            input: series_file_list=series_files,
            sereise_file_firstsamples=series_file_firstsample,
            json_file=j_file,
            source_bgq_table_name=input_bgq_table_name,
            destination_bucket_name=first_task.created_dataset,
            task_index=i

        }
        # Object OutputSt = { 
            
        # } 
    }
    call sub_.create_dicomstores as third_task{
        input: dataset_name = convert_all_series.filled_bucket_name[0]
    }
    
    output{
        String filled_bucket_name = third_task.created_dicomstores
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
        Int task_index
    }
    String study_local_folder = 'data_results'
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
        '~{study_local_folder}',
        )

    log_folder = 'Logs'
    logs = [(os.path.join(log_folder, i),
             os.path.join(log_folder, 'task[{:06d}]{}'.format(~{task_index},i))
            ) for i in os.listdir(log_folder)]
    for src, dst in logs:
        os.rename(src, dst)

    CODE
    mv Logs convert_all_series && mkdir Logs && mv convert_all_series Logs/
    gsutil cp -r Logs gs://~{destination_bucket_name}/
    >>>
    runtime {
        docker: "afshinmha/dicom-multiframe-conversion:latest"
        memory: "8GB"
        disks: "local-disk 30 HDD"
    }
    output{
        String filled_bucket_name = destination_bucket_name
    }
    meta {
        author: "Afshin"
        email: "akbarzadehm@gmail.com"
        description: "deep prognosis pipeline task."
    }
    


}
