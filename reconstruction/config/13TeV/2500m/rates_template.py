import FWCore.ParameterSet.Config as cms

process = cms.Process("rpRateExtraction")

# minimum of logs
process.load("Configuration.TotemCommon.LoggerMin_cfi")

# data source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
$input_files
    )
)

# without this line cmsRun crashes...
process.load("Configuration.TotemOpticsConfiguration.OpticsConfig_6500GeV_19p2_cfi")

# rate module
process.rpRates = cms.EDAnalyzer("RPRate",
    tagClusters = cms.InputTag("RPClustProd"),
    tagPatterns = cms.InputTag("NonParallelTrackFinder"),
    tagTracks = cms.InputTag("RPSingleTrackCandCollFit"),
    outputFileName = cms.string("rates.out")
)

process.p = cms.Path(
    process.rpRates
)
