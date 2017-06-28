import FWCore.ParameterSet.Config as cms

process = cms.Process("reconstruction")

# minimum of logs
process.load("Configuration.TotemCommon.LoggerMin_cfi")

# input data
process.load('TotemRawData.Readers.RawDataSource_cfi')
process.source.verbosity = 0
process.source.printProgressFrequency = 0
process.source.fileNames = cms.untracked.vstring(
$input_files
)

#process.maxEvents = cms.untracked.PSet(
#     input = cms.untracked.int32(100)
#)

# RP geometry and alignment
process.load("Configuration.TotemCommon.geometryRP_cfi")
process.XMLIdealGeometryESSource.geomXMLFiles.append("Geometry/TotemRPData/data/$geometry/RP_Dist_Beam_Cent.xml")

process.load("TotemAlignment.RPDataFormats.TotemRPIncludeAlignments_cfi")
process.TotemRPIncludeAlignments.RealFiles = cms.vstring($alignment_files)

# optics
process.load("Configuration.TotemOpticsConfiguration.OpticsConfig_6500GeV_90_50urad_cfi")

# random number generator service
process.load("Configuration.TotemCommon.RandomNumbers_cfi")

# raw to digi conversion
process.load('TotemCondFormats.DAQInformation.DAQMappingSourceXML_cfi')
process.DAQMappingSourceXML.mappingFileNames = cms.untracked.vstring($mapping)

process.DAQMappingSourceXML.maskFileNames = cms.untracked.vstring(
    '/afs/cern.ch/work/j/jkaspar/software/offline/704_production/user/reconstruction/config/13TeV/90m_5sigma/analysis_mask.xml'
)

process.load('TotemRawData.RawToDigi.Raw2DigiProducer_cfi')
process.Raw2DigiProducer.verbosity = 0

# T2 modules
process.load("Configuration.TotemStandardSequences/T2_Digi_and_TrackReconstruction_cfi")
process.load("SimTotem.T2Digitizer.T2DigisSTDGeoEffi_cfi")#T2DigisOnlyPrim_cfi
process.T2Digis.saveDigiVFAT=cms.bool(True)
process.T2Digis.Misalignment.simulatemisalign=cms.untracked.bool(True)
process.T2Digis.Misalignment.inputFileNameMisal= "/afs/cern.ch/work/j/jkaspar/software/offline/704_production/user/reconstruction/config/13TeV/90m_5sigma/T2AlignGlobInt2015_9836to9845.dat"

process.load("RecoTotemT1T2.T2MakeCluster.T2MakeCluster_cfi")
#process.T2MCl.T2PadDigiCollectionLabel = "t2DataOutput"#T2DetIdT2PadDigiTotemDigiCollection_Raw2DigiProducer_t2DataOutput_RawProducer edmDumpEventContent
#process.T2MCl.T2StripDigiCollectionLabel = "t2DataOutput"
process.T2MCl.T2PadDigiCollectionLabel = cms.InputTag("Raw2DigiProducer", "T2PadDigi")
process.T2MCl.T2StripDigiCollectionLabel = cms.InputTag("Raw2DigiProducer", "T2StripDigi")
process.T2MCl.TakeCleanEventOnly=cms.bool(False) #IMPORTANT
#process.T2MCl.maskvect = cms.vuint32(21,23,25,27,29)
process.T2MCl.SimuClusterEfficiency=cms.bool(False)
process.T2MCl.EffiGeoRootFileName= cms.string("RecoTotemT1T2/T2MakeCluster/data/Geom_effiOutput_All8372_Effi_V2Pl.root")

process.load("RecoTotemT1T2.T2RecHit.T2RecHit_cfi")
process.T2Hits.Cl1MaxPad = cms.uint32(25) #Tune better
process.T2Hits.Cl1MaxStrip = cms.uint32(25)
process.T2Hits.IncludeClass0Hits = True
process.T2Hits.inputFileNameMisal=cms.untracked.string('TotemAlignment/T2TrkBasedInternalAlignment/test/T2AlignGlobInt2015_9836to9845.dat')
#TotemAlignment/T2TrkBasedInternalAlignment/test/ExampleAl2015HIPV0_M2V0_ShadV12.dat
process.T2Hits.useTXTfile=cms.bool(True)
process.T2Hits.InsertAlignmentbyCFG=cms.bool(True) # True for data True
process.T2Hits.verbosity=cms.untracked.bool(False)
process.T2Hits.CorrectWithResolution=cms.bool(True) #False:Old Strategy True:New Strategy

