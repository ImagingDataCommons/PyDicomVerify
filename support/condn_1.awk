#  cond" nestinglevel "n.awk Copyright (c) 1993-2018, David A. Clunie DBA PixelMed Publishing. All rights reserved.
# create C++ headers from conditions template 

# can set these values on the command line:
#


NR==1	{
	print "# Automatically generated from template - EDITS WILL BE LOST"
	print ""
	print "from cond" nestinglevel "n_cc import *"
	print "from sopclc_h import *"
	print "from pydicom.tag import Tag"
	print "from pydicom.dataset import Dataset"
	print "def Condition_Never(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:"  
	print "\t return False"
	print "def Condition_Always(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:" 
	print "\t return True"
	


	condition=""
	}

/^[ 	]*Condition=/ {

	condition=""
	if (match($0,"Condition=\"[^\"]*\""))
		condition=substr($0,RSTART+length("Condition=\""),
			RLENGTH-length("Condition=\"")-1);

		nestinglevel=0
		print "def Condition_" condition "(ds:Dataset, parentds:Dataset, rootds:Dataset)->bool:"
		print "\tcond" nestinglevel " = False" 
	}

/^[ 	]*ConditionEnd/ {

	print "\treturn cond" nestinglevel ""
	condition=""

	}

/^[ 	]*Element/ {

	element=""
	if (match($0,"Element=\"[^\"]*\""))
		element=substr($0,RSTART+length("Element=\""),
			RLENGTH-length("Element=\"")-1);

	operator=""
	if (match($0,"Operator=\"[^\"]*\""))
		operator=substr($0,RSTART+length("Operator=\""),
			RLENGTH-length("Operator=\"")-1);

	if (operator == " or " || operator == "Or" || operator == "|" || operator == "||") {
		operator="or"
	}
	else if (operator == "xor" || operator == "Xor" || operator == "^") {
		operator=" ^ "
	}
	else if (operator == "and" || operator == "And" || operator == "&" || operator == "&&") {
		operator=" and "
	}
	else if (length(operator) == 0) {
		operator=" or "
	}
	else {
		print "Error - Operator \"" operator "\" invalid, assuming or, at line" FNR >"/dev/tty"
	}

	modifier=""
	if (match($0,"Modifier=\"[^\"]*\""))
		modifier=substr($0,RSTART+length("Modifier=\""),
			RLENGTH-length("Modifier=\"")-1);

	if (modifier == "not" || modifier == "Not" || modifier == "~" || modifier == "!") {
		modifier=" not "
	}
	else if (length(modifier) == 0) {
		modifier=""
	}
	else {
		print "Error - Modifier \"" modifier "\" invalid, assuming none, at line" FNR >"/dev/tty"
	}

	selector=""
	if (match($0,"ValueSelector=\"[^\"]*\""))
		selector=substr($0,RSTART+length("ValueSelector=\""),
			RLENGTH-length("ValueSelector=\"")-1);

	if (length(selector) == 0) {
		selector="-1"		# default is wildcard not 1st value !
	}
	else if (selector == "*") {
		selector="-1"		# wildcard
	}

	valuepresent=0
	if (match($0,"ValuePresent=\"[^\"]*\"")) {
		valuepresent=1
	}
	
	elementpresent=0
	elementpresentmask=""
	if (match($0,"ElementPresent=\"[^\"]*\"")) {
		elementpresent=1;
		elementpresentmask=substr($0,RSTART+length("ElementPresent=\""),
			RLENGTH-length("ElementPresent=\"")-1);
	}

	elementpresentabove=0
	if (match($0,"ElementPresentAbove=\"[^\"]*\"")) {
		elementpresentabove=1;
	}

	elementpresentinroot=0
	if (match($0,"ElementPresentInRoot=\"[^\"]*\"")) {
		elementpresentinroot=1;
	}

	elementpresentwithin=0
	elementpresentwithinsequence=""
	if (match($0,"ElementPresentWithin=\"[^\"]*\"")) {
		elementpresentwithin=1;
		elementpresentwithinsequence=substr($0,RSTART+length("ElementPresentWithin=\""),
			RLENGTH-length("ElementPresentWithin=\"")-1);
	}

	elementpresentinpath=0
	elementpresentinpathfromroot=""
	if (match($0,"ElementPresentInPathFromRoot=\"[^\"]*\"")) {
		elementpresentinpath=1;
		elementpresentinpathfromroot=substr($0,RSTART+length("ElementPresentInPathFromRoot=\""),
			RLENGTH-length("ElementPresentInPathFromRoot=\"")-1);
	}

	elementpresentinpathfirstitem=0
	elementpresentinpathfromrootfirstitem=""
	if (match($0,"ElementPresentInPathFromRootFirstItem=\"[^\"]*\"")) {
		elementpresentinpathfirstitem=1;
		elementpresentinpathfromrootfirstitem=substr($0,RSTART+length("ElementPresentInPathFromRootFirstItem=\""),
			RLENGTH-length("ElementPresentInPathFromRootFirstItem=\"")-1);
	}

	grouppresent=0;
	grouppresentmask=""
	if (match($0,"GroupPresent=\"[^\"]*\"")) {
		grouppresent=1;
		grouppresentmask=substr($0,RSTART+length("GroupPresent=\""),
			RLENGTH-length("GroupPresent=\"")-1);
	}

	stringconstant=""
	stringconstantused=0
	if (match($0,"StringConstant=\"[^\"]*\"")) {
		stringconstantused=1
		stringconstant=substr($0,RSTART+length("StringConstant=\""),
			RLENGTH-length("StringConstant=\"")-1);
	}
	
	stringconstantfromrootattribute=""
	stringconstantfromrootattributeused=0
	if (match($0,"StringConstantFromRootAttribute=\"[^\"]*\"")) {
		stringconstantfromrootattributeused=1
		stringconstantfromrootattribute=substr($0,RSTART+length("StringConstantFromRootAttribute=\""),
			RLENGTH-length("StringConstantFromRootAttribute=\"")-1);
	}

	stringvalue=""
	stringvalueused=0
	if (match($0,"StringValue=\"[^\"]*\"")) {
		stringvalueused=1
		stringvalue=substr($0,RSTART+length("StringValue=\""),
			RLENGTH-length("StringValue=\"")-1);
	}
	
	stringvalueabove=""
	stringvalueaboveused=0
	if (match($0,"StringValueAbove=\"[^\"]*\"")) {
		stringvalueaboveused=1
		stringvalueabove=substr($0,RSTART+length("StringValueAbove=\""),
			RLENGTH-length("StringValueAbove=\"")-1);
	}
	
	stringvaluefromrootattribute=""
	stringvaluefromrootattributeused=0
	if (match($0,"StringValueFromRootAttribute=\"[^\"]*\"")) {
		stringvaluefromrootattributeused=1
		stringvaluefromrootattribute=substr($0,RSTART+length("StringValueFromRootAttribute=\""),
			RLENGTH-length("StringValueFromRootAttribute=\"")-1);
	}

	binaryvalue=""
	binaryvaluematchoperator=""
	if (match($0,"BinaryValue=\"[^\"]*\"")) {
		binaryvaluewithoperator=substr($0,RSTART+length("BinaryValue=\""),
			RLENGTH-length("BinaryValue=\"")-1);
		# e.g., "== 1" ; "< 367"
		spacestart=index(binaryvaluewithoperator," "); # 3 ; 2
		binaryvalue=substr(binaryvaluewithoperator,spacestart+1,length(binaryvaluewithoperator)-spacestart);	# 4, 4-3=1 ; 3, 5-2=3
		matchoperatorstring=substr(binaryvaluewithoperator,1,spacestart-1);	# 1,2 ; 1,1
		if (matchoperatorstring == "==") binaryvaluematchoperator = "BinaryValueMatchOperator.Equals"
		else if (matchoperatorstring == "!=") binaryvaluematchoperator = "BinaryValueMatchOperator.NotEquals"
		else if (matchoperatorstring == "<") binaryvaluematchoperator = "BinaryValueMatchOperator.LessThan"
		else if (matchoperatorstring == "<=") binaryvaluematchoperator = "BinaryValueMatchOperator.LessThanOrEquals"
		else if (matchoperatorstring == ">") binaryvaluematchoperator = "BinaryValueMatchOperator.GreaterThan"
		else if (matchoperatorstring == ">=") binaryvaluematchoperator = "BinaryValueMatchOperator.GreaterThanOrEquals"
		else print "Error - Binary Match Operator \"" matchoperatorstring "\" invalid at line" FNR >"/dev/tty"
	}

	binaryvaluefromrootattribute=""
	binaryvaluematchoperatorfromrootattribute=""
	if (match($0,"BinaryValueFromRootAttribute=\"[^\"]*\"")) {
		binaryvaluewithoperator=substr($0,RSTART+length("BinaryValueFromRootAttribute=\""),
			RLENGTH-length("BinaryValueFromRootAttribute=\"")-1);
		# e.g., "== 1" ; "< 367"
		spacestart=index(binaryvaluewithoperator," "); # 3 ; 2
		binaryvaluefromrootattribute=substr(binaryvaluewithoperator,spacestart+1,length(binaryvaluewithoperator)-spacestart);	# 4, 4-3=1 ; 3, 5-2=3
		matchoperatorstring=substr(binaryvaluewithoperator,1,spacestart-1);	# 1,2 ; 1,1
		if (matchoperatorstring == "==") binaryvaluematchoperatorfromrootattribute = "BinaryValueMatchOperator.Equals"
		else if (matchoperatorstring == "!=") binaryvaluematchoperatorfromrootattribute = "BinaryValueMatchOperator.NotEquals"
		else if (matchoperatorstring == "<") binaryvaluematchoperatorfromrootattribute = "BinaryValueMatchOperator.LessThan"
		else if (matchoperatorstring == "<=") binaryvaluematchoperatorfromrootattribute = "BinaryValueMatchOperator.LessThanOrEquals"
		else if (matchoperatorstring == ">") binaryvaluematchoperatorfromrootattribute = "BinaryValueMatchOperator.GreaterThan"
		else if (matchoperatorstring == ">=") binaryvaluematchoperatorfromrootattribute = "BinaryValueMatchOperator.GreaterThanOrEquals"
		else print "Error - Binary Match Operator \"" matchoperatorstring "\" invalid at line" FNR >"/dev/tty"
	}

	tagvalue=""
	if (match($0,"TagValue=\"[^\"]*\""))
		tagvalue=substr($0,RSTART+length("TagValue=\""),
			RLENGTH-length("TagValue=\"")-1);

	tagvaluefromrootattribute=""
	if (match($0,"TagValueFromRootAttribute=\"[^\"]*\""))
		tagvaluefromrootattribute=substr($0,RSTART+length("TagValueFromRootAttribute=\""),
			RLENGTH-length("TagValueFromRootAttribute=\"")-1);

	sequencehasitems=0
	if (match($0,"SequenceHasItems=\"[^\"]*\"")) {
		sequencehasitems=1;
	}

	sequencehasoneitem=0
	if (match($0,"SequenceHasOneItem=\"[^\"]*\"")) {
		sequencehasoneitem=1;
	}
	
	sequencehasmultipleitems=0
	if (match($0,"SequenceHasMultipleItems=\"[^\"]*\"")) {
		sequencehasmultipleitems=1;
	}

		if (valuepresent) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator  modifier "(ValuePresent(ds , \"" element "\", " selector "))"
		}
		if (elementpresent) {
			if (length(elementpresentmask) > 0) {
				print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(ElementPresentMasked(ds , \"" element "\", " elementpresentmask "))"
			}
			else {
				print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(ElementPresent(ds , \"" element "\"))"
			}
		}
		if (elementpresentabove) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(ElementPresentAbove(parentds , \"" element "\"))"
		}
		if (elementpresentwithin) {
			if (length(elementpresentwithinsequence) > 0) {
				if (stringvalueused) {
					print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(ElementStringValueMatchWithin(ds , \"" element "\", \""  elementpresentwithinsequence "\", " selector ", \"" stringvalue "\"))"
					stringvalueused=0	# i.e., don't use it again below !
				}
				else if (stringconstantused) {
					print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(ElementStringValueMatchWithin(ds , \"" element "\", \""  elementpresentwithinsequence "\", " selector ", \"\""  stringconstant "\"\"))"
					stringconstantused=0	# i.e., don't use it again below !
				}
				else {
					print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(ElementPresentWithin(ds , \"" element "\", \""  elementpresentwithinsequence "\"))"
				}
			}
			else {
				print "Error - Must specify sequence attribute argument for ElementPresentWithin " FNR >"/dev/tty"
			}
		}
		if (elementpresentinpath) {
			# For now we only support descending from root into items of a top level sequence
			if (length(elementpresentinpathfromroot) > 0) {
				print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(ElementPresentInPathFromRoot(rootds , \"" element "\", \"" elementpresentinpathfromroot "\"))"
			}
			else {
				print "Error - Must specify sequence attribute argument for ElementPresentInPathFromRoot " FNR >"/dev/tty"
			}
		}
		if (elementpresentinpathfirstitem) {
			# For now we only support descending from root into items of a top level sequence
			if (length(elementpresentinpathfromrootfirstitem) > 0) {
				print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(ElementPresentInPathFromRootFirstItem(rootds , \"" element "\", \"" elementpresentinpathfromrootfirstitem "\"))"
			}
			else {
				print "Error - Must specify sequence attribute argument for ElementPresentInPathFromRoot " FNR >"/dev/tty"
			}
		}
		if (elementpresentinroot) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(ElementPresent(rootds , \"" element "\"))"
		}
		if (grouppresent) {
			if (length(grouppresentmask) > 0) {
				print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(GroupPresentMasked(ds , \"" element "\", " grouppresentmask "))"
			}
			else {
				print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "GroupPresent(ds , \"" element "\")"
			}
		}
		if (stringconstantused) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(StringValueMatch(ds , \"" element "\", " selector ", "  stringconstant "))"
		}
		if (stringconstantfromrootattributeused) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(StringValueMatch(rootds , \"" element "\", " selector ", " stringconstantfromrootattribute "))"
		}
		if (stringvalueused) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(StringValueMatch(ds , \"" element "\", " selector ", \"" stringvalue "\"))"
		}
		if (stringvalueaboveused) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(StringValueMatch(parentds , \"" element "\", " selector ", \"" stringvalueabove "\"))"
		}
		if (stringvaluefromrootattributeused) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(StringValueMatch(rootds , \"" element "\", " selector ", \"" stringvaluefromrootattribute "\"))"
		}
		if (length(binaryvalue) > 0) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(BinaryValueMatch(ds , \"" element "\", " selector ", " binaryvaluematchoperator ", " binaryvalue "))"
		}
		if (length(binaryvaluefromrootattribute) > 0) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(BinaryValueMatch(rootds , \"" element "\", " selector ", " binaryvaluematchoperatorfromrootattribute ", " binaryvaluefromrootattribute "))"
		}
		if (length(tagvalue) > 0) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(TagValueMatch(ds , \"" element "\", " selector ", Tag(" tagvalue ")))"
		}
		if (length(tagvaluefromrootattribute) > 0) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(TagValueMatch(rootds , \"" element "\", " selector ", Tag(" tagvaluefromrootattribute ")))"
		}
		if (sequencehasitems) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(SequenceHasItems(ds , \"" element "\"))"
		}
		if (sequencehasoneitem) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(SequenceHasOneItem(ds , \"" element "\"))"
		}
		if (sequencehasmultipleitems) {
			print "\tcond" nestinglevel " = cond" nestinglevel "" " " operator modifier "(SequenceHasMultipleItems(ds , \"" element "\"))"
		}


	}

/^[ 	]*[(]/ {
				++nestinglevel
		print "\tcond" nestinglevel " = False"
	
	}
	
/^[ 	]*[)]/ {
	operator=""
	if (match($0,"Operator=\"[^\"]*\""))
		operator=substr($0,RSTART+length("Operator=\""),
			RLENGTH-length("Operator=\"")-1);

	if (operator == "or" || operator == "Or" || operator == "|" || operator == "||") {
		operator= " or "
	}
	else if (operator == "xor" || operator == "Xor" || operator == "^") {
		operator="^"
	}
	else if (operator == "and" || operator == "And" || operator == "&" || operator == "&&") {
		operator=" and "
	}
	else if (length(operator) == 0) {
		operator=" or "
	}
	else {
		print "Error - Operator \"" operator "\" invalid, assuming or, at line" FNR >"/dev/tty"
	}

	modifier=""
	if (match($0,"Modifier=\"[^\"]*\""))
		modifier=substr($0,RSTART+length("Modifier=\""),
			RLENGTH-length("Modifier=\"")-1);

	if (modifier == "not" || modifier == "Not" || modifier == "~" || modifier == "!") {
		modifier=" not "
	}
	else if (length(modifier) == 0) {
		modifier=""
	}
	else {
		print "Error - Modifier \"" modifier "\" invalid, assuming none, at line" FNR >"/dev/tty"
	}

	print "\tcond" (nestinglevel-1) " = cond" (nestinglevel-1) operator modifier "cond" nestinglevel 
		--nestinglevel
	
	}
	
END {
	#end of file
}

