roll.nes: src/*.fab chr/*.png
	./nesfab/nesfab roll.cfg --mlb "roll.mlb"

run: roll.nes
	mesen roll.nes
clean:
	rm roll.nes roll.mlb
