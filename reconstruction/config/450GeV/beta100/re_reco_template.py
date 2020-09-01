import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("CTPPSReReRecoWithAlignment", eras.ctpps_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# define global tag
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_dataRun2_v28', '')

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

  #lumisToProcess = cms.untracked.VLuminosityBlockRange($ls_selection),

  dropDescendantsOfDroppedBranches=cms.untracked.bool(False),
  inputCommands = cms.untracked.vstring(
    'drop *',
    'keep TotemRPRecHitedmDetSetVector_*_*_*',
    'keep CTPPSPixelRecHitedmDetSetVector_*_*_*',
    'keep edmTriggerResults_*_*_*',
    'keep GlobalAlgBlkBXVector_*_*_*',
  )
)

#process.maxEvents = cms.untracked.PSet(
#  input = cms.untracked.int32(1000)
#)

# geometry
process.load("Geometry.VeryForwardGeometry.geometryRPFromDD_2018_cfi")
del(process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles[-1])
process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.append("$geometry")

# add alignment corrections
process.load("CalibPPS.ESProducers.ctppsRPAlignmentCorrectionsDataESSourceXML_cfi")
process.ctppsRPAlignmentCorrectionsDataESSourceXML.RealFiles += cms.vstring($alignment_files)
process.ap = cms.ESPrefer("CTPPSRPAlignmentCorrectionsDataESSourceXML", "ctppsRPAlignmentCorrectionsDataESSourceXML")

# RP reconstruction chain
process.load("RecoCTPPS.TotemRPLocal.totemRPLocalReconstruction_cff")

process.load("RecoCTPPS.PixelLocal.ctppsPixelLocalReconstruction_cff")

process.load("RecoCTPPS.TotemRPLocal.ctppsLocalTrackLiteProducer_cff")
process.ctppsLocalTrackLiteProducer.includeDiamonds = False

# reconstruction sequences
process.path_reco = cms.Path(
  process.totemRPUVPatternFinder
  * process.totemRPLocalTrackFitter

  * process.ctppsPixelLocalTracks

  * process.ctppsLocalTrackLiteProducer
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    "drop *",

    'keep TotemRPRecHitedmDetSetVector_*_*_*',
    'keep TotemRPUVPatternedmDetSetVector_*_*_*',

    #'keep CTPPSPixelRecHitedmDetSetVector_*_*_*',

    'keep CTPPSLocalTrackLites_*_*_*'
  )
)

process.outpath = cms.EndPath(process.output)
