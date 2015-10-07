import os
WSSS_ROOT = os.environ['WSSS_ROOT']

dropTable = WSSS_ROOT + "/db/DropTable.py"
CreateTable = WSSS_ROOT + "/db/CreateTable.py"
InsertCandidates = WSSS_ROOT + "/db/InsertCandidates.py"
execfile(dropTable)
execfile(CreateTable)
execfile(InsertCandidates)