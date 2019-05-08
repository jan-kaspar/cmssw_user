import FWCore.ParameterSet.Config as cms

process = cms.Process("Reduction")

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
  statistics = cms.untracked.vstring(),
  destinations = cms.untracked.vstring('cout'),
  categories = cms.untracked.vstring('FwkReport'),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string('WARNING'),
    FwkReport = cms.untracked.PSet(
      reportEvery = cms.untracked.int32(1000)
    )
  )
)

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag.globaltag = "101X_dataRun2_Express_v8"
process.GlobalTag.globaltag = "101X_dataRun2_Prompt_v11"

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
$input_files
  ),

  dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
  inputCommands = cms.untracked.vstring(
    'drop *',
    'keep *_generalTracks_*_*',
    'keep *_dedxHarmonic2_*_*',
    'keep *_dedxPixelHarmonic2_*_*',
    'keep *_offlinePrimaryVertices_*_*',
    'keep *_totemRPRecHitProducer_*_*',
    'keep *_totemRPUVPatternFinder_*_*',
    'keep *_ctppsLocalTrackLiteProducer_*_*',
  ),

  lumisToProcess = cms.untracked.VLuminosityBlockRange($ls_selection)
)

process.filter = cms.EDFilter("PromptAnalyzer",
  tracks = cms.InputTag('generalTracks'),
  dedxs = cms.InputTag('dedxHarmonic2'),
  dedxPIXs = cms.InputTag('dedxPixelHarmonic2'),
  #dedxpixels = cms.InputTag('dedxHitInfo'),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  #triggers = cms.InputTag('TriggerResults','','HLT'),
  #pflows = cms.InputTag('particleFlow'),
  #muons = cms.InputTag('muons'),

  rpRecHitTag = cms.InputTag('totemRPRecHitProducer'),
  rpPatternTag = cms.InputTag('totemRPUVPatternFinder'),
  rpTrackTag = cms.InputTag('ctppsLocalTrackLiteProducer'),

  outputFileName = cms.string("")
)

process.path_filter = cms.Path(
  process.filter
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),

  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('path_filter')
  )
)

process.path_output = cms.EndPath(process.output)

# schedule
#process.schedule = cms.Schedule(process.path_filter, process.path_output)
