import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("CTPPSReReco", eras.ctpps_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# define global tag
process.GlobalTag.globaltag = '101X_dataRun2_HLT_v7'

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
  fileNames = cms.untracked.vstring(
$input_files
  ),

  lumisToProcess = cms.untracked.VLuminosityBlockRange('$run:1-$run:max'),
)

#process.maxEvents = cms.untracked.PSet(
#  input = cms.untracked.int32(100)
#)

# filter
process.lv1BitFilter = cms.EDFilter("L1BitFilter",
    lv1Bits = cms.vuint32($lv1Bits),
    verbosity = cms.untracked.uint32(0)
)

process.path_filter = cms.Path(
  process.lv1BitFilter
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    "drop *",
    'keep CTPPSLocalTrackLites_*_*_*',
    'keep edmTriggerResults_*_*_*',
    'keep *BXVector_*_*_*',
    'keep l1t*_*_*_*',
    'keep L1GlobalTriggerReadoutRecord_*_*_*'
  ),
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('path_filter')
  )
)

process.outpath = cms.EndPath(process.output)
