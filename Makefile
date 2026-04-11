%.py: FORCE
	pyinstaller --onefile $@
	mv dist/$(basename $(notdir $@)) $(basename $@)
	mkdir -p $(shell dirname $(realpath $@))/forthepeoplewhohavepython
	mv $@ $(shell dirname $(realpath $@))/forthepeoplewhohavepython/$(notdir $@)
	rm -rf dist build *.spec

FORCE:

clean:
	rm -rf dist build *.spec
