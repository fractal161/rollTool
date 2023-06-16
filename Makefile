roll.nes: src/*.fab chr/*.png scripts/patch_mmc3.py
	./nesfab/nesfab roll.cfg --mlb "roll.mlb"
	python3 scripts/patch_mmc3.py
	sed -i "s/NesPrgRom/P/g" roll.mlb

chr/hz.png: scripts/build_hz_tiles.py
	python3 scripts/build_hz_tiles.py

run: roll.nes
	mesen roll.nes

release: roll.nes
	cp roll.nes release/roll.nes
	zip release/roll.zip roll.nes

clean:
	rm roll.nes roll.mlb
