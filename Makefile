roll.nes: src/*.fab chr/*.png scripts/patch_mmc3.py
	./nesfab/nesfab roll.cfg --mlb "roll.mlb"
	python scripts/patch_mmc3.py

chr/hz.png: scripts/build_hz_tiles.py
	python scripts/build_hz_tiles.py

run: roll.nes
	mesen roll.nes

release: roll.nes
	cp roll.nes release/roll.nes
	zip release/roll.zip roll.nes

clean:
	rm roll.nes roll.mlb
