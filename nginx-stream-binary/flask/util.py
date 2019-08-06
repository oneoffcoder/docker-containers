import base64
import os
import argparse
import sys


def encode_file(file_path):
  """
  Base64 encode a file.
  :param file_path: File path.
  :return: Base64 encoded file.
  """
  with open(file_path, 'rb') as f:
    s = base64.b64encode(f.read())
    return s.decode('utf-8')


def get_output_path(file_path):
  """
  Gets the output path.
  :param file_path: File path.
  :return: Output file path.
  """
  name, ext = os.path.splitext(file_path)
  o = './docs/{}-{}.txt'.format(name, ext.replace('.', ''))
  return o


def write(data, file_path):
  """
  Writes data.
  :param data: Base64 encoded data/string.
  :param file_path: File path.
  :return: None.
  """
  with open(file_path, 'w') as f:
    f.write(data)


def to_base64():
  """
  Converts to base64 encoding.
  """
  files = ['file.docx', 'file.xlsx', 'file.pptx', 'file.pdf']
  for f in files:
    p = './docs/{}'.format(f)
    s = encode_file(p)
    o = get_output_path(f)
    print(o)
    write(s, o)


def from_base64():
  """
  Converts from base64 data to binary.
  """
  extensions = ['docx', 'xlsx', 'pptx', 'pdf']
  for e in extensions:
    p = './docs/file-{}.txt'.format(e)
    with open(p, 'r') as f:
      s = f.read()
      b = base64.b64decode(s)
      o = './docs/ffile.{}'.format(e)
      with open(o, 'wb') as of:
        of.write(b)


def parse_args(args):
  """
  Parses arguments.
  :param args: Arguments.
  :return: Arguments.
  """
  parser = argparse.ArgumentParser(description='Base64 encode files')
  parser.add_argument('--op', required=False, help='operation <to|from>', default='to')
  return parser.parse_args()


if __name__ == '__main__':
  args = parse_args(sys.argv[1:])
  if 'to' == args.op:
    to_base64()
  else:
    from_base64()