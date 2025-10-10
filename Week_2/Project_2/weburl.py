def url(input):
    output_file_path = ""
    output_domain = ""
    output_string = input.split("/")

    if output_string[0] == ("https:" or "http:"):
        domain, file_path = 3,4
    else:
        domain, file_path = 0,1




    if len(output_string) >= domain:
        output_domain = output_string[domain]
    else:
        return(None,None)#if it is not valid 
    if len(output_string) <= file_path:
        output_file_path = "/"
        
    else:
        for i in range(file_path, len(output_string)):
            output_file_path += "/" + output_string[i]

    return (output_domain, output_file_path)