process.load("RecoTotemT1T2.T2RoadPadFinder.NewLabelT2RoadPadFinder_cfi")#T2RoadPadFinder_cfi
process.T2RoadPadFinder.HitLabel=cms.string("T2Hits")#T2HitsSTD for effi reco |  #T2Hits for std reco
process.T2RoadPadFinder.CluLabel=cms.string("T2MCl")#T2MClSTD for effi reco |   T2MCl  for std reco
process.T2RoadPadFinder.verbosity = 0
process.T2RoadPadFinder.TwoPointsTubesAngularCollinearity=0.09#0.07 default
process.T2RoadPadFinder.MinCluSize_considered_asBlobs = cms.int32(5)
process.T2RoadPadFinder.MinimumNumCl1Hit= 3
process.T2RoadPadFinder.chi2XYProb_Thr= 0.01
process.T2RoadPadFinder.Nmin_padsFinal= 4
process.T2RoadPadFinder.T2RoadCollProdName="NewRoadFinderRELOAD"
process.T2RoadPadFinder.AllowsPadReAssociation=False
process.T2RoadPadFinder.AllowsConcurrentBranches=False
process.T2RoadPadFinder.useStraightPadTowers= cms.bool(True)#False for internal alignment studies
process.T2RoadPadFinder.ResolveOverlapDoubleCount = cms.bool(False) #Default is True, False for shadow alignment and dndeta An
process.T2RoadPadFinder.OverlapDoubleCountDR = cms.double(2.0) #Depend on your alignment Resol
process.T2RoadPadFinder.OverlapDoubleCountDPhi =cms.double(3.5)
process.T2RoadPadFinder.OverlapDoubleCountDTheta =  cms.double(0.01)
#process.T2RoadPadFinder.VplaneToExclude = cms.vint32(9,19,29,39)
process.T2RoadPadFinder.QuartedSelected = cms.vint32(0,1,2,3)
process.T2RoadPadFinder.BiggestTubeAngleConsidered =cms.double(0.3)
process.T2RoadPadFinder.NumSigma= cms.double(2.)#Important for ALignment (6) istead of 2
#TolleranceDX
process.T2RoadPadFinder.NumPadCluOccupancyAlert= cms.double(60.)#default 50 also in the 8 TeV.
process.T2RoadPadFinder.InefficiencyMaxJump= cms.int32(3)#2 is default
process.T2RoadPadFinder.Nmin_padsFinal= 4

process.load("RecoTotemT1T2.T2TrackProducer3.T2TrackColl3_cfi")
process.T2TrackColl3.StripFitting=cms.bool(False)
process.T2TrackColl3.RoadModuleLabel="T2RoadPadFinder"
process.T2TrackColl3.RoadInstanceLabel="NewRoadFinderRELOAD"
process.T2TrackColl3.verbosity=False
process.T2TrackColl3.RemoveOutliers=True #False for Internal  ALignment studies
process.T2TrackColl3.GhostSuppression=True
process.T2TrackColl3.PickUpDisplacedHit=False
process.T2TrackColl3.PickUpRadius=2.0

# RP: clusterization
process.load("RecoTotemRP.RPClusterSigmaService.ClusterSigmaServiceConf_cfi")
process.load("RecoTotemRP.RPClusterizer.RPClusterizationConf_cfi")
process.RPClustProd.DigiLabel = cms.InputTag("Raw2DigiProducer", "rpDataOutput")

# RP: reco hit production
process.load("RecoTotemRP.RPRecoHitProducer.RPRecoHitProdConf_cfi")

# RP: non-parallel pattern recognition
process.load("RecoTotemRP.RPNonParallelTrackCandidateFinder.RPNonParallelTrackCandidateFinder_cfi")
process.NonParallelTrackFinder.verbosity = 0
process.NonParallelTrackFinder.maxHitsPerPlaneToSearch = 5
process.NonParallelTrackFinder.minPlanesPerProjectionToSearch = 2
process.NonParallelTrackFinder.minPlanesPerProjectionToFit = 3
process.NonParallelTrackFinder.threshold = 2.99
process.NonParallelTrackFinder.DetSetVectorRPRecoHitLabel = cms.InputTag("RPRecoHitProd")

# RP: local track fitting
process.load("RecoTotemRP.RPTrackCandidateCollectionFitter.RPSingleTrackCandCollFitted_cfi")
process.RPSingleTrackCandCollFit.Verbosity = 0
process.RPSingleTrackCandCollFit.RPTrackCandCollProducer = 'NonParallelTrackFinder' # takes up the non-parallel pattern recognition

# RP: multi-track fitting
process.load("RecoTotemRP.RPMulTrackCandidateCollectionFitter.RPMulTrackNonParallelRecoFitter_cfi")
process.RPMulTrackNonParallelCandCollFit.Verbosity = 0

# RP: inelastic reconstruction
process.load("RecoTotemRP.RPInelasticReconstruction.Rec_6500GeV_beta_90_50urad_cfi")
process.RP220Reconst.BeamProtTransportSetup = process.BeamProtTransportSetup


# configure output
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("$output_file"),
    outputCommands = cms.untracked.vstring('keep *')
)

# processing paths
process.path = cms.Path(
    process.Raw2DigiProducer

    *process.T2MCl
    *process.T2Hits
    *process.T2RoadPadFinder
    *process.T2TrackColl3

    *process.RPClustProd
    *process.RPRecoHitProd
    *process.NonParallelTrackFinder
    *process.RPSingleTrackCandCollFit
    *process.RPMulTrackNonParallelCandCollFit
    *process.RP220Reconst
)

process.outpath = cms.EndPath(process.output)

# dump expanded configuration file
print("----------------------------------------------------------------------------------------------------")
print("")
print(process.dumpConfig())
print("")
print("----------------------------------------------------------------------------------------------------")
