# Purpose

This application is a simple demonstration of streaming binary data (e.g. Word, Excel, PowerPoint and PDF) back using Flask. There are 2 types of data being streamed back; one being the binary file itself and the other being the base64 encoded version of the binary file. For now, when the binary file is streamed back, it is chunked; however, for the base64 encoded version, there is no chunking (someone work on that and contribute) as the whole file is read and then streamed back. Chunking is important to avoid memory issues.

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/nginx-stream-binary)

# Docker

Pull it.

```bash
docker pull oneoffcoder/nginx-stream-binary:latest
```

Run it.

```bash
docker run -it -p 80:80 --rm oneoffcoder/nginx-stream-binary
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
