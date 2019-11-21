MichifVerbs.fomabin:

%.fomabin: %.lexc
	foma -e "read lexc $<" -e "save stack $@" -s

plain-text.txt: MichifVerbs.fomabin
	./libexec/print-pairs.py $< | tee $@

test: plain-text.txt

sigma: MichifVerbs.fomabin
	foma -e "load stack $<" -e "sigma" -s
	

# Always try to recreate plain-text, even if it is already up-to-date.
.PHONY: plain-text.txt
.PHONY: sigma
