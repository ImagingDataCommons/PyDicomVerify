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
    python3 <<CODE
    import sys
    sys.path.insert(1, '/fix/')
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
        memory: "1GB"
    }
    output{
        Array[File] json = glob(json_file_name + '*.json')
    }
}