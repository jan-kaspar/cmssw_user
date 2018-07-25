import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("CTPPSReRecoWithAlignmentAndPixel", eras.ctpps_2016)

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

  inputCommands = cms.untracked.vstring(
    'keep *',
    'drop TotemRPUVPatternedmDetSetVector_*_*_*',
    'drop TotemRPLocalTrackedmDetSetVector_*_*_*',
    'drop CTPPSLocalTrackLites_*_*_*'
  )
)

#process.maxEvents = cms.untracked.PSet(
#  input = cms.untracked.int32(100)
#)

# define global tag
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_dataRun2_ReReco_EOY17_v2', '')

# use the correct geometry
process.load("Geometry.VeryForwardGeometry.geometryRPFromDD_2017_cfi")

del(process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles[-1])
process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.append("$geometry")

# load reco sequences
process.load("RecoCTPPS.Configuration.recoCTPPS_sequences_cff")
process.recoCTPPS = cms.Sequence(process.recoCTPPSdets)

# add alignment corrections
process.ctppsIncludeAlignmentsFromXML.RealFiles += cms.vstring($alignment_files)

# reconstruction sequences
process.stripReProcessing = cms.Sequence(
  process.totemRPUVPatternFinder
  * process.totemRPLocalTrackFitter
)

process.p = cms.Path(
  process.stripReProcessing
  * process.ctppsPixelLocalReconstruction
  * process.ctppsLocalTrackLiteProducer
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    "drop *",
    'keep TotemRPUVPatternedmDetSetVector_*_*_*',
    'keep CTPPSDiamondRecHitedmDetSetVector_*_*_*',
    'keep CTPPSPixelRecHitedmDetSetVector_*_*_*',
    'keep CTPPSLocalTrackLites_*_*_*'
  )
)

process.outpath = cms.EndPath(process.output)
