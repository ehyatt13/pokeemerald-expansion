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
