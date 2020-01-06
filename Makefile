all: michif.fomabin

michif.fomabin: build.fomascript phon_rules.xfscript MichifVerbs.fomabin
	foma -l "build.fomascript" -e "save stack $@" -s

%.fomabin: %.lexc
	foma -e "read lexc $<" -e "save stack $@" -s

plain-text.txt: michif.fomabin
	./libexec/print-pairs.py $<

plain-text-no-phonology.txt: MichifVerbs.fomabin
	./libexec/print-pairs.py $< > $@

test: plain-text.txt plain-text-no-phonology.txt
	@echo plain-text.txt

qa: MichifVerbs.lexc
	./libexec/check-flags.py $<
	
sigma: MichifVerbs.fomabin
	foma -e "load stack $<" -e "sigma" -s
	

# Always try to recreate plain-text, even if it is already up-to-date.
.PHONY: plain-text.txt
.PHONY: all qa sigma test
