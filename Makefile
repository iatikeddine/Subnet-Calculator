.PHONY: run clean

.SILENT:

run:
	-@python3 src.py $(ARGS)

clean:
	rm -rf __pycache__