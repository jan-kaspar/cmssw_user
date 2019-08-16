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
process.load("Geometry.VeryForwardGeometry.geometryRPFromDD_2017_cfi")
del(process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles[-1])
process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.append("data/geometry/2016_September/2016_09_24_fill5322/RP_Dist_Beam_Cent.xml")

# include alignments, if any
process.load("CalibPPS.ESProducers.ctppsRPAlignmentCorrectionsDataESSourceXML_cfi")
process.ctppsRPAlignmentCorrectionsDataESSourceXML.RealFiles = cms.vstring(
  "data/alignment/2016_September/s/version1/45.xml",
  "data/alignment/2016_September/s/version1/56.xml",
)

# worker
process.load("Alignment.CTPPSTrackBased.ctppsModifySingularModes_cfi")

# input beam position (mm)
x_45_210_fr = +2.108
y_45_210_fr = +0.180

x_45_210_nr = +2.455
y_45_210_nr = +0.033

x_56_210_nr = +2.776
y_56_210_nr = 0.000

x_56_210_fr = +1.864
y_56_210_fr = +0.200


# settings for sector 45
process.ctppsModifySingularModes_45 = process.ctppsModifySingularModes.clone()

process.ctppsModifySingularModes_45.inputFile = "data/alignment/2016_September/s/version1/45.xml"
process.ctppsModifySingularModes_45.outputFile = "output_45.xml"

process.ctppsModifySingularModes_45.z1 = -203.377 * 1E3 # 45-210-nr-vr
process.ctppsModifySingularModes_45.z2 = -213.000 * 1E3 # 45-210-fr-vr

process.ctppsModifySingularModes_45.de_x1 = -x_45_210_nr
process.ctppsModifySingularModes_45.de_x2 = -x_45_210_fr

process.ctppsModifySingularModes_45.de_y1 = -y_45_210_nr
process.ctppsModifySingularModes_45.de_y2 = -y_45_210_fr

process.ctppsModifySingularModes_45.de_rho1 = 0
process.ctppsModifySingularModes_45.de_rho2 = 0

# settings for sector 56
process.ctppsModifySingularModes_56 = process.ctppsModifySingularModes.clone()

process.ctppsModifySingularModes_56.inputFile = "data/alignment/2016_September/s/version1/56.xml"
process.ctppsModifySingularModes_56.outputFile = "output_56.xml"

process.ctppsModifySingularModes_56.z1 = 203.377 * 1E3 # 56-210-nr-vr
process.ctppsModifySingularModes_56.z2 = 213.000 * 1E3 # 56-210-fr-vr

process.ctppsModifySingularModes_56.de_x1 = -x_56_210_nr
process.ctppsModifySingularModes_56.de_x2 = -x_56_210_fr

process.ctppsModifySingularModes_56.de_y1 = -y_56_210_nr
process.ctppsModifySingularModes_56.de_y2 = -y_56_210_fr

process.ctppsModifySingularModes_56.de_rho1 = 0
process.ctppsModifySingularModes_56.de_rho2 = 0


# processing path
process.p = cms.Path(
    process.ctppsModifySingularModes_45
    + process.ctppsModifySingularModes_56
)
