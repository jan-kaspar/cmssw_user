import FWCore.ParameterSet.Config as cms
import fnmatch

from Configuration.StandardSequences.Eras import eras
process = cms.Process("CTPPSRawToDigi", eras.ctpps_2016)

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
    statistics = cms.untracked.vstring(),
    destinations = cms.untracked.vstring('cout'),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING')
    )
)

# raw data source
process.load("TotemRawData.Readers.TotemStandaloneRawDataSource_cfi")
process.source.fileNames = cms.untracked.vstring(
$input_files
)

#process.maxEvents = cms.untracked.PSet(
#    input = cms.untracked.int32(100)
#)

# raw-to-digi conversion
process.load("CondFormats.CTPPSReadoutObjects.totemDAQMappingESSourceXML_cfi")
process.totemDAQMappingESSourceXML.subSystem = "TrackingStrip"
process.totemDAQMappingESSourceXML.configuration = cms.VPSet(
  cms.PSet(
    validityRange = cms.EventRange("1:min - 3999999999:max"),
    mappingFileNames = cms.vstring("CondFormats/CTPPSReadoutObjects/xml/mapping_tracking_strip_alignment_run_2016_Sep.xml"),
    maskFileNames = cms.vstring()
  )
)

process.load("EventFilter.CTPPSRawToDigi.totemRPRawToDigi_cfi")
process.totemRPRawToDigi.rawDataTag = cms.InputTag("source")
process.totemRPRawToDigi.fedIds = cms.vuint32(437, 438, 445, 446)
process.totemRPRawToDigi.RawUnpacking.verbosity = 0
process.totemRPRawToDigi.RawToDigi.verbosity = 0

process.load("EventFilter.CTPPSRawToDigi.totemTriggerRawToDigi_cfi")
process.totemTriggerRawToDigi.rawDataTag = cms.InputTag("source")
process.totemTriggerRawToDigi.fedId = 668

# processing path
process.p = cms.Path(
    process.totemRPRawToDigi
    * process.totemTriggerRawToDigi
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    'drop *_*_*_*',
    'keep TotemRPDigiedmDetSetVector_*_*_*',
    'keep TotemTriggerCounters_*_*_*'
  )
)

process.outpath = cms.EndPath(process.output)
