# iodcomp.awk Copyright (c) 1993-2018, David A. Clunie DBA PixelMed Publishing. All rights reserved.
# create C++ headers from composite iod template

# can set these values on the command line:
#


NR==1	{
	print "# Automatically generated from template - EDITS WILL BE LOST"
	print ""
	print "#s Generated by iodcomps_1.awk "
	print ""
	print "from pydicom.dataset import Dataset"
	print "from condn_h import *"
	print "from iodcomp_h import *"

	print "def SelectAndRunCompositeIOD(ds:Dataset, verbose:bool, log:list, ElementDictionary:dict, profile: str)->bool:"
	print ""
	print "\tiod = False"
	iodcomp=""
	ie=""
	}

/^[ 	]*CompositeIOD=/ {

	iodcomp=""
	if (match($0, "CompositeIOD=\"[^\"]*\""))
		iodcomp=substr($0,RSTART+length("CompositeIOD=\""),
			RLENGTH-length("CompositeIOD=\"")-1);

	condition=""
	if (match($0, "Condition=\"[^\"]*\""))
		condition=substr($0,RSTART+length("Condition=\""),
			RLENGTH-length("Condition=\"")-1);

	profile=""
	if (match($0, "Profile=\"[^\"]*\""))
		profile=substr($0,RSTART+length("Profile=\""),
			RLENGTH-length("Profile=\"")-1);

	retired="false"
	if (match($0, "[Rr]etired=\"[^\"]*\""))
		retired=substr($0,RSTART+length("retired=\""),
			RLENGTH-length("retired=\"")-1);
	
	if (role == "declare") {
		print "CompositeIOD_" iodcomp "_verify"
	}

	if (length(condition) > 0) {
		if (length(profile) == 0) {
			print "\t" selectelse "if Condition_" condition "(ds, 0, ds) and profile == \"\":"
		}
		else{
			print "\t" selectelse "if Condition_" condition "(ds, 0, ds) and profile ==\"" profile "\":"
		}
		print "\t\tiod = CompositeIOD_" iodcomp "_verify(ds, verbose, log, ElementDictionary)"
		selectelse="el"
	}

	}

/^[ 	]*CompositeIODEnd/ {

	
		print ""

	iodcomp=""

	}

/^[ 	]*Module/ {

	module=""
	if (match($0, "Module=\"[^\"]*\""))
		module=substr($0,RSTART+length("Module=\""),
			RLENGTH-length("Module=\"")-1);

	usage=""
	if (match($0, "Usage=\"[^\"]*\""))
		usage=substr($0,RSTART+length("Usage=\""),
			RLENGTH-length("Usage=\"")-1);

	condition=""
	if (match($0, "Condition=\"[^\"]*\""))
		condition=substr($0,RSTART+length("Condition=\""),
			RLENGTH-length("Condition=\"")-1);

	}

/^[ 	]*InformationEntity=/ {
	ie=""
	if (match($0, "InformationEntity=\"[^\"]*\""))
		ie=substr($0,RSTART+length("InformationEntity=\""),
			RLENGTH-length("InformationEntity=\"")-1);
}

END {
			print ""
		print "\treturn iod"
		#print "}"
		print ""

}

