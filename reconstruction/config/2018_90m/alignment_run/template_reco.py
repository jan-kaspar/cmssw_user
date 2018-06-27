import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("CTPPSReReco", eras.ctpps_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
  statistics = cms.untracked.vstring(),
  destinations = cms.untracked.vstring('cout'),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string('WARNING')
  )
)

# pixel mappings
process.load("CondFormats.CTPPSReadoutObjects.CTPPSPixelDAQMappingESSourceXML_cfi")

# data source
process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
$input_files
  ),

  lumisToProcess = cms.untracked.VLuminosityBlockRange('$run:1-$run:max'),
)

#process.maxEvents = cms.untracked.PSet(
#  input = cms.untracked.int32(100)
#)

# define global tag
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_dataRun2_ReReco_EOY17_v2', '')

# raw-to-digi conversion
process.load("EventFilter.CTPPSRawToDigi.ctppsRawToDigi_cff")

# RP reconstruction chain with standard settings
process.load("RecoCTPPS.Configuration.recoCTPPS_DD_cff")

process.p = cms.Path(
  process.ctppsRawToDigi *
  process.recoCTPPS
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    "drop *",
#    'keep TotemRPUVPatternedmDetSetVector_*_*_*',
#    'keep CTPPSDiamondRecHitedmDetSetVector_*_*_*',
#    'keep CTPPSPixelRecHitedmDetSetVector_*_*_*',
    'keep CTPPSLocalTrackLites_*_*_*',
    'keep edmTriggerResults_*_*_*',
  )
)

process.outpath = cms.EndPath(process.output)
