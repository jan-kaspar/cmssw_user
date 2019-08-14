import FWCore.ParameterSet.Config as cms
import fnmatch

from Configuration.StandardSequences.Eras import eras
process = cms.Process("CTPPSReduction", eras.ctpps_2016)

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
#    input = cms.untracked.int32(1000)
#)

# raw-to-digi conversion
process.load("CondFormats.TotemReadoutObjects.TotemDAQMappingESSourceXML_cfi")
#process.TotemDAQMappingESSourceXML.mappingFileNames.append("CondFormats/TotemReadoutObjects/xml/totem_rp_2016_210_mapping.xml")
process.TotemDAQMappingESSourceXML.mappingFileNames.append("CondFormats/CTPPSReadoutObjects/xml/mapping_tracking_strip_2016_to_fill_5288.xml")

process.load("EventFilter.TotemRawToDigi.totemRPRawToDigi_cfi")
process.totemRPRawToDigi.rawDataTag = cms.InputTag("source")
#process.totemRPRawToDigi.fedIds = cms.vuint32(437, 438, 445, 446)

# geometry
for item in fnmatch.filter(process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles, "*/RP_Dist_Beam_Cent.xml"):
    process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.remove(item)
process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.append("$geometry")

process.load("Geometry.VeryForwardGeometryBuilder.TotemRPIncludeAlignments_cfi")
process.TotemRPIncludeAlignments.RealFiles = cms.vstring($alignment_files)

# local RP reconstruction chain with standard settings
process.load("RecoCTPPS.Configuration.recoCTPPS_cff")

# processing path
process.p = cms.Path(
    process.totemRPRawToDigi *
    process.recoCTPPS
)

# output configuration
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    'drop *_*_*_*',
    'keep CTPPSLocalTrackLites_*_*_*'
  )
)

process.outpath = cms.EndPath(process.output)
