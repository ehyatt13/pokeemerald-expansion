Route102_MapScripts::
	.byte 0

Route102_EventScript_LittleBoy::
	msgbox Route102_Text_ImNotVeryTall, MSGBOX_NPC
	giverandomtm
	end

Route102_EventScript_RouteSignOldale::
	msgbox Route102_Text_RouteSignOldale, MSGBOX_SIGN
	end

Route102_EventScript_RouteSignPetalburg::
	msgbox Route102_Text_RouteSignPetalburg, MSGBOX_SIGN
	end

Route102_EventScript_Boy::
	msgbox Route102_Text_CatchWholeBunchOfPokemon, MSGBOX_NPC
	end

Route102_EventScript_Calvin::
	trainerbattle_single TRAINER_CALVIN_1, Route102_Text_CalvinIntro, Route102_Text_CalvinDefeated, Route102_EventScript_CalvinRegisterMatchCallAfterBattle
	specialvar VAR_RESULT, ShouldTryRematchBattle
	goto_if_eq VAR_RESULT, TRUE, Route102_EventScript_CalvinRematch
	setvar VAR_0x8004, TRAINER_CALVIN_1
	specialvar VAR_RESULT, IsTrainerRegistered
	goto_if_eq VAR_RESULT, FALSE, Route102_EventScript_CalvinTryRegister
	msgbox Route102_Text_CalvinPostBattle, MSGBOX_DEFAULT
	release
	end

Route102_EventScript_CalvinRegisterMatchCallAfterBattle::
	special PlayerFaceTrainerAfterBattle
	waitmovement 0
	goto_if_set FLAG_HAS_MATCH_CALL, Route102_EventScript_CalvinRegisterMatchCall
	release
	end

Route102_EventScript_CalvinRegisterMatchCall::
	msgbox Route102_Text_CalvinRegisterShort, MSGBOX_DEFAULT
	register_matchcall TRAINER_CALVIN_1
	release
	end

Route102_EventScript_CalvinTryRegister::
	goto_if_set FLAG_HAS_MATCH_CALL, Route102_EventScript_CalvinRegister
	msgbox Route102_Text_CalvinPostBattle, MSGBOX_DEFAULT
	release
	end

Route102_EventScript_CalvinRegister::
	msgbox Route102_Text_CalvinRegister, MSGBOX_DEFAULT
	register_matchcall TRAINER_CALVIN_1
	release
	end

Route102_EventScript_CalvinRematch::
	trainerbattle_rematch TRAINER_CALVIN_1, Route102_Text_CalvinRematchIntro, Route102_Text_CalvinRematchDefeated
	msgbox Route102_Text_CalvinRematchPostBattle, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_Rick::
	trainerbattle_single TRAINER_RICK, Route102_Text_RickIntro, Route102_Text_RickDefeated
	msgbox Route102_Text_RickPostBattle, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_Tiana::
	trainerbattle_single TRAINER_TIANA, Route102_Text_TianaIntro, Route102_Text_TianaDefeated
	msgbox Route102_Text_TianaPostBattle, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_Allen::
	trainerbattle_single TRAINER_ALLEN, Route102_Text_AllenIntro, Route102_Text_AllenDefeated
	msgbox Route102_Text_AllenPostBattle, MSGBOX_AUTOCLOSE
	end

Route102_EventScript_Promoter::
	lock
	faceplayer
	goto_if_set FLAG_ROUTE_102_PROMOTER, Route102_EventScript_PromoterSeeOthers
	bufferitemname STR_VAR_1, ITEM_COVERT_CLOAK
	msgbox Route102_Text_Promotion, MSGBOX_DEFAULT
	call Route102_EventScript_CountTrainersRemaining
	copyvar VAR_0x8001, VAR_0x8000
	goto_if_ne VAR_0x8001, 0, Route102_EventScript_PromoterGoDefeat
	playfanfare(MUS_SLOTS_JACKPOT)
	msgbox Route102_Text_Congratulations, MSGBOX_DEFAULT
	waitfanfare
	closemessage
	giveitem ITEM_COVERT_CLOAK, 1
	goto_if_eq VAR_RESULT, 0, Common_EventScript_ShowBagIsFull
	setflag FLAG_ROUTE_102_PROMOTER
	release
	end

Route102_EventScript_CountTrainersRemaining::
	setvar VAR_0x8000, 4
	goto_if_not_defeated TRAINER_CALVIN_1, Route102_EventScript_CheckRick
	subvar VAR_0x8000, 1
Route102_EventScript_CheckRick::
	goto_if_not_defeated TRAINER_RICK, Route102_EventScript_CheckAllen
	subvar VAR_0x8000, 1
Route102_EventScript_CheckAllen::
	goto_if_not_defeated TRAINER_ALLEN, Route102_EventScript_CheckTiana
	subvar VAR_0x8000, 1
Route102_EventScript_CheckTiana::
	goto_if_not_defeated TRAINER_TIANA, Route102_EventScript_StopCountingTrainers
	subvar VAR_0x8000, 1
Route102_EventScript_StopCountingTrainers::
	return

Route102_EventScript_PromoterGoDefeat::
	buffernumberstring STR_VAR_1, VAR_0x8000
	msgbox Route102_Text_RemainingTrainers, MSGBOX_DEFAULT
	release
	end

Route102_EventScript_PromoterSeeOthers::
	msgbox Route102_Text_OtherPromoters, MSGBOX_DEFAULT
	release
	end

Route102_Text_WatchMeCatchPokemon:
	.string "WALLY: {PLAYER}…\n"
	.string "POKéMON hide in tall grass like this,\l"
	.string "don't they?\p"
	.string "Please watch me and see if I can\n"
	.string "catch one properly.\p"
	.string "…Whoa!$"

Route102_Text_WallyIDidIt:
	.string "WALLY: I did it… It's my…\n"
	.string "My POKéMON!$"

Route102_Text_LetsGoBack:
	.string "{PLAYER}, thank you!\n"
	.string "Let's go back to the GYM!$"

Route102_Text_ImNotVeryTall:
	.string "I'm…not very tall, so I sink right\n"
	.string "into tall grass.\p"
	.string "The grass goes up my nose and…\n"
	.string "Fwafwafwafwafwa…\p"
	.string "Fwatchoo!$"

Route102_Text_CatchWholeBunchOfPokemon:
	.string "I'm going to catch a whole bunch of\n"
	.string "POKéMON!$"

Route102_Text_RouteSignOldale:
	.string "ROUTE 102\n"
	.string "{RIGHT_ARROW} OLDALE TOWN$"

Route102_Text_RouteSignPetalburg:
	.string "ROUTE 102\n"
	.string "{LEFT_ARROW} PETALBURG CITY$"

Route102_Text_Promotion:
	.string "My company is currently\n"
	.string "running a promotion for\l"
	.string "a prize!\p"
	.string "My promotion is: \n"
	.string "If you can defeat all of the\l"
	.string "trainers on this route, you'll\l"
	.string "get a {STR_VAR_1}!$"

Route102_Text_RemainingTrainers:
	.string "You still have {STR_VAR_1}\n"
	.string "trainer(s) left to defeat.\p"
	.string "Get to it, trainer!$"

Route102_Text_Congratulations:
	.string "Congratulations! You did it!\n"
	.string "Here's your prize!$"

Route102_Text_OtherPromoters:
	.string "You might come across my\n"
	.string "coworkers on other routes.\p"
	.string "If you do, you should see\n"
	.string "if you can complete their tasks\l"
	.string "for a prize!$"
