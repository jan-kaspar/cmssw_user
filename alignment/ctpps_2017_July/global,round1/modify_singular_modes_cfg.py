import FWCore.ParameterSet.Config as cms

process = cms.Process("modifySingularModes")

# minimum of logs
process.MessageLogger = cms.Service("MessageLogger",
  statistics = cms.untracked.vstring(),
  destinations = cms.untracked.vstring('cout'),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string('WARNING')
  )
)

# empty source
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# geometry
process.load("Geometry.VeryForwardGeometry.geometryRP_without_RP_dist_cfi")
process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.append("Geometry/VeryForwardData/data/2017_07_08_fill5912/RP_Dist_Beam_Cent.xml")

# include alignments, if any
process.load("Geometry.VeryForwardGeometryBuilder.TotemRPIncludeAlignments_cfi")
process.TotemRPIncludeAlignments.RealFiles = cms.vstring(
    "Alignment/CTPPS/data/2017_07_08_fill5912/sr/version1/45.xml",
    "Alignment/CTPPS/data/2017_07_08_fill5912/sr/version1/56.xml"
)

# worker
process.load("Alignment.CTPPS.ctppsModifySingularModes_cfi")

# settings for sector 45
process.ctppsModifySingularModes_45 = process.ctppsModifySingularModes.clone()

process.ctppsModifySingularModes_45.inputFile = "Alignment/CTPPS/data/2017_07_08_fill5912/sr/version1/45.xml"
process.ctppsModifySingularModes_45.outputFile = "output_45.xml"

process.ctppsModifySingularModes_45.z1 = -213.000 * 1E3 # 45-210-fr-vr
process.ctppsModifySingularModes_45.z2 = -220.000 * 1E3 # 45-220-fr-vr

process.ctppsModifySingularModes_45.de_x1 = -0.528
process.ctppsModifySingularModes_45.de_x2 = -0.197

process.ctppsModifySingularModes_45.de_y1 = -2.620
process.ctppsModifySingularModes_45.de_y2 = -2.245

process.ctppsModifySingularModes_45.de_rho1 = 0
process.ctppsModifySingularModes_45.de_rho2 = 0

# settings for sector 56
process.ctppsModifySingularModes_56 = process.ctppsModifySingularModes.clone()

process.ctppsModifySingularModes_56.inputFile = "Alignment/CTPPS/data/2017_07_08_fill5912/sr/version1/56.xml"
process.ctppsModifySingularModes_56.outputFile = "output_56.xml"

process.ctppsModifySingularModes_56.z1 = 213.000 * 1E3 # 56-210-fr-vr
process.ctppsModifySingularModes_56.z2 = 220.000 * 1E3 # 56-220-fr-vr

process.ctppsModifySingularModes_56.de_x1 = -0.117
process.ctppsModifySingularModes_56.de_x2 = -0.936

process.ctppsModifySingularModes_56.de_y1 = -2.063
process.ctppsModifySingularModes_56.de_y2 = -2.283

process.ctppsModifySingularModes_56.de_rho1 = 0
process.ctppsModifySingularModes_56.de_rho2 = 0


# processing path
process.p = cms.Path(
    process.ctppsModifySingularModes_45
    + process.ctppsModifySingularModes_56
)
