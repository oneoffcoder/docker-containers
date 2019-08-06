import json
import os
import datetime
import base64

from flask import Flask, request, Response
from flask_cors import CORS
from werkzeug.datastructures import Headers

app = Flask(__name__)
app.config.from_object('config')
CORS(app, resources={r'/*': {
    'origins': '*',
    'supports_credentials': True,
    'allow_headers': '*'
}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Accept,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, HEAD, POST, OPTIONS, PUT, PATCH, DELETE')
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  """
  Gets dummy message.
  """
  return json.dumps({
    'message': 'no one was here',
    'ms': get_epochtime_ms()
    })


@app.route('/v1/test', methods=['GET'])
def hello():
  """
  Gets headers JSON.
  """
  h = {}
  for k, v in request.headers.items():
      h[k] = v
  h['ms'] = get_epochtime_ms()

  return json.dumps(h)


@app.route('/v1/docx')
def get_docx():
  """
  Streams DOCX.
  """
  return stream_it('file.docx')


@app.route('/v1/xlsx')
def get_xlsx():
  """
  Streams XLSX.
  """
  return stream_it('file.xlsx')


@app.route('/v1/pptx')
def get_pptx():
  """
  Streams PPTX.
  """
  return stream_it('file.pptx')


@app.route('/v1/pdf')
def get_pdf():
  """
  Streams PDF.
  """
  return stream_it('file.pdf')


@app.route('/v1/b64/docx')
def get_b64_docx():
  """
  Streams DOCX from base64 encoded data.
  """
  return stream_base64('file-docx.txt', 'file.docx')


@app.route('/v1/b64/xlsx')
def get_b64_xlsx():
  """
  Streams XLSX from base64 encoded data.
  """
  return stream_base64('file-xlsx.txt', 'file.xlsx')


@app.route('/v1/b64/pptx')
def get_b64_pptx():
  """
  Streams PPTX from base64 encoded data.
  """
  return stream_base64('file-pptx.txt', 'file.pptx')


@app.route('/v1/b64/pdf')
def get_b64_pdf():
  """
  Streams PDF from base64 encoded data.
  """
  return stream_base64('file-pdf.txt', 'file.pdf')


def stream_it(file_path):
  """
  Streams binary data back.
  :param file_path: File path.
  :return: Response.
  """
  return Response(
    get_binary_content(file_path), 
    headers=get_headers(file_path),
    mimetype=get_mime_type(file_path), 
    content_type='application/octet-stream')


def stream_base64(file_path, filename):
  """
  Streams base64 encoded data as binary data.
  :param file_path: File path.
  :return: Response.
  """
  return Response(
    get_base64_content(file_path), 
    headers=get_headers(filename),
    mimetype=get_mime_type(filename), 
    content_type='application/octet-stream')


def get_headers(file_path):
  """
  Gets the headers.
  :param file_path: File path.
  :return: Headers.
  """
  h = Headers()
  h.add('Content-Disposition', 'attachment', filename=file_path)
  return h


def get_binary_content(file_path, dir_path='./docs'):
  """
  Gets the binary content in chunks.
  :param file_path: File path.
  :param dir_path: Directory path. Default is ./docs.
  :return: Generator yielding binary data.
  """
  p = '{}/{}'.format(dir_path, file_path)
  with open(p, mode='rb') as f:
    for line in f:
      yield line


def get_base64_content(file_path, dir_path='./docs'):
  """
  Gets base64 encoded content as binary data.
  :param file_path: File path.
  :param dir_path: Directory path. Default is ./docs.
  :return: Generator yielding binary data.
  """
  p = '{}/{}'.format(dir_path, file_path)
  with open(p, mode='r') as f:
    s = f.read()
    b = base64.b64decode(s)
    yield b


def get_mime_type(file_path):
  """
  Gets the MIME type of the file based on extension.
  :param file_path: File path or file name.
  :return: MIME type.
  """
  mtypes = {
    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    '.pdf': 'application/pdf'
  }

  _, ext = os.path.splitext(file_path)
  if ext in mtypes:
    return mtypes[ext]
  return 'application/octet-stream'


def get_epochtime_ms():
  """
  Gets milliseconds past epoch.
  :return: Milliseconds past epoch.
  """
  return round(datetime.datetime.utcnow().timestamp() * 1000)


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    print('final port is {}'.format(port))
    app.run(debug=False, host='0.0.0.0', port=port)