import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process("ReReco", eras.ctpps_2016)

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
    'keep TotemRPDigiedmDetSetVector_*_*_*',
    'keep CTPPSPixelDigiedmDetSetVector_*_*_*',
    'keep CTPPSDiamondDigiedmDetSetVector_*_*_*',
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

# define global tag
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, "auto:run2_data")

# load geometry from XML files
process.load("Geometry.VeryForwardGeometry.geometryRPFromDD_2017_cfi") # NB: OK for 2016 data

# add alignment corrections
#process.ctppsRPAlignmentCorrectionsDataESSourceXML.RealFiles = cms.vstring($alignment_files)

# load reco sequences
process.load("RecoCTPPS.TotemRPLocal.totemRPLocalReconstruction_cff")
process.load("RecoCTPPS.TotemRPLocal.ctppsLocalTrackLiteProducer_cff")

process.totemRPClusterProducer.tagDigi = cms.InputTag("totemRPRawToDigi", "RP")

process.ctppsLocalTrackLiteProducer.includePixels = False
process.ctppsLocalTrackLiteProducer.includeDiamonds = False

# processing sequence
process.path = cms.Path(
  process.totemRPLocalReconstruction
  * process.ctppsLocalTrackLiteProducer
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    "drop *",
    #'keep TotemRPRecHitedmDetSetVector_*_*_*',
    #'keep CTPPSPixelRecHitedmDetSetVector_*_*_*',
    #'keep CTPPSDiamondDigiedmDetSetVector_*_*_*',
    #'keep CTPPSDiamondRecHitedmDetSetVector_*_*_*',
    'keep CTPPSLocalTrackLites_*_*_*'
  )
)

process.outpath = cms.EndPath(process.output)
