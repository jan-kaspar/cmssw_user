import FWCore.ParameterSet.Config as cms

process = cms.Process("trackBasedAlignment")

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
$inputFiles
    ),
    lumisToProcess = cms.untracked.VLuminosityBlockRange($lsList)
)

# geometry
process.load("Geometry.VeryForwardGeometry.geometryRPFromDD_2018_cfi")
del(process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles[-1])
process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.append("$geometry/RP_Dist_Beam_Cent.xml")

# initial alignments
process.load("Geometry.VeryForwardGeometryBuilder.ctppsIncludeAlignmentsFromXML_cfi")
process.ctppsIncludeAlignmentsFromXML.RealFiles = cms.vstring($alignmentFiles)

# aligner
process.load("Alignment.CTPPSTrackBased.ctppsStraightTrackAligner_cfi")

process.ctppsStraightTrackAligner.verbosity = 1
process.ctppsStraightTrackAligner.factorizationVerbosity = 1

process.ctppsStraightTrackAligner.tagUVPatternsStrip = cms.InputTag("totemRPUVPatternFinder")
process.ctppsStraightTrackAligner.tagDiamondHits = cms.InputTag("ctppsDiamondRecHits")
process.ctppsStraightTrackAligner.tagPixelHits = cms.InputTag("ctppsPixelRecHits")

process.ctppsStraightTrackAligner.maxEvents = $maxEvents

process.ctppsStraightTrackAligner.rpIds = [$rps]
process.ctppsStraightTrackAligner.excludePlanes = cms.vuint32($excludePlanes)
process.ctppsStraightTrackAligner.z0 = $z0

process.ctppsStraightTrackAligner.maxResidualToSigma = $maxResidualToSigma
process.ctppsStraightTrackAligner.minimumHitsPerProjectionPerRP = $minimumHitsPerProjectionPerRP

process.ctppsStraightTrackAligner.removeImpossible = True
process.ctppsStraightTrackAligner.requireNumberOfUnits = $requireNumberOfUnits
process.ctppsStraightTrackAligner.requireOverlap = $requireOverlap
process.ctppsStraightTrackAligner.requireAtLeast3PotsInOverlap = $requireAtLeast3PotsInOverlap
process.ctppsStraightTrackAligner.additionalAcceptedRPSets = "$additionalAcceptedRPSets"

process.ctppsStraightTrackAligner.cutOnChiSqPerNdf = True
process.ctppsStraightTrackAligner.chiSqPerNdfCut = $chiSqPerNdfCut

process.ctppsStraightTrackAligner.maxTrackAx = $maxTrackAx
process.ctppsStraightTrackAligner.maxTrackAy = $maxTrackAy

optimize="$optimize"
process.ctppsStraightTrackAligner.resolveShR = $resolveShR
process.ctppsStraightTrackAligner.resolveShZ = False
process.ctppsStraightTrackAligner.resolveRotZ = $resolveRotZ

process.ctppsStraightTrackAligner.constraintsType = cms.string("standard")
process.ctppsStraightTrackAligner.standardConstraints.units = cms.vuint32($final_constraints_units)

process.ctppsStraightTrackAligner.algorithms = cms.vstring("Jan")

process.ctppsStraightTrackAligner.JanAlignmentAlgorithm.stopOnSingularModes = False

results_dir="$results_dir"

process.ctppsStraightTrackAligner.taskDataFileName = "" # results_dir + "/task_data.root"

process.ctppsStraightTrackAligner.fileNamePrefix = results_dir + "/results_iteration_"
process.ctppsStraightTrackAligner.expandedFileNamePrefix = results_dir + "/results_cumulative_expanded_"
process.ctppsStraightTrackAligner.factoredFileNamePrefix = results_dir + "/results_cumulative_factored_"

process.ctppsStraightTrackAligner.diagnosticsFile = results_dir + '/diagnostics.root'
process.ctppsStraightTrackAligner.buildDiagnosticPlots = $buildDiagnosticPlots
process.ctppsStraightTrackAligner.JanAlignmentAlgorithm.buildDiagnosticPlots = $buildDiagnosticPlots

# processing sequence
process.p = cms.Path(
  process.ctppsStraightTrackAligner
)
