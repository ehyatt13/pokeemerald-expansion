#include "global.h"
#include "battle.h"
#include "battle_pike.h"
#include "pokemon_powder_jar.h"
#include "main.h"
#include "menu.h"
#include "party_menu.h"
#include "sound.h"
#include "string_util.h"
#include "constants/abilities.h"
#include "constants/battle.h"
#include "constants/item_effects.h"
#include "constants/songs.h"

static const void PokemonPowderJar_BufferBlockedStatusMessage(u32 status)
{
    switch (status)
    {
        case STATUS1_SLEEP:
            StringCopy(gStringVar3,COMPOUND_STRING("asleep"));
            break;
        case STATUS1_TOXIC_POISON:
            StringCopy(gStringVar3,COMPOUND_STRING("poisoned"));
            break;
        case STATUS1_BURN:
            StringCopy(gStringVar3,COMPOUND_STRING("burned"));
            break;
        case STATUS1_FROSTBITE:
            StringCopy(gStringVar3,COMPOUND_STRING("frostbit"));
            break;
        case STATUS1_FREEZE:
            StringCopy(gStringVar3,COMPOUND_STRING("frozen"));
            break;
        case STATUS1_PARALYSIS:
            StringCopy(gStringVar3,COMPOUND_STRING("paralyzed"));
            break;
        default:
            StringCopy(gStringVar3,COMPOUND_STRING("new status!"));
            break;
    }
}
static const void PokemonPowderJar_BufferStatusFailureText(u32 status)
{
    switch (status)
    {
        case STATUS1_SLEEP:
            StringCopy(gStringVar3,COMPOUND_STRING("falling asleep"));
            break;
        case STATUS1_TOXIC_POISON:
            StringCopy(gStringVar3,COMPOUND_STRING("being poisoned"));
            break;
        case STATUS1_BURN:
            StringCopy(gStringVar3,COMPOUND_STRING("being burned"));
            break;
        case STATUS1_FROSTBITE:
            StringCopy(gStringVar3,COMPOUND_STRING("getting frostbite"));
            break;
        case STATUS1_FREEZE:
            StringCopy(gStringVar3,COMPOUND_STRING("being frozen"));
            break;
        case STATUS1_PARALYSIS:
            StringCopy(gStringVar3,COMPOUND_STRING("being paralyzed"));
            break;
        default:
            StringCopy(gStringVar3,COMPOUND_STRING("new status!"));
            break;
    }
}

static void PokemonPowderJar_BufferStatusAfflictionText(u32 status)
{
    switch (status)
    {
        case STATUS1_SLEEP:
            StringCopy(gStringVar2, COMPOUND_STRING("fell asleep"));
            break;
        case STATUS1_TOXIC_POISON:
            StringCopy(gStringVar2, COMPOUND_STRING("was poisoned"));
            break;
        case STATUS1_BURN:
            StringCopy(gStringVar2, COMPOUND_STRING("was burned"));
            break;
        case STATUS1_FROSTBITE:
            StringCopy(gStringVar2, COMPOUND_STRING("got frostbite"));
            break;
        case STATUS1_FREEZE:
            StringCopy(gStringVar2, COMPOUND_STRING("was frozen solid"));
            break;
        case STATUS1_PARALYSIS:
            StringCopy(gStringVar2, COMPOUND_STRING("is paralyzed"));
            break;
        default:
            StringCopy(gStringVar2, COMPOUND_STRING("new status!"));
    }
}

static bool32 PokemonPowderJar_DoesTypeBlockStatus(u32 species, u32 typeIndex, u32 status)
{
    u32 type = gSpeciesInfo[species].types[typeIndex];
    switch (status)
    {
        case STATUS1_TOXIC_POISON:
            return (type == TYPE_STEEL || type == TYPE_POISON);
        case STATUS1_FREEZE:
        case STATUS1_FROSTBITE:
            return (type == TYPE_ICE);
        case STATUS1_PARALYSIS:
            return (B_PARALYZE_ELECTRIC >= GEN_6 && type == TYPE_ELECTRIC);
        case STATUS1_BURN:
            return (type == TYPE_FIRE);
        default:
            return FALSE;
    }
}

