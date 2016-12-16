import FWCore.ParameterSet.Config as cms

process = cms.Process("rpNtuplization")

# minimum of logs
process.load("Configuration.TotemCommon.LoggerMin_cfi")

# data source
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string('checkEachFile'),
    fileNames = cms.untracked.vstring(
$input_files
    )
)

# fake optics - required by the ntuplizer
process.load("Configuration.TotemOpticsConfiguration.OpticsConfig_6500GeV_19p2_cfi")

# ntuplizer
process.load("TotemAnalysis.TotemNtuplizer.TotemNtuplizer_cfi")
process.TotemNtuplizer.verbosity = 0

process.TotemNtuplizer.modules = cms.vstring("raw", "trigger", "rp")

process.TotemNtuplizer.includeDigi = True
process.TotemNtuplizer.includePatterns = True
process.TotemNtuplizer.includeMultiTrack = True
process.TotemNtuplizer.includeCCBits = False

process.TotemNtuplizer.ProductLabelSimu = "rpCCOutput"
process.TotemNtuplizer.ModulLabelSimu = "Raw2DigiProducer"
process.TotemNtuplizer.RPMulFittedTrackCollectionLabel = cms.InputTag("RPMulTrackNonParallelCandCollFit")

process.TotemNtuplizer.outputFileName = '$output_file'

process.p = cms.Path(
    process.TotemNtuplizer
)

# dump expanded configuration file
print("----------------------------------------------------------------------------------------------------")
print("")
print(process.dumpConfig())
print("")
print("----------------------------------------------------------------------------------------------------")
