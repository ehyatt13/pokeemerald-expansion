
LittlerootTown_SecondLab_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, LittlerootTown_SecondLab_OnTransition
	map_script MAP_SCRIPT_ON_FRAME_TABLE, LittlerootTown_SecondLab_OnFrame
	.byte 0

LittlerootTown_SecondLab_OnTransition:
	call_if_eq VAR_LITTLEROOT_INTRO_STATE, 9, LittlerootTown_SecondLab_MoveBirchToDoor
	end

LittlerootTown_SecondLab_MoveBirchToDoor:
	setobjectxyperm LOCALID_LAB_BIRCH, 6, 12
	setobjectmovementtype LOCALID_LAB_BIRCH, MOVEMENT_TYPE_FACE_UP
	return

LittlerootTown_SecondLab_OnFrame:
	map_script_2 VAR_LITTLEROOT_INTRO_STATE, 9, LittlerootTown_SecondLab_EventScript_EnterLab
	.2byte 0

LittlerootTown_SecondLab_EventScript_EnterLab::
	lockall
	applymovement LOCALID_LAB_BIRCH, LittlerootTown_SecondLab_Movement_ApproachTable
	applymovement LOCALID_PLAYER, LittlerootTown_SecondLab_Movement_ApproachTable
	waitmovement 0
	applymovement LOCALID_LAB_BIRCH, Common_Movement_WalkInPlaceFasterRight
	applymovement LOCALID_PLAYER, Common_Movement_WalkInPlaceFasterLeft
	waitmovement 0
	msgbox LittlerootTown_SecondLab_Text_BirchPickOne
	closemessage
	applymovement LOCALID_LAB_BIRCH, LittlerootTown_SecondLab_Movement_BirchToTable
	waitmovement 0
    setvar VAR_LITTLEROOT_INTRO_STATE, 10
    setvar VAR_TEMP_9, 2
	releaseall
	end

LittlerootTown_SecondLab_Movement_ApproachTable:
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	walk_up
	step_end

LittlerootTown_SecondLab_Movement_BirchToTable:
	walk_up
	walk_up
	walk_right
	walk_right
	walk_in_place_faster_down
	step_end

LittlerootTown_SecondLab_Text_BirchPickOne:
	.string "PROF. BIRCH: Well, here we are {PLAYER}.\n"
	.string "As you can see, there are 3 POKéBALLS\l"
	.string "on the table.\p"
	.string "Each one contains a POKéMON of the\n"
	.string "GRASS, FIRE, or WATER type.\p"
	.string "The three currently displayed are from\n"
	.string "our region, HOENN.\p"
	.string "Take a look and decide which one you\n"
	.string "like best.\p"
	.string "However, if you find that you are not\n"
	.string "drawn to any of the three POKéMON, let\l"
	.string "me know and I can show you some POKéMON\l"
	.string "from other regions that I have been\l"
    .string "studying.$"

LittlerootTown_SecondLab_Text_BirchQuestion:
	.string "PROF. BIRCH: Would you like to see a\n"
	.string "different region's POKéMON?$"

LittlerootTown_SecondLab_Text_Wise:
	.string "Choose wisely, {PLAYER}.$"

LittlerootTown_SecondLab_Text_AlreadyPicked:
	.string "PROF. BIRCH: You've already picked\n"
    .string "a POKéMON!$"

LittlerootTown_SecondLab_Text_WhichRegion:
	.string "Which region's POKéMON would you like to\n"
	.string "see instead?$"

LittlerootTown_SecondLab_Text_ReceivedStarter:
	.string "{PLAYER} received the {STR_VAR_1}\n"
	.string "from PROF. BIRCH!$"

LittlerootTown_SecondLab_Text_DeclineStarter:
    .string "PROF. BIRCH: Take your time.$"

LittlerootTown_SecondLab_Text_RegionAlreadyShown:
    .string "That region's POKéMON are already being\n"
    .string "shown.$"

