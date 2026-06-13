# Pokémon Dragon Version — Main Game To Do List

## Next
- Nothing currently queued

## In Progress
- Nothing currently in progress

## Open Questions (need answers before building)

## Resolved
- **Friend nicknames** — everyone goes by a short nickname in dialogue: NH, Z, S, I, A, NR
- **Castelia City story beat** — Team Fairy convoy of armoured cars; NH and I flip them with a steel pipe; senate seal found in documents; NH gets Diancie Fragment
- **Route 21 Hydrapple event** — Team Fairy bullying a Hydrapple; NH drives them off; Hydrapple joins the party at starter's current level
- **Sabina's team** — Gallade changed to Kirlia
- **NR's first battle team** — Gible + Caterpie
- **Saffron City mall** — the main hub; gym is inside the mall; Team Fairy hideout is on floor -1, only accessible after beating the gym
- **Draconia gimmick** — Azerbaijan parallel: senate oligarchy, oil wealth, "Land of Fire and Scale"; no emperor
- **City names** — reverted to original Pokémon names (Saffron City, Goldenrod City, Slateport City, etc.); trainer names are normal names too now — only Route 1 still uses Azerbaijani names
- **Gym leader names** — kept original (Whiteout, Coral, Vance, Rook, Lysara, Tide, Flint); route trainers use normal names except on Route 1 (Azerbaijani)
- **I, S, NR** — no political roles; just friends of NH who travel with the group
- **Routes between Saffron and Goldenrod** — all 7 routes built (Routes 1–7 done)
- **Routes between Goldenrod and Slateport** — 5 routes; need building before Slateport

## Done
- [x] route22.py–route27.py — Routes 22–27 with wild Pokémon and trainer battles (Castelia → Lumiose), levels 47–51; rewired Castelia exit to lead into Route 22
- [x] Debug menu (main.py) now lists every location: all 7 cities + Routes 1–27
- [x] Sky Buggy — shared module (sky_buggy.py); available in every city except Saffron (Goldenrod, Slateport, Jubilife, Castelia, Lumiose); each lists everywhere explored up to that point; Bakil City option plays the home cutscene (Mom + sick Dad) and heals the team
- [x] Designed NR's full rival team progression (Gible→Gabite ace, Caterpie→Butterfree; battles in saffron_city.py and goldenrod_city.py)
- [x] castelia_city.py — Castelia City: Team Fairy convoy (NH + I flip 3 cars with steel pipe), senate seal discovery, Diancie Fragment obtained, Rook skyscraper gym (Shadow Badge), street shop + TM dealer
- [x] route16.py–route21.py — Routes 16–21 with wild Pokémon and trainer battles (Jubilife → Castelia); Route 21 has mid-route Hydrapple event
- [x] Added Hydrapple, Tropius, Skiddo, Gogoat to pokedex, learnsets, evolutions; added Energy Ball, Leaf Blade, Night Slash, Brick Break to moves
- [x] jubilife_city.py — Jubilife City: Z arrival + Mega Stone, Team Fairy Airship double battles with S, dungeon rescue with Z, Vance gym (Iron Badge), Jubilife Mall (shop + TM shop + Move Reminder)
- [x] route13.py–route15.py — Routes 13–15 with wild Pokémon and trainer battles (Slateport → Jubilife)
- [x] slateport_city.py — Slateport City: Coral gym (gym 3, Water/Dragon), mall, Team Fairy story beat
- [x] route8.py–route12.py — Routes 8–12 with wild Pokémon and trainer battles (Goldenrod → Slateport)
- [x] goldenrod_city.py — Goldenrod City: arrival, NR reunite, Radio Tower (3 floors, Clio admin boss), Whiteout gym double battle with NR
- [x] saffron_city.py — arrival, Team Fairy grunt blocks exit, city exploration, NR battle (Gible + Caterpie), mall (shop, TM shop, gym, hideout), Sabina gym battle, Team Fairy hideout on floor -1, exit unlocks after hideout cleared
- [x] Added Caterpie to pokedex.py and learnsets.py; added Pikachu learnset
- [x] main.py — full intro: home scene (Mom, Dad, A, boiled eggs), Larch arrives, starter selection, Haci gives items
- [x] battle.py — full battle system: Fight, Bag, Pokémon, Run; type effectiveness, damage formula, catching, switching, EXP gain, leveling up
- [x] moves.py — move database with power, type, category for all moves in learnsets
- [x] pokemon.py — create_pokemon with level-scaled stats, get_moves, level_up, EXP system
- [x] route1.py — Route 1: Teymur battle, tall grass wild encounters, Mira battle, arrive at Saffron City
- [x] Created routes.py — Routes 1–7 with wild Pokémon and trainer battles
- [x] Added Pikachu to pokedex.py
- [x] Changed Trapinch/Vibrava/Flygon from Ground to Bug type in pokedex.py
- [x] Resolved all open lore questions and inconsistencies (see Lore Notes section)
- [x] Wrote full lore bible (lore.md)
- [x] Designed all 9 gym leader teams (gym_leaders.py)
- [x] Set up pokedex.py (all Pokémon including custom Draconia lines)
- [x] Set up learnsets.py
- [x] Set up evolutions.py
- [x] Changed starter lines to Dragon type (Frodger→Dragon/Fire, Buliz→Dragon/Water, Falake→Dragon/Grass)
- [x] Fixed Zweilous type to Dragon/Dark
- [x] Added Psychic types: Abra/Kadabra/Alakazam, Ralts/Kirlia/Gallade, Bronzor/Bronzong

## Lore Notes (resolved)
- Senators involved in Team Fairy are just called "senators" — no named villain senators
- Draponie: wild encounter (post-game), flashback, and cutscene in main game
- Zygarde: post-game encounter in Lumiose City depths
- Deep Thing final battle: horde battle — entire party vs the Deep Thing
- E4/Champion are in Draconia City
- Haci (E4 1) uses Dragon/Oil types
- NR's signature Pokémon is Gible (Garchomp line) — NOT Dragapult
- I's signature Pokémon is Dragapult
