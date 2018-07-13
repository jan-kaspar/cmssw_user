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

#run = "319097"
#run = "319125"
#run = "319266"
#run = "319273"

# input data
process.source = cms.Source("PoolSource",
    skipBadFiles = cms.untracked.bool(True),
    fileNames = cms.untracked.vstring(
      "root://eostotem.cern.ch//eos/totem/user/j/jkaspar/reco/2018_90m/10sigma-ZeroBias-version3/run_" + run + ".0_re_reco_ZeroBias.root",
    )
)

process.CTPPSFastSimulationValidator = cms.EDAnalyzer("CTPPSFastSimulationValidator",
    simuTracksTag = cms.InputTag("ctppsLocalTrackLiteProducer", "", "RECO"),
    recoTracksTag = cms.InputTag("ctppsLocalTrackLiteProducer", "", "ReRecoWithAlignment"),
    outputFile = cms.string("output_" + run + ".root")
)

# processing sequence
process.p = cms.Path(
    process.CTPPSFastSimulationValidator
)