LittlerootTown_SecondLab_Text_SwapText:
    .string "Okay, I've swapped in a new batch of\n"
    .string "POKéMON from the region you selected.$"

LittlerootTown_SecondLab_EventScript_Birch::
	lockall
	faceplayer
	goto_if_unset FLAG_HIDE_GRASS_STARTER, LittlerootTown_SecondLab_EventScript_Birch_4
LittlerootTown_SecondLab_EventScript_Birch_3:
	msgbox LittlerootTown_SecondLab_Text_AlreadyPicked
LittlerootTown_SecondLab_EventScript_Birch_1:
	waitmessage
	releaseall
	end

LittlerootTown_SecondLab_EventScript_Birch_2:
	msgbox LittlerootTown_SecondLab_Text_BirchQuestion, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_10
LittlerootTown_SecondLab_EventScript_Birch_9:
	msgbox LittlerootTown_SecondLab_Text_Wise
	goto LittlerootTown_SecondLab_EventScript_Birch_1

LittlerootTown_SecondLab_EventScript_Birch_4:
	goto_if_unset FLAG_HIDE_FIRE_STARTER, LittlerootTown_SecondLab_EventScript_Birch_6
	goto LittlerootTown_SecondLab_EventScript_Birch_3

LittlerootTown_SecondLab_EventScript_Birch_6:
	goto_if_unset FLAG_HIDE_WATER_STARTER, LittlerootTown_SecondLab_EventScript_Birch_2
	goto LittlerootTown_SecondLab_EventScript_Birch_3

LittlerootTown_SecondLab_EventScript_Birch_10:
	message LittlerootTown_SecondLab_Text_WhichRegion
	multichoicegrid 25, 5, MULTI_STARTER_REGION_CHOICE, 3, 1
	closemessage
	compare VAR_RESULT, VAR_TEMP_9
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_12
	compare VAR_RESULT, 0
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_16
	compare VAR_RESULT, 1
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_17
	compare VAR_RESULT, 2
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_18
	compare VAR_RESULT, 3
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_19
	compare VAR_RESULT, 4
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_20
	compare VAR_RESULT, 5
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_21
	compare VAR_RESULT, 6
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_22
	compare VAR_RESULT, 7
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_23
	compare VAR_RESULT, 8
	goto_if_eq LittlerootTown_SecondLab_EventScript_Birch_24
LittlerootTown_SecondLab_EventScript_Birch_15:
	call LittlerootTown_SecondLab_EventScript_BirchSwap
	goto LittlerootTown_SecondLab_EventScript_Birch_9

LittlerootTown_SecondLab_EventScript_Birch_12:
	msgbox LittlerootTown_SecondLab_Text_RegionAlreadyShown
	goto LittlerootTown_SecondLab_EventScript_Birch_9

LittlerootTown_SecondLab_EventScript_Birch_16:
	setvar VAR_TEMP_9, 0
	goto LittlerootTown_SecondLab_EventScript_Birch_15

LittlerootTown_SecondLab_EventScript_Birch_17:
	setvar VAR_TEMP_9, 1
	goto LittlerootTown_SecondLab_EventScript_Birch_15

LittlerootTown_SecondLab_EventScript_Birch_18:
	setvar VAR_TEMP_9, 2
	goto LittlerootTown_SecondLab_EventScript_Birch_15

LittlerootTown_SecondLab_EventScript_Birch_19:
	setvar VAR_TEMP_9, 3
	goto LittlerootTown_SecondLab_EventScript_Birch_15

LittlerootTown_SecondLab_EventScript_Birch_20:
	setvar VAR_TEMP_9, 4
	goto LittlerootTown_SecondLab_EventScript_Birch_15

LittlerootTown_SecondLab_EventScript_Birch_21:
	setvar VAR_TEMP_9, 5
	goto LittlerootTown_SecondLab_EventScript_Birch_15

LittlerootTown_SecondLab_EventScript_Birch_22:
	setvar VAR_TEMP_9, 6
	goto LittlerootTown_SecondLab_EventScript_Birch_15

