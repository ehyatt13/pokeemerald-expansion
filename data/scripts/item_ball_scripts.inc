Common_EventScript_FindItem::
	callnative GetItemBallIdAndAmountFromTemplate
	finditem VAR_RESULT VAR_0x8009
	end

Common_EventScript_FindRandomTM::
	callnative GetItemBallIdAndAmountFromTemplate
	random 229
	addvar VAR_RESULT 582
	finditem VAR_RESULT VAR_0x8009
	end

Common_EventScript_FindRandomMint::
	callnative GetItemBallIdAndAmountFromTemplate
	random 21
	addvar VAR_RESULT 81
	finditem VAR_RESULT VAR_0x8009
	end

Common_EventScript_FindRandomEvoitem::
	callnative GetItemBallIdAndAmountFromTemplate
	random 33
	addvar VAR_RESULT 211
	finditem VAR_RESULT VAR_0x8009
	end

Common_EventScript_FindRandomHeldItemFirst::
	callnative GetItemBallIdAndAmountFromTemplate
	random 21
	addvar VAR_RESULT 425
	finditem VAR_RESULT VAR_0x8009
	end

Common_EventScript_FindRandomHeldItemSecond::
	callnative GetItemBallIdAndAmountFromTemplate
	random 55
	addvar VAR_RESULT 458
	finditem VAR_RESULT VAR_0x8009
	end
