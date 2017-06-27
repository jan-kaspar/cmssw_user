import FWCore.ParameterSet.Config as cms

process = cms.Process("ntuplization")

# minimum of logs
process.load("Configuration.TotemCommon.LoggerMin_cfi")

# data source
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string('checkEachFile'),
    fileNames = cms.untracked.vstring(
$input_files
    )
)

# declare optics
process.load("Configuration.TotemOpticsConfiguration.OpticsConfig_6500GeV_90_50urad_cfi")

# ntuplizer
process.load("TotemAnalysis.TotemNtuplizer.TotemNtuplizer_cfi")
process.TotemNtuplizer.verbosity = 0

process.TotemNtuplizer.modules = cms.vstring("raw", "trigger", "rp", "t1", "t2")

process.TotemNtuplizer.includeDigi = True
process.TotemNtuplizer.includePatterns = True
process.TotemNtuplizer.includeMultiTrack = True
process.TotemNtuplizer.includeCCBits = True
process.TotemNtuplizer.T2IncludePadAndStripDigi = True

process.TotemNtuplizer.RawEventLabel = 'source'
process.TotemNtuplizer.T1DigiVfatCollectionLabel = cms.InputTag("Raw2DigiProducer", "t1DataOutput")
process.TotemNtuplizer.T1DigiWireCollectionLabel = cms.InputTag("Raw2DigiProducer", "t1DataOutput")
process.TotemNtuplizer.T2PadDigiCollectionLabel = cms.InputTag("Raw2DigiProducer", "T2PadDigi")
process.TotemNtuplizer.T2StripDigiCollectionLabel = cms.InputTag("Raw2DigiProducer", "T2StripDigi")
process.TotemNtuplizer.RPReconstructedProtonCollectionLabel = cms.InputTag('RP220Reconst')
process.TotemNtuplizer.RPReconstructedProtonPairCollectionLabel = cms.InputTag('RP220Reconst')

process.TotemNtuplizer.ProductLabelSimu = "rpCCOutput"
process.TotemNtuplizer.ModulLabelSimu = "Raw2DigiProducer"
process.TotemNtuplizer.RPMulFittedTrackCollectionLabel = cms.InputTag("RPMulTrackNonParallelCandCollFit")

process.TotemNtuplizer.outputFileName = '$output_file'

# processing path
process.p = cms.Path(
   process.TotemNtuplizer
)

# dump expanded configuration file
print("----------------------------------------------------------------------------------------------------")
print("")
print(process.dumpConfig())
print("")
print("----------------------------------------------------------------------------------------------------")