LittlerootTown_SecondLab_EventScript_Birch_23:
	setvar VAR_TEMP_9, 7
	goto LittlerootTown_SecondLab_EventScript_Birch_15

LittlerootTown_SecondLab_EventScript_Birch_24:
	setvar VAR_TEMP_9, 8
	goto LittlerootTown_SecondLab_EventScript_Birch_15


LittlerootTown_SecondLab_EventScript_BirchSwap::
	fadescreen FADE_TO_BLACK
	delay 16
	fadescreen FADE_FROM_BLACK
	msgbox LittlerootTown_SecondLab_Text_SwapText
	return


LittlerootTown_SecondLab_EventScript_GrassBall::
	lockall
	goto_if_unset FLAG_HIDE_GRASS_STARTER, LittlerootTown_SecondLab_EventScript_GrassBall_4
LittlerootTown_SecondLab_EventScript_GrassBall_3:
	msgbox LittlerootTown_SecondLab_Text_AlreadyPicked
LittlerootTown_SecondLab_EventScript_GrassBall_1:
	waitmessage
	releaseall
	end

LittlerootTown_SecondLab_EventScript_GrassBall_2:
	compare VAR_TEMP_9, 0
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassBall_10
	compare VAR_TEMP_9, 1
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassBall_11
	compare VAR_TEMP_9, 2
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassBall_12
	compare VAR_TEMP_9, 3
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassBall_13
	compare VAR_TEMP_9, 4
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassBall_14
	compare VAR_TEMP_9, 5
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassBall_15
	compare VAR_TEMP_9, 6
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassBall_16
	compare VAR_TEMP_9, 7
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassBall_17
	compare VAR_TEMP_9, 8
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassBall_18
LittlerootTown_SecondLab_EventScript_GrassBall_9:
	bufferspeciesname STR_VAR_1, VAR_TEMP_8
	call LittlerootTown_SecondLab_EventScript_GrassStarter
	goto LittlerootTown_SecondLab_EventScript_GrassBall_1

LittlerootTown_SecondLab_EventScript_GrassBall_4:
	goto_if_unset FLAG_HIDE_FIRE_STARTER, LittlerootTown_SecondLab_EventScript_GrassBall_6
	goto LittlerootTown_SecondLab_EventScript_GrassBall_3

LittlerootTown_SecondLab_EventScript_GrassBall_6:
	goto_if_unset FLAG_HIDE_WATER_STARTER, LittlerootTown_SecondLab_EventScript_GrassBall_2
	goto LittlerootTown_SecondLab_EventScript_GrassBall_3

LittlerootTown_SecondLab_EventScript_GrassBall_10:
	setvar VAR_TEMP_8, SPECIES_BULBASAUR
	goto LittlerootTown_SecondLab_EventScript_GrassBall_9

LittlerootTown_SecondLab_EventScript_GrassBall_11:
	setvar VAR_TEMP_8, SPECIES_CHIKORITA
	goto LittlerootTown_SecondLab_EventScript_GrassBall_9

LittlerootTown_SecondLab_EventScript_GrassBall_12:
	setvar VAR_TEMP_8, SPECIES_TREECKO
	goto LittlerootTown_SecondLab_EventScript_GrassBall_9

LittlerootTown_SecondLab_EventScript_GrassBall_13:
	setvar VAR_TEMP_8, SPECIES_TURTWIG
	goto LittlerootTown_SecondLab_EventScript_GrassBall_9

LittlerootTown_SecondLab_EventScript_GrassBall_14:
	setvar VAR_TEMP_8, SPECIES_SNIVY
	goto LittlerootTown_SecondLab_EventScript_GrassBall_9

LittlerootTown_SecondLab_EventScript_GrassBall_15:
	setvar VAR_TEMP_8, SPECIES_CHESPIN
	goto LittlerootTown_SecondLab_EventScript_GrassBall_9

LittlerootTown_SecondLab_EventScript_GrassBall_16:
	setvar VAR_TEMP_8, SPECIES_ROWLET
	goto LittlerootTown_SecondLab_EventScript_GrassBall_9

