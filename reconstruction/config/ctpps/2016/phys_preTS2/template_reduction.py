import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("CTPPSReduction", eras.ctpps_2016)

# import of standard configurations
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

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

  lumisToProcess = cms.untracked.VLuminosityBlockRange($ls_selection),
  dropDescendantsOfDroppedBranches = cms.untracked.bool(False),

  inputCommands = cms.untracked.vstring(
    'drop *',
    'keep CTPPSLocalTrackLites_*_*_*'
  )
)

#process.maxEvents = cms.untracked.PSet(
#  input = cms.untracked.int32(100)
#)


# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file")
)

process.outpath = cms.EndPath(process.output)
