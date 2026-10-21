import budoux, pathlib, re
d = pathlib.Path(__file__).parent
src = (d / 'index.src.html').read_text()
head, rest = src.split('<body>', 1)
body, tail = rest.split('<script>', 1)
body = budoux.load_default_japanese_parser().translate_html_string(body)
(d / 'index.html').write_text(head + '<body>' + body + '<script>' + tail)
