#ifndef GUARD_POKEMON_POWDER_JAR_H
#define GUARD_POKEMON_POWDER_JAR_H

#include "constants/pokemon_powder_jar.h"

#define POKEMON_POWDER_JAR_BLOCK_STATUS       TRUE // When TRUE, a Pokémon that is afflicted by a non-volatile status decision cannot get a status condition from the Pokemon Powder Jar.

enum PokemonPowderJarResultCodes PokemonPowderJar_TryInflictStatus(struct Pokemon*, u32);
u32 PokemonPowderJar_ConvertMenuPosToStatus(u32);
void PokemonPowderJar_ConstructStatusFailureMessage(struct Pokemon*);
void PokemonPowderJar_ConstructSuccessMessage(struct Pokemon*, u32);
void PokemonPowderJar_ConstructAbilityFailureMessage(struct Pokemon*, u32);
void PokemonPowderJar_ConstructTypeFailureMessage(struct Pokemon*, u32, enum PokemonPowderJarResultCodes);
void Task_UsePokemonPowderJarFromField(u8);

#endif // GUARD_POKEMON_POWDER_JAR_H