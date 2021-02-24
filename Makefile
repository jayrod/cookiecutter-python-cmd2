BAKE_OPTIONS=--no-input

help:
	@echo "bake 	generate project using defaults"
	@echo "clean 	removes previous baked project"

clean:
	rm -rf pythonboilerplatecmd2

bake: clean
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists
