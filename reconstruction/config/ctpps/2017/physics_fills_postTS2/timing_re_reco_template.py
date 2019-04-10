import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process("reduction", eras.ctpps_2016)

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
  statistics = cms.untracked.vstring(),
  destinations = cms.untracked.vstring('cout'),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string('WARNING')
  )
)

# data source
process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(),
  skipBadFiles = cms.untracked.bool(True),
  duplicateCheckMode = cms.untracked.string("checkAllFilesOpened"),
  dropDescendantsOfDroppedBranches = cms.untracked.bool(False),

  inputCommands = cms.untracked.vstring(
    'drop *',
    'keep CTPPSDiamondDigiedmDetSetVector_*_*_*',
    'keep CTPPSLocalTrackLites_*_*_*'
  )
)
$input_file_commands

#process.maxEvents = cms.untracked.PSet(
#  input = cms.untracked.int32(100)
#)

# apply JSON file
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
JSONfile = '$ls_selection'
myLumis = LumiList.LumiList(filename = JSONfile).getCMSSWString().split(',')
process.source.lumisToProcess.extend(myLumis)

# declare global tag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "auto:run2_data")

# load geometry from XML files
process.load("Geometry.VeryForwardGeometry.geometryRPFromDD_2017_cfi")

# local RP reconstruction chain
process.load("RecoCTPPS.Configuration.recoCTPPS_sequences_cff")

# add alignment corrections
process.ctppsRPAlignmentCorrectionsDataESSourceXML.RealFiles += cms.vstring($alignment_files)

# processing sequence
process.path = cms.Path(
  process.ctppsDiamondRecHits
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    "drop *",
    'keep CTPPSDiamondRecHitedmDetSetVector_*_*_*',
    'keep CTPPSLocalTrackLites_*_*_*'
  )
)

process.outpath = cms.EndPath(process.output)
