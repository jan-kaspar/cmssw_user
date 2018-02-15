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
process.load("Geometry.VeryForwardGeometry.geometryRP_cfi")
del(process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles[-1])
process.XMLIdealGeometryESSource_CTPPS.geomXMLFiles.append("Geometry/VeryForwardData/data/2017_09_21_fill6228/RP_Dist_Beam_Cent.xml")

# include alignments, if any
process.load("Geometry.VeryForwardGeometryBuilder.ctppsIncludeAlignmentsFromXML_cfi")
process.ctppsIncludeAlignmentsFromXML.RealFiles = cms.vstring(
  "alignment/2017_postTS2/s/version1/45.xml",
  "alignment/2017_postTS2/s/version1/56.xml",
)

# worker
process.load("Alignment.CTPPSTrackBased.ctppsModifySingularModes_cfi")

# input beam position (mm)
x_45_220_fr = -0.119
y_45_220_fr = +1.936

x_45_210_fr = +0.602
y_45_210_fr = +2.731

x_56_210_fr = +0.416
y_56_210_fr = +2.316

x_56_220_fr = +0.891
y_56_220_fr = +2.131

# settings for sector 45
process.ctppsModifySingularModes_45 = process.ctppsModifySingularModes.clone()

process.ctppsModifySingularModes_45.inputFile = "alignment/2017_postTS2/s/version1/45.xml"
process.ctppsModifySingularModes_45.outputFile = "output_45.xml"

process.ctppsModifySingularModes_45.z1 = -213.000 * 1E3 # 45-210-fr-vr
process.ctppsModifySingularModes_45.z2 = -220.000 * 1E3 # 45-220-fr-vr

process.ctppsModifySingularModes_45.de_x1 = -x_45_210_fr
process.ctppsModifySingularModes_45.de_x2 = -x_45_220_fr

process.ctppsModifySingularModes_45.de_y1 = -y_45_210_fr
process.ctppsModifySingularModes_45.de_y2 = -y_45_220_fr

process.ctppsModifySingularModes_45.de_rho1 = 0
process.ctppsModifySingularModes_45.de_rho2 = 0

# settings for sector 56
process.ctppsModifySingularModes_56 = process.ctppsModifySingularModes.clone()

process.ctppsModifySingularModes_56.inputFile = "alignment/2017_postTS2/s/version1/56.xml"
process.ctppsModifySingularModes_56.outputFile = "output_56.xml"

process.ctppsModifySingularModes_56.z1 = 213.000 * 1E3 # 56-210-fr-vr
process.ctppsModifySingularModes_56.z2 = 220.000 * 1E3 # 56-220-fr-vr

process.ctppsModifySingularModes_56.de_x1 = -x_56_210_fr
process.ctppsModifySingularModes_56.de_x2 = -x_56_220_fr

process.ctppsModifySingularModes_56.de_y1 = -y_56_210_fr
process.ctppsModifySingularModes_56.de_y2 = -y_56_220_fr

process.ctppsModifySingularModes_56.de_rho1 = 0
process.ctppsModifySingularModes_56.de_rho2 = 0


# processing path
process.p = cms.Path(
    process.ctppsModifySingularModes_45
    + process.ctppsModifySingularModes_56
)
