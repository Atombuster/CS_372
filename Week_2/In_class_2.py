mime_mapping = {
    "": "application/octet-stream",
    "txt": "text/plain",
    "html": "text/html",
    "gif": "image/gif",
    "jpg": "image/jpeg",
}


def url(input):
    output_string = input.split("/")
    #print(output_string)
    output_string[3]
    output = ""
    if len(output_string) >= 3:
        for i in range(3, len(output_string)):
            output += "/" + output_string[i]
    else:
        output = "/"

    #print(output)
    return output





mime = url("https://example.com/baz/foo/bar.foo.jpg").split("/")
mime = mime[(len(mime)-1)].split('.')
#print(mime[(len(mime)-1)])
mime_key = mime[len(mime)-1]
print(mime_mapping.get(mime_key))