LittlerootTown_SecondLab_EventScript_GrassBall_17:
	setvar VAR_TEMP_8, SPECIES_GROOKEY
	goto LittlerootTown_SecondLab_EventScript_GrassBall_9

LittlerootTown_SecondLab_EventScript_GrassBall_18:
	setvar VAR_TEMP_8, SPECIES_SPRIGATITO
	goto LittlerootTown_SecondLab_EventScript_GrassBall_9


LittlerootTown_SecondLab_EventScript_FireBall::
	lockall
	goto_if_unset FLAG_HIDE_GRASS_STARTER, LittlerootTown_SecondLab_EventScript_FireBall_4
LittlerootTown_SecondLab_EventScript_FireBall_3:
	msgbox LittlerootTown_SecondLab_Text_AlreadyPicked
LittlerootTown_SecondLab_EventScript_FireBall_1:
	waitmessage
	releaseall
	end

LittlerootTown_SecondLab_EventScript_FireBall_2:
	compare VAR_TEMP_9, 0
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireBall_10
	compare VAR_TEMP_9, 1
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireBall_11
	compare VAR_TEMP_9, 2
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireBall_12
	compare VAR_TEMP_9, 3
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireBall_13
	compare VAR_TEMP_9, 4
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireBall_14
	compare VAR_TEMP_9, 5
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireBall_15
	compare VAR_TEMP_9, 6
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireBall_16
	compare VAR_TEMP_9, 7
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireBall_17
	compare VAR_TEMP_9, 8
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireBall_18
LittlerootTown_SecondLab_EventScript_FireBall_9:
	bufferspeciesname STR_VAR_1, VAR_TEMP_8
	call LittlerootTown_SecondLab_EventScript_FireStarter
	goto LittlerootTown_SecondLab_EventScript_FireBall_1

LittlerootTown_SecondLab_EventScript_FireBall_4:
	goto_if_unset FLAG_HIDE_FIRE_STARTER, LittlerootTown_SecondLab_EventScript_FireBall_6
	goto LittlerootTown_SecondLab_EventScript_FireBall_3

LittlerootTown_SecondLab_EventScript_FireBall_6:
	goto_if_unset FLAG_HIDE_WATER_STARTER, LittlerootTown_SecondLab_EventScript_FireBall_2
	goto LittlerootTown_SecondLab_EventScript_FireBall_3

LittlerootTown_SecondLab_EventScript_FireBall_10:
	setvar VAR_TEMP_8, SPECIES_CHARMANDER
	goto LittlerootTown_SecondLab_EventScript_FireBall_9

LittlerootTown_SecondLab_EventScript_FireBall_11:
	setvar VAR_TEMP_8, SPECIES_CYNDAQUIL
	goto LittlerootTown_SecondLab_EventScript_FireBall_9

LittlerootTown_SecondLab_EventScript_FireBall_12:
	setvar VAR_TEMP_8, SPECIES_TORCHIC
	goto LittlerootTown_SecondLab_EventScript_FireBall_9

LittlerootTown_SecondLab_EventScript_FireBall_13:
	setvar VAR_TEMP_8, SPECIES_CHIMCHAR
	goto LittlerootTown_SecondLab_EventScript_FireBall_9

LittlerootTown_SecondLab_EventScript_FireBall_14:
	setvar VAR_TEMP_8, SPECIES_TEPIG
	goto LittlerootTown_SecondLab_EventScript_FireBall_9

LittlerootTown_SecondLab_EventScript_FireBall_15:
	setvar VAR_TEMP_8, SPECIES_FENNEKIN
	goto LittlerootTown_SecondLab_EventScript_FireBall_9

LittlerootTown_SecondLab_EventScript_FireBall_16:
	setvar VAR_TEMP_8, SPECIES_LITTEN
	goto LittlerootTown_SecondLab_EventScript_FireBall_9

