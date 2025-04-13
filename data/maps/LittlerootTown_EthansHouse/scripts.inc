
LittlerootTown_EthansHouse_MapScripts::
	.byte 0

MegaStoneGuy::
	lockall
	applymovement 3, MegaStoneGuy_Movement_0
	msgbox MegaStoneGuy_Text_0
	goto_if_set FLAG_BADGE02_GET, MegaStoneGuy_2
	msgbox MegaStoneGuy_Text_2
MegaStoneGuy_1:
	releaseall
	end

MegaStoneGuy_2:
	pokemart MegaStoneStore
	msgbox MegaStoneGuy_Text_1
	goto MegaStoneGuy_1


	.align 2
MegaStoneStore:
	.2byte ITEM_VENUSAURITE
	.2byte ITEM_CHARIZARDITE_X
	.2byte ITEM_CHARIZARDITE_Y
	.2byte ITEM_BLASTOISINITE
	.2byte ITEM_BEEDRILLITE
	.2byte ITEM_PIDGEOTITE
	.2byte ITEM_ALAKAZITE
	.2byte ITEM_SLOWBRONITE
	.2byte ITEM_GENGARITE
	.2byte ITEM_KANGASKHANITE
	.2byte ITEM_PINSIRITE
	.2byte ITEM_GYARADOSITE
	.2byte ITEM_AERODACTYLITE
	.2byte ITEM_MEWTWONITE_X
	.2byte ITEM_MEWTWONITE_Y
	.2byte ITEM_AMPHAROSITE
	.2byte ITEM_STEELIXITE
	.2byte ITEM_SCIZORITE
	.2byte ITEM_HERACRONITE
	.2byte ITEM_HOUNDOOMINITE
	.2byte ITEM_TYRANITARITE
	.2byte ITEM_SCEPTILITE
	.2byte ITEM_BLAZIKENITE
	.2byte ITEM_SWAMPERTITE
	.2byte ITEM_GARDEVOIRITE
	.2byte ITEM_SABLENITE
	.2byte ITEM_MAWILITE
	.2byte ITEM_AGGRONITE
	.2byte ITEM_MEDICHAMITE
	.2byte ITEM_MANECTITE
	.2byte ITEM_SHARPEDONITE
	.2byte ITEM_CAMERUPTITE
	.2byte ITEM_ALTARIANITE
	.2byte ITEM_BANETTITE
	.2byte ITEM_ABSOLITE
	.2byte ITEM_GLALITITE
	.2byte ITEM_SALAMENCITE
	.2byte ITEM_METAGROSSITE
	.2byte ITEM_LATIASITE
	.2byte ITEM_LATIOSITE
	.2byte ITEM_LOPUNNITE
	.2byte ITEM_GARCHOMPITE
	.2byte ITEM_LUCARIONITE
	.2byte ITEM_ABOMASITE
	.2byte ITEM_GALLADITE
	.2byte ITEM_AUDINITE
	.2byte ITEM_DIANCITE
	.2byte ITEM_NONE

MegaStoneGuy_Movement_0:
	face_player
	step_end

MegaStoneGuy_Text_0:
	.string "Are you interested in any mega-stones?$"

MegaStoneGuy_Text_1:
	.string "Drop by again some time.$"

MegaStoneGuy_Text_2:
	.string "Sorry, you can't handle any of these yet.$"
