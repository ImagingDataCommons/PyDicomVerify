version 1.0
import "tasks/query_series.wdl" as sub_
workflow  main{
    input {
        Int number_of_series_in_chunk = -1
        Int whole_number_of_series_to_qurey = -1
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
    # Array[Object] flattened_inputs = flatten(inputs)
    
    scatter (i in range(length(inputs)))
    {
        File json_file = input_series.json[i]
        scatter (j in range(length(inputs[i])))
        {
            Array[File] series_files= inputs[i][j].SERIES_PATH     
        }
        Array[File] flat_series_file = flatten(series_files)
        call test_task
        { 
            input: series_file_list=series_files,
            json_file=json_file
        }
        # Object OutputSt = { 
            
        # } 

    }
   
    # output {
    #     Array[Object] wf_output =  OutputSt
    #     # Array[File] w_output1 = flatten(deep_prognosis_task.files_1)
    #     # Array[File] w_output2 = flatten(deep_prognosis_task.files_2)
    #     # File jj = jjjjsss
    #     # File inn = innnppp
    # }
    meta {
    allowNestedInputs: true
    }
}
task test_task
{
    input { 
        Array[Array[File]] series_file_list
        File json_file
    }
    String ct_interpolation = 'linear'
    String output_dtype = "int"
    Float prob_logit_0 = 0.0
    Float prob_logit_1 = 0.0
    Array[Array[File]] series_file_list_trans = transpose(series_file_list)
    Array[File] sample_sereis_file = series_file_list_trans[0]

    command
    <<<
    python3 <<CODE
    print('~{json_file}')
    print('~{sep = "\n"  sample_sereis_file}'')
    CODE
    >>>
    runtime {
        docker: "afshinmha/dicom-multiframe-conversion:latest"
        memory: "16GB"
    }
    output {
        Object out_ = read_json("output.json")
    }
    meta {
        author: "Afshin"
        email: "akbarzadehm@gmail.com"
        description: "deep prognosis pipeline task."
    }
    


}