LittlerootTown_SecondLab_EventScript_FireBall_17:
	setvar VAR_TEMP_8, SPECIES_SCORBUNNY
	goto LittlerootTown_SecondLab_EventScript_FireBall_9

LittlerootTown_SecondLab_EventScript_FireBall_18:
	setvar VAR_TEMP_8, SPECIES_FUECOCO
	goto LittlerootTown_SecondLab_EventScript_FireBall_9


LittlerootTown_SecondLab_EventScript_WaterBall::
	lockall
	goto_if_unset FLAG_HIDE_GRASS_STARTER, LittlerootTown_SecondLab_EventScript_WaterBall_4
LittlerootTown_SecondLab_EventScript_WaterBall_3:
	msgbox LittlerootTown_SecondLab_Text_AlreadyPicked
LittlerootTown_SecondLab_EventScript_WaterBall_1:
	waitmessage
	releaseall
	end

LittlerootTown_SecondLab_EventScript_WaterBall_2:
	compare VAR_TEMP_9, 0
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterBall_10
	compare VAR_TEMP_9, 1
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterBall_11
	compare VAR_TEMP_9, 2
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterBall_12
	compare VAR_TEMP_9, 3
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterBall_13
	compare VAR_TEMP_9, 4
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterBall_14
	compare VAR_TEMP_9, 5
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterBall_15
	compare VAR_TEMP_9, 6
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterBall_16
	compare VAR_TEMP_9, 7
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterBall_17
	compare VAR_TEMP_9, 8
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterBall_18
LittlerootTown_SecondLab_EventScript_WaterBall_9:
	bufferspeciesname STR_VAR_1, VAR_TEMP_8
	call LittlerootTown_SecondLab_EventScript_WaterStarter
	goto LittlerootTown_SecondLab_EventScript_WaterBall_1

LittlerootTown_SecondLab_EventScript_WaterBall_4:
	goto_if_unset FLAG_HIDE_FIRE_STARTER, LittlerootTown_SecondLab_EventScript_WaterBall_6
	goto LittlerootTown_SecondLab_EventScript_WaterBall_3

LittlerootTown_SecondLab_EventScript_WaterBall_6:
	goto_if_unset FLAG_HIDE_WATER_STARTER, LittlerootTown_SecondLab_EventScript_WaterBall_2
	goto LittlerootTown_SecondLab_EventScript_WaterBall_3

LittlerootTown_SecondLab_EventScript_WaterBall_10:
	setvar VAR_TEMP_8, SPECIES_SQUIRTLE
	goto LittlerootTown_SecondLab_EventScript_WaterBall_9

LittlerootTown_SecondLab_EventScript_WaterBall_11:
	setvar VAR_TEMP_8, SPECIES_TOTODILE
	goto LittlerootTown_SecondLab_EventScript_WaterBall_9

LittlerootTown_SecondLab_EventScript_WaterBall_12:
	setvar VAR_TEMP_8, SPECIES_MUDKIP
	goto LittlerootTown_SecondLab_EventScript_WaterBall_9

LittlerootTown_SecondLab_EventScript_WaterBall_13:
	setvar VAR_TEMP_8, SPECIES_PIPLUP
	goto LittlerootTown_SecondLab_EventScript_WaterBall_9

LittlerootTown_SecondLab_EventScript_WaterBall_14:
	setvar VAR_TEMP_8, SPECIES_OSHAWOTT
	goto LittlerootTown_SecondLab_EventScript_WaterBall_9

LittlerootTown_SecondLab_EventScript_WaterBall_15:
	setvar VAR_TEMP_8, SPECIES_FROAKIE
	goto LittlerootTown_SecondLab_EventScript_WaterBall_9

LittlerootTown_SecondLab_EventScript_WaterBall_16:
	setvar VAR_TEMP_8, SPECIES_POPPLIO
	goto LittlerootTown_SecondLab_EventScript_WaterBall_9

LittlerootTown_SecondLab_EventScript_WaterBall_17:
	setvar VAR_TEMP_8, SPECIES_SOBBLE
	goto LittlerootTown_SecondLab_EventScript_WaterBall_9

