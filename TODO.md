# Pokémon Dragon Version — Main Game To Do List

## Next
- Build Saffron City (arrive, look around, mall, enter gym)
- Build Gym 1 battle (Sabina — Psychic/Dragon)
- Build Nico first meetup and battle in Saffron City
- Build Routes 2 and 3
- Design Nico's full rival team progression

## Open Questions (need answers before building)
- **Nico's first battle team** — just Gible, and what level?
- **Team Fairy hideout (mall floor -1)** — what happens when NH goes down there after beating the gym? Story cutscene, grunt battles, both?
- **TMs on mall floor 2** — specific TMs in mind, or should a sensible early-game selection be picked?

## In Progress
- Nothing currently in progress

## Done
- [x] main.py — full intro: home scene (Narmina, Hasan, Aziza, boiled eggs), Larch arrives, starter selection, Haci gives items
- [x] battle.py — full battle system: Fight, Bag, Pokémon, Run; type effectiveness, damage formula, catching, switching, EXP gain, leveling up
- [x] moves.py — move database with power, type, category for all moves in learnsets
- [x] pokemon.py — create_pokemon with level-scaled stats, get_moves, level_up, EXP system
- [x] route1.py — Route 1: Teymur battle, tall grass wild encounters, Mira battle, arrive at Saffron City
- [x] Created routes.py — Routes 1, 2, and 3 with wild Pokémon and young trainer battles
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
