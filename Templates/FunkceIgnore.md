Oprav mi chybu v mojí aplikaci

Traceback (most recent call last):
  File "/Users/petr.fuk/Repository/FukjemiCZ/TuringCoder/main.py", line 26, in <module>
    process_files(APP_DIR, output_file)
  File "/Users/petr.fuk/Repository/FukjemiCZ/TuringCoder/lib/file_content.py", line 23, in process_files
    add_file_content(APP_DIR, output_file, file_path)
  File "/Users/petr.fuk/Repository/FukjemiCZ/TuringCoder/lib/file_content.py", line 10, in add_file_content
    f.write(content_file.read())
            ^^^^^^^^^^^^^^^^^^^
  File "<frozen codecs>", line 322, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcb in position 0: invalid continuation byte

# Zdrojový kod aplikace