LittlerootTown_SecondLab_EventScript_WaterBall_18:
	setvar VAR_TEMP_8, SPECIES_QUAXLY
	goto LittlerootTown_SecondLab_EventScript_WaterBall_9


LittlerootTown_SecondLab_EventScript_GrassStarter::
	showmonpic VAR_TEMP_8, 10, 3
	playmoncry VAR_TEMP_8, CRY_MODE_NORMAL
	msgbox LittlerootTown_SecondLab_EventScript_GrassStarter_Text_0, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassStarter_1
	hidemonpic
	msgbox LittlerootTown_SecondLab_Text_DeclineStarter
	return

LittlerootTown_SecondLab_EventScript_GrassStarter_1:
	copyvar VAR_TEMP_TRANSFERRED_SPECIES, VAR_TEMP_8
	givemon VAR_TEMP_8, 5
	compare VAR_RESULT, MON_GIVEN_TO_PARTY
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassStarter_4
	compare VAR_RESULT, MON_GIVEN_TO_PC
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassStarter_5
	hidemonpic
	goto Common_EventScript_NoMoreRoomForPokemon
	return

LittlerootTown_SecondLab_EventScript_GrassStarter_4:
	playfanfare MUS_OBTAIN_ITEM
	message LittlerootTown_SecondLab_Text_ReceivedStarter
	waitmessage
	waitfanfare
	removeobject 2
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassStarter_10
LittlerootTown_SecondLab_EventScript_GrassStarter_9:
	hidemonpic
	setflag FLAG_HIDE_GRASS_STARTER
	setflag FLAG_SYS_POKEMON_GET
	setvar VAR_STARTER_MON, 0
	goto LittlerootTown_SecondLab_EventScript_BirchAfterChoice
	return

LittlerootTown_SecondLab_EventScript_GrassStarter_5:
	playfanfare MUS_OBTAIN_ITEM
	message LittlerootTown_SecondLab_Text_ReceivedStarter
	waitmessage
	waitfanfare
	removeobject 2
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_GrassStarter_13
LittlerootTown_SecondLab_EventScript_GrassStarter_12:
	hidemonpic
	setflag FLAG_HIDE_GRASS_STARTER
	setflag FLAG_SYS_POKEMON_GET
	setvar VAR_STARTER_MON, 0
	goto LittlerootTown_SecondLab_EventScript_BirchAfterChoice
	return

LittlerootTown_SecondLab_EventScript_GrassStarter_10:
	call Common_EventScript_GetGiftMonPartySlot
	call Common_EventScript_NameReceivedPartyMon
	goto LittlerootTown_SecondLab_EventScript_GrassStarter_9

LittlerootTown_SecondLab_EventScript_GrassStarter_13:
	call Common_EventScript_NameReceivedBoxMon
	call Common_EventScript_TransferredToPC
	goto LittlerootTown_SecondLab_EventScript_GrassStarter_12


LittlerootTown_SecondLab_EventScript_FireStarter::
	showmonpic VAR_TEMP_8, 10, 3
	playmoncry VAR_TEMP_8, CRY_MODE_NORMAL
	msgbox LittlerootTown_SecondLab_EventScript_GrassStarter_Text_0, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireStarter_1
	hidemonpic
	msgbox LittlerootTown_SecondLab_Text_DeclineStarter
	return

LittlerootTown_SecondLab_EventScript_FireStarter_1:
	copyvar VAR_TEMP_TRANSFERRED_SPECIES, VAR_TEMP_8
	givemon VAR_TEMP_8, 5
	compare VAR_RESULT, MON_GIVEN_TO_PARTY
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireStarter_4
	compare VAR_RESULT, MON_GIVEN_TO_PC
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireStarter_5
	hidemonpic
	goto Common_EventScript_NoMoreRoomForPokemon
	return

