import FWCore.ParameterSet.Config as cms

process = cms.Process("bla")

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
  statistics = cms.untracked.vstring(),
  destinations = cms.untracked.vstring('cout'),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string('WARNING')
  )
)

# input data
process.source = cms.Source("PoolSource",
    skipBadFiles = cms.untracked.bool(True),
    fileNames = cms.untracked.vstring(
      #"root://eostotem.cern.ch//eos/totem/user/j/jkaspar/reco/2018_90m/version9/run_318546.0_filter_TOTEM1_bit347.root",
      #"root://eostotem.cern.ch//eos/totem/user/j/jkaspar/reco/2018_90m/version9/run_318547.0_filter_TOTEM1_bit347.root",
      "root://eostotem.cern.ch//eos/totem/user/j/jkaspar/reco/2018_90m/version9/run_318548.0_filter_TOTEM1_bit347.root",
      #"root://eostotem.cern.ch//eos/totem/user/j/jkaspar/reco/2018_90m/version9/run_318549.0_filter_TOTEM1_bit347.root",
    )
)

process.CTPPSFastSimulationValidator = cms.EDAnalyzer("CTPPSFastSimulationValidator",
    simuTracksTag = cms.InputTag("ctppsLocalTrackLiteProducer", "", "RECO"),
    recoTracksTag = cms.InputTag("ctppsLocalTrackLiteProducer", "", "ReRecoWithAlignment"),
    outputFile = cms.string("output_318548.root")
)

# processing sequence
process.p = cms.Path(
    process.CTPPSFastSimulationValidator
)
