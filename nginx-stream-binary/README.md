![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

This application is a simple demonstration of streaming binary data (e.g. Word, Excel, PowerPoint and PDF) back using Flask. There are 2 types of data being streamed back; one being the binary file itself and the other being the base64 encoded version of the binary file. For now, when the binary file is streamed back, it is chunked; however, for the base64 encoded version, there is no chunking (someone work on that and contribute) as the whole file is read and then streamed back. Chunking is important to avoid memory issues.

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/nginx-stream-binary)

# Docker

Build it.

```bash
./docker-local.sh
```

Run it.

```bash
docker run -it -p 80:80 --rm nginx-stream-binary:local
```

Observe it.

* http://localhost/v1/docx
* http://localhost/v1/pptx
* http://localhost/v1/xlsx
* http://localhost/v1/pdf
* http://localhost/v1/b64/docx
* http://localhost/v1/b64/pptx
* http://localhost/v1/b64/xlsx
* http://localhost/v1/b64/pdf

# References

* [Reading a binary file with Python](https://stackoverflow.com/questions/8710456/reading-a-binary-file-with-python/8711061)
* [Flask make response with large files](https://stackoverflow.com/questions/24318084/flask-make-response-with-large-files)
* [Flask streaming](http://flask.pocoo.org/docs/1.0/patterns/streaming/)
* [Office 2007 file format mime types for http content streaming](https://blogs.msdn.microsoft.com/vsofficedeveloper/2008/05/08/office-2007-file-format-mime-types-for-http-content-streaming-2/)
* [Flask Headers](https://werkzeug.palletsprojects.com/en/0.15.x/datastructures/#werkzeug.datastructures.Headers)
* [Flask Response Objects](http://flask.pocoo.org/docs/0.12/api/#response-objects)
* [Extrating extension from file in Python](https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python)
* [Unknown file type MIME](https://stackoverflow.com/questions/1176022/unknown-file-type-mime)
* [Get the current time in milliseconds in Python](https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python)
* [Encoding image file with base64](https://stackoverflow.com/questions/3715493/encoding-an-image-file-with-base64)
* [Convert bytes to string](https://stackoverflow.com/questions/606191/convert-bytes-to-a-string)
* [Writing and reading chunked base64](https://stackoverflow.com/questions/22734401/base64-encode-decode-to-from-files-in-chunks-with-python-2-7)

# Take a Look!

Check out [Martin Fowler](https://martinfowler.com/). He's my among my favorite coding gurus.

# Citation

```
@misc{oneoffcoder_nginx_stream_binary_2019, 
title={HOWTO stream binary files with Flask}, 
url={https://github.com/oneoffcoder/docker-containers/tree/master/nginx-stream-binary}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Jun}}
```
