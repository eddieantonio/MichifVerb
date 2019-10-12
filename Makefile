MichifVerbs.fomabin:

%.fomabin: %.lexc
	foma -e "read lexc $<" -e "save stack $@" -s

plain-text.txt: MichifVerbs.fomabin
	foma -q -e "load stack $<" -e "print pairs" -s | tee $@

test: plain-text.txt

# Always try to recreate plain-text, even if it is already up-to-date.
.PHONY: plain-text.txt
