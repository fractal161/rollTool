roll.nes: src/*.fab chr/*.png
	./nesfab/nesfab roll.cfg --mlb "roll.mlb"
	python scripts/patch_mmc3.py

chr/hz.png:
	python scripts/build_hz_tiles.py

run: roll.nes
	mesen roll.nes
clean:
	rm roll.nes roll.mlb
