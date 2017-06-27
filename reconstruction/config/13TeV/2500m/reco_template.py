import FWCore.ParameterSet.Config as cms

process = cms.Process("rpReconstruction")

# minimum of logs
process.load("Configuration.TotemCommon.LoggerMin_cfi")

process.load('TotemRawData.Readers.RawDataSource_cfi')
process.source.verbosity = 0
process.source.printProgressFrequency = 0
process.source.fileNames = cms.untracked.vstring(
$input_files
)

# raw to digi conversion
process.load('TotemCondFormats.DAQInformation.DAQMappingSourceXML_cfi')
process.DAQMappingSourceXML.mappingFileNames = cms.untracked.vstring($mapping)
process.DAQMappingSourceXML.maskFileNames = cms.untracked.vstring("/afs/cern.ch/work/j/jkaspar/software/offline/704/user-new/reconstruction/config/13TeV/2500m/analysis_mask.xml")  # remove from reconstruction the planes for which it was not possible to determine alignment

process.load('TotemRawData.RawToDigi.Raw2DigiProducer_cfi')
process.Raw2DigiProducer.verbosity = 0

# clusterization
process.load("RecoTotemRP.RPClusterSigmaService.ClusterSigmaServiceConf_cfi")
process.load("RecoTotemRP.RPClusterizer.RPClusterizationConf_cfi")
process.RPClustProd.DigiLabel = cms.InputTag("Raw2DigiProducer", "rpDataOutput")

# reco hit production
process.load("RecoTotemRP.RPRecoHitProducer.RPRecoHitProdConf_cfi")

# geometry
process.load("Configuration.TotemCommon.geometryRP_cfi")
process.XMLIdealGeometryESSource.geomXMLFiles.append("Geometry/TotemRPData/data/$geometry/RP_Dist_Beam_Cent.xml")

process.load("TotemAlignment.RPDataFormats.TotemRPIncludeAlignments_cfi")
process.TotemRPIncludeAlignments.RealFiles = cms.vstring($alignment_files)

# non-parallel pattern recognition
process.load("RecoTotemRP.RPNonParallelTrackCandidateFinder.RPNonParallelTrackCandidateFinder_cfi")
process.NonParallelTrackFinder.verbosity = 0
process.NonParallelTrackFinder.maxHitsPerPlaneToSearch = 5
process.NonParallelTrackFinder.minPlanesPerProjectionToSearch = 2
process.NonParallelTrackFinder.minPlanesPerProjectionToFit = 3
process.NonParallelTrackFinder.threshold = 2.99
#process.NonParallelTrackFinder.exceptionalSettings = cms.VPSet(
#    cms.PSet(
#        rpId = cms.uint32(20),
#        minPlanesPerProjectionToFit_U = cms.uint32(2),
#        minPlanesPerProjectionToFit_V = cms.uint32(3),
#        threshold_U = cms.double(1.99),
#        threshold_V = cms.double(2.99)
#    )
#)

# track fitting
process.load("RecoTotemRP.RPTrackCandidateCollectionFitter.RPSingleTrackCandCollFitted_cfi")
process.RPSingleTrackCandCollFit.Verbosity = 0
process.RPSingleTrackCandCollFit.RPTrackCandCollProducer = 'NonParallelTrackFinder' # takes up the non-parallel pattern recognition

# multi-track fitting
process.load("RecoTotemRP.RPMulTrackCandidateCollectionFitter.RPMulTrackNonParallelRecoFitter_cfi")
process.RPMulTrackNonParallelCandCollFit.Verbosity = 0

process.p = cms.Path(
    process.Raw2DigiProducer *
    process.RPClustProd * 
    process.RPRecoHitProd *
    process.NonParallelTrackFinder *
    process.RPSingleTrackCandCollFit *
    process.RPMulTrackNonParallelCandCollFit
)

# store desired results
process.output = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string("$output_file"),
  outputCommands = cms.untracked.vstring(
    'drop *',
    'keep TotemRawEvent_*_*_*',
    'keep RPDigClusteredmDetSetVector_*_*_*',
    'keep RPRecognizedPatternsCollection_*_*_*',
    'keep RPTrackCandidateCollection_*_*_*',
    'keep RPFittedTrackCollection_*_*_*',
    'keep RPMulFittedTrackCollection_*_*_*'
  )
)

process.outpath = cms.EndPath(process.output)

print("----------------------------------------------------------------------------------------------------")
print("")
print(process.dumpConfig())
print("")
print("----------------------------------------------------------------------------------------------------")
