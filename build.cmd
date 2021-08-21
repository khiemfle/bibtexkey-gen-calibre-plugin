REM https://sevenzip.osdn.jp/chm/cmdline/commands/add.htm
del archived.zip

7z a archived.zip *.py
7z a archived.zip gen/*.py
7z a archived.zip tests/*.py
7z a archived.zip plugin-import-name-add_google_style_bibtex_key.txt