static bool8 PokemonPowderJar_DoesAbilityPreventStatus(struct Pokemon *mon, u32 status)
{
    u16 ability = GetMonAbility(mon);
    bool8 ret = FALSE;

    if (ability == ABILITY_COMATOSE)
        return TRUE;

    switch (status)
    {
    case STATUS1_FREEZE:
    case STATUS1_FROSTBITE:
        if (ability == ABILITY_MAGMA_ARMOR)
            ret = TRUE;
        break;
    case STATUS1_BURN:
        if (ability == ABILITY_WATER_VEIL || ability == ABILITY_WATER_BUBBLE)
            ret = TRUE;
        break;
    case STATUS1_PARALYSIS:
        if (ability == ABILITY_LIMBER)
            ret = TRUE;
        break;
    case STATUS1_SLEEP:
        if (ability == ABILITY_INSOMNIA || ability == ABILITY_VITAL_SPIRIT)
            ret = TRUE;
        break;
    case STATUS1_TOXIC_POISON:
        if (ability == ABILITY_IMMUNITY || ability == ABILITY_PASTEL_VEIL)
            ret = TRUE;
        break;
    }
    return ret;
}
static bool32 PokemonPowderJar_ShouldExistingStatusBlock(struct Pokemon *mon)
{
    return POKEMON_POWDER_JAR_BLOCK_STATUS && (GetMonData(mon, MON_DATA_STATUS) & STATUS1_ANY);
}

enum PokemonPowderJarResultCodes PokemonPowderJar_TryInflictStatus(struct Pokemon *mon, u32 status)
{
    u32 clearStatus;
    u32 species = GetMonData(mon,MON_DATA_SPECIES);

    if (PokemonPowderJar_ShouldExistingStatusBlock(mon))
        return POKEMON_POWDER_JAR_RESULT_FAIL_HAS_STATUS;

    if (PokemonPowderJar_DoesAbilityPreventStatus(mon, status))
        return POKEMON_POWDER_JAR_RESULT_FAIL_ABILITY;

    if (PokemonPowderJar_DoesTypeBlockStatus(species, 0, status))
        return POKEMON_POWDER_JAR_RESULT_FAIL_TYPE_0;

    if (PokemonPowderJar_DoesTypeBlockStatus(species, 1, status))
        return POKEMON_POWDER_JAR_RESULT_FAIL_TYPE_1;

    clearStatus = STATUS1_NONE;
    SetMonData(mon, MON_DATA_STATUS, &clearStatus);
    SetMonData(mon, MON_DATA_STATUS, &status);

    return POKEMON_POWDER_JAR_RESULT_SUCCESS;
}

u32 PokemonPowderJar_ConvertMenuPosToStatus(u32 pos)
{
    static const u32 statusMap[] = {
        STATUS1_BURN,
        STATUS1_PARALYSIS,
        STATUS1_TOXIC_POISON,
#if B_USE_FROSTBITE == TRUE
        STATUS1_FROSTBITE,
#else
        STATUS1_FREEZE,
#endif
        STATUS1_SLEEP,
        STATUS1_NONE
    };

    return statusMap[pos];
}

void PokemonPowderJar_ConstructSuccessMessage(struct Pokemon* mon, u32 status)
{
    GetMonNickname(mon, gStringVar1);
    PokemonPowderJar_BufferStatusAfflictionText(status);
    StringExpandPlaceholders(gStringVar4, COMPOUND_STRING("{STR_VAR_1} {STR_VAR_2}!{PAUSE_UNTIL_PRESS}"));
}

void PokemonPowderJar_ConstructTypeFailureMessage(struct Pokemon *mon, u32 status, enum PokemonPowderJarResultCodes result)
{
    u32 type = gSpeciesInfo[GetMonData(mon, MON_DATA_SPECIES)].types[result];
    GetMonNickname(mon, gStringVar1);
    StringCopy(gStringVar2, gTypesInfo[type].name);
    PokemonPowderJar_BufferStatusFailureText(status);
    StringExpandPlaceholders(gStringVar4, COMPOUND_STRING("{STR_VAR_1}'s {STR_VAR_2}-type prevents it from\n{STR_VAR_3}!{PAUSE_UNTIL_PRESS}"));
}

void PokemonPowderJar_ConstructAbilityFailureMessage(struct Pokemon* mon, u32 status)
{
    u32 ability = GetAbilityBySpecies(GetMonData(mon, MON_DATA_SPECIES), GetMonData(mon, MON_DATA_ABILITY_NUM));

    GetMonNickname(mon, gStringVar1);
    StringCopy(gStringVar2, gAbilitiesInfo[ability].name);
    PokemonPowderJar_BufferStatusFailureText(status);
    StringExpandPlaceholders(gStringVar4, COMPOUND_STRING("{STR_VAR_1}'s {STR_VAR_2}\nprevents it from {STR_VAR_3}!{PAUSE_UNTIL_PRESS}"));
}

void PokemonPowderJar_ConstructStatusFailureMessage(struct Pokemon* mon)
{
    u32 status = GetMonData(mon, MON_DATA_STATUS);
    GetMonNickname(mon, gStringVar1);
    PokemonPowderJar_BufferBlockedStatusMessage(status);
    StringExpandPlaceholders(gStringVar4, COMPOUND_STRING("{STR_VAR_1} is already {STR_VAR_3}!{PAUSE_UNTIL_PRESS}"));
}

void Task_UsePokemonPowderJarFromField(u8 taskId)
{
    ItemUseCB_PokemonPowderJar(taskId,NULL);
}