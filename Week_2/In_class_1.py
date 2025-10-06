
def url(input):
    output_string = input.split("/")
    print(output_string)
    output_string[3]
    output = ""
    if len(output_string) >= 3:
        for i in range(3, len(output_string)):
            output += "/" + output_string[i]
    else:
        output = "/"

    print(output)





url("https://example.com/")
