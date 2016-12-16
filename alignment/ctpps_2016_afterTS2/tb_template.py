import FWCore.ParameterSet.Config as cms

process = cms.Process("trackBasedAlignment")

process.source = cms.Source("PoolSource",
    skipBadFiles = cms.untracked.bool(True),
    fileNames = cms.untracked.vstring(
$inputFiles
    )
)

# event filter
#process.load("TotemRawData.Filters.EventNumberTimeFilter_cfi")
#process.EventNumberTimeFilter.timestamp.active = False
#process.EventNumberTimeFilter.timestamp.min = 1341630984
#process.EventNumberTimeFilter.timestamp.max = 1341631067

# minimum of logs
process.load("Configuration.TotemCommon.LoggerMin_cfi")

# geometry
process.load("Configuration.TotemCommon.geometryRP_cfi")
process.XMLIdealGeometryESSource.geomXMLFiles.append("Geometry/TotemRPData/data/$geometry/RP_Dist_Beam_Cent.xml")
process.TotemRPGeometryESModule = cms.ESProducer("TotemRPGeometryESModule")

# initial alignments
process.load("TotemAlignment.RPDataFormats.TotemRPIncludeAlignments_cfi")
process.TotemRPIncludeAlignments.RealFiles = cms.vstring($alignmentFiles)

# aligner
process.load("TotemAlignment.RPTrackBased.RPStraightTrackAligner_cfi")
process.RPStraightTrackAligner.verbosity = 1
process.RPStraightTrackAligner.factorizationVerbosity = 2
process.RPStraightTrackAligner.tagRecognizedPatterns = cms.InputTag('NonParallelTrackFinder')

process.RPStraightTrackAligner.maxEvents = $maxEvents

process.RPStraightTrackAligner.RPIds = [$rps]
process.RPStraightTrackAligner.excludePlanes = cms.vuint32($excludePlanes)
process.RPStraightTrackAligner.z0 = $z0

process.RPStraightTrackAligner.singularLimit = 1E-8
process.RPStraightTrackAligner.useExternalFitter = False
   
process.RPStraightTrackAligner.minimumHitsPerProjectionPerRP = $minimumHitsPerProjectionPerRP
process.RPStraightTrackAligner.removeImpossible = True
process.RPStraightTrackAligner.requireNumberOfUnits = $requireNumberOfUnits
process.RPStraightTrackAligner.requireOverlap = $requireOverlap
process.RPStraightTrackAligner.requireAtLeast3PotsInOverlap = $requireAtLeast3PotsInOverlap
process.RPStraightTrackAligner.additionalAcceptedRPSets = "$additionalAcceptedRPSets"

process.RPStraightTrackAligner.cutOnChiSqPerNdf = True
process.RPStraightTrackAligner.chiSqPerNdfCut = $chiSqPerNdfCut
process.RPStraightTrackAligner.maxResidualToSigma = $maxResidualToSigma

process.RPStraightTrackAligner.maxTrackAx = $maxTrackAx
process.RPStraightTrackAligner.maxTrackAy = $maxTrackAy

optimize="$optimize"
process.RPStraightTrackAligner.resolveShR = $resolveShR
process.RPStraightTrackAligner.resolveRotZ = $resolveRotZ
process.RPStraightTrackAligner.resolveShZ = False
process.RPStraightTrackAligner.resolveRPShZ = False

process.RPStraightTrackAligner.algorithms = cms.vstring('Jan')
process.RPStraightTrackAligner.constraintsType = "$constraintsType"

process.RPStraightTrackAligner.useExtendedRotZConstraint = $useExtendedConstraints
process.RPStraightTrackAligner.useZeroThetaRotZConstraint = $useZeroThetaRotZConstraint
process.RPStraightTrackAligner.useExtendedShZConstraints = $useExtendedConstraints
process.RPStraightTrackAligner.useExtendedRPShZConstraint = $useExtendedConstraints
process.RPStraightTrackAligner.oneRotZPerPot = $oneRotZPerPot
process.RPStraightTrackAligner.useEqualMeanUMeanVRotZConstraint = $useEqualMeanUMeanVRotZConstraint

process.RPStraightTrackAligner.homogeneousConstraints.RPShZ_values = cms.vdouble(0, 0)
process.RPStraightTrackAligner.homogeneousConstraints.RotZ_values = cms.vdouble(0, 0, 0, 0)

process.RPStraightTrackAligner.fixedDetectorsConstraints.ShR.ids = cms.vuint32($fixed_planes_shr)
process.RPStraightTrackAligner.fixedDetectorsConstraints.ShR.values = cms.vdouble($fixed_planes_values_shr)

process.RPStraightTrackAligner.fixedDetectorsConstraints.RotZ.ids = cms.vuint32($fixed_planes_rotz)
process.RPStraightTrackAligner.fixedDetectorsConstraints.RotZ.values = cms.vdouble($fixed_planes_values_rotz)

process.RPStraightTrackAligner.fixedDetectorsConstraints.ShZ.ids = cms.vuint32(1200, 1201, 1208, 1209)
process.RPStraightTrackAligner.fixedDetectorsConstraints.RPShZ.ids = cms.vuint32(1200, 1240)
process.RPStraightTrackAligner.fixedDetectorsConstraints.RPShZ.values = cms.vdouble(0, 0)

process.RPStraightTrackAligner.finalConstraints.units = cms.vuint32($final_constraints_units)

process.RPStraightTrackAligner.JanAlignmentAlgorithm.stopOnSingularModes = False

results_dir='$results_dir'

process.RPStraightTrackAligner.taskDataFileName = results_dir + '/task_data.root'

process.RPStraightTrackAligner.fileNamePrefix = results_dir + '/results_'
process.RPStraightTrackAligner.cumulativeFileNamePrefix = ''
process.RPStraightTrackAligner.expandedFileNamePrefix = results_dir + '/cumulative_expanded_results_'
process.RPStraightTrackAligner.factoredFileNamePrefix = results_dir + '/cumulative_factored_results_'

if $buildDiagnosticPlots:
  process.RPStraightTrackAligner.diagnosticsFile = results_dir + '/diagnostics.root'
  process.RPStraightTrackAligner.buildDiagnosticPlots = True
  process.RPStraightTrackAligner.JanAlignmentAlgorithm.buildDiagnosticPlots = True
else:
  process.RPStraightTrackAligner.diagnosticsFile = ''
  process.RPStraightTrackAligner.buildDiagnosticPlots = False
  process.RPStraightTrackAligner.JanAlignmentAlgorithm.buildDiagnosticPlots = False


process.p = cms.Path(
#    process.EventNumberTimeFilter *
    process.RPStraightTrackAligner
)
