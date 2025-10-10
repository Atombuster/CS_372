


def mime (url):
    mime_mapping = {
    "": "application/octet-stream",
    "txt": "text/plain; charset=iso-8859-1",
    "html": "text/html",
    "gif": "image/gif",
    "jpg": "image/jpeg",
    }
    mime = url.split("/")
    mime = mime[(len(mime)-1)].split('.')
    mime_key = mime[len(mime)-1]
    return(mime_mapping.get(mime_key))

