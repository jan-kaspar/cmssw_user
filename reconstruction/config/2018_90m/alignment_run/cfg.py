import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("ReRecoWithAlignment", eras.ctpps_2016)

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
		"/store/data/Run2018B/TOTEM10/AOD/PromptReco-v2/000/318/546/00000/788C8DBE-DC79-E811-9B86-02163E01A083.root"
  ),

  lumisToProcess = cms.untracked.VLuminosityBlockRange('318546:1-318546:max'),

  dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
  inputCommands = cms.untracked.vstring(
    'drop *',
    'keep TotemRPRecHitedmDetSetVector_*_*_*',
    'keep CTPPSPixelRecHitedmDetSetVector_*_*_*',
    'keep CTPPSDiamondRecHitedmDetSetVector_*_*_*',
    'keep CTPPSDiamondLocalTrackedmDetSetVector_*_*_*',
  )
)

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(10)
)

# define global tag
process.GlobalTag.globaltag = '101X_dataRun2_HLT_v7'

# RP reconstruction chain with standard settings
process.load("RecoCTPPS.Configuration.recoCTPPS_DD_cff")

# use the correct geometry
del(process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles[-1])
process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.append("data/geometry/2018_90m/2018_06_25_fill6837_align/RP_Dist_Beam_Cent.xml")

# add alignment corrections
process.ctppsIncludeAlignmentsFromXML.RealFiles += cms.vstring()

process.dump = cms.EDAnalyzer("EventContentAnalyzer")

# reconstruction sequences
process.stripReProcessing = cms.Sequence(
  process.totemRPUVPatternFinder
  * process.totemRPLocalTrackFitter
)

process.pixelReProcessing = cms.Sequence(
  process.ctppsPixelLocalTracks
)

process.p = cms.Path(
  #process.dump *
  process.stripReProcessing
  * process.pixelReProcessing
  * process.ctppsLocalTrackLiteProducer
  #* process.dump
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("output.root"),
  outputCommands = cms.untracked.vstring(
    "drop *",
    'keep TotemRPRecHitedmDetSetVector_*_*_*',
    'keep TotemRPUVPatternedmDetSetVector_*_*_*',
    'keep CTPPSPixelRecHitedmDetSetVector_*_*_*',
    'keep CTPPSDiamondRecHitedmDetSetVector_*_*_*',
    'keep CTPPSLocalTrackLites_*_*_*',
  )
)

process.outpath = cms.EndPath(process.output)
