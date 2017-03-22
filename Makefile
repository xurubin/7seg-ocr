%.jpeg:
	@unzip -p corpus.zip $@ | python ocr.py -i - -d
