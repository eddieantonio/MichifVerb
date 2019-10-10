MichifVerbs.fomabin:

%.fomabin: %.lexc
	foma -e "read lexc $<" -e "save stack $@" -s

plain-text.txt: MichifVerbs.fomabin
	foma -q -e "load stack $<" -e "print pairs" -s | tee $@

test: plain-text.txt