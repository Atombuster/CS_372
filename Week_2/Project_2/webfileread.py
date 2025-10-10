def read_file(filename):
    try:
        with open(filename, "rb") as fp:
            data = fp.read()   # Read entire file
            return data

    except:
        return ""