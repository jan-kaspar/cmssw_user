import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process("CTPPSReReco", eras.ctpps_2016)

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
  statistics = cms.untracked.vstring(),
  destinations = cms.untracked.vstring('cout'),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string('WARNING')
  )
)

# geometry
process.load("Configuration.Geometry.geometry_CTPPS_alaTotem_fill5912_cfi")

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

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(100)
)

# strips: non-parallel pattern recognition
process.load("RecoCTPPS.TotemRPLocal.totemRPUVPatternFinder_cfi")

# strips: local track fitting
process.load("RecoCTPPS.TotemRPLocal.totemRPLocalTrackFitter_cfi")

# pixels: clusterisation
process.clusterProd = cms.EDProducer("CTPPSPixelClusterProducer",
  label=cms.untracked.string("ctppsPixelDigis"),
  RPixVerbosity = cms.int32(0),
  SeedADCThreshold = cms.int32(10),
  ADCThreshold = cms.int32(10),
  ElectronADCGain = cms.double(135.0),
  VCaltoElectronOffset = cms.int32(-411),
  VCaltoElectronGain = cms.int32(50),
  CalibrationFile = cms.string("/afs/cern.ch/work/j/jkaspar/software/ctpps/development/pixel_from_Enrico/CMSSW_9_2_0/src/Gain_Fed_1462-1463_Run_107.root"),
  DAQCalibration = cms.bool(True),
  doSingleCalibration = cms.bool(False)
)

# pixels: rechit producer
process.load("RecoCTPPS.CTPPSPixelLocal.CTPPSPixelRecHit_cfi")
process.rechitProd.RPixVerbosity = cms.int32(0)

# common: lite tracks
process.load("RecoCTPPS.TotemRPLocal.ctppsLocalTrackLiteProducer_cfi")

# processing sequences
process.stripReProcessing = cms.Sequence(
  process.totemRPUVPatternFinder
  * process.totemRPLocalTrackFitter
)

process.pixelAdditionalProcessing = cms.Sequence(
  process.clusterProd
  * process.rechitProd
)

process.p = cms.Path(
  process.stripReProcessing
  + process.pixelAdditionalProcessing
  + process.ctppsLocalTrackLiteProducer
)

# output configuration
from RecoCTPPS.Configuration.RecoCTPPS_EventContent_cff import RecoCTPPSAOD
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = RecoCTPPSAOD.outputCommands
)

process.outpath = cms.EndPath(process.output)
