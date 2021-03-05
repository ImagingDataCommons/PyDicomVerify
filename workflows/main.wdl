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
    
    scatter (i in range(length(flattened_inputs)))
    {
        String pid = flattened_inputs[i].PATIENTID
        String src_bukcet = flattened_inputs[i].GCS_BUCKET
        call deep_prognosis_task
        { 
            input: dicom_ct_list=flattened_inputs[i].INPUT_CT,
            dicom_rt_list=flattened_inputs[i].INPUT_RT,
            output_dir_bucket="./Output/" + src_bukcet,
            pat_id=pid,
            dest_bucket_name=dest_bucket_name
        }
        Object OutputSt = { 
            "Patient_id": pid,
            "ctSeriesInstanceUID":flattened_inputs[i].CTSERIESINSTANCEUID,
            "rtstructSeriesInstanceUID":flattened_inputs[i].RTSTRUCTSERIESINSTANCEUID,
            "prob_logit_0": deep_prognosis_task.out_.prob_logit_0,
            "prob_logit_1": deep_prognosis_task.out_.prob_logit_1,
            "output": deep_prognosis_task.out_.destination,
        } 

    }
   
    output {
        Array[Object] wf_output =  OutputSt
        # Array[File] w_output1 = flatten(deep_prognosis_task.files_1)
        # Array[File] w_output2 = flatten(deep_prognosis_task.files_2)
        # File jj = jjjjsss
        # File inn = innnppp
    }
    meta {
    allowNestedInputs: true
    }
}
task deep_prognosis_task
{
    input { 
        Array[File] dicom_ct_list
        Array[File] dicom_rt_list
        String output_dir_bucket
        String pat_id
        String dest_bucket_name
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
        import sys
        sys.path.insert(1, '/deep-prognosis-code/terra/src')
        import os
        import subprocess
        import json
        from patient_convert import patient_convert
        from patient_preprocess import patient_preprocess
        from patient_inference import patient_inference

        dicom_ct_path = os.path.dirname('~{dicom_ct_list[0]}')
        print('dicom_ct_path = {}'.format(dicom_ct_path))
        dicom_rt_path = '~{dicom_rt_list[0]}'
        print('dicom_rt_path = {}'.format(dicom_rt_path))
        destination_bucket_name = '~{dest_bucket_path}'
        patient_id = '~{pat_id}'
        output_dir = os.path.abspath('~{output_dir_pat}')
        print('out dir abs is ', output_dir)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        network_architect_json_path = '/deep-prognosis-code/terra/models/architecture.json'
        network_weights_path = '/deep-prognosis-code/terra/models/weights.h5'
        patient_convert(dicom_ct_path, dicom_rt_path, output_dir,patient_id)
        patient_preprocess(patient_id, output_dir)
        inference = patient_inference(
            network_architect_json_path,
            network_weights_path,
            output_dir,
            patient_id)
        level1 = os.path.basename(output_dir)
        level2 = os.path.basename(os.path.dirname(output_dir))
        dest2 = os.path.join(destination_bucket_name, level2) 
        dest1 = os.path.join(dest2, level1) 

        inference['destination'] = dest1 
        inference['output_parent'] = os.path.dirname(output_dir) 
        filename = 'output.json'
        with open(filename, 'w') as fp:
            json.dump(inference, fp, indent=4)
        CODE
        gsutil cp -r '~{output_dir_bucket}' '~{dest_bucket_path}'
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