LittlerootTown_SecondLab_EventScript_FireStarter_4:
	playfanfare MUS_OBTAIN_ITEM
	message LittlerootTown_SecondLab_Text_ReceivedStarter
	waitmessage
	waitfanfare
	removeobject 3
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireStarter_10
LittlerootTown_SecondLab_EventScript_FireStarter_9:
	hidemonpic
	setflag FLAG_HIDE_FIRE_STARTER
	setflag FLAG_SYS_POKEMON_GET
	setvar VAR_STARTER_MON, 1
	goto LittlerootTown_SecondLab_EventScript_BirchAfterChoice
	return

LittlerootTown_SecondLab_EventScript_FireStarter_5:
	playfanfare MUS_OBTAIN_ITEM
	message LittlerootTown_SecondLab_Text_ReceivedStarter
	waitmessage
	waitfanfare
	removeobject 3
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_FireStarter_13
LittlerootTown_SecondLab_EventScript_FireStarter_12:
	hidemonpic
	setflag FLAG_HIDE_FIRE_STARTER
	setflag FLAG_SYS_POKEMON_GET
	setvar VAR_STARTER_MON, 1
	goto LittlerootTown_SecondLab_EventScript_BirchAfterChoice
	return

LittlerootTown_SecondLab_EventScript_FireStarter_10:
	call Common_EventScript_GetGiftMonPartySlot
	call Common_EventScript_NameReceivedPartyMon
	goto LittlerootTown_SecondLab_EventScript_FireStarter_9

LittlerootTown_SecondLab_EventScript_FireStarter_13:
	call Common_EventScript_NameReceivedBoxMon
	call Common_EventScript_TransferredToPC
	goto LittlerootTown_SecondLab_EventScript_FireStarter_12


LittlerootTown_SecondLab_EventScript_WaterStarter::
	showmonpic VAR_TEMP_8, 10, 3
	playmoncry VAR_TEMP_8, CRY_MODE_NORMAL
	msgbox LittlerootTown_SecondLab_EventScript_GrassStarter_Text_0, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterStarter_1
	hidemonpic
	msgbox LittlerootTown_SecondLab_Text_DeclineStarter
	return

LittlerootTown_SecondLab_EventScript_WaterStarter_1:
	copyvar VAR_TEMP_TRANSFERRED_SPECIES, VAR_TEMP_8
	givemon VAR_TEMP_8, 5
	compare VAR_RESULT, MON_GIVEN_TO_PARTY
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterStarter_4
	compare VAR_RESULT, MON_GIVEN_TO_PC
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterStarter_5
	hidemonpic
	goto Common_EventScript_NoMoreRoomForPokemon
	return

LittlerootTown_SecondLab_EventScript_WaterStarter_4:
	playfanfare MUS_OBTAIN_ITEM
	message LittlerootTown_SecondLab_Text_ReceivedStarter
	waitmessage
	waitfanfare
	removeobject 4
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterStarter_10
LittlerootTown_SecondLab_EventScript_WaterStarter_9:
	hidemonpic
	setflag FLAG_HIDE_WATER_STARTER
	setflag FLAG_SYS_POKEMON_GET
	setvar VAR_STARTER_MON, 2
	goto LittlerootTown_SecondLab_EventScript_BirchAfterChoice
	return

LittlerootTown_SecondLab_EventScript_WaterStarter_5:
	playfanfare MUS_OBTAIN_ITEM
	message LittlerootTown_SecondLab_Text_ReceivedStarter
	waitmessage
	waitfanfare
	removeobject 4
	msgbox gText_NicknameThisPokemon, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq LittlerootTown_SecondLab_EventScript_WaterStarter_13
LittlerootTown_SecondLab_EventScript_WaterStarter_12:
	hidemonpic
	setflag FLAG_HIDE_WATER_STARTER
	setflag FLAG_SYS_POKEMON_GET
	setvar VAR_STARTER_MON, 2
	goto LittlerootTown_SecondLab_EventScript_BirchAfterChoice
	return

LittlerootTown_SecondLab_EventScript_WaterStarter_10:
	call Common_EventScript_GetGiftMonPartySlot
	call Common_EventScript_NameReceivedPartyMon
	goto LittlerootTown_SecondLab_EventScript_WaterStarter_9

