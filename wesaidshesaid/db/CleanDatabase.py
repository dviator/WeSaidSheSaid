import os
WSSS_ROOT = os.environ['WSSS_ROOT']

dropTable = WSSS_ROOT + "/wesaidshesaid/db/DropTable.py"
CreateTable = WSSS_ROOT + "/wesaidshesaid/db/CreateTable.py"
InsertCandidates = WSSS_ROOT + "/wesaidshesaid/db/InsertCandidates.py"
execfile(dropTable)
execfile(CreateTable)
execfile(InsertCandidates)
