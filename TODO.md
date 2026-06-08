# Pokémon Dragon Version — Main Game To Do List

## Next
- Design Nico's full rival team progression

## In Progress
- Nothing currently in progress

## Open Questions (need answers before building)

## Resolved
- **Nico's first battle team** — Gible + Caterpie
- **Saffron City mall** — the main hub; gym is inside the mall; Team Fairy hideout is on floor -1, only accessible after beating the gym
- **Draconia gimmick** — Azerbaijan parallel: senate oligarchy, oil wealth, "Land of Fire and Scale"; no emperor
- **City names** — reverted to original Pokémon names (Saffron City, Goldenrod City, Slateport City, etc.); only route trainers use Azerbaijani names
- **Gym leader names** — kept original (Whiteout, Coral, Vance, Rook, Lysara, Tide, Flint); only route trainers use Azerbaijani names
- **Isaac, Sam, Nico** — no political roles; just friends of NH who travel with the group
- **Routes between Saffron and Goldenrod** — all 7 routes built (Routes 1–7 done)
- **Routes between Goldenrod and Slateport** — 5 routes; need building before Slateport

## Done
- [x] jubilife_city.py — Jubilife City: Z arrival + Mega Stone, Team Fairy Airship double battles with S, dungeon rescue with Z, Vance gym (Iron Badge), Jubilife Mall (shop + TM shop + Move Reminder)
- [x] route13.py–route15.py — Routes 13–15 with wild Pokémon and trainer battles (Slateport → Jubilife)
- [x] slateport_city.py — Slateport City: Coral gym (gym 3, Water/Dragon), mall, Team Fairy story beat
- [x] route8.py–route12.py — Routes 8–12 with wild Pokémon and trainer battles (Goldenrod → Slateport)
- [x] goldenrod_city.py — Goldenrod City: arrival, Nico reunite, Radio Tower (3 floors, Clio admin boss), Whiteout gym double battle with Nico
- [x] saffron_city.py — arrival, Team Fairy grunt blocks exit, city exploration, Nico battle (Gible + Caterpie), mall (shop, TM shop, gym, hideout), Sabina gym battle, Team Fairy hideout on floor -1, exit unlocks after hideout cleared
- [x] Added Caterpie to pokedex.py and learnsets.py; added Pikachu learnset
- [x] main.py — full intro: home scene (Narmina, Hasan, Aziza, boiled eggs), Larch arrives, starter selection, Haci gives items
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
- Nico's signature Pokémon is Gible (Garchomp line) — NOT Dragapult
- Isaac's signature Pokémon is Dragapult
