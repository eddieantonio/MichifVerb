MichifVerbs.fomabin:

%.fomabin: %.lexc
	foma -e "read lexc $<" -e "save stack $@" -s

test: MichifVerbs.fomabin
	foma -e "load stack $<" -e "print pairs" -s