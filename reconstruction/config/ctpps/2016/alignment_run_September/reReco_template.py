import FWCore.ParameterSet.Config as cms
import fnmatch

from Configuration.StandardSequences.Eras import eras
process = cms.Process("CTPPSReReco", eras.ctpps_2016)

# global tag not needed
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, "auto:run2_data")

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

  labelRawDataLikeMC = cms.untracked.bool(False)
)

#process.maxEvents = cms.untracked.PSet(
#  input = cms.untracked.int32(100)
#)

# geometry
process.load("Geometry.VeryForwardGeometry.geometryRPFromDD_2017_cfi")

for item in fnmatch.filter(process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles, "*/RP_Dist_Beam_Cent.xml"):
    process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.remove(item)
process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.append("$geometry")

# alignment corrections
process.load("CalibPPS.ESProducers.ctppsRPAlignmentCorrectionsDataESSourceXML_cfi")
process.ctppsRPAlignmentCorrectionsDataESSourceXML.RealFiles = cms.vstring($alignment_files)

# local RP reconstruction chain with standard settings
process.load("RecoCTPPS.TotemRPLocal.totemRPLocalReconstruction_cff")

process.load("RecoCTPPS.TotemRPLocal.ctppsLocalTrackLiteProducer_cff")
process.ctppsLocalTrackLiteProducer.includeDiamonds = False
process.ctppsLocalTrackLiteProducer.includePixels = False

#process.dump = cms.EDAnalyzer("EventContentAnalyzer")

# processing path
process.p = cms.Path(
  process.totemRPLocalReconstruction
  * process.ctppsLocalTrackLiteProducer
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    "drop *",
    'keep TotemTriggerCounters_*_*_*',
    'keep TotemRPUVPatternedmDetSetVector_*_*_*',
    'keep CTPPSLocalTrackLites_*_*_*'
  )
)

process.outpath = cms.EndPath(process.output)
