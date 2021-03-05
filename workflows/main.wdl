version 1.0
import "tasks/query_series.wdl" as sub_
workflow  {
    input {
        Int number_of_sereis_in_chunk = -1
        Int whole_number_of_sereis_to_qurey = -1
        String dest_bucket_name
    }
    String json_file = 'sereies_info'
    String json_var = 'data'
    call sub_.query_series as input_sereis{
        input: json_file_name=json_file
        json_var_name=json_var
        series_chunk_size=number_of_sereis_in_chunk
        max_series_to_query=whole_number_of_sereis_to_qurey
    }

    scatter(j in range(length(input_sereis.json)))
    {
        Object tmp = read_json(input_sereis.json[j])
        Array[Object] inputs = tmp.${json_var}

    }
    # Array[Object] flattened_inputs = flatten(inputs)
    
    scatter (i in range(length(inputs)))
    {
        File json_file = inputs[i]
        scatter (j in range(length(inputs[i])))
        {
            Array[File] series_files= inputs[i][j].SERIES_PATH     
        }
        call test_task
        { 
            input: sereis_file_list=series_files,
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
        Array[Array[File]] sereis_file_list
        File json_file
    }
    String dest_bucket_path = 'gs://' + dest_bucket_name
    String ct_interpolation = 'linear'
    String output_dtype = "int"
    String output_dir_pat = output_dir_bucket + '/' + pat_id
    Float prob_logit_0 = 0.0
    Float prob_logit_1 = 0.0
    command
    <<<
    python3 <<CODE
    print('~{json_file}')
    pirnt('~{sereis_file_list}')
    #     import sys
    #     sys.path.insert(1, '/deep-prognosis-code/terra/src')
    #     import os
    #     import subprocess
    #     import json
    #     from patient_convert import patient_convert
    #     from patient_preprocess import patient_preprocess
    #     from patient_inference import patient_inference

    #     dicom_ct_path = os.path.dirname('~{dicom_ct_list[0]}')
    #     print('dicom_ct_path = {}'.format(dicom_ct_path))
    #     dicom_rt_path = '~{dicom_rt_list[0]}'
    #     print('dicom_rt_path = {}'.format(dicom_rt_path))
    #     destination_bucket_name = '~{dest_bucket_path}'
    #     patient_id = '~{pat_id}'
    #     output_dir = os.path.abspath('~{output_dir_pat}')
    #     print('out dir abs is ', output_dir)
    #     if not os.path.exists(output_dir):
    #         os.makedirs(output_dir)
    #     network_architect_json_path = '/deep-prognosis-code/terra/models/architecture.json'
    #     network_weights_path = '/deep-prognosis-code/terra/models/weights.h5'
    #     patient_convert(dicom_ct_path, dicom_rt_path, output_dir,patient_id)
    #     patient_preprocess(patient_id, output_dir)
    #     inference = patient_inference(
    #         network_architect_json_path,
    #         network_weights_path,
    #         output_dir,
    #         patient_id)
    #     level1 = os.path.basename(output_dir)
    #     level2 = os.path.basename(os.path.dirname(output_dir))
    #     dest2 = os.path.join(destination_bucket_name, level2) 
    #     dest1 = os.path.join(dest2, level1) 

    #     inference['destination'] = dest1 
    #     inference['output_parent'] = os.path.dirname(output_dir) 
    #     filename = 'output.json'
    #     with open(filename, 'w') as fp:
    #         json.dump(inference, fp, indent=4)
    CODE
    #     gsutil cp -r '~{output_dir_bucket}' '~{dest_bucket_path}'
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