LittlerootTown_SecondLab_EventScript_WaterStarter_13:
	call Common_EventScript_NameReceivedBoxMon
	call Common_EventScript_TransferredToPC
	goto LittlerootTown_SecondLab_EventScript_WaterStarter_12


LittlerootTown_SecondLab_EventScript_BirchAfterChoice::
	lock
	applymovement LOCALID_LAB_BIRCH, LittlerootTown_SecondLab_EventScript_BirchAfterChoice_Movement_0
	delay 15
	applymovement LOCALID_PLAYER, LittlerootTown_SecondLab_EventScript_BirchAfterChoice_Movement_1
	delay 15
	msgbox TestBattle
	closemessage
	trainerbattle_no_intro TRAINER_SECOND_LAB_BIRCH, SecondLab_Text_Birch_Defeat
	bufferspeciesname STR_VAR_1, VAR_TEMP_8
	msgbox GoSeeRival
	closemessage
	clearflag FLAG_HIDE_ROUTE_101_BOY
	setvar VAR_BIRCH_LAB_STATE, 3
	setflag FLAG_HIDE_ROUTE_101_BIRCH_ZIGZAGOON_BATTLE
	clearflag FLAG_HIDE_LITTLEROOT_TOWN_BIRCHS_LAB_BIRCH
	setflag FLAG_HIDE_ROUTE_101_BIRCH_STARTERS_BAG
	setflag FLAG_RESCUED_BIRCH
	setflag FLAG_HIDE_ROUTE_101_ZIGZAGOON
	setvar VAR_ROUTE101_STATE, 3
	setvar VAR_LITTLEROOT_TOWN_STATE, 2
	checkplayergender
	call_if_eq VAR_RESULT, MALE, Route101_EventScript_HideMayInBedroom
	call_if_eq VAR_RESULT, FEMALE, Route101_EventScript_HideBrendanInBedroom
	release
	return


LittlerootTown_SecondLab_EventScript_DontLeave::
	lock
	msgbox WhereAreYouGoing
	closemessage
	applymovement LOCALID_PLAYER, LittlerootTown_SecondLab_EventScript_DontLeave_Movement_0
	waitmovement 0
	release
	return


LittlerootTown_SecondLab_EventScript_BirchAfterChoice_Movement_0:
	walk_in_place_faster_left
	step_end

LittlerootTown_SecondLab_EventScript_BirchAfterChoice_Movement_1:
	walk_in_place_faster_right
	step_end

LittlerootTown_SecondLab_EventScript_DontLeave_Movement_0:
	walk_up
	step_end

LittlerootTown_SecondLab_EventScript_GrassStarter_Text_0:
	.string "Do you want to choose {STR_VAR_1}?$"

TestBattle::
	.string "PROF. BIRCH: So, you chose\n"
	.string "{STR_VAR_1}, {PLAYER}?\p"
	.string "That seems like a good choice. I can see\n"
	.string "a connection between the two of you.\p"
	.string "Okay then, why don't we have a battle to\n"
	.string "see just how well you and\l"
	.string "{STR_VAR_1} can work together!$"

GoSeeRival::
	.string "Great battle, {PLAYER}! You and\n"
	.string "{STR_VAR_1} were really in-sync!\p"
	.string "Now that you two have shown you can\n"
	.string "handle yourselves, you should go see\l"
	.string "{RIVAL} on ROUTE 103.\p"
	.string "I'm sure {RIVAL} would enjoy the\n"
	.string "company and this would be a good\l"
	.string "opportunity for you and {STR_VAR_1}\l"
	.string "to grow even closer.\p"
	.string "I'll see you when you get back. Have\n"
	.string "fun!$"

WhereAreYouGoing::
	.string "PROF. BIRCH: Where are you going\n"
	.string "{PLAYER}?\p"
	.string "Don't be shy! Go ahead and pick a\n"
	.string "POKéMON!$"
