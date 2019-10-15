import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.Config as cms

process = cms.Process("TreeProducer")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/50000/7C434F1C-82C4-E611-B0D3-008CFA0518D4.root'),
    skipEvents = cms.untracked.uint32(0)
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.CondDBTauConnection = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS')
)

process.EmptyJetIdParams = cms.PSet(
    Pt010_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt010_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt010_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt1020_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt1020_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt1020_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt2030_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt2030_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt2030_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt3050_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt3050_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
    Pt3050_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0)
)

process.JetIdParams = cms.PSet(
    Pt010_Loose = cms.vdouble(0.0, 0.0, 0.0, 0.2),
    Pt010_Medium = cms.vdouble(0.2, 0.4, 0.2, 0.6),
    Pt010_Tight = cms.vdouble(0.5, 0.6, 0.6, 0.9),
    Pt1020_Loose = cms.vdouble(-0.4, -0.4, -0.4, 0.4),
    Pt1020_Medium = cms.vdouble(-0.3, 0.0, 0.0, 0.5),
    Pt1020_Tight = cms.vdouble(-0.2, 0.2, 0.2, 0.6),
    Pt2030_Loose = cms.vdouble(0.0, 0.0, 0.2, 0.6),
    Pt2030_Medium = cms.vdouble(0.2, 0.2, 0.5, 0.7),
    Pt2030_Tight = cms.vdouble(0.3, 0.4, 0.7, 0.8),
    Pt3050_Loose = cms.vdouble(0.0, 0.0, 0.6, 0.2),
    Pt3050_Medium = cms.vdouble(0.3, 0.2, 0.7, 0.8),
    Pt3050_Tight = cms.vdouble(0.5, 0.4, 0.8, 0.9)
)

process.METSignificanceParams = cms.PSet(
    dRMatch = cms.double(0.4),
    jetThreshold = cms.double(15),
    jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
    jpar = cms.vdouble(1.29, 1.19, 1.07, 1.13, 1.12),
    pjpar = cms.vdouble(-0.04, 0.6504)
)

process.METSignificance_params = cms.PSet(
    EB_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    EB_PhiResPar = cms.vdouble(0.00502),
    EE_EtResPar = cms.vdouble(0.2, 0.03, 0.005),
    EE_PhiResPar = cms.vdouble(0.02511),
    HB_EtResPar = cms.vdouble(0.0, 1.22, 0.05),
    HB_PhiResPar = cms.vdouble(0.02511),
    HE_EtResPar = cms.vdouble(0.0, 1.3, 0.05),
    HE_PhiResPar = cms.vdouble(0.02511),
    HF_EtResPar = cms.vdouble(0.0, 1.82, 0.09),
    HF_PhiResPar = cms.vdouble(0.05022),
    HO_EtResPar = cms.vdouble(0.0, 1.3, 0.005),
    HO_PhiResPar = cms.vdouble(0.02511),
    PF_EtResType1 = cms.vdouble(0.05, 0, 0),
    PF_EtResType2 = cms.vdouble(0.05, 0, 0),
    PF_EtResType3 = cms.vdouble(0.05, 0, 0),
    PF_EtResType4 = cms.vdouble(0.042, 0.1, 0.0),
    PF_EtResType5 = cms.vdouble(0.41, 0.52, 0.25),
    PF_EtResType6 = cms.vdouble(0.0, 1.22, 0.05),
    PF_EtResType7 = cms.vdouble(0.0, 1.22, 0.05),
    PF_PhiResType1 = cms.vdouble(0.002),
    PF_PhiResType2 = cms.vdouble(0.002),
    PF_PhiResType3 = cms.vdouble(0.002),
    PF_PhiResType4 = cms.vdouble(0.0028, 0.0, 0.0022),
    PF_PhiResType5 = cms.vdouble(0.1, 0.1, 0.13),
    PF_PhiResType6 = cms.vdouble(0.02511),
    PF_PhiResType7 = cms.vdouble(0.02511),
    jdphi0 = cms.vdouble(0.034, 0.034, 0.034, 0.034, 0.032, 
        0.031, 0.028, 0.027, 0.027, 0.027),
    jdphi1 = cms.vdouble(0.034, 0.035, 0.035, 0.035, 0.035, 
        0.034, 0.031, 0.03, 0.029, 0.027),
    jdphi2 = cms.vdouble(0.04, 0.04, 0.04, 0.04, 0.04, 
        0.038, 0.036, 0.035, 0.034, 0.033),
    jdphi3 = cms.vdouble(0.042, 0.043, 0.044, 0.043, 0.041, 
        0.039, 0.039, 0.036, 0.034, 0.031),
    jdphi4 = cms.vdouble(0.042, 0.042, 0.043, 0.042, 0.038, 
        0.036, 0.036, 0.033, 0.031, 0.031),
    jdphi5 = cms.vdouble(0.069, 0.069, 0.064, 0.058, 0.053, 
        0.049, 0.049, 0.043, 0.039, 0.04),
    jdphi6 = cms.vdouble(0.084, 0.08, 0.072, 0.065, 0.066, 
        0.06, 0.051, 0.049, 0.045, 0.045),
    jdphi7 = cms.vdouble(0.077, 0.072, 0.059, 0.05, 0.045, 
        0.042, 0.039, 0.039, 0.037, 0.031),
    jdphi8 = cms.vdouble(0.059, 0.057, 0.051, 0.044, 0.038, 
        0.035, 0.037, 0.032, 0.028, 0.028),
    jdphi9 = cms.vdouble(0.062, 0.059, 0.053, 0.047, 0.042, 
        0.045, 0.036, 0.032, 0.034, 0.044),
    jdpt0 = cms.vdouble(0.749, 0.829, 1.099, 1.355, 1.584, 
        1.807, 2.035, 2.217, 2.378, 2.591),
    jdpt1 = cms.vdouble(0.718, 0.813, 1.133, 1.384, 1.588, 
        1.841, 2.115, 2.379, 2.508, 2.772),
    jdpt2 = cms.vdouble(0.841, 0.937, 1.316, 1.605, 1.919, 
        2.295, 2.562, 2.722, 2.943, 3.293),
    jdpt3 = cms.vdouble(0.929, 1.04, 1.46, 1.74, 2.042, 
        2.289, 2.639, 2.837, 2.946, 2.971),
    jdpt4 = cms.vdouble(0.85, 0.961, 1.337, 1.593, 1.854, 
        2.005, 2.209, 2.533, 2.812, 3.047),
    jdpt5 = cms.vdouble(1.049, 1.149, 1.607, 1.869, 2.012, 
        2.219, 2.289, 2.412, 2.695, 2.865),
    jdpt6 = cms.vdouble(1.213, 1.298, 1.716, 2.015, 2.191, 
        2.612, 2.863, 2.879, 2.925, 2.902),
    jdpt7 = cms.vdouble(1.094, 1.139, 1.436, 1.672, 1.831, 
        2.05, 2.267, 2.549, 2.785, 2.86),
    jdpt8 = cms.vdouble(0.889, 0.939, 1.166, 1.365, 1.553, 
        1.805, 2.06, 2.22, 2.268, 2.247),
    jdpt9 = cms.vdouble(0.843, 0.885, 1.245, 1.665, 1.944, 
        1.981, 1.972, 2.875, 3.923, 7.51),
    ptresolthreshold = cms.double(10.0),
    resolutionsAlgo = cms.string('AK5PF'),
    resolutionsEra = cms.string('Spring10')
)

process.PhilV0 = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt010_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt010_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt1020_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt1020_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt1020_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt2030_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt2030_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt2030_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt3050_Loose = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt3050_Medium = cms.vdouble(-999.0, -999.0, -999.0, -999.0),
        Pt3050_Tight = cms.vdouble(-999.0, -999.0, -999.0, -999.0)
    ),
    cutBased = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    tmvaMethod = cms.string('JetID'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/mva_JetID.weights.xml.gz'),
    version = cms.int32(0)
)

process.PhilV1 = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(0.0, 0.0, 0.0, 0.2),
        Pt010_Medium = cms.vdouble(0.2, 0.4, 0.2, 0.6),
        Pt010_Tight = cms.vdouble(0.5, 0.6, 0.6, 0.9),
        Pt1020_Loose = cms.vdouble(-0.4, -0.4, -0.4, 0.4),
        Pt1020_Medium = cms.vdouble(-0.3, 0.0, 0.0, 0.5),
        Pt1020_Tight = cms.vdouble(-0.2, 0.2, 0.2, 0.6),
        Pt2030_Loose = cms.vdouble(0.0, 0.0, 0.2, 0.6),
        Pt2030_Medium = cms.vdouble(0.2, 0.2, 0.5, 0.7),
        Pt2030_Tight = cms.vdouble(0.3, 0.4, 0.7, 0.8),
        Pt3050_Loose = cms.vdouble(0.0, 0.0, 0.6, 0.2),
        Pt3050_Medium = cms.vdouble(0.3, 0.2, 0.7, 0.8),
        Pt3050_Tight = cms.vdouble(0.5, 0.4, 0.8, 0.9)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('philv1'),
    tmvaMethod = cms.string('JetID'),
    tmvaSpectators = cms.vstring(),
    tmvaVariables = cms.vstring('nvtx', 
        'jetPt', 
        'jetEta', 
        'jetPhi', 
        'dZ', 
        'd0', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dRMean', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/mva_JetID_v1.weights.xml.gz'),
    version = cms.int32(-1)
)

process.PuJetIdCutBased_wp = cms.PSet(
    Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
    Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
    Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
    Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
    Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
    Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
    Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
    Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
    Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
    Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
    Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
    Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
    Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
    Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
    Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
    Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
    Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
)

process.PuJetIdMinMVA_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.9, -0.9, -0.94, -0.9),
    Pt010_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
    Pt010_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
    Pt1020_Loose = cms.vdouble(-0.9, -0.9, -0.94, -0.9),
    Pt1020_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
    Pt1020_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
    Pt2030_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
    Pt2030_Medium = cms.vdouble(0.1, -0.4, -0.5, -0.45),
    Pt2030_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0),
    Pt3050_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
    Pt3050_Medium = cms.vdouble(0.1, -0.4, -0.5, -0.45),
    Pt3050_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0)
)

process.PuJetIdOptMVA_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.9, -0.9, -0.9, -0.9),
    Pt010_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
    Pt010_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
    Pt1020_Loose = cms.vdouble(-0.9, -0.9, -0.9, -0.9),
    Pt1020_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
    Pt1020_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
    Pt2030_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
    Pt2030_Medium = cms.vdouble(0.1, -0.4, -0.4, -0.45),
    Pt2030_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0),
    Pt3050_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
    Pt3050_Medium = cms.vdouble(0.1, -0.4, -0.4, -0.45),
    Pt3050_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0)
)

process.cutbased = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
        Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
        Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
        Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
        Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
        Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
        Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
        Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
        Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
        Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
        Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
        Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
        Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
        Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
        Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
        Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
        Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
    ),
    cutBased = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('cutbased')
)

process.full = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.9, -0.9, -0.9, -0.9),
        Pt010_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
        Pt010_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
        Pt1020_Loose = cms.vdouble(-0.9, -0.9, -0.9, -0.9),
        Pt1020_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
        Pt1020_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
        Pt2030_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
        Pt2030_Medium = cms.vdouble(0.1, -0.4, -0.4, -0.45),
        Pt2030_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0),
        Pt3050_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
        Pt3050_Medium = cms.vdouble(0.1, -0.4, -0.4, -0.45),
        Pt3050_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    tmvaMethod = cms.string('PuJetIdOptMVA'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta'),
    tmvaVariables = cms.vstring('frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'nvtx', 
        'nNeutrals', 
        'beta', 
        'betaStar', 
        'dZ', 
        'nCharged'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_PuJetIdOptMVA.weights.xml.gz'),
    version = cms.int32(-1)
)

process.full_53x = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        Pt010_MET = cms.vdouble(0.0, -0.6, -0.4, -0.4),
        Pt010_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
        Pt010_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
        Pt1020_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        Pt1020_MET = cms.vdouble(0.3, -0.2, -0.4, -0.4),
        Pt1020_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
        Pt1020_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
        Pt2030_Loose = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
        Pt2030_MET = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        Pt2030_Medium = cms.vdouble(0.1, -0.36, -0.54, -0.54),
        Pt2030_Tight = cms.vdouble(0.73, 0.05, -0.26, -0.42),
        Pt3050_Loose = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
        Pt3050_MET = cms.vdouble(0.0, 0.0, -0.1, -0.2),
        Pt3050_Medium = cms.vdouble(0.1, -0.36, -0.54, -0.54),
        Pt3050_Tight = cms.vdouble(0.73, 0.05, -0.26, -0.42)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full53x'),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta', 
        'jetPhi'),
    tmvaVariables = cms.vstring('nvtx', 
        'dZ', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dR2Mean', 
        'ptD', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'),
    tmvaWeights = cms.string('CondFormats/JetMETObjects/data/TMVAClassificationCategory_JetID_53X_Dec2012.weights.xml'),
    version = cms.int32(-1)
)

process.full_53x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        Pt010_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
        Pt010_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
        Pt1020_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
        Pt1020_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
        Pt1020_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
        Pt2030_Loose = cms.vdouble(-0.15, -0.26, -0.16, -0.16),
        Pt2030_Medium = cms.vdouble(-0.07, -0.09, 0.0, -0.06),
        Pt2030_Tight = cms.vdouble(0.78, 0.5, 0.17, 0.17),
        Pt3050_Loose = cms.vdouble(-0.15, -0.26, -0.16, -0.16),
        Pt3050_Medium = cms.vdouble(-0.07, -0.09, 0.0, -0.06),
        Pt3050_Tight = cms.vdouble(0.78, 0.5, 0.17, 0.17)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta', 
        'jetPhi'),
    tmvaVariables = cms.vstring('nvtx', 
        'dZ', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dR2Mean', 
        'ptD', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'),
    tmvaWeights = cms.string('CondFormats/JetMETObjects/data/TMVAClassificationCategory_JetID_53X_chs_Dec2012.weights.xml'),
    version = cms.int32(-1)
)

process.full_53x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
    Pt010_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
    Pt010_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
    Pt1020_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
    Pt1020_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
    Pt1020_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
    Pt2030_Loose = cms.vdouble(-0.15, -0.26, -0.16, -0.16),
    Pt2030_Medium = cms.vdouble(-0.07, -0.09, 0.0, -0.06),
    Pt2030_Tight = cms.vdouble(0.78, 0.5, 0.17, 0.17),
    Pt3050_Loose = cms.vdouble(-0.15, -0.26, -0.16, -0.16),
    Pt3050_Medium = cms.vdouble(-0.07, -0.09, 0.0, -0.06),
    Pt3050_Tight = cms.vdouble(0.78, 0.5, 0.17, 0.17)
)

process.full_53x_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
    Pt010_MET = cms.vdouble(0.0, -0.6, -0.4, -0.4),
    Pt010_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
    Pt010_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
    Pt1020_Loose = cms.vdouble(-0.95, -0.96, -0.94, -0.95),
    Pt1020_MET = cms.vdouble(0.3, -0.2, -0.4, -0.4),
    Pt1020_Medium = cms.vdouble(-0.83, -0.92, -0.9, -0.92),
    Pt1020_Tight = cms.vdouble(-0.83, -0.81, -0.74, -0.81),
    Pt2030_Loose = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
    Pt2030_MET = cms.vdouble(0.0, 0.0, 0.0, 0.0),
    Pt2030_Medium = cms.vdouble(0.1, -0.36, -0.54, -0.54),
    Pt2030_Tight = cms.vdouble(0.73, 0.05, -0.26, -0.42),
    Pt3050_Loose = cms.vdouble(-0.63, -0.6, -0.55, -0.45),
    Pt3050_MET = cms.vdouble(0.0, 0.0, -0.1, -0.2),
    Pt3050_Medium = cms.vdouble(0.1, -0.36, -0.54, -0.54),
    Pt3050_Tight = cms.vdouble(0.73, 0.05, -0.26, -0.42)
)

process.full_5x = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.95, -0.97, -0.97, -0.97),
        Pt010_Medium = cms.vdouble(-0.83, -0.96, -0.95, -0.96),
        Pt010_Tight = cms.vdouble(-0.47, -0.92, -0.92, -0.94),
        Pt1020_Loose = cms.vdouble(-0.95, -0.97, -0.97, -0.97),
        Pt1020_Medium = cms.vdouble(-0.83, -0.96, -0.95, -0.96),
        Pt1020_Tight = cms.vdouble(-0.47, -0.92, -0.92, -0.94),
        Pt2030_Loose = cms.vdouble(-0.8, -0.85, -0.84, -0.85),
        Pt2030_Medium = cms.vdouble(-0.4, -0.74, -0.76, -0.81),
        Pt2030_Tight = cms.vdouble(0.32, -0.49, -0.61, -0.74),
        Pt3050_Loose = cms.vdouble(-0.8, -0.85, -0.84, -0.85),
        Pt3050_Medium = cms.vdouble(-0.4, -0.74, -0.76, -0.81),
        Pt3050_Tight = cms.vdouble(0.32, -0.49, -0.61, -0.74)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    tmvaMethod = cms.string('BDT_fullPlusRMS'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta'),
    tmvaVariables = cms.vstring('frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'dR2Mean', 
        'nvtx', 
        'nNeutrals', 
        'beta', 
        'betaStar', 
        'dZ', 
        'nCharged'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_JetID_MET_53X_Dec2012.weights.xml.gz'),
    version = cms.int32(-1)
)

process.full_5x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.98, -0.95, -0.94, -0.94),
        Pt010_Medium = cms.vdouble(-0.94, -0.91, -0.91, -0.92),
        Pt010_Tight = cms.vdouble(-0.59, -0.75, -0.78, -0.8),
        Pt1020_Loose = cms.vdouble(-0.98, -0.95, -0.94, -0.94),
        Pt1020_Medium = cms.vdouble(-0.94, -0.91, -0.91, -0.92),
        Pt1020_Tight = cms.vdouble(-0.59, -0.75, -0.78, -0.8),
        Pt2030_Loose = cms.vdouble(-0.89, -0.77, -0.69, -0.75),
        Pt2030_Medium = cms.vdouble(-0.58, -0.65, -0.57, -0.67),
        Pt2030_Tight = cms.vdouble(0.41, -0.1, -0.2, -0.45),
        Pt3050_Loose = cms.vdouble(-0.89, -0.77, -0.69, -0.57),
        Pt3050_Medium = cms.vdouble(-0.58, -0.65, -0.57, -0.67),
        Pt3050_Tight = cms.vdouble(0.41, -0.1, -0.2, -0.45)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    tmvaMethod = cms.string('BDT_chsFullPlusRMS'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta'),
    tmvaVariables = cms.vstring('frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'dR2Mean', 
        'nvtx', 
        'nNeutrals', 
        'beta', 
        'betaStar', 
        'dZ', 
        'nCharged'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_5x_BDT_chsFullPlusRMS.weights.xml.gz'),
    version = cms.int32(-1)
)

process.full_5x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.98, -0.95, -0.94, -0.94),
    Pt010_Medium = cms.vdouble(-0.94, -0.91, -0.91, -0.92),
    Pt010_Tight = cms.vdouble(-0.59, -0.75, -0.78, -0.8),
    Pt1020_Loose = cms.vdouble(-0.98, -0.95, -0.94, -0.94),
    Pt1020_Medium = cms.vdouble(-0.94, -0.91, -0.91, -0.92),
    Pt1020_Tight = cms.vdouble(-0.59, -0.75, -0.78, -0.8),
    Pt2030_Loose = cms.vdouble(-0.89, -0.77, -0.69, -0.75),
    Pt2030_Medium = cms.vdouble(-0.58, -0.65, -0.57, -0.67),
    Pt2030_Tight = cms.vdouble(0.41, -0.1, -0.2, -0.45),
    Pt3050_Loose = cms.vdouble(-0.89, -0.77, -0.69, -0.57),
    Pt3050_Medium = cms.vdouble(-0.58, -0.65, -0.57, -0.67),
    Pt3050_Tight = cms.vdouble(0.41, -0.1, -0.2, -0.45)
)

process.full_5x_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.95, -0.97, -0.97, -0.97),
    Pt010_Medium = cms.vdouble(-0.83, -0.96, -0.95, -0.96),
    Pt010_Tight = cms.vdouble(-0.47, -0.92, -0.92, -0.94),
    Pt1020_Loose = cms.vdouble(-0.95, -0.97, -0.97, -0.97),
    Pt1020_Medium = cms.vdouble(-0.83, -0.96, -0.95, -0.96),
    Pt1020_Tight = cms.vdouble(-0.47, -0.92, -0.92, -0.94),
    Pt2030_Loose = cms.vdouble(-0.8, -0.85, -0.84, -0.85),
    Pt2030_Medium = cms.vdouble(-0.4, -0.74, -0.76, -0.81),
    Pt2030_Tight = cms.vdouble(0.32, -0.49, -0.61, -0.74),
    Pt3050_Loose = cms.vdouble(-0.8, -0.85, -0.84, -0.85),
    Pt3050_Medium = cms.vdouble(-0.4, -0.74, -0.76, -0.81),
    Pt3050_Tight = cms.vdouble(0.32, -0.49, -0.61, -0.74)
)

process.full_74x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
        Pt010_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
        Pt010_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
        Pt1020_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
        Pt1020_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
        Pt1020_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
        Pt2030_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
        Pt2030_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
        Pt2030_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
        Pt3050_Loose = cms.vdouble(-0.8, -0.95, -0.97, -0.99),
        Pt3050_Medium = cms.vdouble(-0.6, -0.85, -0.85, -0.99),
        Pt3050_Tight = cms.vdouble(-0.5, -0.77, -0.8, -0.98)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta', 
        'nTrueInt', 
        'dRMatch'),
    trainings = cms.VPSet(cms.PSet(
        jEtaMax = cms.double(2.0),
        jEtaMin = cms.double(0.0),
        tmvaVariables = cms.vstring('dR2Mean', 
            'rho', 
            'nParticles', 
            'nCharged', 
            'majW', 
            'minW', 
            'frac01', 
            'frac02', 
            'frac03', 
            'frac04', 
            'ptD', 
            'beta', 
            'betaStar', 
            'pull', 
            'jetR', 
            'jetRchg'),
        tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights_jteta_0_2_newNames.xml.gz')
    ), 
        cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(2.0),
            tmvaVariables = cms.vstring('dR2Mean', 
                'rho', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'betaStar', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights_jteta_2_2p5_newNames.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring('dR2Mean', 
                'rho', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'betaStar', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights_jteta_2p5_3_newNames.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring('dR2Mean', 
                'rho', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_BDTG.weights_jteta_3_5_newNames.xml.gz')
        )),
    version = cms.int32(-1)
)

process.full_74x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
    Pt010_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
    Pt010_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
    Pt1020_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
    Pt1020_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
    Pt1020_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
    Pt2030_Loose = cms.vdouble(-0.8, -0.97, -0.97, -0.99),
    Pt2030_Medium = cms.vdouble(-0.3, -0.87, -0.87, -0.99),
    Pt2030_Tight = cms.vdouble(-0.1, -0.83, -0.83, -0.98),
    Pt3050_Loose = cms.vdouble(-0.8, -0.95, -0.97, -0.99),
    Pt3050_Medium = cms.vdouble(-0.6, -0.85, -0.85, -0.99),
    Pt3050_Tight = cms.vdouble(-0.5, -0.77, -0.8, -0.98)
)

process.full_76x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
        Pt010_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
        Pt010_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
        Pt1020_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
        Pt1020_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
        Pt1020_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
        Pt2030_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
        Pt2030_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
        Pt2030_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
        Pt3050_Loose = cms.vdouble(-0.93, -0.52, -0.39, -0.31),
        Pt3050_Medium = cms.vdouble(-0.2, -0.39, -0.24, -0.19),
        Pt3050_Tight = cms.vdouble(0.52, -0.19, -0.06, -0.03)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta'),
    trainings = cms.VPSet(cms.PSet(
        jEtaMax = cms.double(2.5),
        jEtaMin = cms.double(0.0),
        tmvaVariables = cms.vstring('nvtx', 
            'dR2Mean', 
            'nParticles', 
            'nCharged', 
            'majW', 
            'minW', 
            'frac01', 
            'frac02', 
            'frac03', 
            'frac04', 
            'ptD', 
            'beta', 
            'pull', 
            'jetR', 
            'jetRchg'),
        tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_76x_Eta0to2p5_BDT.weights.xml.gz')
    ), 
        cms.PSet(
            jEtaMax = cms.double(2.75),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_76x_Eta2p5to2p75_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.75),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_76x_Eta2p75to3_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_76x_Eta3to5_BDT.weights.xml.gz')
        )),
    version = cms.int32(-1)
)

process.full_76x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
    Pt010_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
    Pt010_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
    Pt1020_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
    Pt1020_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
    Pt1020_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
    Pt2030_Loose = cms.vdouble(-0.96, -0.62, -0.53, -0.49),
    Pt2030_Medium = cms.vdouble(-0.58, -0.52, -0.4, -0.36),
    Pt2030_Tight = cms.vdouble(0.09, -0.37, -0.24, -0.21),
    Pt3050_Loose = cms.vdouble(-0.93, -0.52, -0.39, -0.31),
    Pt3050_Medium = cms.vdouble(-0.2, -0.39, -0.24, -0.19),
    Pt3050_Tight = cms.vdouble(0.52, -0.19, -0.06, -0.03)
)

process.full_80x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
        Pt010_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
        Pt010_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
        Pt1020_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
        Pt1020_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
        Pt1020_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
        Pt2030_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
        Pt2030_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
        Pt2030_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
        Pt3050_Loose = cms.vdouble(-0.92, -0.56, -0.44, -0.39),
        Pt3050_Medium = cms.vdouble(-0.06, -0.42, -0.3, -0.23),
        Pt3050_Tight = cms.vdouble(0.62, -0.21, -0.07, -0.03)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta'),
    trainings = cms.VPSet(cms.PSet(
        jEtaMax = cms.double(2.5),
        jEtaMin = cms.double(0.0),
        tmvaVariables = cms.vstring('nvtx', 
            'dR2Mean', 
            'nParticles', 
            'nCharged', 
            'majW', 
            'minW', 
            'frac01', 
            'frac02', 
            'frac03', 
            'frac04', 
            'ptD', 
            'beta', 
            'pull', 
            'jetR', 
            'jetRchg'),
        tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80X_Eta0to2p5_BDT.weights.xml.gz')
    ), 
        cms.PSet(
            jEtaMax = cms.double(2.75),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80X_Eta2p5to2p75_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.75),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80X_Eta2p75to3_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80X_Eta3to5_BDT.weights.xml.gz')
        )),
    version = cms.int32(-1)
)

process.full_80x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
    Pt010_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
    Pt010_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
    Pt1020_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
    Pt1020_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
    Pt1020_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
    Pt2030_Loose = cms.vdouble(-0.96, -0.64, -0.56, -0.54),
    Pt2030_Medium = cms.vdouble(-0.49, -0.53, -0.44, -0.42),
    Pt2030_Tight = cms.vdouble(0.26, -0.34, -0.24, -0.26),
    Pt3050_Loose = cms.vdouble(-0.92, -0.56, -0.44, -0.39),
    Pt3050_Medium = cms.vdouble(-0.06, -0.42, -0.3, -0.23),
    Pt3050_Tight = cms.vdouble(0.62, -0.21, -0.07, -0.03)
)

process.full_81x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
        Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
        Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
        Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
        Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
        Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(True),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('full'),
    nEtaBins = cms.int32(4),
    tmvaMethod = cms.string('JetIDMVAHighPt'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta'),
    trainings = cms.VPSet(cms.PSet(
        jEtaMax = cms.double(2.5),
        jEtaMin = cms.double(0.0),
        tmvaVariables = cms.vstring('nvtx', 
            'dR2Mean', 
            'nParticles', 
            'nCharged', 
            'majW', 
            'minW', 
            'frac01', 
            'frac02', 
            'frac03', 
            'frac04', 
            'ptD', 
            'beta', 
            'pull', 
            'jetR', 
            'jetRchg'),
        tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta0to2p5_BDT.weights.xml.gz')
    ), 
        cms.PSet(
            jEtaMax = cms.double(2.75),
            jEtaMin = cms.double(2.5),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p5to2p75_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(3.0),
            jEtaMin = cms.double(2.75),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p75to3_BDT.weights.xml.gz')
        ), 
        cms.PSet(
            jEtaMax = cms.double(5.0),
            jEtaMin = cms.double(3.0),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'pull', 
                'jetR'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta3to5_BDT.weights.xml.gz')
        )),
    version = cms.int32(-1)
)

process.full_81x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
    Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
    Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
    Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
    Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
    Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
    Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
    Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
    Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
    Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
    Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
    Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.met_53x = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt010_MET = cms.vdouble(-0.2, -0.3, -0.5, -0.5),
        Pt010_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt010_Tight = cms.vdouble(-2, -2, -2, -2, -2),
        Pt1020_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt1020_MET = cms.vdouble(-0.2, -0.2, -0.5, -0.3),
        Pt1020_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt1020_Tight = cms.vdouble(-2, -2, -2, -2, -2),
        Pt2030_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt2030_MET = cms.vdouble(-0.2, -0.2, -0.2, 0.1),
        Pt2030_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt2030_Tight = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_Loose = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_MET = cms.vdouble(-0.2, -0.2, 0.0, 0.2),
        Pt3050_Medium = cms.vdouble(-2, -2, -2, -2, -2),
        Pt3050_Tight = cms.vdouble(-2, -2, -2, -2, -2)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('met53x'),
    tmvaMethod = cms.string('JetIDMVAMET'),
    tmvaSpectators = cms.vstring(),
    tmvaVariables = cms.vstring('nvtx', 
        'jetPt', 
        'jetEta', 
        'jetPhi', 
        'dZ', 
        'beta', 
        'betaStar', 
        'nCharged', 
        'nNeutrals', 
        'dR2Mean', 
        'ptD', 
        'frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassificationCategory_JetID_MET_53X_Dec2012.weights.xml.gz'),
    version = cms.int32(-1)
)

process.met_53x_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-2, -2, -2, -2, -2),
    Pt010_MET = cms.vdouble(-0.2, -0.3, -0.5, -0.5),
    Pt010_Medium = cms.vdouble(-2, -2, -2, -2, -2),
    Pt010_Tight = cms.vdouble(-2, -2, -2, -2, -2),
    Pt1020_Loose = cms.vdouble(-2, -2, -2, -2, -2),
    Pt1020_MET = cms.vdouble(-0.2, -0.2, -0.5, -0.3),
    Pt1020_Medium = cms.vdouble(-2, -2, -2, -2, -2),
    Pt1020_Tight = cms.vdouble(-2, -2, -2, -2, -2),
    Pt2030_Loose = cms.vdouble(-2, -2, -2, -2, -2),
    Pt2030_MET = cms.vdouble(-0.2, -0.2, -0.2, 0.1),
    Pt2030_Medium = cms.vdouble(-2, -2, -2, -2, -2),
    Pt2030_Tight = cms.vdouble(-2, -2, -2, -2, -2),
    Pt3050_Loose = cms.vdouble(-2, -2, -2, -2, -2),
    Pt3050_MET = cms.vdouble(-0.2, -0.2, 0.0, 0.2),
    Pt3050_Medium = cms.vdouble(-2, -2, -2, -2, -2),
    Pt3050_Tight = cms.vdouble(-2, -2, -2, -2, -2)
)

process.metfull_53x_wp = cms.PSet(
    Pt010_MET = cms.vdouble(-0.2, -0.3, -0.5, -0.5),
    Pt1020_MET = cms.vdouble(-0.2, -0.2, -0.5, -0.3),
    Pt2030_MET = cms.vdouble(0.0, 0.0, 0.0, 0.0),
    Pt3050_MET = cms.vdouble(0.0, 0.0, -0.1, -0.2)
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_producer_config = cms.PSet(
    mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.253, 0.081, -0.081, 0.965, 0.917, 
            0.683),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_PHYS14_PU20bx25_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.483, -0.267, -0.323, 0.933, 0.825, 
            0.337),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Phys14NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-PHYS14-PU20bx25-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(False)
)

process.mvaEleID_Spring15_25ns_Trig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.988153, 0.96791, 0.841729),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp80')
)

process.mvaEleID_Spring15_25ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.972153, 0.922126, 0.610764),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp90')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(0.287435, 0.221846, -0.303263, 0.967083, 0.929117, 
            0.726311),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp80')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.083313, -0.235222, -0.67099, 0.913286, 0.805013, 
            0.358969),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp90')
)

process.mvaEleID_Spring15_25ns_nonTrig_V1_wpLoose = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
        mvaCuts = cms.vdouble(-0.265, -0.556, -0.551, -0.072, -0.286, 
            -0.267),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wpLoose')
)

process.mvaEleID_Spring15_50ns_Trig_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
    mvaTag = cms.string('50nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vdouble(0.981841, 0.946762, 0.79704),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring15_50ns_Trig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('GsfEleMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Categories"),
        mvaCuts = cms.vdouble(0.953843, 0.849994, 0.514118),
        mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig50nsV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaEleID-Spring15-50ns-Trig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaEleID_Spring16_GeneralPurpose_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring16GeneralPurpose'),
    mvaTag = cms.string('V1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
)

process.mvaEleID_Spring16_HZZ_V1_producer_config = cms.PSet(
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversionsAOD = cms.InputTag("allConversions"),
    conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
    mvaName = cms.string('ElectronMVAEstimatorRun2Spring16HZZ'),
    mvaTag = cms.string('V1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('25nsV2p1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(False),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
)

process.mvaPhoID_Spring15_25ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.374, 0.336),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig25nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-25ns-nonTrig-V2p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_producer_config = cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('50nsV2p1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(False),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
)

process.mvaPhoID_Spring15_50ns_nonTrig_V2p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Categories"),
        mvaCuts = cms.vdouble(0.29538, 0.45837),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring15NonTrig50nsV2p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring15-50ns-nonTrig-V2p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring16_nonTrig_V1_producer_config = cms.PSet(
    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring16NonTrig'),
    mvaTag = cms.string('V1'),
    phoChargedIsolation = cms.InputTag("egmPhotonIsolation","h+-DR030-"),
    phoIsoCutoff = cms.double(2.5),
    phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
    phoPhotonIsolation = cms.InputTag("egmPhotonIsolation","gamma-DR030-"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolationWithConeVeto"),
    rho = cms.InputTag("fixedGridRhoAll"),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EB_V3.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EE_V3.weights.xml')
)

process.mvaPhoID_Spring16_nonTrig_V1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
        mvaCuts = cms.vdouble(0.68, 0.6),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_Spring16_nonTrig_V1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
        mvaCuts = cms.vdouble(0.2, 0.2),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.pset = cms.PSet(
    etaMax = cms.double(-2.901376),
    etaMin = cms.double(-5.2),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('egammaHFMinus'),
    px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
    py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
    type = cms.int32(7),
    varType = cms.int32(0)
)

process.simple = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.9, -0.9, -0.94, -0.9),
        Pt010_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
        Pt010_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
        Pt1020_Loose = cms.vdouble(-0.9, -0.9, -0.94, -0.9),
        Pt1020_Medium = cms.vdouble(-0.73, -0.89, -0.89, -0.83),
        Pt1020_Tight = cms.vdouble(-0.5, -0.2, -0.83, -0.7),
        Pt2030_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
        Pt2030_Medium = cms.vdouble(0.1, -0.4, -0.5, -0.45),
        Pt2030_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0),
        Pt3050_Loose = cms.vdouble(-0.4, -0.85, -0.7, -0.6),
        Pt3050_Medium = cms.vdouble(0.1, -0.4, -0.5, -0.45),
        Pt3050_Tight = cms.vdouble(-0.2, 0.0, 0.0, 0.0)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('simple'),
    tmvaMethod = cms.string('PuJetIdMinMVA'),
    tmvaSpectators = cms.vstring('nvtx', 
        'jetPt', 
        'jetEta'),
    tmvaVariables = cms.vstring('frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'beta', 
        'betaStar'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_PuJetIdMinMVA.weights.xml.gz'),
    version = cms.int32(-1)
)

process.simple_5x = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.95, -0.97, -0.96, -0.97),
        Pt010_Medium = cms.vdouble(-0.85, -0.96, -0.95, -0.96),
        Pt010_Tight = cms.vdouble(-0.54, -0.93, -0.93, -0.94),
        Pt1020_Loose = cms.vdouble(-0.95, -0.97, -0.96, -0.97),
        Pt1020_Medium = cms.vdouble(-0.85, -0.96, -0.95, -0.96),
        Pt1020_Tight = cms.vdouble(-0.54, -0.93, -0.93, -0.94),
        Pt2030_Loose = cms.vdouble(-0.8, -0.86, -0.8, -0.84),
        Pt2030_Medium = cms.vdouble(-0.4, -0.73, -0.74, -0.8),
        Pt2030_Tight = cms.vdouble(0.26, -0.54, -0.63, -0.74),
        Pt3050_Loose = cms.vdouble(-0.8, -0.86, -0.8, -0.84),
        Pt3050_Medium = cms.vdouble(-0.4, -0.73, -0.74, -0.8),
        Pt3050_Tight = cms.vdouble(0.26, -0.54, -0.63, -0.74)
    ),
    cutBased = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('simple'),
    tmvaMethod = cms.string('BDT_simpleNoVtxCat'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta'),
    tmvaVariables = cms.vstring('frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'nvtx', 
        'beta', 
        'betaStar'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_5x_BDT_simpleNoVtxCat.weights.xml.gz'),
    version = cms.int32(-1)
)

process.simple_5x_chs = cms.PSet(
    JetIdParams = cms.PSet(
        Pt010_Loose = cms.vdouble(-0.98, -0.96, -0.94, -0.94),
        Pt010_Medium = cms.vdouble(-0.95, -0.94, -0.92, -0.91),
        Pt010_Tight = cms.vdouble(-0.6, -0.74, -0.78, -0.81),
        Pt1020_Loose = cms.vdouble(-0.98, -0.96, -0.94, -0.94),
        Pt1020_Medium = cms.vdouble(-0.95, -0.94, -0.92, -0.91),
        Pt1020_Tight = cms.vdouble(-0.6, -0.74, -0.78, -0.81),
        Pt2030_Loose = cms.vdouble(-0.89, -0.75, -0.72, -0.75),
        Pt2030_Medium = cms.vdouble(-0.59, -0.65, -0.56, -0.68),
        Pt2030_Tight = cms.vdouble(-0.47, -0.06, -0.23, -0.47),
        Pt3050_Loose = cms.vdouble(-0.89, -0.75, -0.72, -0.75),
        Pt3050_Medium = cms.vdouble(-0.59, -0.65, -0.56, -0.68),
        Pt3050_Tight = cms.vdouble(-0.47, -0.06, -0.23, -0.47)
    ),
    cutBased = cms.bool(False),
    etaBinnedWeights = cms.bool(False),
    impactParTkThreshold = cms.double(1.0),
    label = cms.string('simple'),
    tmvaMethod = cms.string('BDT_chsSimpleNoVtxCat'),
    tmvaSpectators = cms.vstring('jetPt', 
        'jetEta'),
    tmvaVariables = cms.vstring('frac01', 
        'frac02', 
        'frac03', 
        'frac04', 
        'frac05', 
        'nvtx', 
        'beta', 
        'betaStar'),
    tmvaWeights = cms.string('RecoJets/JetProducers/data/TMVAClassification_5x_BDT_chsSimpleNoVtxCat.weights.xml.gz'),
    version = cms.int32(-1)
)

process.simple_5x_chs_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.98, -0.96, -0.94, -0.94),
    Pt010_Medium = cms.vdouble(-0.95, -0.94, -0.92, -0.91),
    Pt010_Tight = cms.vdouble(-0.6, -0.74, -0.78, -0.81),
    Pt1020_Loose = cms.vdouble(-0.98, -0.96, -0.94, -0.94),
    Pt1020_Medium = cms.vdouble(-0.95, -0.94, -0.92, -0.91),
    Pt1020_Tight = cms.vdouble(-0.6, -0.74, -0.78, -0.81),
    Pt2030_Loose = cms.vdouble(-0.89, -0.75, -0.72, -0.75),
    Pt2030_Medium = cms.vdouble(-0.59, -0.65, -0.56, -0.68),
    Pt2030_Tight = cms.vdouble(-0.47, -0.06, -0.23, -0.47),
    Pt3050_Loose = cms.vdouble(-0.89, -0.75, -0.72, -0.75),
    Pt3050_Medium = cms.vdouble(-0.59, -0.65, -0.56, -0.68),
    Pt3050_Tight = cms.vdouble(-0.47, -0.06, -0.23, -0.47)
)

process.simple_5x_wp = cms.PSet(
    Pt010_Loose = cms.vdouble(-0.95, -0.97, -0.96, -0.97),
    Pt010_Medium = cms.vdouble(-0.85, -0.96, -0.95, -0.96),
    Pt010_Tight = cms.vdouble(-0.54, -0.93, -0.93, -0.94),
    Pt1020_Loose = cms.vdouble(-0.95, -0.97, -0.96, -0.97),
    Pt1020_Medium = cms.vdouble(-0.85, -0.96, -0.95, -0.96),
    Pt1020_Tight = cms.vdouble(-0.54, -0.93, -0.93, -0.94),
    Pt2030_Loose = cms.vdouble(-0.8, -0.86, -0.8, -0.84),
    Pt2030_Medium = cms.vdouble(-0.4, -0.73, -0.74, -0.8),
    Pt2030_Tight = cms.vdouble(0.26, -0.54, -0.63, -0.74),
    Pt3050_Loose = cms.vdouble(-0.8, -0.86, -0.8, -0.84),
    Pt3050_Medium = cms.vdouble(-0.4, -0.73, -0.74, -0.8),
    Pt3050_Tight = cms.vdouble(0.26, -0.54, -0.63, -0.74)
)

process.IsoConeDefinitions = cms.VPSet(cms.PSet(
    coneSize = cms.double(0.3),
    isolateAgainst = cms.string('h+'),
    isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
    miniAODVertexCodes = cms.vuint32(2, 3),
    vertexIndex = cms.int32(0)
), 
    cms.PSet(
        coneSize = cms.double(0.3),
        isolateAgainst = cms.string('h0'),
        isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
        miniAODVertexCodes = cms.vuint32(2, 3),
        vertexIndex = cms.int32(0)
    ), 
    cms.PSet(
        coneSize = cms.double(0.3),
        isolateAgainst = cms.string('gamma'),
        isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
        miniAODVertexCodes = cms.vuint32(2, 3),
        vertexIndex = cms.int32(0)
    ))

process.multPhiCorrParams_T0pcT1T2Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0pcT1T2Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0pcT1Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0pcT1Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0pcTxy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0pcTxy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0rtT1T2Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0rtT1T2Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0rtT1Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0rtT1Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0rtTxy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T0rtTxy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T1T2Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T1T2Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T1Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_T1Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.multPhiCorrParams_Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.mvaConfigsForEleProducer = cms.VPSet(cms.PSet(
    mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
    mvaTag = cms.string('25nsV1'),
    weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
        'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
        mvaTag = cms.string('50nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring16HZZ'),
        mvaTag = cms.string('V1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
    ), 
    cms.PSet(
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversionsAOD = cms.InputTag("allConversions"),
        conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
        mvaName = cms.string('ElectronMVAEstimatorRun2Spring16GeneralPurpose'),
        mvaTag = cms.string('V1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
    ))

process.mvaConfigsForPhoProducer = cms.VPSet(cms.PSet(
    esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
    full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
    full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
    full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
    full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
    full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
    mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
    mvaTag = cms.string('50nsV2p1'),
    phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
    phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
    phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    useValueMaps = cms.bool(False),
    weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
        'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
), 
    cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('25nsV2p1'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(False),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
    ), 
    cms.PSet(
        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring16NonTrig'),
        mvaTag = cms.string('V1'),
        phoChargedIsolation = cms.InputTag("egmPhotonIsolation","h+-DR030-"),
        phoIsoCutoff = cms.double(2.5),
        phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
        phoPhotonIsolation = cms.InputTag("egmPhotonIsolation","gamma-DR030-"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolationWithConeVeto"),
        rho = cms.InputTag("fixedGridRhoAll"),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EB_V3.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EE_V3.weights.xml')
    ))

process.patMultPhiCorrParams_T0pcT1SmearTxy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T0pcT1SmearTxy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T0pcT1T2SmearTxy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T0pcT1T2SmearTxy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T0pcT1T2Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T0pcT1T2Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T0pcT1Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T0pcT1Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T0pcTxy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T0pcTxy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T1SmearTxy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T1SmearTxy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T1T2SmearTxy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T1T2SmearTxy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T1T2Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T1T2Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T1Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_T1Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_Txy_25ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
    py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
        py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
        py = cms.vdouble(0.00798098092474, -0.000103998219585),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00305719113962, -0.00032676418359),
        py = cms.vdouble(-0.00345131507897, 0.000164816815994),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.000159031461755, 0.00012231873804),
        py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
        py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
        py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
        py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
        py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
        py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
        py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
        py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.patMultPhiCorrParams_Txy_50ns = cms.VPSet(cms.PSet(
    etaMax = cms.double(2.7),
    etaMin = cms.double(0),
    fx = cms.string('(x*[0])+(sq(x)*[1])'),
    fy = cms.string('(x*[0])+(sq(x)*[1])'),
    name = cms.string('hEtaPlus'),
    px = cms.vdouble(-0.00220049396857, 4.86017686051e-07),
    py = cms.vdouble(0.000301784350668, -2.55951949068e-07),
    type = cms.int32(1),
    varType = cms.int32(0)
), 
    cms.PSet(
        etaMax = cms.double(0),
        etaMin = cms.double(-2.7),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaMinus'),
        px = cms.vdouble(-0.000217969078412, 3.0200051094e-07),
        py = cms.vdouble(-0.0014606200538, -2.29508676725e-06),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.392),
        etaMin = cms.double(-1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0Barrel'),
        px = cms.vdouble(-0.0135587323577, 5.55593286464e-05),
        py = cms.vdouble(0.00848783774079, -0.00022596699093),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3),
        etaMin = cms.double(1.392),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapPlus'),
        px = cms.vdouble(-0.00285895832031, -6.08161900014e-05),
        py = cms.vdouble(-0.00934018266651, 0.000259105827172),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.392),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('h0EndcapMinus'),
        px = cms.vdouble(-0.00537876208774, 0.000209817129512),
        py = cms.vdouble(0.011148063877, -4.44149746767e-06),
        type = cms.int32(5),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(1.479),
        etaMin = cms.double(-1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaBarrel'),
        px = cms.vdouble(-0.00192842680623, 2.61152485314e-06),
        py = cms.vdouble(-0.000507607323037, 4.48832037695e-06),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(3.0),
        etaMin = cms.double(1.479),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapPlus'),
        px = cms.vdouble(-0.000519297328533, -2.0682880001e-05),
        py = cms.vdouble(0.00282867507264, 6.66930895313e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-1.479),
        etaMin = cms.double(-3.0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('gammaEndcapMinus'),
        px = cms.vdouble(-0.00103112559755, 1.33699817646e-05),
        py = cms.vdouble(-0.00209888421545, -3.30667819828e-05),
        type = cms.int32(4),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFPlus'),
        px = cms.vdouble(-0.000392672935556, -9.65693700264e-07),
        py = cms.vdouble(0.000114612488388, -3.44552389568e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hHFMinus'),
        px = cms.vdouble(-0.00093227965176, 7.74599924874e-07),
        py = cms.vdouble(-2.95036363418e-05, -7.98830257983e-07),
        type = cms.int32(6),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(5.2),
        etaMin = cms.double(2.901376),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFPlus'),
        px = cms.vdouble(0.00275218993341, -1.69184089548e-05),
        py = cms.vdouble(-0.00113061539637, 6.05994897808e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ), 
    cms.PSet(
        etaMax = cms.double(-2.901376),
        etaMin = cms.double(-5.2),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('egammaHFMinus'),
        px = cms.vdouble(0.00136623849956, -5.55451851761e-06),
        py = cms.vdouble(0.00117549065237, -6.54719096891e-06),
        type = cms.int32(7),
        varType = cms.int32(0)
    ))

process.puppiCentral = cms.VPSet(cms.PSet(
    algoId = cms.int32(5),
    applyLowPUCorr = cms.bool(False),
    combOpt = cms.int32(0),
    cone = cms.double(0.4),
    rmsPtMin = cms.double(0.1),
    rmsScaleFactor = cms.double(1.0),
    useCharged = cms.bool(True)
))

process.puppiForward = cms.VPSet(cms.PSet(
    algoId = cms.int32(5),
    applyLowPUCorr = cms.bool(False),
    combOpt = cms.int32(0),
    cone = cms.double(0.4),
    rmsPtMin = cms.double(0.5),
    rmsScaleFactor = cms.double(1.0),
    useCharged = cms.bool(False)
))

process.HBHENoiseFilterResultProducer = cms.EDProducer("HBHENoiseFilterResultProducer",
    IgnoreTS4TS5ifJetInLowBVRegion = cms.bool(False),
    defaultDecision = cms.string('HBHENoiseFilterResultRun2Loose'),
    minHPDHits = cms.int32(17),
    minHPDNoOtherHits = cms.int32(10),
    minIsolatedNoiseSumE = cms.double(50.0),
    minIsolatedNoiseSumEt = cms.double(25.0),
    minNumIsolatedNoiseChannels = cms.int32(10),
    minZeros = cms.int32(99999),
    noiselabel = cms.InputTag("hcalnoise"),
    useBunchSpacingProducer = cms.bool(True)
)


process.PFCandAssoMap = cms.EDProducer("PFCand_AssoMap",
    AssociationType = cms.InputTag("Both"),
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ConversionsCollection = cms.InputTag("allConversions"),
    FinalAssociation = cms.untracked.int32(1),
    GetCleanedCollections = cms.bool(False),
    MaxNumberOfAssociations = cms.int32(1),
    NIVertexCollection = cms.InputTag("particleFlowDisplacedVertex"),
    PFCandidateCollection = cms.InputTag("particleFlow"),
    V0KshortCollection = cms.InputTag("generalV0Candidates","Kshort"),
    V0LambdaCollection = cms.InputTag("generalV0Candidates","Lambda"),
    VertexCollection = cms.InputTag("offlinePrimaryVertices"),
    doReassociation = cms.bool(True),
    ignoreMissingCollection = cms.bool(True),
    nTrackWeight = cms.double(0.001)
)


process.ak4CaloL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1FastjetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4CaloL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL1OffsetCorrector", "ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4CaloL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector")
)


process.ak4CaloL2L3CorrectorPuppi = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag(cms.InputTag("ak4CaloL2RelativeCorrectorPuppi"), cms.InputTag("ak4CaloL3AbsoluteCorrectorPuppi"))
)


process.ak4CaloL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloL6SLBCorrector")
)


process.ak4CaloL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4CaloL2RelativeCorrector", "ak4CaloL3AbsoluteCorrector", "ak4CaloResidualCorrector")
)


process.ak4CaloL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL2RelativeCorrectorPuppi = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2Relative')
)


process.ak4CaloL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL3AbsoluteCorrectorPuppi = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L3Absolute')
)


process.ak4CaloL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(True),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4CaloJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4CaloJetsSoftMuonTagInfos")
)


process.ak4CaloResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L2L3Residual')
)


process.ak4JPTL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4JPTL1FastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4JPTL1FastjetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK5Calo'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAllCalo")
)


process.ak4JPTL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4JPTL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector")
)


process.ak4JPTL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4L1JPTOffsetCorrector", "ak4JPTL2RelativeCorrector", "ak4JPTL3AbsoluteCorrector", "ak4JPTResidualCorrector")
)


process.ak4JPTL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2Relative')
)


process.ak4JPTL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L3Absolute')
)


process.ak4JPTResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4JPT'),
    level = cms.string('L2L3Residual')
)


process.ak4L1JPTOffsetCorrector = cms.EDProducer("L1JPTOffsetCorrectorProducer",
    algorithm = cms.string('AK5JPT'),
    level = cms.string('L1JPTOffset'),
    offsetService = cms.InputTag("ak4CaloL1OffsetCorrector")
)


process.ak4PFCHSL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1FastL2L3CorrectorPuppi = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag(cms.InputTag("ak4PFCHSL1FastjetCorrectorPuppi"), cms.InputTag("ak4PFCHSL2RelativeCorrectorPuppi"), cms.InputTag("ak4PFCHSL3AbsoluteCorrectorPuppi"))
)


process.ak4PFCHSL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1FastjetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1FastL2L3ResidualCorrectorPuppi = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag(cms.InputTag("ak4PFCHSL1FastjetCorrectorPuppi"), cms.InputTag("ak4PFCHSL2RelativeCorrectorPuppi"), cms.InputTag("ak4PFCHSL3AbsoluteCorrectorPuppi"), cms.InputTag("ak4PFCHSResidualCorrectorPuppi"))
)


process.ak4PFCHSL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1FastjetCorrectorPuppi = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFCHSL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL1OffsetCorrector", "ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFCHSL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector")
)


process.ak4PFCHSL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFCHSL2RelativeCorrector", "ak4PFCHSL3AbsoluteCorrector", "ak4PFCHSResidualCorrector")
)


process.ak4PFCHSL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL2RelativeCorrectorPuppi = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2Relative')
)


process.ak4PFCHSL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSL3AbsoluteCorrectorPuppi = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L3Absolute')
)


process.ak4PFCHSResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFCHSResidualCorrectorPuppi = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFchs'),
    level = cms.string('L2L3Residual')
)


process.ak4PFL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1FastL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1FastjetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL1OffsetCorrector", "ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector")
)


process.ak4PFL2L3L6Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFL6SLBCorrector")
)


process.ak4PFL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFL2RelativeCorrector", "ak4PFL3AbsoluteCorrector", "ak4PFResidualCorrector")
)


process.ak4PFL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2Relative')
)


process.ak4PFL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L3Absolute')
)


process.ak4PFL6SLBCorrector = cms.EDProducer("L6SLBCorrectorProducer",
    addMuonToJet = cms.bool(False),
    algorithm = cms.string(''),
    level = cms.string('L6SLB'),
    srcBTagInfoElectron = cms.InputTag("ak4PFJetsSoftElectronTagInfos"),
    srcBTagInfoMuon = cms.InputTag("ak4PFJetsSoftMuonTagInfos")
)


process.ak4PFPuppiL1FastL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1FastL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1FastjetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1FastjetCorrector = cms.EDProducer("L1FastjetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1FastJet'),
    srcRho = cms.InputTag("fixedGridRhoFastjetAll")
)


process.ak4PFPuppiL1L2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL1L2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL1OffsetCorrector", "ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL1OffsetCorrector = cms.EDProducer("L1OffsetCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L1Offset'),
    minVtxNdof = cms.int32(4),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.ak4PFPuppiL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector")
)


process.ak4PFPuppiL2L3ResidualCorrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4PFPuppiL2RelativeCorrector", "ak4PFPuppiL3AbsoluteCorrector", "ak4PFPuppiResidualCorrector")
)


process.ak4PFPuppiL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2Relative')
)


process.ak4PFPuppiL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L3Absolute')
)


process.ak4PFPuppiResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PFPuppi'),
    level = cms.string('L2L3Residual')
)


process.ak4PFResidualCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4PF'),
    level = cms.string('L2L3Residual')
)


process.ak4TrackL2L3Corrector = cms.EDProducer("ChainedJetCorrectorProducer",
    correctors = cms.VInputTag("ak4TrackL2RelativeCorrector", "ak4TrackL3AbsoluteCorrector")
)


process.ak4TrackL2RelativeCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L2Relative')
)


process.ak4TrackL3AbsoluteCorrector = cms.EDProducer("LXXXCorrectorProducer",
    algorithm = cms.string('AK4TRK'),
    level = cms.string('L3Absolute')
)


process.basicJetsForMet = cms.EDProducer("PATJetCleanerForType1MET",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("patJetsReapplyJEC"),
    type1JetPtThreshold = cms.double(15.0)
)


process.basicJetsForMetPuppi = cms.EDProducer("PATJetCleanerForType1MET",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("patJetsReapplyJECPuppi"),
    type1JetPtThreshold = cms.double(15.0)
)


process.caloMetT1 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"))
)


process.caloMetT1Puppi = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1Puppi","type1"))
)


process.caloMetT1T2 = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1","type1"), cms.InputTag("corrCaloMetType2"))
)


process.caloMetT1T2Puppi = cms.EDProducer("CorrectedCaloMETProducer",
    src = cms.InputTag("caloMetM"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrCaloMetType1Puppi","type1"), cms.InputTag("corrCaloMetType2Puppi"))
)


process.cleanedPatJets = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("slimmedElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("slimmedMuons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("jetSelectorForMet")
)


process.cleanedPatJetsPuppi = cms.EDProducer("PATJetCleaner",
    checkOverlaps = cms.PSet(
        electrons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("slimmedElectrons")
        ),
        muons = cms.PSet(
            algorithm = cms.string('byDeltaR'),
            checkRecoComponents = cms.bool(False),
            deltaR = cms.double(0.5),
            pairCut = cms.string(''),
            preselection = cms.string(''),
            requireNoOverlaps = cms.bool(False),
            src = cms.InputTag("slimmedMuons")
        )
    ),
    finalCut = cms.string(''),
    preselection = cms.string(''),
    src = cms.InputTag("jetSelectorForMetPuppi")
)


process.corrCaloMetType1 = cms.EDProducer("CaloJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4CaloL2L3Corrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    src = cms.InputTag("ak4CaloJets"),
    srcMET = cms.InputTag("caloMetM"),
    type1JetPtThreshold = cms.double(20.0)
)


process.corrCaloMetType1Puppi = cms.EDProducer("CaloJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4CaloL2L3CorrectorPuppi"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    src = cms.InputTag("ak4CaloJets"),
    srcMET = cms.InputTag("caloMetM"),
    type1JetPtThreshold = cms.double(20.0)
)


process.corrCaloMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrCaloMetType1","type2"), cms.InputTag("muCaloMetCorr")),
    type2CorrFormula = cms.string('A + B*TMath::Exp(-C*x)'),
    type2CorrParameter = cms.PSet(
        A = cms.double(2.0),
        B = cms.double(1.3),
        C = cms.double(0.1)
    )
)


process.corrCaloMetType2Puppi = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrCaloMetType1Puppi","type2"), cms.InputTag("muCaloMetCorrPuppi")),
    type2CorrFormula = cms.string('A + B*TMath::Exp(-C*x)'),
    type2CorrParameter = cms.PSet(
        A = cms.double(2.0),
        B = cms.double(1.3),
        C = cms.double(0.1)
    )
)


process.corrPfMetType0PfCand = cms.EDProducer("Type0PFMETcorrInputProducer",
    correction = cms.PSet(
        formula = cms.string('(x<35)?(-( [0]+x*[1]+pow(x, 2)*[2]+pow(x, 3)*[3] )):(-( [0]+35*[1]+pow(35, 2)*[2]+pow(35, 3)*[3] ))'),
        par0 = cms.double(-0.181414),
        par1 = cms.double(-0.476934),
        par2 = cms.double(0.00863564),
        par3 = cms.double(-4.94181e-05)
    ),
    minDz = cms.double(0.2),
    srcHardScatterVertex = cms.InputTag("selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0"),
    srcPFCandidateToVertexAssociations = cms.InputTag("pfCandidateToVertexAssociation")
)


process.corrPfMetType1 = cms.EDProducer("PFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelRes = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    offsetCorrLabel = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("ak4PFJetsCHS"),
    type1JetPtThreshold = cms.double(15.0)
)


process.corrPfMetType1Puppi = cms.EDProducer("PFJetMETcorrInputProducer",
    jetCorrEtaMax = cms.double(9.9),
    jetCorrLabel = cms.InputTag("ak4PFPuppiL1FastL2L3Corrector"),
    jetCorrLabelRes = cms.InputTag("ak4PFPuppiL1FastL2L3ResidualCorrector"),
    offsetCorrLabel = cms.InputTag("ak4PFPuppiL1FastjetCorrector"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("ak4PFJetsPuppi"),
    type1JetPtThreshold = cms.double(15.0)
)


process.corrPfMetType2 = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrPfMetType1","type2"), cms.InputTag("corrPfMetType1","offset"), cms.InputTag("pfCandMETcorr")),
    type2CorrFormula = cms.string('A'),
    type2CorrParameter = cms.PSet(
        A = cms.double(1.4)
    )
)


process.corrPfMetType2Puppi = cms.EDProducer("Type2CorrectionProducer",
    srcUnclEnergySums = cms.VInputTag(cms.InputTag("corrPfMetType1Puppi","type2"), cms.InputTag("corrPfMetType1Puppi","offset"), cms.InputTag("pfCandMETcorrPuppi")),
    type2CorrFormula = cms.string('A'),
    type2CorrParameter = cms.PSet(
        A = cms.double(1.4)
    )
)


process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(cms.PSet(
        idDefinition = cms.PSet(
            cutFlow = cms.VPSet(cms.PSet(
                cutName = cms.string('MinPtCut'),
                isIgnored = cms.bool(False),
                minPt = cms.double(5.0),
                needsAdditionalProducts = cms.bool(False)
            ), 
                cms.PSet(
                    allowedEtaRanges = cms.VPSet(cms.PSet(
                        maxEta = cms.double(1.479),
                        minEta = cms.double(0.0)
                    ), 
                        cms.PSet(
                            maxEta = cms.double(2.5),
                            minEta = cms.double(1.479)
                        )),
                    cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False),
                    useAbsEta = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDEtaInCut'),
                    dEtaInCutValueEB = cms.double(0.0105),
                    dEtaInCutValueEE = cms.double(0.00814),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDPhiInCut'),
                    dPhiInCutValueEB = cms.double(0.115),
                    dPhiInCutValueEE = cms.double(0.182),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                    full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0103),
                    full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0301),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleHadronicOverEMCut'),
                    hadronicOverEMCutValueEB = cms.double(0.104),
                    hadronicOverEMCutValueEE = cms.double(0.0897),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDxyCut'),
                    dxyCutValueEB = cms.double(0.0261),
                    dxyCutValueEE = cms.double(0.118),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                    vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleDzCut'),
                    dzCutValueEB = cms.double(0.41),
                    dzCutValueEE = cms.double(0.822),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                    vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                    eInverseMinusPInverseCutValueEB = cms.double(0.102),
                    eInverseMinusPInverseCutValueEE = cms.double(0.126),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                    isIgnored = cms.bool(False),
                    isRelativeIso = cms.bool(True),
                    isoCutEBHighPt = cms.double(0.0893),
                    isoCutEBLowPt = cms.double(0.0893),
                    isoCutEEHighPt = cms.double(0.121),
                    isoCutEELowPt = cms.double(0.121),
                    needsAdditionalProducts = cms.bool(True),
                    ptCutOff = cms.double(20.0),
                    rho = cms.InputTag("fixedGridRhoFastjetAll")
                ), 
                cms.PSet(
                    beamspotSrc = cms.InputTag("offlineBeamSpot"),
                    conversionSrc = cms.InputTag("allConversions"),
                    conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                    cutName = cms.string('GsfEleConversionVetoCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('GsfEleMissingHitsCut'),
                    isIgnored = cms.bool(False),
                    maxMissingHitsEB = cms.uint32(2),
                    maxMissingHitsEE = cms.uint32(1),
                    needsAdditionalProducts = cms.bool(False)
                )),
            idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-loose')
        ),
        idMD5 = cms.string('4fab9e4d09a2c1a36cbbd2279deb3627'),
        isPOGApproved = cms.untracked.bool(True)
    ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInCut'),
                        dEtaInCutValueEB = cms.double(0.0103),
                        dEtaInCutValueEE = cms.double(0.00733),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0336),
                        dPhiInCutValueEE = cms.double(0.114),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0101),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0283),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0876),
                        hadronicOverEMCutValueEE = cms.double(0.0678),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.0118),
                        dxyCutValueEE = cms.double(0.0739),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDzCut'),
                        dzCutValueEB = cms.double(0.373),
                        dzCutValueEE = cms.double(0.602),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0174),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0898),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0766),
                        isoCutEBLowPt = cms.double(0.0766),
                        isoCutEEHighPt = cms.double(0.0678),
                        isoCutEELowPt = cms.double(0.0678),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-medium')
            ),
            idMD5 = cms.string('aa291aba714c148fcba156544907c440'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInCut'),
                        dEtaInCutValueEB = cms.double(0.00926),
                        dEtaInCutValueEE = cms.double(0.00724),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0336),
                        dPhiInCutValueEE = cms.double(0.0918),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0101),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0279),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0597),
                        hadronicOverEMCutValueEE = cms.double(0.0615),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.0111),
                        dxyCutValueEE = cms.double(0.0351),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDzCut'),
                        dzCutValueEB = cms.double(0.0466),
                        dzCutValueEE = cms.double(0.417),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.012),
                        eInverseMinusPInverseCutValueEE = cms.double(0.00999),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0354),
                        isoCutEBLowPt = cms.double(0.0354),
                        isoCutEEHighPt = cms.double(0.0646),
                        isoCutEELowPt = cms.double(0.0646),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-tight')
            ),
            idMD5 = cms.string('4e13b87c0573d3c8ebf91d446fa1d90f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInCut'),
                        dEtaInCutValueEB = cms.double(0.0152),
                        dEtaInCutValueEE = cms.double(0.0113),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.216),
                        dPhiInCutValueEE = cms.double(0.237),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0114),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0352),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.181),
                        hadronicOverEMCutValueEE = cms.double(0.116),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.0564),
                        dxyCutValueEE = cms.double(0.222),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDzCut'),
                        dzCutValueEB = cms.double(0.472),
                        dzCutValueEE = cms.double(0.921),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.207),
                        eInverseMinusPInverseCutValueEE = cms.double(0.174),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.126),
                        isoCutEBLowPt = cms.double(0.126),
                        isoCutEEHighPt = cms.double(0.144),
                        isoCutEELowPt = cms.double(0.144),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Spring15-25ns-V1-standalone-veto')
            ),
            idMD5 = cms.string('202030579ee3eec90fdc2d236ba3de7e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00477),
                        dEtaInSeedCutValueEE = cms.double(0.00868),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.222),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0314),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.298),
                        hadronicOverEMCutValueEE = cms.double(0.101),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.241),
                        eInverseMinusPInverseCutValueEE = cms.double(0.14),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0994),
                        isoCutEBLowPt = cms.double(0.0994),
                        isoCutEEHighPt = cms.double(0.107),
                        isoCutEELowPt = cms.double(0.107),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-loose')
            ),
            idMD5 = cms.string('c1c4c739f1ba0791d40168c123183475'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00311),
                        dEtaInSeedCutValueEE = cms.double(0.00609),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.103),
                        dPhiInCutValueEE = cms.double(0.045),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0298),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.253),
                        hadronicOverEMCutValueEE = cms.double(0.0878),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.134),
                        eInverseMinusPInverseCutValueEE = cms.double(0.13),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0695),
                        isoCutEBLowPt = cms.double(0.0695),
                        isoCutEEHighPt = cms.double(0.0821),
                        isoCutEELowPt = cms.double(0.0821),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-medium')
            ),
            idMD5 = cms.string('71b43f74a27d2fd3d27416afd22e8692'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00308),
                        dEtaInSeedCutValueEE = cms.double(0.00605),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0816),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0292),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0414),
                        hadronicOverEMCutValueEE = cms.double(0.0641),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0129),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0588),
                        isoCutEBLowPt = cms.double(0.0588),
                        isoCutEEHighPt = cms.double(0.0571),
                        isoCutEELowPt = cms.double(0.0571),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-tight')
            ),
            idMD5 = cms.string('ca2a9db2976d80ba2c13f9bfccdc32f2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00749),
                        dEtaInSeedCutValueEE = cms.double(0.00895),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.228),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0115),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.037),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.356),
                        hadronicOverEMCutValueEE = cms.double(0.211),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.299),
                        eInverseMinusPInverseCutValueEE = cms.double(0.15),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.175),
                        isoCutEBLowPt = cms.double(0.175),
                        isoCutEEHighPt = cms.double(0.159),
                        isoCutEELowPt = cms.double(0.159),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-veto')
            ),
            idMD5 = cms.string('0025c1841da1ab64a08d703ded72409b'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
                    mvaCuts = cms.vdouble(0.988153, 0.96791, 0.841729),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp80')
            ),
            idMD5 = cms.string('81046ab478185af337be1be9b30948ae'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
                    mvaCuts = cms.vdouble(0.972153, 0.922126, 0.610764),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring15-25ns-Trig-V1-wp90')
            ),
            idMD5 = cms.string('bb430b638bf3a4d970627021b0da63ae'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
                    mvaCuts = cms.vdouble(0.287435, 0.221846, -0.303263, 0.967083, 0.929117, 
                        0.726311),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp80')
            ),
            idMD5 = cms.string('113c47ceaea0fa687b8bd6d880eb4957'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
                    mvaCuts = cms.vdouble(-0.083313, -0.235222, -0.67099, 0.913286, 0.805013, 
                        0.358969),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wp90')
            ),
            idMD5 = cms.string('ac4fdc160eefe9eae7338601c02ed4bb'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
                    mvaCuts = cms.vdouble(-0.265, -0.556, -0.551, -0.072, -0.286, 
                        -0.267),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring15-25ns-nonTrig-V1-wpLoose')
            ),
            idMD5 = cms.string('99ff36834c4342110d84ea2350a1229c'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vdouble(0.940962684155, 0.899208843708, 0.758484721184),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80')
            ),
            idMD5 = cms.string('b490bc0b0af2d5f3e9efea562370af2a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vdouble(0.836695742607, 0.715337944031, 0.356799721718),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90')
            ),
            idMD5 = cms.string('14c153aaf3c207deb3ad4932586647a7'),
            isPOGApproved = cms.untracked.bool(True)
        )),
    physicsObjectSrc = cms.InputTag("slimmedElectrons")
)


process.egmPhotonIDs = cms.EDProducer("VersionedPhotonIdProducer",
    physicsObjectIDs = cms.VPSet(cms.PSet(
        idDefinition = cms.PSet(
            cutFlow = cms.VPSet(cms.PSet(
                cutName = cms.string('MinPtCut'),
                isIgnored = cms.bool(False),
                minPt = cms.double(5.0),
                needsAdditionalProducts = cms.bool(False)
            ), 
                cms.PSet(
                    allowedEtaRanges = cms.VPSet(cms.PSet(
                        maxEta = cms.double(1.479),
                        minEta = cms.double(0.0)
                    ), 
                        cms.PSet(
                            maxEta = cms.double(2.5),
                            minEta = cms.double(1.479)
                        )),
                    cutName = cms.string('PhoSCEtaMultiRangeCut'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False),
                    useAbsEta = cms.bool(True)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                    hadronicOverEMCutValueEB = cms.double(0.05),
                    hadronicOverEMCutValueEE = cms.double(0.05),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                    cutValueEB = cms.double(0.0102),
                    cutValueEE = cms.double(0.0274),
                    full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                cms.PSet(
                    C1_EB = cms.double(3.32),
                    C1_EE = cms.double(1.97),
                    C2_EB = cms.double(0),
                    C2_EE = cms.double(0.0),
                    anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoAnyPFIsoWithEACut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfChargedHadrons_25ns_NULLcorrection.txt'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    useRelativeIso = cms.bool(False)
                ), 
                cms.PSet(
                    C1_EB = cms.double(1.92),
                    C1_EE = cms.double(11.86),
                    C2_EB = cms.double(0.014),
                    C2_EE = cms.double(0.0139),
                    C3_EB = cms.double(1.9e-05),
                    C3_EE = cms.double(2.5e-05),
                    anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfNeutralHadrons_25ns_90percentBased.txt'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    useRelativeIso = cms.bool(False)
                ), 
                cms.PSet(
                    C1_EB = cms.double(0.81),
                    C1_EE = cms.double(0.83),
                    C2_EB = cms.double(0.0053),
                    C2_EE = cms.double(0.0034),
                    anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                    barrelCutOff = cms.double(1.479),
                    cutName = cms.string('PhoAnyPFIsoWithEACut'),
                    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfPhotons_25ns_90percentBased.txt'),
                    isIgnored = cms.bool(False),
                    needsAdditionalProducts = cms.bool(True),
                    rho = cms.InputTag("fixedGridRhoFastjetAll"),
                    useRelativeIso = cms.bool(False)
                )),
            idName = cms.string('cutBasedPhotonID-Spring15-25ns-V1-standalone-loose')
        ),
        idMD5 = cms.string('3dbb7c6922f3e1b9eb9cf1c679ff70bb'),
        isPOGApproved = cms.untracked.bool(True)
    ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.05),
                        hadronicOverEMCutValueEE = cms.double(0.05),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0102),
                        cutValueEE = cms.double(0.0268),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.37),
                        C1_EE = cms.double(1.1),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfChargedHadrons_25ns_NULLcorrection.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(1.06),
                        C1_EE = cms.double(2.69),
                        C2_EB = cms.double(0.014),
                        C2_EE = cms.double(0.0139),
                        C3_EB = cms.double(1.9e-05),
                        C3_EE = cms.double(2.5e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfNeutralHadrons_25ns_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.28),
                        C1_EE = cms.double(0.39),
                        C2_EB = cms.double(0.0053),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfPhotons_25ns_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring15-25ns-V1-standalone-medium')
            ),
            idMD5 = cms.string('3c31de4198e6c34a0668e11fae83ac21'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('MinPtCut'),
                    isIgnored = cms.bool(False),
                    minPt = cms.double(5.0),
                    needsAdditionalProducts = cms.bool(False)
                ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(cms.PSet(
                            maxEta = cms.double(1.479),
                            minEta = cms.double(0.0)
                        ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.05),
                        hadronicOverEMCutValueEE = cms.double(0.05),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01),
                        cutValueEE = cms.double(0.0268),
                        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.76),
                        C1_EE = cms.double(0.56),
                        C2_EB = cms.double(0.0),
                        C2_EE = cms.double(0.0),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfChargedHadrons_25ns_NULLcorrection.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.97),
                        C1_EE = cms.double(2.09),
                        C2_EB = cms.double(0.014),
                        C2_EE = cms.double(0.0139),
                        C3_EB = cms.double(1.9e-05),
                        C3_EE = cms.double(2.5e-05),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEAAndQuadScalingCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfNeutralHadrons_25ns_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        C1_EB = cms.double(0.08),
                        C1_EE = cms.double(0.16),
                        C2_EB = cms.double(0.0053),
                        C2_EE = cms.double(0.0034),
                        anyPFIsoMap = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoAnyPFIsoWithEACut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring15/effAreaPhotons_cone03_pfPhotons_25ns_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        useRelativeIso = cms.bool(False)
                    )),
                idName = cms.string('cutBasedPhotonID-Spring15-25ns-V1-standalone-tight')
            ),
            idMD5 = cms.string('82ed54bcaf3c8d0ac4f2ae51aa8ff37d'),
            isPOGApproved = cms.untracked.bool(True)
        )),
    physicsObjectSrc = cms.InputTag("slimmedPhotons")
)


process.egmPhotonIsolation = cms.EDProducer("CITKPFIsolationSumProducer",
    isolationConeDefinitions = cms.VPSet(cms.PSet(
        coneSize = cms.double(0.3),
        isolateAgainst = cms.string('h+'),
        isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
        miniAODVertexCodes = cms.vuint32(2, 3),
        vertexIndex = cms.int32(0)
    ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('h0'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            vertexIndex = cms.int32(0)
        ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('gamma'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            vertexIndex = cms.int32(0)
        )),
    srcForIsolationCone = cms.InputTag("packedPFCandidates"),
    srcToIsolate = cms.InputTag("slimmedPhotons")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        mvaName = cms.string('ElectronMVAEstimatorRun2Phys14NonTrig'),
        mvaTag = cms.string('25nsV1'),
        weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_5_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB1_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EB2_10_oldscenario2phys14_BDT.weights.xml', 
            'RecoEgamma/ElectronIdentification/data/PHYS14/EIDmva_EE_10_oldscenario2phys14_BDT.weights.xml')
    ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('25nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_5_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldNonTrigSpring15_ConvVarCwoBoolean_TMVA412_FullStatLowPt_PairNegWeightsGlobal_BDT.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
            mvaTag = cms.string('50nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_50ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring15Trig'),
            mvaTag = cms.string('25nsV1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB1_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EB2_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring15/EIDmva_EE_10_oldTrigSpring15_25ns_data_1_VarD_TMVA412_Sig6BkgAll_MG_noSpec_BDT.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring16HZZ'),
            mvaTag = cms.string('V1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml')
        ), 
        cms.PSet(
            beamSpot = cms.InputTag("offlineBeamSpot"),
            conversionsAOD = cms.InputTag("allConversions"),
            conversionsMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
            mvaName = cms.string('ElectronMVAEstimatorRun2Spring16GeneralPurpose'),
            mvaTag = cms.string('V1'),
            weightFileNames = cms.vstring('RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml')
        )),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.electronRegressionValueMapProducer = cms.EDProducer("ElectronRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedGsfElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
)


process.genMetExtractor = cms.EDProducer("GenMETExtractor",
    metSource = cms.InputTag("slimmedMETs","","@skipCurrentProcess")
)


process.genMetExtractorPuppi = cms.EDProducer("GenMETExtractor",
    metSource = cms.InputTag("slimmedMETs","","@skipCurrentProcess")
)


process.metrawCalo = cms.EDProducer("RecoMETExtractor",
    correctionLevel = cms.string('rawCalo'),
    metSource = cms.InputTag("slimmedMETs","","@skipCurrentProcess")
)


process.metrawCaloPuppi = cms.EDProducer("RecoMETExtractor",
    correctionLevel = cms.string('rawCalo'),
    metSource = cms.InputTag("slimmedMETsPuppi","","@skipCurrentProcess")
)


process.muCaloMetCorr = cms.EDProducer("MuonMETcorrInputProducer",
    src = cms.InputTag("muons"),
    srcMuonCorrections = cms.InputTag("muonMETValueMapProducer","muCorrData")
)


process.muCaloMetCorrPuppi = cms.EDProducer("MuonMETcorrInputProducer",
    src = cms.InputTag("muons"),
    srcMuonCorrections = cms.InputTag("muonMETValueMapProducer","muCorrData")
)


process.particleFlowDisplacedVertex = cms.EDProducer("PFDisplacedVertexProducer",
    avfParameters = cms.PSet(
        Tini = cms.double(256.0),
        ratio = cms.double(0.25),
        sigmacut = cms.double(6.0)
    ),
    debug = cms.untracked.bool(False),
    longSize = cms.double(5),
    mainVertexLabel = cms.InputTag("offlinePrimaryVertices"),
    minAdaptWeight = cms.double(0.5),
    offlineBeamSpotLabel = cms.InputTag("offlineBeamSpot"),
    primaryVertexCut = cms.double(1.8),
    switchOff2TrackVertex = cms.untracked.bool(True),
    tecCut = cms.double(220),
    tobCut = cms.double(100),
    tracksSelectorParameters = cms.PSet(
        bSelectTracks = cms.bool(True),
        dxy_min = cms.double(0.2),
        nChi2_max = cms.double(5.0),
        nChi2_min = cms.double(0.5),
        nHits_min = cms.int32(6),
        nOuterHits_max = cms.int32(9),
        pt_min = cms.double(0.2),
        quality = cms.string('HighPurity')
    ),
    transvSize = cms.double(1.0),
    verbose = cms.untracked.bool(False),
    vertexCandidatesLabel = cms.InputTag("particleFlowDisplacedVertexCandidate"),
    vertexIdentifierParameters = cms.PSet(
        angles = cms.vdouble(15, 15),
        bIdentifyVertices = cms.bool(True),
        logPrimSec_min = cms.double(0.0),
        looper_eta_max = cms.double(0.1),
        masses = cms.vdouble(0.05, 0.485, 0.515, 0.48, 0.52, 
            1.107, 1.125, 0.2),
        pt_kink_min = cms.double(3.0),
        pt_min = cms.double(0.5)
    )
)


process.particleFlowPtrs = cms.EDProducer("PFCandidateFwdPtrProducer",
    src = cms.InputTag("particleFlow")
)


process.particleFlowPtrsPuppi = cms.EDProducer("PFCandidateFwdPtrProducer",
    src = cms.InputTag("particleFlow")
)


process.patCaloMet = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(False),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetTrue"),
    metSource = cms.InputTag("metrawCalo"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.29, 1.19, 1.07, 1.13, 1.12),
        pjpar = cms.vdouble(-0.04, 0.6504)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("particleFlow"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetCorrFactorsReapplyJEC = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsReapplyJECPuppi = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring('L1FastJet', 
        'L2Relative', 
        'L3Absolute'),
    payload = cms.string('AK4PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJetsPuppi"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetsReapplyJEC = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJEC")),
    jetSource = cms.InputTag("slimmedJets"),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("", "pileupJetIdUpdated:fullDiscriminant")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("", "pileupJetIdUpdated:fullId")
        )
    )
)


process.patJetsReapplyJECPuppi = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsReapplyJECPuppi")),
    jetSource = cms.InputTag("slimmedJetsPuppi"),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patMETs = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(False),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetTrue"),
    metSource = cms.InputTag("pfMetT1"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.29, 1.19, 1.07, 1.13, 1.12),
        pjpar = cms.vdouble(-0.04, 0.6504)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag("selectedPatElectrons", "selectedPatMuons", "selectedPatPhotons"),
    srcPFCands = cms.InputTag("particleFlow"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patPFMet = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(True),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetExtractor"),
    metSource = cms.InputTag("pfMet"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.29, 1.19, 1.07, 1.13, 1.12),
        pjpar = cms.vdouble(-0.04, 0.6504)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFchs_phi'),
    srcJetResPt = cms.string('AK4PFchs_pt'),
    srcJetSF = cms.string('AK4PFchs'),
    srcJets = cms.InputTag("cleanedPatJets"),
    srcLeptons = cms.VInputTag(cms.InputTag("slimmedElectrons"), cms.InputTag("slimmedMuons"), cms.InputTag("slimmedPhotons")),
    srcPFCands = cms.InputTag("packedPFCandidates"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patPFMetPuppi = cms.EDProducer("PATMETProducer",
    addEfficiencies = cms.bool(False),
    addGenMET = cms.bool(True),
    addMuonCorrections = cms.bool(False),
    addResolutions = cms.bool(False),
    computeMETSignificance = cms.bool(True),
    efficiencies = cms.PSet(

    ),
    genMETSource = cms.InputTag("genMetExtractorPuppi"),
    metSource = cms.InputTag("pfMetPuppi"),
    muonSource = cms.InputTag("muons"),
    parameters = cms.PSet(
        dRMatch = cms.double(0.4),
        jetThreshold = cms.double(15),
        jeta = cms.vdouble(0.8, 1.3, 1.9, 2.5),
        jpar = cms.vdouble(1.29, 1.19, 1.07, 1.13, 1.12),
        pjpar = cms.vdouble(-0.04, 0.6504)
    ),
    resolutions = cms.PSet(

    ),
    srcJetResPhi = cms.string('AK4PFPuppi_phi'),
    srcJetResPt = cms.string('AK4PFPuppi_pt'),
    srcJetSF = cms.string('AK4PFPuppi'),
    srcJets = cms.InputTag("cleanedPatJetsPuppi"),
    srcLeptons = cms.VInputTag(cms.InputTag("slimmedElectrons"), cms.InputTag("slimmedMuons"), cms.InputTag("slimmedPhotons")),
    srcPFCands = cms.InputTag("puppiForMET"),
    srcRho = cms.InputTag("fixedGridRhoAll"),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patPFMetT0Corr = cms.EDProducer("Type0PFMETcorrInputProducer",
    correction = cms.PSet(
        formula = cms.string('(x<35)?(-( [0]+x*[1]+pow(x, 2)*[2]+pow(x, 3)*[3] )):(-( [0]+35*[1]+pow(35, 2)*[2]+pow(35, 3)*[3] ))'),
        par0 = cms.double(-0.181414),
        par1 = cms.double(-0.476934),
        par2 = cms.double(0.00863564),
        par3 = cms.double(-4.94181e-05)
    ),
    minDz = cms.double(0.2),
    srcHardScatterVertex = cms.InputTag("selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0"),
    srcPFCandidateToVertexAssociations = cms.InputTag("pfCandidateToVertexAssociation")
)


process.patPFMetT0CorrPuppi = cms.EDProducer("Type0PFMETcorrInputProducer",
    correction = cms.PSet(
        formula = cms.string('(x<35)?(-( [0]+x*[1]+pow(x, 2)*[2]+pow(x, 3)*[3] )):(-( [0]+35*[1]+pow(35, 2)*[2]+pow(35, 3)*[3] ))'),
        par0 = cms.double(-0.181414),
        par1 = cms.double(-0.476934),
        par2 = cms.double(0.00863564),
        par3 = cms.double(-4.94181e-05)
    ),
    minDz = cms.double(0.2),
    srcHardScatterVertex = cms.InputTag("selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0Puppi"),
    srcPFCandidateToVertexAssociations = cms.InputTag("pfCandidateToVertexAssociation")
)


process.patPFMetT0pcT1 = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT0Corr"))
)


process.patPFMetT0pcT1Puppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2CorrPuppi","type1"), cms.InputTag("patPFMetT0CorrPuppi"))
)


process.patPFMetT0pcT1Smear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorr","type1"), cms.InputTag("patPFMetT0Corr"))
)


process.patPFMetT0pcT1T2 = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT2Corr","type2"), cms.InputTag("patPFMetT0Corr"))
)


process.patPFMetT0pcT1T2Puppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2CorrPuppi","type1"), cms.InputTag("patPFMetT2CorrPuppi","type2"), cms.InputTag("patPFMetT0CorrPuppi"))
)


process.patPFMetT0pcT1T2Smear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorr","type1"), cms.InputTag("patPFMetT2SmearCorr","type2"), cms.InputTag("patPFMetT0Corr"))
)


process.patPFMetT0pcT1T2Txy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT2Corr","type2"), cms.InputTag("patPFMetT0Corr"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT0pcT1T2TxySmear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorr","type1"), cms.InputTag("patPFMetT2SmearCorr","type2"), cms.InputTag("patPFMetT0Corr"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT0pcT1Txy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT0Corr"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT0pcT1TxySmear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorr","type1"), cms.InputTag("patPFMetT0Corr"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1 = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"))
)


process.patPFMetT1ElectronEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnDown"))
)


process.patPFMetT1ElectronEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnDownPuppi"))
)


process.patPFMetT1ElectronEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnUp"))
)


process.patPFMetT1ElectronEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnUpPuppi"))
)


process.patPFMetT1JetEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnDown"))
)


process.patPFMetT1JetEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnDownPuppi"))
)


process.patPFMetT1JetEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnUp"))
)


process.patPFMetT1JetEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnUpPuppi"))
)


process.patPFMetT1JetResDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetResDown"))
)


process.patPFMetT1JetResDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetResDownPuppi"))
)


process.patPFMetT1JetResUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetResUp"))
)


process.patPFMetT1JetResUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetResUpPuppi"))
)


process.patPFMetT1MuonEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnDown"))
)


process.patPFMetT1MuonEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnDownPuppi"))
)


process.patPFMetT1MuonEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnUp"))
)


process.patPFMetT1MuonEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnUpPuppi"))
)


process.patPFMetT1PhotonEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnDown"))
)


process.patPFMetT1PhotonEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnDownPuppi"))
)


process.patPFMetT1PhotonEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnUp"))
)


process.patPFMetT1PhotonEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnUpPuppi"))
)


process.patPFMetT1Puppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2CorrPuppi","type1"))
)


process.patPFMetT1Smear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorr","type1"))
)


process.patPFMetT1SmearElectronEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnDown"))
)


process.patPFMetT1SmearElectronEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnDownPuppi"))
)


process.patPFMetT1SmearElectronEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnUp"))
)


process.patPFMetT1SmearElectronEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrElectronEnUpPuppi"))
)


process.patPFMetT1SmearJetEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnDown"))
)


process.patPFMetT1SmearJetEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnDownPuppi"))
)


process.patPFMetT1SmearJetEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnUp"))
)


process.patPFMetT1SmearJetEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrJetEnUpPuppi"))
)


process.patPFMetT1SmearJetResDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrSmearedJetResDown"))
)


process.patPFMetT1SmearJetResDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrSmearedJetResDownPuppi"))
)


process.patPFMetT1SmearJetResUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrSmearedJetResUp"))
)


process.patPFMetT1SmearJetResUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrSmearedJetResUpPuppi"))
)


process.patPFMetT1SmearMuonEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnDown"))
)


process.patPFMetT1SmearMuonEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnDownPuppi"))
)


process.patPFMetT1SmearMuonEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnUp"))
)


process.patPFMetT1SmearMuonEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrMuonEnUpPuppi"))
)


process.patPFMetT1SmearPhotonEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnDown"))
)


process.patPFMetT1SmearPhotonEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnDownPuppi"))
)


process.patPFMetT1SmearPhotonEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnUp"))
)


process.patPFMetT1SmearPhotonEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrPhotonEnUpPuppi"))
)


process.patPFMetT1SmearPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorrPuppi","type1"))
)


process.patPFMetT1SmearTauEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnDown"))
)


process.patPFMetT1SmearTauEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnDownPuppi"))
)


process.patPFMetT1SmearTauEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnUp"))
)


process.patPFMetT1SmearTauEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnUpPuppi"))
)


process.patPFMetT1SmearUnclusteredEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnDown"))
)


process.patPFMetT1SmearUnclusteredEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnDownPuppi"))
)


process.patPFMetT1SmearUnclusteredEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Smear"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnUp"))
)


process.patPFMetT1SmearUnclusteredEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1SmearPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnUpPuppi"))
)


process.patPFMetT1T2 = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT2Corr","type2"))
)


process.patPFMetT1T2Corr = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("cleanedPatJets"),
    type1JetPtThreshold = cms.double(15.0)
)


process.patPFMetT1T2CorrPuppi = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag(""),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("cleanedPatJetsPuppi"),
    type1JetPtThreshold = cms.double(15.0)
)


process.patPFMetT1T2Puppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2CorrPuppi","type1"), cms.InputTag("patPFMetT2CorrPuppi","type2"))
)


process.patPFMetT1T2Smear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorr","type1"), cms.InputTag("patPFMetT2SmearCorr","type2"))
)


process.patPFMetT1T2SmearCorr = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("selectedPatJetsForMetT1T2SmearCorr"),
    type1JetPtThreshold = cms.double(15.0)
)


process.patPFMetT1T2SmearCorrPuppi = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag(""),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("selectedPatJetsForMetT1T2SmearCorrPuppi"),
    type1JetPtThreshold = cms.double(15.0)
)


process.patPFMetT1T2Txy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetT2Corr","type2"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1T2TxySmear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorr","type1"), cms.InputTag("patPFMetT2SmearCorr","type2"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1TauEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnDown"))
)


process.patPFMetT1TauEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnDownPuppi"))
)


process.patPFMetT1TauEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnUp"))
)


process.patPFMetT1TauEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrTauEnUpPuppi"))
)


process.patPFMetT1Txy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2Corr","type1"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1TxyPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2CorrPuppi","type1"), cms.InputTag("patPFMetTxyCorrPuppi"))
)


process.patPFMetT1TxySmear = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetT1T2SmearCorr","type1"), cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetT1UnclusteredEnDown = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnDown"))
)


process.patPFMetT1UnclusteredEnDownPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnDownPuppi"))
)


process.patPFMetT1UnclusteredEnUp = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnUp"))
)


process.patPFMetT1UnclusteredEnUpPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetT1Puppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("shiftedPatMETCorrUnclusteredEnUpPuppi"))
)


process.patPFMetT2Corr = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("cleanedPatJets"),
    type1JetPtThreshold = cms.double(15.0)
)


process.patPFMetT2CorrPuppi = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag(""),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("cleanedPatJetsPuppi"),
    type1JetPtThreshold = cms.double(15.0)
)


process.patPFMetT2SmearCorr = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("selectedPatJetsForMetT2SmearCorr"),
    type1JetPtThreshold = cms.double(15.0)
)


process.patPFMetT2SmearCorrPuppi = cms.EDProducer("PATPFJetMETcorrInputProducer",
    jetCorrLabel = cms.InputTag("L3Absolute"),
    jetCorrLabelRes = cms.InputTag("L2L3Residual"),
    offsetCorrLabel = cms.InputTag("L1FastJet"),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.9),
    skipMuonSelection = cms.string('isGlobalMuon | isStandAloneMuon'),
    skipMuons = cms.bool(True),
    src = cms.InputTag("selectedPatJetsForMetT2SmearCorrPuppi"),
    type1JetPtThreshold = cms.double(15.0)
)


process.patPFMetTxy = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetTxyCorr"))
)


process.patPFMetTxyCorr = cms.EDProducer("MultShiftMETcorrInputProducer",
    parameters = cms.VPSet(cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
        cms.PSet(
            etaMax = cms.double(0),
            etaMin = cms.double(-2.7),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hEtaMinus'),
            px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
            py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
            type = cms.int32(1),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(1.392),
            etaMin = cms.double(-1.392),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0Barrel'),
            px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
            py = cms.vdouble(0.00798098092474, -0.000103998219585),
            type = cms.int32(5),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(3),
            etaMin = cms.double(1.392),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0EndcapPlus'),
            px = cms.vdouble(-0.00305719113962, -0.00032676418359),
            py = cms.vdouble(-0.00345131507897, 0.000164816815994),
            type = cms.int32(5),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-1.392),
            etaMin = cms.double(-3.0),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0EndcapMinus'),
            px = cms.vdouble(-0.000159031461755, 0.00012231873804),
            py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
            type = cms.int32(5),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(1.479),
            etaMin = cms.double(-1.479),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaBarrel'),
            px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
            py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
            type = cms.int32(4),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(3.0),
            etaMin = cms.double(1.479),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaEndcapPlus'),
            px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
            py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
            type = cms.int32(4),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-1.479),
            etaMin = cms.double(-3.0),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaEndcapMinus'),
            px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
            py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
            type = cms.int32(4),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(5.2),
            etaMin = cms.double(2.901376),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hHFPlus'),
            px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
            py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
            type = cms.int32(6),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-2.901376),
            etaMin = cms.double(-5.2),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hHFMinus'),
            px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
            py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
            type = cms.int32(6),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(5.2),
            etaMin = cms.double(2.901376),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('egammaHFPlus'),
            px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
            py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
            type = cms.int32(7),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-2.901376),
            etaMin = cms.double(-5.2),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('egammaHFMinus'),
            px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
            py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
            type = cms.int32(7),
            varType = cms.int32(0)
        )),
    srcPFlow = cms.InputTag("packedPFCandidates"),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.patPFMetTxyCorrPuppi = cms.EDProducer("MultShiftMETcorrInputProducer",
    parameters = cms.VPSet(cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
        cms.PSet(
            etaMax = cms.double(0),
            etaMin = cms.double(-2.7),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hEtaMinus'),
            px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
            py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
            type = cms.int32(1),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(1.392),
            etaMin = cms.double(-1.392),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0Barrel'),
            px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
            py = cms.vdouble(0.00798098092474, -0.000103998219585),
            type = cms.int32(5),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(3),
            etaMin = cms.double(1.392),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0EndcapPlus'),
            px = cms.vdouble(-0.00305719113962, -0.00032676418359),
            py = cms.vdouble(-0.00345131507897, 0.000164816815994),
            type = cms.int32(5),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-1.392),
            etaMin = cms.double(-3.0),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0EndcapMinus'),
            px = cms.vdouble(-0.000159031461755, 0.00012231873804),
            py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
            type = cms.int32(5),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(1.479),
            etaMin = cms.double(-1.479),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaBarrel'),
            px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
            py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
            type = cms.int32(4),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(3.0),
            etaMin = cms.double(1.479),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaEndcapPlus'),
            px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
            py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
            type = cms.int32(4),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-1.479),
            etaMin = cms.double(-3.0),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaEndcapMinus'),
            px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
            py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
            type = cms.int32(4),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(5.2),
            etaMin = cms.double(2.901376),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hHFPlus'),
            px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
            py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
            type = cms.int32(6),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-2.901376),
            etaMin = cms.double(-5.2),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hHFMinus'),
            px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
            py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
            type = cms.int32(6),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(5.2),
            etaMin = cms.double(2.901376),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('egammaHFPlus'),
            px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
            py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
            type = cms.int32(7),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-2.901376),
            etaMin = cms.double(-5.2),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('egammaHFMinus'),
            px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
            py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
            type = cms.int32(7),
            varType = cms.int32(0)
        )),
    srcPFlow = cms.InputTag("puppiForMET"),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.patPFMetTxyPuppi = cms.EDProducer("CorrectedPATMETProducer",
    src = cms.InputTag("patPFMetPuppi"),
    srcCorrections = cms.VInputTag(cms.InputTag("patPFMetTxyCorrPuppi"))
)


process.patSmearedJets = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    variation = cms.int32(0)
)


process.patSmearedJetsPuppi = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJetsPuppi"),
    variation = cms.int32(0)
)


process.pfCandMETcorr = cms.EDProducer("PFCandMETcorrInputProducer",
    src = cms.InputTag("pfCandsNotInJetsForMetCorr")
)


process.pfCandMETcorrPuppi = cms.EDProducer("PFCandMETcorrInputProducer",
    src = cms.InputTag("pfCandsNotInJetsForMetCorrPuppi")
)


process.pfCandidateToVertexAssociation = cms.EDProducer("PFCand_AssoMap",
    AssociationType = cms.InputTag("Both"),
    BeamSpot = cms.InputTag("offlineBeamSpot"),
    ConversionsCollection = cms.InputTag("allConversions"),
    FinalAssociation = cms.untracked.int32(1),
    GetCleanedCollections = cms.bool(False),
    MaxNumberOfAssociations = cms.int32(1),
    NIVertexCollection = cms.InputTag("particleFlowDisplacedVertex"),
    PFCandidateCollection = cms.InputTag("particleFlow"),
    UseBeamSpotCompatibility = cms.untracked.bool(True),
    V0KshortCollection = cms.InputTag("generalV0Candidates","Kshort"),
    V0LambdaCollection = cms.InputTag("generalV0Candidates","Lambda"),
    VertexCollection = cms.InputTag("offlinePrimaryVertices"),
    doReassociation = cms.bool(True),
    ignoreMissingCollection = cms.bool(True),
    nTrackWeight = cms.double(0.001)
)


process.pfCandsForUnclusteredUnc = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("pfCandsNoJetsNoEleNoMuNoTau"),
    veto = cms.InputTag("slimmedPhotons")
)


process.pfCandsForUnclusteredUncPuppi = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("pfCandsNoJetsNoEleNoMuNoTauPuppi"),
    veto = cms.InputTag("slimmedPhotons")
)


process.pfCandsNoJets = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("packedPFCandidates"),
    veto = cms.InputTag("cleanedPatJets")
)


process.pfCandsNoJetsNoEle = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("pfCandsNoJets"),
    veto = cms.InputTag("slimmedElectrons")
)


process.pfCandsNoJetsNoEleNoMu = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("pfCandsNoJetsNoEle"),
    veto = cms.InputTag("slimmedMuons")
)


process.pfCandsNoJetsNoEleNoMuNoTau = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("pfCandsNoJetsNoEleNoMu"),
    veto = cms.InputTag("slimmedTaus")
)


process.pfCandsNoJetsNoEleNoMuNoTauPuppi = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("pfCandsNoJetsNoEleNoMuPuppi"),
    veto = cms.InputTag("slimmedTaus")
)


process.pfCandsNoJetsNoEleNoMuPuppi = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("pfCandsNoJetsNoElePuppi"),
    veto = cms.InputTag("slimmedMuons")
)


process.pfCandsNoJetsNoElePuppi = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("pfCandsNoJetsPuppi"),
    veto = cms.InputTag("slimmedElectrons")
)


process.pfCandsNoJetsPuppi = cms.EDProducer("CandPtrProjector",
    src = cms.InputTag("puppiForMET"),
    veto = cms.InputTag("cleanedPatJetsPuppi")
)


process.pfCandsNotInJetsForMetCorr = cms.EDProducer("PFCandidateFromFwdPtrProducer",
    src = cms.InputTag("pfCandsNotInJetsPtrForMetCorr")
)


process.pfCandsNotInJetsForMetCorrPuppi = cms.EDProducer("PFCandidateFromFwdPtrProducer",
    src = cms.InputTag("pfCandsNotInJetsPtrForMetCorr")
)


process.pfCandsNotInJetsPtrForMetCorr = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrForMetCorr"),
    verbose = cms.untracked.bool(False)
)


process.pfCandsNotInJetsPtrForMetCorrPuppi = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("particleFlowPtrsPuppi"),
    enable = cms.bool(True),
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrForMetCorrPuppi"),
    verbose = cms.untracked.bool(False)
)


process.pfJetsPtrForMetCorr = cms.EDProducer("PFJetFwdPtrProducer",
    src = cms.InputTag("ak4PFJets")
)


process.pfJetsPtrForMetCorrPuppi = cms.EDProducer("PFJetFwdPtrProducer",
    src = cms.InputTag("ak4PFJets")
)


process.pfMETcorrType0 = cms.EDProducer("Type0PFMETcorrInputProducer",
    correction = cms.PSet(
        formula = cms.string('(x<35)?(-( [0]+x*[1]+pow(x, 2)*[2]+pow(x, 3)*[3] )):(-( [0]+35*[1]+pow(35, 2)*[2]+pow(35, 3)*[3] ))'),
        par0 = cms.double(-0.181414),
        par1 = cms.double(-0.476934),
        par2 = cms.double(0.00863564),
        par3 = cms.double(-4.94181e-05)
    ),
    minDz = cms.double(0.2),
    srcHardScatterVertex = cms.InputTag("selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0"),
    srcPFCandidateToVertexAssociations = cms.InputTag("pfCandidateToVertexAssociation")
)


process.pfMEtMultShiftCorr = cms.EDProducer("MultShiftMETcorrInputProducer",
    parameters = cms.VPSet(cms.PSet(
        etaMax = cms.double(2.7),
        etaMin = cms.double(0),
        fx = cms.string('(x*[0])+(sq(x)*[1])'),
        fy = cms.string('(x*[0])+(sq(x)*[1])'),
        name = cms.string('hEtaPlus'),
        px = cms.vdouble(-0.00229295500096, 3.15487850373e-07),
        py = cms.vdouble(0.000114282381437, -1.58467325852e-08),
        type = cms.int32(1),
        varType = cms.int32(0)
    ), 
        cms.PSet(
            etaMax = cms.double(0),
            etaMin = cms.double(-2.7),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hEtaMinus'),
            px = cms.vdouble(-0.000198571488347, -1.94054852726e-07),
            py = cms.vdouble(-0.00137832489313, -2.02238617742e-06),
            type = cms.int32(1),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(1.392),
            etaMin = cms.double(-1.392),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0Barrel'),
            px = cms.vdouble(-0.0153652906396, -3.80210366974e-05),
            py = cms.vdouble(0.00798098092474, -0.000103998219585),
            type = cms.int32(5),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(3),
            etaMin = cms.double(1.392),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0EndcapPlus'),
            px = cms.vdouble(-0.00305719113962, -0.00032676418359),
            py = cms.vdouble(-0.00345131507897, 0.000164816815994),
            type = cms.int32(5),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-1.392),
            etaMin = cms.double(-3.0),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('h0EndcapMinus'),
            px = cms.vdouble(-0.000159031461755, 0.00012231873804),
            py = cms.vdouble(0.0260436390996, -8.17994745657e-05),
            type = cms.int32(5),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(1.479),
            etaMin = cms.double(-1.479),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaBarrel'),
            px = cms.vdouble(-0.00163144589987, 3.17557692226e-06),
            py = cms.vdouble(-0.000710945802217, 6.45810884842e-06),
            type = cms.int32(4),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(3.0),
            etaMin = cms.double(1.479),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaEndcapPlus'),
            px = cms.vdouble(-0.00108893779312, -2.53584544941e-05),
            py = cms.vdouble(0.00188026342884, 8.15028097381e-05),
            type = cms.int32(4),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-1.479),
            etaMin = cms.double(-3.0),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('gammaEndcapMinus'),
            px = cms.vdouble(-0.00130486432072, 1.72313009972e-05),
            py = cms.vdouble(-0.00367119684052, -1.63143116342e-05),
            type = cms.int32(4),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(5.2),
            etaMin = cms.double(2.901376),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hHFPlus'),
            px = cms.vdouble(-0.000218928792083, -1.0492437382e-06),
            py = cms.vdouble(2.7982430778e-05, -6.87804028426e-08),
            type = cms.int32(6),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-2.901376),
            etaMin = cms.double(-5.2),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('hHFMinus'),
            px = cms.vdouble(-0.000851170798547, 3.18768998961e-07),
            py = cms.vdouble(6.10447368609e-05, -5.92655106387e-07),
            type = cms.int32(6),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(5.2),
            etaMin = cms.double(2.901376),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('egammaHFPlus'),
            px = cms.vdouble(0.00138084425101, -6.39459000901e-06),
            py = cms.vdouble(-0.000532336534523, 2.21305870813e-06),
            type = cms.int32(7),
            varType = cms.int32(0)
        ), 
        cms.PSet(
            etaMax = cms.double(-2.901376),
            etaMin = cms.double(-5.2),
            fx = cms.string('(x*[0])+(sq(x)*[1])'),
            fy = cms.string('(x*[0])+(sq(x)*[1])'),
            name = cms.string('egammaHFMinus'),
            px = cms.vdouble(0.00102598393499, -3.37284909389e-06),
            py = cms.vdouble(0.000439449053802, -2.3750891943e-06),
            type = cms.int32(7),
            varType = cms.int32(0)
        )),
    srcPFlow = cms.InputTag("particleFlow"),
    vertexCollection = cms.InputTag("offlinePrimaryVertices")
)


process.pfMet = cms.EDProducer("RecoMETExtractor",
    correctionLevel = cms.string('raw'),
    metSource = cms.InputTag("slimmedMETs","","@skipCurrentProcess")
)


process.pfMetPuppi = cms.EDProducer("PFMETProducer",
    alias = cms.string('pfMet'),
    calculateSignificance = cms.bool(False),
    globalThreshold = cms.double(0.0),
    src = cms.InputTag("puppiForMET")
)


process.pfMetT0pc = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"))
)


process.pfMetT0pcT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT0pcT1T2Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0pcT1Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0pcTxy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0PfCand"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0rt = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"))
)


process.pfMetT0rtT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"), cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT0rtT1T2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrackForType2"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"))
)


process.pfMetT0rtT1T2Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrackForType2"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0rtT1Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"), cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT0rtT2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrackForType2"), cms.InputTag("corrPfMetType2"))
)


process.pfMetT0rtTxy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType0RecoTrack"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT1 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"))
)


process.pfMetT1Puppi = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1Puppi","type1"))
)


process.pfMetT1T2 = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"))
)


process.pfMetT1T2Puppi = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1Puppi","type1"), cms.InputTag("corrPfMetType2Puppi"))
)


process.pfMetT1T2Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetType2"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetT1Txy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetType1","type1"), cms.InputTag("corrPfMetXYMult"))
)


process.pfMetTxy = cms.EDProducer("CorrectedPFMETProducer",
    src = cms.InputTag("pfMet"),
    srcCorrections = cms.VInputTag(cms.InputTag("corrPfMetXYMult"))
)


process.pfNoJet = cms.EDProducer("TPPFJetsOnPFCandidates",
    bottomCollection = cms.InputTag("pfNoElectronJME"),
    enable = cms.bool(True),
    name = cms.untracked.string('noJet'),
    topCollection = cms.InputTag("pfJetsPtrs"),
    verbose = cms.untracked.bool(False)
)


process.photonIDValueMapProducer = cms.EDProducer("PhotonIDValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
    pfCandidates = cms.InputTag("particleFlow"),
    pfCandidatesMiniAOD = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.photonMVAValueMapProducer = cms.EDProducer("PhotonMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
        full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
        full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
        full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
        full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
        full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
        full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
        mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
        mvaTag = cms.string('50nsV2p1'),
        phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
        phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
        phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        useValueMaps = cms.bool(False),
        weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EB_V2.weights.xml', 
            'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_50ns_EE_V2.weights.xml')
    ), 
        cms.PSet(
            esEffSigmaRRMap = cms.InputTag("photonIDValueMapProducer","phoESEffSigmaRR"),
            full5x5E1x3Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E1x3"),
            full5x5E2x2Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x2"),
            full5x5E2x5MaxMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5E2x5Max"),
            full5x5E5x5Map = cms.InputTag("photonIDValueMapProducer","phoFull5x5E5x5"),
            full5x5SigmaIEtaIEtaMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIEta"),
            full5x5SigmaIEtaIPhiMap = cms.InputTag("photonIDValueMapProducer","phoFull5x5SigmaIEtaIPhi"),
            mvaName = cms.string('PhotonMVAEstimatorRun2Spring15NonTrig'),
            mvaTag = cms.string('25nsV2p1'),
            phoChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
            phoPhotonIsolation = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
            phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
            rho = cms.InputTag("fixedGridRhoFastjetAll"),
            useValueMaps = cms.bool(False),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EB_V2.weights.xml', 
                'RecoEgamma/PhotonIdentification/data/Spring15/photon_general_MVA_Spring15_25ns_EE_V2.weights.xml')
        ), 
        cms.PSet(
            effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
            mvaName = cms.string('PhotonMVAEstimatorRun2Spring16NonTrig'),
            mvaTag = cms.string('V1'),
            phoChargedIsolation = cms.InputTag("egmPhotonIsolation","h+-DR030-"),
            phoIsoCutoff = cms.double(2.5),
            phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
            phoPhotonIsolation = cms.InputTag("egmPhotonIsolation","gamma-DR030-"),
            phoWorstChargedIsolation = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolationWithConeVeto"),
            rho = cms.InputTag("fixedGridRhoAll"),
            weightFileNames = cms.vstring('RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EB_V3.weights.xml', 
                'RecoEgamma/PhotonIdentification/data/Spring16/photon_general_MVA_Spring16_EE_V3.weights.xml')
        )),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.photonRegressionValueMapProducer = cms.EDProducer("PhotonRegressionValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    useFull5x5 = cms.bool(False)
)


process.pileupJetId = cms.EDProducer("PileupJetIdProducer",
    algos = cms.VPSet(cms.PSet(
        JetIdParams = cms.PSet(
            Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
            Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
            Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
            Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
            Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
            Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
            Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
            Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
            Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
            Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
            Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
            Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
        ),
        cutBased = cms.bool(False),
        etaBinnedWeights = cms.bool(True),
        impactParTkThreshold = cms.double(1.0),
        label = cms.string('full'),
        nEtaBins = cms.int32(4),
        tmvaMethod = cms.string('JetIDMVAHighPt'),
        tmvaSpectators = cms.vstring('jetPt', 
            'jetEta'),
        trainings = cms.VPSet(cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(0.0),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta0to2p5_BDT.weights.xml.gz')
        ), 
            cms.PSet(
                jEtaMax = cms.double(2.75),
                jEtaMin = cms.double(2.5),
                tmvaVariables = cms.vstring('nvtx', 
                    'dR2Mean', 
                    'nParticles', 
                    'nCharged', 
                    'majW', 
                    'minW', 
                    'frac01', 
                    'frac02', 
                    'frac03', 
                    'frac04', 
                    'ptD', 
                    'beta', 
                    'pull', 
                    'jetR', 
                    'jetRchg'),
                tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p5to2p75_BDT.weights.xml.gz')
            ), 
            cms.PSet(
                jEtaMax = cms.double(3.0),
                jEtaMin = cms.double(2.75),
                tmvaVariables = cms.vstring('nvtx', 
                    'dR2Mean', 
                    'nParticles', 
                    'nCharged', 
                    'majW', 
                    'minW', 
                    'frac01', 
                    'frac02', 
                    'frac03', 
                    'frac04', 
                    'ptD', 
                    'beta', 
                    'pull', 
                    'jetR', 
                    'jetRchg'),
                tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p75to3_BDT.weights.xml.gz')
            ), 
            cms.PSet(
                jEtaMax = cms.double(5.0),
                jEtaMin = cms.double(3.0),
                tmvaVariables = cms.vstring('nvtx', 
                    'dR2Mean', 
                    'nParticles', 
                    'majW', 
                    'minW', 
                    'frac01', 
                    'frac02', 
                    'frac03', 
                    'frac04', 
                    'ptD', 
                    'pull', 
                    'jetR'),
                tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta3to5_BDT.weights.xml.gz')
            )),
        version = cms.int32(-1)
    ), 
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
                Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
            ),
            cutBased = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('cutbased')
        )),
    applyJec = cms.bool(True),
    inputIsCorrected = cms.bool(False),
    jec = cms.string('AK4PFchs'),
    jetids = cms.InputTag(""),
    jets = cms.InputTag("ak4PFJetsCHS"),
    produceJetIds = cms.bool(True),
    residualsFromTxt = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runMvas = cms.bool(True),
    vertexes = cms.InputTag("offlinePrimaryVertices")
)


process.pileupJetIdCalculator = cms.EDProducer("PileupJetIdProducer",
    algos = cms.VPSet(cms.PSet(
        JetIdParams = cms.PSet(
            Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
            Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
            Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
            Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
            Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
            Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
            Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
            Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
            Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
            Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
            Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
            Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
            Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
            Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
            Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
            Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
            Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
        ),
        cutBased = cms.bool(True),
        impactParTkThreshold = cms.double(1.0),
        label = cms.string('cutbased')
    )),
    applyJec = cms.bool(True),
    inputIsCorrected = cms.bool(False),
    jec = cms.string('AK4PFchs'),
    jetids = cms.InputTag(""),
    jets = cms.InputTag("ak4PFJetsCHS"),
    produceJetIds = cms.bool(True),
    residualsFromTxt = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runMvas = cms.bool(False),
    vertexes = cms.InputTag("offlinePrimaryVertices")
)


process.pileupJetIdEvaluator = cms.EDProducer("PileupJetIdProducer",
    algos = cms.VPSet(cms.PSet(
        JetIdParams = cms.PSet(
            Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
            Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
            Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
            Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
            Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
            Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
            Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
            Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
            Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
            Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
            Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
            Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
        ),
        cutBased = cms.bool(False),
        etaBinnedWeights = cms.bool(True),
        impactParTkThreshold = cms.double(1.0),
        label = cms.string('full'),
        nEtaBins = cms.int32(4),
        tmvaMethod = cms.string('JetIDMVAHighPt'),
        tmvaSpectators = cms.vstring('jetPt', 
            'jetEta'),
        trainings = cms.VPSet(cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(0.0),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta0to2p5_BDT.weights.xml.gz')
        ), 
            cms.PSet(
                jEtaMax = cms.double(2.75),
                jEtaMin = cms.double(2.5),
                tmvaVariables = cms.vstring('nvtx', 
                    'dR2Mean', 
                    'nParticles', 
                    'nCharged', 
                    'majW', 
                    'minW', 
                    'frac01', 
                    'frac02', 
                    'frac03', 
                    'frac04', 
                    'ptD', 
                    'beta', 
                    'pull', 
                    'jetR', 
                    'jetRchg'),
                tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p5to2p75_BDT.weights.xml.gz')
            ), 
            cms.PSet(
                jEtaMax = cms.double(3.0),
                jEtaMin = cms.double(2.75),
                tmvaVariables = cms.vstring('nvtx', 
                    'dR2Mean', 
                    'nParticles', 
                    'nCharged', 
                    'majW', 
                    'minW', 
                    'frac01', 
                    'frac02', 
                    'frac03', 
                    'frac04', 
                    'ptD', 
                    'beta', 
                    'pull', 
                    'jetR', 
                    'jetRchg'),
                tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p75to3_BDT.weights.xml.gz')
            ), 
            cms.PSet(
                jEtaMax = cms.double(5.0),
                jEtaMin = cms.double(3.0),
                tmvaVariables = cms.vstring('nvtx', 
                    'dR2Mean', 
                    'nParticles', 
                    'majW', 
                    'minW', 
                    'frac01', 
                    'frac02', 
                    'frac03', 
                    'frac04', 
                    'ptD', 
                    'pull', 
                    'jetR'),
                tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta3to5_BDT.weights.xml.gz')
            )),
        version = cms.int32(-1)
    ), 
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
                Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
            ),
            cutBased = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('cutbased')
        )),
    applyJec = cms.bool(True),
    inputIsCorrected = cms.bool(False),
    jec = cms.string('AK4PFchs'),
    jetids = cms.InputTag("pileupJetIdCalculator"),
    jets = cms.InputTag("ak4PFJetsCHS"),
    produceJetIds = cms.bool(False),
    residualsFromTxt = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runMvas = cms.bool(True),
    vertexes = cms.InputTag("offlinePrimaryVertices")
)


process.pileupJetIdUpdated = cms.EDProducer("PileupJetIdProducer",
    algos = cms.VPSet(cms.PSet(
        JetIdParams = cms.PSet(
            Pt010_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
            Pt010_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
            Pt010_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
            Pt1020_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
            Pt1020_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
            Pt1020_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
            Pt2030_Loose = cms.vdouble(-0.97, -0.68, -0.53, -0.47),
            Pt2030_Medium = cms.vdouble(0.18, -0.55, -0.42, -0.36),
            Pt2030_Tight = cms.vdouble(0.69, -0.35, -0.26, -0.21),
            Pt3050_Loose = cms.vdouble(-0.89, -0.52, -0.38, -0.3),
            Pt3050_Medium = cms.vdouble(0.61, -0.35, -0.23, -0.17),
            Pt3050_Tight = cms.vdouble(0.86, -0.1, -0.05, -0.01)
        ),
        cutBased = cms.bool(False),
        etaBinnedWeights = cms.bool(True),
        impactParTkThreshold = cms.double(1.0),
        label = cms.string('full'),
        nEtaBins = cms.int32(4),
        tmvaMethod = cms.string('JetIDMVAHighPt'),
        tmvaSpectators = cms.vstring('jetPt', 
            'jetEta'),
        trainings = cms.VPSet(cms.PSet(
            jEtaMax = cms.double(2.5),
            jEtaMin = cms.double(0.0),
            tmvaVariables = cms.vstring('nvtx', 
                'dR2Mean', 
                'nParticles', 
                'nCharged', 
                'majW', 
                'minW', 
                'frac01', 
                'frac02', 
                'frac03', 
                'frac04', 
                'ptD', 
                'beta', 
                'pull', 
                'jetR', 
                'jetRchg'),
            tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta0to2p5_BDT.weights.xml.gz')
        ), 
            cms.PSet(
                jEtaMax = cms.double(2.75),
                jEtaMin = cms.double(2.5),
                tmvaVariables = cms.vstring('nvtx', 
                    'dR2Mean', 
                    'nParticles', 
                    'nCharged', 
                    'majW', 
                    'minW', 
                    'frac01', 
                    'frac02', 
                    'frac03', 
                    'frac04', 
                    'ptD', 
                    'beta', 
                    'pull', 
                    'jetR', 
                    'jetRchg'),
                tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p5to2p75_BDT.weights.xml.gz')
            ), 
            cms.PSet(
                jEtaMax = cms.double(3.0),
                jEtaMin = cms.double(2.75),
                tmvaVariables = cms.vstring('nvtx', 
                    'dR2Mean', 
                    'nParticles', 
                    'nCharged', 
                    'majW', 
                    'minW', 
                    'frac01', 
                    'frac02', 
                    'frac03', 
                    'frac04', 
                    'ptD', 
                    'beta', 
                    'pull', 
                    'jetR', 
                    'jetRchg'),
                tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta2p75to3_BDT.weights.xml.gz')
            ), 
            cms.PSet(
                jEtaMax = cms.double(5.0),
                jEtaMin = cms.double(3.0),
                tmvaVariables = cms.vstring('nvtx', 
                    'dR2Mean', 
                    'nParticles', 
                    'majW', 
                    'minW', 
                    'frac01', 
                    'frac02', 
                    'frac03', 
                    'frac04', 
                    'ptD', 
                    'pull', 
                    'jetR'),
                tmvaWeights = cms.string('RecoJets/JetProducers/data/pileupJetId_80XvarFix_Eta3to5_BDT.weights.xml.gz')
            )),
        version = cms.int32(-1)
    ), 
        cms.PSet(
            JetIdParams = cms.PSet(
                Pt010_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt010_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt010_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt010_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt010_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt1020_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt1020_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt1020_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.07),
                Pt1020_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt1020_RMSTight = cms.vdouble(0.06, 0.07, 0.04, 0.05),
                Pt2030_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt2030_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt2030_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt2030_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt2030_RMSTight = cms.vdouble(0.05, 0.07, 0.03, 0.045),
                Pt3050_BetaStarLoose = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarMedium = cms.vdouble(0.2, 0.3, 999.0, 999.0),
                Pt3050_BetaStarTight = cms.vdouble(0.15, 0.15, 999.0, 999.0),
                Pt3050_RMSLoose = cms.vdouble(0.06, 0.05, 0.05, 0.055),
                Pt3050_RMSMedium = cms.vdouble(0.06, 0.03, 0.03, 0.04),
                Pt3050_RMSTight = cms.vdouble(0.05, 0.06, 0.03, 0.04)
            ),
            cutBased = cms.bool(True),
            impactParTkThreshold = cms.double(1.0),
            label = cms.string('cutbased')
        )),
    applyJec = cms.bool(True),
    inputIsCorrected = cms.bool(True),
    jec = cms.string('AK4PFchs'),
    jetids = cms.InputTag(""),
    jets = cms.InputTag("slimmedJets"),
    produceJetIds = cms.bool(True),
    residualsFromTxt = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runMvas = cms.bool(True),
    vertexes = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.puppi = cms.EDProducer("PuppiProducer",
    DeltaZCut = cms.double(0.3),
    MinPuppiWeight = cms.double(0.01),
    UseDeltaZCut = cms.bool(True),
    algos = cms.VPSet(cms.PSet(
        EtaMaxExtrap = cms.double(2.0),
        MedEtaSF = cms.vdouble(1.0),
        MinNeutralPt = cms.vdouble(0.2),
        MinNeutralPtSlope = cms.vdouble(0.015),
        RMSEtaSF = cms.vdouble(1.0),
        etaMax = cms.vdouble(2.5),
        etaMin = cms.vdouble(0.0),
        ptMin = cms.vdouble(0.0),
        puppiAlgos = cms.VPSet(cms.PSet(
            algoId = cms.int32(5),
            applyLowPUCorr = cms.bool(False),
            combOpt = cms.int32(0),
            cone = cms.double(0.4),
            rmsPtMin = cms.double(0.1),
            rmsScaleFactor = cms.double(1.0),
            useCharged = cms.bool(True)
        ))
    ), 
        cms.PSet(
            EtaMaxExtrap = cms.double(2.0),
            MedEtaSF = cms.vdouble(0.9, 0.75),
            MinNeutralPt = cms.vdouble(1.7, 2.0),
            MinNeutralPtSlope = cms.vdouble(0.08, 0.08),
            RMSEtaSF = cms.vdouble(1.2, 0.95),
            etaMax = cms.vdouble(3.0, 10.0),
            etaMin = cms.vdouble(2.5, 3.0),
            ptMin = cms.vdouble(0.0, 0.0),
            puppiAlgos = cms.VPSet(cms.PSet(
                algoId = cms.int32(5),
                applyLowPUCorr = cms.bool(False),
                combOpt = cms.int32(0),
                cone = cms.double(0.4),
                rmsPtMin = cms.double(0.5),
                rmsScaleFactor = cms.double(1.0),
                useCharged = cms.bool(False)
            ))
        )),
    applyCHS = cms.bool(True),
    candName = cms.InputTag("packedPFCandidates"),
    clonePackedCands = cms.bool(True),
    invertPuppi = cms.bool(False),
    puppiDiagnostics = cms.bool(False),
    puppiForLeptons = cms.bool(False),
    useExistingWeights = cms.bool(False),
    useExp = cms.bool(False),
    useWeightsNoLep = cms.bool(False),
    vertexName = cms.InputTag("offlineSlimmedPrimaryVertices"),
    vtxNdofCut = cms.int32(4),
    vtxZCut = cms.double(24)
)


process.puppiForMET = cms.EDProducer("PuppiPhoton",
    candName = cms.InputTag("packedPFCandidates"),
    dRMatch = cms.vdouble(0.005, 0.005, 0.005, 0.005),
    eta = cms.double(2.5),
    pdgids = cms.vint32(22, 11, 211, 130),
    photonId = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring15-25ns-V1-standalone-loose"),
    photonName = cms.InputTag("slimmedPhotons"),
    pt = cms.double(10),
    puppiCandName = cms.InputTag("puppiMerged"),
    recoToPFMap = cms.InputTag("reducedEgamma","reducedPhotonPfCandMap"),
    runOnMiniAOD = cms.bool(True),
    useRefs = cms.bool(False),
    useValueMap = cms.bool(False),
    weight = cms.double(1.0),
    weightsName = cms.InputTag("puppi")
)


process.puppiMerged = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("puppiNoLep", "pfLeptonsPUPPET")
)


process.puppiNoLep = cms.EDProducer("PuppiProducer",
    DeltaZCut = cms.double(0.3),
    MinPuppiWeight = cms.double(0.01),
    UseDeltaZCut = cms.bool(True),
    algos = cms.VPSet(cms.PSet(
        EtaMaxExtrap = cms.double(2.0),
        MedEtaSF = cms.vdouble(1.0),
        MinNeutralPt = cms.vdouble(0.2),
        MinNeutralPtSlope = cms.vdouble(0.015),
        RMSEtaSF = cms.vdouble(1.0),
        etaMax = cms.vdouble(2.5),
        etaMin = cms.vdouble(0.0),
        ptMin = cms.vdouble(0.0),
        puppiAlgos = cms.VPSet(cms.PSet(
            algoId = cms.int32(5),
            applyLowPUCorr = cms.bool(False),
            combOpt = cms.int32(0),
            cone = cms.double(0.4),
            rmsPtMin = cms.double(0.1),
            rmsScaleFactor = cms.double(1.0),
            useCharged = cms.bool(True)
        ))
    ), 
        cms.PSet(
            EtaMaxExtrap = cms.double(2.0),
            MedEtaSF = cms.vdouble(0.9, 0.75),
            MinNeutralPt = cms.vdouble(1.7, 2.0),
            MinNeutralPtSlope = cms.vdouble(0.08, 0.08),
            RMSEtaSF = cms.vdouble(1.2, 0.95),
            etaMax = cms.vdouble(3.0, 10.0),
            etaMin = cms.vdouble(2.5, 3.0),
            ptMin = cms.vdouble(0.0, 0.0),
            puppiAlgos = cms.VPSet(cms.PSet(
                algoId = cms.int32(5),
                applyLowPUCorr = cms.bool(False),
                combOpt = cms.int32(0),
                cone = cms.double(0.4),
                rmsPtMin = cms.double(0.5),
                rmsScaleFactor = cms.double(1.0),
                useCharged = cms.bool(False)
            ))
        )),
    applyCHS = cms.bool(True),
    candName = cms.InputTag("pfNoLepPUPPI"),
    clonePackedCands = cms.bool(True),
    invertPuppi = cms.bool(False),
    puppiDiagnostics = cms.bool(False),
    puppiForLeptons = cms.bool(False),
    useExistingWeights = cms.bool(False),
    useExp = cms.bool(False),
    useWeightsNoLep = cms.bool(True),
    vertexName = cms.InputTag("offlineSlimmedPrimaryVertices"),
    vtxNdofCut = cms.int32(4),
    vtxZCut = cms.double(24)
)


process.puppiPhoton = cms.EDProducer("PuppiPhoton",
    candName = cms.InputTag("particleFlow"),
    dRMatch = cms.vdouble(0.005, 0.005, 0.005, 0.005),
    eta = cms.double(2.5),
    pdgids = cms.vint32(22, 11, 211, 130),
    photonId = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring15-25ns-V1-standalone-loose"),
    photonName = cms.InputTag("reducedEgamma","reducedGedPhotons"),
    pt = cms.double(10),
    puppiCandName = cms.InputTag("puppi"),
    recoToPFMap = cms.InputTag("reducedEgamma","reducedPhotonPfCandMap"),
    runOnMiniAOD = cms.bool(False),
    useRefs = cms.bool(True),
    useValueMap = cms.bool(False),
    weight = cms.double(1.0),
    weightsName = cms.InputTag("puppi")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.rerunDiscriminationByIsolationMVArun2v1Loose = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff80'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1Medium = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff70'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1Tight = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff60'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1VLoose = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff90'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1VTight = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff50'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1VVTight = cms.EDProducer("PATTauDiscriminantCutMultiplexer",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    key = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw","category"),
    loadMVAfromDB = cms.bool(True),
    mapping = cms.VPSet(cms.PSet(
        category = cms.uint32(0),
        cut = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff40'),
        variable = cms.string('pt')
    )),
    mvaOutput_normalization = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization'),
    toMultiplex = cms.InputTag("rerunDiscriminationByIsolationMVArun2v1raw")
)


process.rerunDiscriminationByIsolationMVArun2v1raw = cms.EDProducer("PATTauDiscriminationByMVAIsolationRun2",
    PATTauProducer = cms.InputTag("slimmedTaus"),
    Prediscriminants = cms.PSet(
        BooleanOperator = cms.string('and')
    ),
    loadMVAfromDB = cms.bool(True),
    mvaName = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1'),
    mvaOpt = cms.string('DBoldDMwLT'),
    requireDecayMode = cms.bool(True),
    srcChargedIsoPtSum = cms.string('chargedIsoPtSum'),
    srcFootprintCorrection = cms.string('footprintCorrection'),
    srcNeutralIsoPtSum = cms.string('neutralIsoPtSum'),
    srcPUcorrPtSum = cms.string('puCorrPtSum'),
    srcPhotonPtSumOutsideSignalCone = cms.string('photonPtSumOutsideSignalCone'),
    verbosity = cms.int32(0)
)


process.shiftedPatElectronEnDown = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("slimmedElectrons"),
    uncertainty = cms.string('((abs(y)<1.479)?(0.006+0*x):(0.015+0*x))')
)


process.shiftedPatElectronEnDownPuppi = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("slimmedElectrons"),
    uncertainty = cms.string('((abs(y)<1.479)?(0.006+0*x):(0.015+0*x))')
)


process.shiftedPatElectronEnUp = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("slimmedElectrons"),
    uncertainty = cms.string('((abs(y)<1.479)?(0.006+0*x):(0.015+0*x))')
)


process.shiftedPatElectronEnUpPuppi = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("slimmedElectrons"),
    uncertainty = cms.string('((abs(y)<1.479)?(0.006+0*x):(0.015+0*x))')
)


process.shiftedPatJetEnDown = cms.EDProducer("ShiftedPATJetProducer",
    addResidualJES = cms.bool(True),
    jetCorrLabelUpToL3 = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    jetCorrPayloadName = cms.string('AK4PFchs'),
    jetCorrUncertaintyTag = cms.string('Uncertainty'),
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("cleanedPatJets")
)


process.shiftedPatJetEnDownPuppi = cms.EDProducer("ShiftedPATJetProducer",
    addResidualJES = cms.bool(True),
    jetCorrLabelUpToL3 = cms.InputTag("ak4PFPuppiL1FastL2L3Corrector"),
    jetCorrLabelUpToL3Res = cms.InputTag("ak4PFPuppiL1FastL2L3ResidualCorrector"),
    jetCorrPayloadName = cms.string('AK4PFPuppi'),
    jetCorrUncertaintyTag = cms.string('Uncertainty'),
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("cleanedPatJetsPuppi")
)


process.shiftedPatJetEnUp = cms.EDProducer("ShiftedPATJetProducer",
    addResidualJES = cms.bool(True),
    jetCorrLabelUpToL3 = cms.InputTag("ak4PFCHSL1FastL2L3Corrector"),
    jetCorrLabelUpToL3Res = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"),
    jetCorrPayloadName = cms.string('AK4PFchs'),
    jetCorrUncertaintyTag = cms.string('Uncertainty'),
    shiftBy = cms.double(1.0),
    src = cms.InputTag("cleanedPatJets")
)


process.shiftedPatJetEnUpPuppi = cms.EDProducer("ShiftedPATJetProducer",
    addResidualJES = cms.bool(True),
    jetCorrLabelUpToL3 = cms.InputTag("ak4PFPuppiL1FastL2L3Corrector"),
    jetCorrLabelUpToL3Res = cms.InputTag("ak4PFPuppiL1FastL2L3ResidualCorrector"),
    jetCorrPayloadName = cms.string('AK4PFPuppi'),
    jetCorrUncertaintyTag = cms.string('Uncertainty'),
    shiftBy = cms.double(1.0),
    src = cms.InputTag("cleanedPatJetsPuppi")
)


process.shiftedPatJetResDown = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    variation = cms.int32(-101)
)


process.shiftedPatJetResDownPuppi = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFPuppi'),
    algopt = cms.string('AK4PFPuppi_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJetsPuppi"),
    variation = cms.int32(-101)
)


process.shiftedPatJetResUp = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    variation = cms.int32(101)
)


process.shiftedPatJetResUpPuppi = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFPuppi'),
    algopt = cms.string('AK4PFPuppi_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJetsPuppi"),
    variation = cms.int32(101)
)


process.shiftedPatMETCorrElectronEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedElectrons"),
    srcShifted = cms.InputTag("shiftedPatElectronEnDown")
)


process.shiftedPatMETCorrElectronEnDownPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedElectrons"),
    srcShifted = cms.InputTag("shiftedPatElectronEnDownPuppi")
)


process.shiftedPatMETCorrElectronEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedElectrons"),
    srcShifted = cms.InputTag("shiftedPatElectronEnUp")
)


process.shiftedPatMETCorrElectronEnUpPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedElectrons"),
    srcShifted = cms.InputTag("shiftedPatElectronEnUpPuppi")
)


process.shiftedPatMETCorrJetEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJets"),
    srcShifted = cms.InputTag("shiftedPatJetEnDown")
)


process.shiftedPatMETCorrJetEnDownPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJetsPuppi"),
    srcShifted = cms.InputTag("shiftedPatJetEnDownPuppi")
)


process.shiftedPatMETCorrJetEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJets"),
    srcShifted = cms.InputTag("shiftedPatJetEnUp")
)


process.shiftedPatMETCorrJetEnUpPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJetsPuppi"),
    srcShifted = cms.InputTag("shiftedPatJetEnUpPuppi")
)


process.shiftedPatMETCorrJetResDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJets"),
    srcShifted = cms.InputTag("shiftedPatJetResDown")
)


process.shiftedPatMETCorrJetResDownPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJetsPuppi"),
    srcShifted = cms.InputTag("shiftedPatJetResDownPuppi")
)


process.shiftedPatMETCorrJetResUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJets"),
    srcShifted = cms.InputTag("shiftedPatJetResUp")
)


process.shiftedPatMETCorrJetResUpPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("cleanedPatJetsPuppi"),
    srcShifted = cms.InputTag("shiftedPatJetResUpPuppi")
)


process.shiftedPatMETCorrMuonEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedMuons"),
    srcShifted = cms.InputTag("shiftedPatMuonEnDown")
)


process.shiftedPatMETCorrMuonEnDownPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedMuons"),
    srcShifted = cms.InputTag("shiftedPatMuonEnDownPuppi")
)


process.shiftedPatMETCorrMuonEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedMuons"),
    srcShifted = cms.InputTag("shiftedPatMuonEnUp")
)


process.shiftedPatMETCorrMuonEnUpPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedMuons"),
    srcShifted = cms.InputTag("shiftedPatMuonEnUpPuppi")
)


process.shiftedPatMETCorrPhotonEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedPhotons"),
    srcShifted = cms.InputTag("shiftedPatPhotonEnDown")
)


process.shiftedPatMETCorrPhotonEnDownPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedPhotons"),
    srcShifted = cms.InputTag("shiftedPatPhotonEnDownPuppi")
)


process.shiftedPatMETCorrPhotonEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedPhotons"),
    srcShifted = cms.InputTag("shiftedPatPhotonEnUp")
)


process.shiftedPatMETCorrPhotonEnUpPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedPhotons"),
    srcShifted = cms.InputTag("shiftedPatPhotonEnUpPuppi")
)


process.shiftedPatMETCorrSmearedJetResDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("selectedPatJetsForMetT1T2SmearCorr"),
    srcShifted = cms.InputTag("shiftedPatSmearedJetResDown")
)


process.shiftedPatMETCorrSmearedJetResDownPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("selectedPatJetsForMetT1T2SmearCorrPuppi"),
    srcShifted = cms.InputTag("shiftedPatSmearedJetResDownPuppi")
)


process.shiftedPatMETCorrSmearedJetResUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("selectedPatJetsForMetT1T2SmearCorr"),
    srcShifted = cms.InputTag("shiftedPatSmearedJetResUp")
)


process.shiftedPatMETCorrSmearedJetResUpPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("selectedPatJetsForMetT1T2SmearCorrPuppi"),
    srcShifted = cms.InputTag("shiftedPatSmearedJetResUpPuppi")
)


process.shiftedPatMETCorrTauEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedTaus"),
    srcShifted = cms.InputTag("shiftedPatTauEnDown")
)


process.shiftedPatMETCorrTauEnDownPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedTaus"),
    srcShifted = cms.InputTag("shiftedPatTauEnDownPuppi")
)


process.shiftedPatMETCorrTauEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedTaus"),
    srcShifted = cms.InputTag("shiftedPatTauEnUp")
)


process.shiftedPatMETCorrTauEnUpPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("slimmedTaus"),
    srcShifted = cms.InputTag("shiftedPatTauEnUpPuppi")
)


process.shiftedPatMETCorrUnclusteredEnDown = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfCandsForUnclusteredUnc"),
    srcShifted = cms.InputTag("shiftedPatUnclusteredEnDown")
)


process.shiftedPatMETCorrUnclusteredEnDownPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfCandsForUnclusteredUncPuppi"),
    srcShifted = cms.InputTag("shiftedPatUnclusteredEnDownPuppi")
)


process.shiftedPatMETCorrUnclusteredEnUp = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfCandsForUnclusteredUnc"),
    srcShifted = cms.InputTag("shiftedPatUnclusteredEnUp")
)


process.shiftedPatMETCorrUnclusteredEnUpPuppi = cms.EDProducer("ShiftedParticleMETcorrInputProducer",
    srcOriginal = cms.InputTag("pfCandsForUnclusteredUncPuppi"),
    srcShifted = cms.InputTag("shiftedPatUnclusteredEnUpPuppi")
)


process.shiftedPatMuonEnDown = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("slimmedMuons"),
    uncertainty = cms.string('((x<100)?(0.002+0*y):(0.05+0*y))')
)


process.shiftedPatMuonEnDownPuppi = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("slimmedMuons"),
    uncertainty = cms.string('((x<100)?(0.002+0*y):(0.05+0*y))')
)


process.shiftedPatMuonEnUp = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("slimmedMuons"),
    uncertainty = cms.string('((x<100)?(0.002+0*y):(0.05+0*y))')
)


process.shiftedPatMuonEnUpPuppi = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("slimmedMuons"),
    uncertainty = cms.string('((x<100)?(0.002+0*y):(0.05+0*y))')
)


process.shiftedPatPhotonEnDown = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("slimmedPhotons"),
    uncertainty = cms.string('((abs(y)<1.479)?(0.01+0*x):(0.025+0*x))')
)


process.shiftedPatPhotonEnDownPuppi = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("slimmedPhotons"),
    uncertainty = cms.string('((abs(y)<1.479)?(0.01+0*x):(0.025+0*x))')
)


process.shiftedPatPhotonEnUp = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("slimmedPhotons"),
    uncertainty = cms.string('((abs(y)<1.479)?(0.01+0*x):(0.025+0*x))')
)


process.shiftedPatPhotonEnUpPuppi = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("slimmedPhotons"),
    uncertainty = cms.string('((abs(y)<1.479)?(0.01+0*x):(0.025+0*x))')
)


process.shiftedPatSmearedJetResDown = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    variation = cms.int32(-1)
)


process.shiftedPatSmearedJetResDownPuppi = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFPuppi'),
    algopt = cms.string('AK4PFPuppi_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJetsPuppi"),
    variation = cms.int32(-1)
)


process.shiftedPatSmearedJetResUp = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFchs'),
    algopt = cms.string('AK4PFchs_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJets"),
    variation = cms.int32(1)
)


process.shiftedPatSmearedJetResUpPuppi = cms.EDProducer("SmearedPATJetProducer",
    algo = cms.string('AK4PFPuppi'),
    algopt = cms.string('AK4PFPuppi_pt'),
    dPtMaxFactor = cms.double(3),
    dRMax = cms.double(0.2),
    debug = cms.untracked.bool(False),
    enabled = cms.bool(True),
    genJets = cms.InputTag("slimmedGenJets"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    seed = cms.uint32(37428479),
    skipGenMatching = cms.bool(False),
    src = cms.InputTag("cleanedPatJetsPuppi"),
    variation = cms.int32(1)
)


process.shiftedPatTauEnDown = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("slimmedTaus"),
    uncertainty = cms.string('0.03+0*x*y')
)


process.shiftedPatTauEnDownPuppi = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("slimmedTaus"),
    uncertainty = cms.string('0.03+0*x*y')
)


process.shiftedPatTauEnUp = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("slimmedTaus"),
    uncertainty = cms.string('0.03+0*x*y')
)


process.shiftedPatTauEnUpPuppi = cms.EDProducer("ShiftedParticleProducer",
    shiftBy = cms.double(1.0),
    src = cms.InputTag("slimmedTaus"),
    uncertainty = cms.string('0.03+0*x*y')
)


process.shiftedPatUnclusteredEnDown = cms.EDProducer("ShiftedParticleProducer",
    binning = cms.VPSet(cms.PSet(
        binSelection = cms.string('charge!=0'),
        binUncertainty = cms.string('sqrt(pow(0.00009*x,2)+pow(0.0085/sqrt(sin(2*atan(exp(-y)))),2))')
    ), 
        cms.PSet(
            binSelection = cms.string('pdgId==130'),
            binUncertainty = cms.string('((abs(y)<1.3)?(min(0.25,sqrt(0.64/x+0.0025))):(min(0.30,sqrt(1.0/x+0.0016))))'),
            energyDependency = cms.bool(True)
        ), 
        cms.PSet(
            binSelection = cms.string('pdgId==22'),
            binUncertainty = cms.string('sqrt(0.0009/x+0.000001)+0*y'),
            energyDependency = cms.bool(True)
        ), 
        cms.PSet(
            binSelection = cms.string('pdgId==1 || pdgId==2'),
            binUncertainty = cms.string('sqrt(1./x+0.0025)+0*y'),
            energyDependency = cms.bool(True)
        )),
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("pfCandsForUnclusteredUnc")
)


process.shiftedPatUnclusteredEnDownPuppi = cms.EDProducer("ShiftedParticleProducer",
    binning = cms.VPSet(cms.PSet(
        binSelection = cms.string('charge!=0'),
        binUncertainty = cms.string('sqrt(pow(0.00009*x,2)+pow(0.0085/sqrt(sin(2*atan(exp(-y)))),2))')
    ), 
        cms.PSet(
            binSelection = cms.string('pdgId==130'),
            binUncertainty = cms.string('((abs(y)<1.3)?(min(0.25,sqrt(0.64/x+0.0025))):(min(0.30,sqrt(1.0/x+0.0016))))'),
            energyDependency = cms.bool(True)
        ), 
        cms.PSet(
            binSelection = cms.string('pdgId==22'),
            binUncertainty = cms.string('sqrt(0.0009/x+0.000001)+0*y'),
            energyDependency = cms.bool(True)
        ), 
        cms.PSet(
            binSelection = cms.string('pdgId==1 || pdgId==2'),
            binUncertainty = cms.string('sqrt(1./x+0.0025)+0*y'),
            energyDependency = cms.bool(True)
        )),
    shiftBy = cms.double(-1.0),
    src = cms.InputTag("pfCandsForUnclusteredUncPuppi")
)


process.shiftedPatUnclusteredEnUp = cms.EDProducer("ShiftedParticleProducer",
    binning = cms.VPSet(cms.PSet(
        binSelection = cms.string('charge!=0'),
        binUncertainty = cms.string('sqrt(pow(0.00009*x,2)+pow(0.0085/sqrt(sin(2*atan(exp(-y)))),2))')
    ), 
        cms.PSet(
            binSelection = cms.string('pdgId==130'),
            binUncertainty = cms.string('((abs(y)<1.3)?(min(0.25,sqrt(0.64/x+0.0025))):(min(0.30,sqrt(1.0/x+0.0016))))'),
            energyDependency = cms.bool(True)
        ), 
        cms.PSet(
            binSelection = cms.string('pdgId==22'),
            binUncertainty = cms.string('sqrt(0.0009/x+0.000001)+0*y'),
            energyDependency = cms.bool(True)
        ), 
        cms.PSet(
            binSelection = cms.string('pdgId==1 || pdgId==2'),
            binUncertainty = cms.string('sqrt(1./x+0.0025)+0*y'),
            energyDependency = cms.bool(True)
        )),
    shiftBy = cms.double(1.0),
    src = cms.InputTag("pfCandsForUnclusteredUnc")
)


process.shiftedPatUnclusteredEnUpPuppi = cms.EDProducer("ShiftedParticleProducer",
    binning = cms.VPSet(cms.PSet(
        binSelection = cms.string('charge!=0'),
        binUncertainty = cms.string('sqrt(pow(0.00009*x,2)+pow(0.0085/sqrt(sin(2*atan(exp(-y)))),2))')
    ), 
        cms.PSet(
            binSelection = cms.string('pdgId==130'),
            binUncertainty = cms.string('((abs(y)<1.3)?(min(0.25,sqrt(0.64/x+0.0025))):(min(0.30,sqrt(1.0/x+0.0016))))'),
            energyDependency = cms.bool(True)
        ), 
        cms.PSet(
            binSelection = cms.string('pdgId==22'),
            binUncertainty = cms.string('sqrt(0.0009/x+0.000001)+0*y'),
            energyDependency = cms.bool(True)
        ), 
        cms.PSet(
            binSelection = cms.string('pdgId==1 || pdgId==2'),
            binUncertainty = cms.string('sqrt(1./x+0.0025)+0*y'),
            energyDependency = cms.bool(True)
        )),
    shiftBy = cms.double(1.0),
    src = cms.InputTag("pfCandsForUnclusteredUncPuppi")
)


process.slimmedMETs = cms.EDProducer("PATMETSlimmer",
    caloMET = cms.InputTag("patCaloMet"),
    rawVariation = cms.InputTag("patPFMet"),
    runningOnMiniAOD = cms.bool(True),
    src = cms.InputTag("patPFMetT1"),
    t01Variation = cms.InputTag("slimmedMETs","","@skipCurrentProcess"),
    t1SmearedVarsAndUncs = cms.InputTag("patPFMetT1Smear%s"),
    t1Uncertainties = cms.InputTag("patPFMetT1%s"),
    tXYUncForT1 = cms.InputTag("patPFMetT1Txy")
)


process.slimmedMETsPuppi = cms.EDProducer("PATMETSlimmer",
    caloMET = cms.InputTag("patCaloMet"),
    rawVariation = cms.InputTag("patPFMetPuppi"),
    runningOnMiniAOD = cms.bool(True),
    src = cms.InputTag("patPFMetT1Puppi"),
    t01Variation = cms.InputTag("slimmedMETsPuppi","","@skipCurrentProcess"),
    t1SmearedVarsAndUncs = cms.InputTag("patPFMetT1Smear%sPuppi"),
    t1Uncertainties = cms.InputTag("patPFMetT1%sPuppi"),
    tXYUncForT1 = cms.InputTag("patPFMetT1TxyPuppi")
)


process.ApplyBaselineHBHEIsoNoiseFilter = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHEIsoNoiseFilterResult"),
    reverseDecision = cms.bool(False)
)


process.ApplyBaselineHBHENoiseFilter = cms.EDFilter("BooleanFlagFilter",
    inputLabel = cms.InputTag("HBHENoiseFilterResultProducer","HBHENoiseFilterResult"),
    reverseDecision = cms.bool(False)
)


process.BadChargedCandidateFilter = cms.EDFilter("BadChargedCandidateFilter",
    PFCandidates = cms.InputTag("packedPFCandidates"),
    debug = cms.bool(False),
    innerTrackRelErr = cms.double(1.0),
    maxDR = cms.double(1e-05),
    minMuonPt = cms.double(100.0),
    minMuonTrackRelErr = cms.double(2.0),
    minPtDiffRel = cms.double(1e-05),
    muons = cms.InputTag("slimmedMuons"),
    segmentCompatibility = cms.double(0.3),
    taggingMode = cms.bool(True)
)


process.BadPFMuonFilter = cms.EDFilter("BadPFMuonFilter",
    PFCandidates = cms.InputTag("packedPFCandidates"),
    algo = cms.int32(14),
    debug = cms.bool(False),
    innerTrackRelErr = cms.double(1.0),
    minDZ = cms.double(0.1),
    minMuPt = cms.double(100),
    minPtError = cms.double(2.0),
    muons = cms.InputTag("slimmedMuons"),
    segmentCompatibility = cms.double(0.3),
    taggingMode = cms.bool(True)
)


process.badGlobalMuonTagger = cms.EDFilter("BadGlobalMuonTagger",
    muonPtCut = cms.double(20),
    muons = cms.InputTag("slimmedMuons"),
    selectClones = cms.bool(False),
    taggingMode = cms.bool(True),
    verbose = cms.untracked.bool(False),
    vtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.badGlobalMuonTaggerMAOD = cms.EDFilter("BadGlobalMuonTagger",
    muonPtCut = cms.double(20),
    muons = cms.InputTag("slimmedMuons"),
    selectClones = cms.bool(False),
    taggingMode = cms.bool(False),
    vtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.cloneGlobalMuonTagger = cms.EDFilter("BadGlobalMuonTagger",
    muonPtCut = cms.double(20),
    muons = cms.InputTag("slimmedMuons"),
    selectClones = cms.bool(True),
    taggingMode = cms.bool(True),
    verbose = cms.untracked.bool(False),
    vtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.cloneGlobalMuonTaggerMAOD = cms.EDFilter("BadGlobalMuonTagger",
    muonPtCut = cms.double(20),
    muons = cms.InputTag("slimmedMuons"),
    selectClones = cms.bool(True),
    taggingMode = cms.bool(False),
    vtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.jetSelectorForMet = cms.EDFilter("PATJetSelector",
    cut = cms.string('pt>15 && abs(eta)<9.9'),
    src = cms.InputTag("basicJetsForMet")
)


process.jetSelectorForMetPuppi = cms.EDFilter("PATJetSelector",
    cut = cms.string('pt>15 && abs(eta)<9.9'),
    src = cms.InputTag("basicJetsForMetPuppi")
)


process.pfLeptonsPUPPET = cms.EDFilter("CandPtrSelector",
    cut = cms.string('abs(pdgId) == 13 || abs(pdgId) == 11 || abs(pdgId) == 15'),
    src = cms.InputTag("packedPFCandidates")
)


process.pfNoLepPUPPI = cms.EDFilter("CandPtrSelector",
    cut = cms.string('abs(pdgId) != 13 && abs(pdgId) != 11 && abs(pdgId) != 15'),
    src = cms.InputTag("packedPFCandidates")
)


process.selectedPatJetsForMetT1T2Corr = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) < 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patJets")
)


process.selectedPatJetsForMetT1T2CorrPuppi = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) < 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patJets")
)


process.selectedPatJetsForMetT1T2SmearCorr = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) < 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patSmearedJets")
)


process.selectedPatJetsForMetT1T2SmearCorrPuppi = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) < 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patSmearedJetsPuppi")
)


process.selectedPatJetsForMetT2Corr = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) > 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patJets")
)


process.selectedPatJetsForMetT2CorrPuppi = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) > 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patJets")
)


process.selectedPatJetsForMetT2SmearCorr = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) > 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patSmearedJets")
)


process.selectedPatJetsForMetT2SmearCorrPuppi = cms.EDFilter("PATJetSelector",
    cut = cms.string('abs(eta) > 9.9'),
    filter = cms.bool(False),
    src = cms.InputTag("patSmearedJetsPuppi")
)


process.selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0 = cms.EDFilter("PATSingleVertexSelector",
    filter = cms.bool(False),
    mode = cms.string('firstVertex'),
    vertices = cms.InputTag("selectedVerticesForPFMEtCorrType0")
)


process.selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0Puppi = cms.EDFilter("PATSingleVertexSelector",
    filter = cms.bool(False),
    mode = cms.string('firstVertex'),
    vertices = cms.InputTag("selectedVerticesForPFMEtCorrType0Puppi")
)


process.selectedVerticesForPFMEtCorrType0 = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof >= 4 & chi2 > 0 & tracksSize > 0 & abs(z) < 24 & abs(position.Rho) < 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.selectedVerticesForPFMEtCorrType0Puppi = cms.EDFilter("VertexSelector",
    cut = cms.string('isValid & ndof >= 4 & chi2 > 0 & tracksSize > 0 & abs(z) < 24 & abs(position.Rho) < 2.'),
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices")
)


process.initroottree = cms.EDAnalyzer("InitAnalyzer",
    GenJets = cms.untracked.bool(True),
    GenParticles = cms.untracked.bool(True),
    IsData = cms.untracked.bool(False)
)


process.makeroottree = cms.EDAnalyzer("NTupleMaker",
    BadChargedCandidateFilter = cms.InputTag("BadChargedCandidateFilter"),
    BadDuplicateMuons = cms.InputTag("cloneGlobalMuonTagger","bad","TreeProducer"),
    BadGlobalMuons = cms.InputTag("badGlobalMuonTagger","bad","TreeProducer"),
    BadPFMuonFilter = cms.InputTag("BadPFMuonFilter"),
    BeamSpotCollectionTag = cms.InputTag("offlineBeamSpot"),
    ElectronCollectionTag = cms.InputTag("slimmedElectrons"),
    Flags = cms.untracked.vstring('Flag_HBHENoiseFilter', 
        'Flag_HBHENoiseIsoFilter', 
        'Flag_CSCTightHalo2015Filter', 
        'Flag_EcalDeadCellTriggerPrimitiveFilter', 
        'Flag_goodVertices', 
        'Flag_eeBadScFilter', 
        'Flag_chargedHadronTrackResolutionFilter', 
        'Flag_muonBadTrackFilter', 
        'Flag_globalTightHalo2016Filter', 
        'Flag_METFilters', 
        'allMetFilterPaths'),
    FlagsProcesses = cms.untracked.vstring('RECO', 
        'PAT'),
    GenJetCollectionTag = cms.InputTag("slimmedGenJets"),
    GenJets = cms.untracked.bool(True),
    GenParticleCollectionTag = cms.InputTag("prunedGenParticles"),
    GenParticles = cms.untracked.bool(True),
    HLTriggerPaths = cms.untracked.vstring('HLT_IsoMu18_v', 
        'HLT_IsoMu20_v', 
        'HLT_IsoMu22_v', 
        'HLT_IsoMu22_eta2p1_v', 
        'HLT_IsoMu24_v', 
        'HLT_IsoMu27_v', 
        'HLT_IsoTkMu18_v', 
        'HLT_IsoTkMu20_v', 
        'HLT_IsoTkMu22_v', 
        'HLT_IsoTkMu22_eta2p1_v', 
        'HLT_IsoTkMu24_v', 
        'HLT_IsoTkMu27_v', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v', 
        'HLT_Mu20_v', 
        'HLT_Mu24_eta2p1_v', 
        'HLT_Mu27_v', 
        'HLT_Mu45_eta2p1_v', 
        'HLT_Mu50_v', 
        'HLT_Mu17_TrkIsoVVL_v', 
        'HLT_Mu8_TrkIsoVVL_v', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_v', 
        'HLT_Ele23_WPLoose_Gsf_v', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_v', 
        'HLT_Ele25_WPTight_Gsf_v', 
        'HLT_Ele25_eta2p1_WPLoose_Gsf_v', 
        'HLT_Ele25_eta2p1_WPTight_Gsf_v', 
        'HLT_Ele27_WPLoose_Gsf_v', 
        'HLT_Ele27_WPTight_Gsf_v', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v', 
        'HLT_Ele27_eta2p1_WPTight_Gsf_v', 
        'HLT_Ele32_eta2p1_WPTight_Gsf_v', 
        'HLT_Ele35_WPLoose_Gsf_v', 
        'HLT_Ele45_WPLoose_Gsf_v', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v', 
        'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v', 
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v', 
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v', 
        'HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded_v', 
        'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v', 
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v', 
        'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v', 
        'HLT_Mu17_Mu8_DZ_v', 
        'HLT_Mu17_Mu8_SameSign_DZ_v', 
        'HLT_Mu17_Mu8_SameSign_v', 
        'HLT_Mu17_Mu8_v', 
        'HLT_Mu17_TkMu8_DZ_v', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v', 
        'HLT_DoubleMu18NoFiltersNoVtx_v', 
        'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v', 
        'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v', 
        'HLT_DoubleMu33NoFiltersNoVtx_v', 
        'HLT_DoubleMu38NoFiltersNoVtx_v', 
        'HLT_TripleMu_12_10_5_v', 
        'HLT_TripleMu_5_3_3_v', 
        'HLT_DoubleIsoMu17_eta2p1_noDzCut_v', 
        'HLT_DoubleIsoMu17_eta2p1_v', 
        'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v', 
        'HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL_v', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v', 
        'HLT_DoubleMediumIsoPFTau32_Trk1_eta2p1_Reg_v', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v', 
        'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v', 
        'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v', 
        'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v', 
        'HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v', 
        'HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v', 
        'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v', 
        'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v', 
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v', 
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v', 
        'HLT_PFJet60_v', 
        'HLT_PFJet80_v', 
        'HLT_PFJet140_v'),
    IsData = cms.untracked.bool(False),
    JetCollectionTag = cms.InputTag("patJetsReapplyJEC","","TreeProducer"),
    L1EGammaCollectionTag = cms.InputTag("caloStage2Digis","EGamma"),
    L1JetCollectionTag = cms.InputTag("caloStage2Digis","Jet"),
    L1MuonCollectionTag = cms.InputTag("gmtStage2Digis","Muon"),
    L1Objects = cms.untracked.bool(True),
    L1TauCollectionTag = cms.InputTag("caloStage2Digis","Tau"),
    MetCollectionTag = cms.InputTag("slimmedMETs","","@skipCurrentProcess"),
    MetCorrCollectionTag = cms.InputTag("slimmedMETs","","TreeProducer"),
    MetCorrCovMatrixTag = cms.InputTag("METCorrSignificance","METCovariance","TreeProducer"),
    MuonCollectionTag = cms.InputTag("slimmedMuons"),
    MvaMetCollectionsTag = cms.VInputTag(cms.InputTag("MVAMET","MVAMET","TreeProducer")),
    PVCollectionTag = cms.InputTag("offlineSlimmedPrimaryVertices"),
    Period = cms.untracked.string('Spring16'),
    PuppiMetCollectionTag = cms.InputTag("slimmedMETsPuppi","","TreeProducer"),
    RecBeamSpot = cms.untracked.bool(True),
    RecElectron = cms.untracked.bool(True),
    RecElectronEtaMax = cms.untracked.double(2.6),
    RecElectronHLTriggerMatching = cms.untracked.vstring('HLT_Ele22_eta2p1_WPLoose_Gsf_v.*:hltSingleEle22WPLooseGsfTrackIsoFilter', 
        'HLT_Ele23_WPLoose_Gsf_v.*:hltEle23WPLooseGsfTrackIsoFilter', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_v.*:hltSingleEle24WPLooseGsfTrackIsoFilter', 
        'HLT_Ele25_WPTight_Gsf_v.*:hltEle25WPTightGsfTrackIsoFilter', 
        'HLT_Ele25_eta2p1_WPLoose_Gsf_v.*:hltEle25erWPLooseGsfTrackIsoFilter', 
        'HLT_Ele25_eta2p1_WPTight_Gsf_v.*:hltEle25erWPTightGsfTrackIsoFilter', 
        'HLT_Ele27_WPLoose_Gsf_v.*:hltEle27noerWPLooseGsfTrackIsoFilter', 
        'HLT_Ele27_WPTight_Gsf_v.*:hltEle27WPTightGsfTrackIsoFilter', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_v.*:hltEle27erWPLooseGsfTrackIsoFilter', 
        'HLT_Ele27_eta2p1_WPTight_Gsf_v.*:hltEle27erWPTightGsfTrackIsoFilter', 
        'HLT_Ele32_eta2p1_WPTight_Gsf_v.*:hltEle32WPTightGsfTrackIsoFilter', 
        'HLT_Ele35_WPLoose_Gsf_v.*:hltEle35WPLooseGsfTrackIsoFilter', 
        'HLT_Ele45_WPLoose_Gsf_v.*:hltEle45WPLooseGsfTrackIsoFilter', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltL1sSingleIsoEG20erIorSingleIsoEG22erIorSingleEG40', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltEle22WPLooseL1SingleIsoEG20erGsfTrackIsoFilter', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoEle22WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltL1sSingleIsoEG22erIorSingleIsoEG24erIorSingleEG40', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltEle24WPLooseL1SingleIsoEG22erGsfTrackIsoFilter', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoEle24WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v.*:hltL1sIsoEG22erTau20erdEtaMin0p2', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v.*:hltEle24WPLooseL1IsoEG22erTau20erGsfTrackIsoFilter', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v.*:hltOverlapFilterIsoEle24WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltL1sSingleEG40IorSingleIsoEG22erIorSingleIsoEG24er,hltL1sSingleEGor', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltEle27erWPLooseGsfTrackIsoFilter', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterIsoEle27WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltL1sSingleEG40IorSingleIsoEG22erIorSingleIsoEG24er,hltL1sSingleEGor', 
        'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltEle32WPLooseGsfTrackIsoFilter,hltEle32erWPLooseGsfTrackIsoFilter', 
        'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterIsoEle32WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele23_CaloIdL_TrackIdL_IsoVL_v.*:hltEle23CaloIdLTrackIdLIsoVLTrackIsoFilter', 
        'HLT_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltEle12CaloIdLTrackIdLIsoVLTrackIsoFilter', 
        'HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded_v.*:hltEle45WPLooseGsfTrackIsoL1TauJetSeededFilter', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v.*:hltEle24WPLooseL1IsoEG22erIsoTau26erGsfTrackIsoFilter', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v.*:hltOverlapFilterIsoEle24WPLooseGsfLooseIsoPFTau30', 
        'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sMu12EG10', 
        'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltMu17TrkIsoVVLEle12CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sMu20EG10,hltL1sMu20EG10IorMu23EG10', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter', 
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sSingleMu20erIorSingleMu22IorSingleMu25,hltL1sSingleMu20erlorSingleMu22lorSingleMu25,hltL1sSingleMu20erIorSingleMu22IorSingleMu25IorMu20IsoEG6', 
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v.*:hltMu23TrkIsoVVLEle8CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter', 
        'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sMu5EG15', 
        'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v.*:hltMu8TrkIsoVVLEle17CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sMu5EG20IorMu5IsoEG18,hltL1sMu5EG20IorMu5IsoEG18IorMu5IsoEG20IorMu5EG23', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v.*:hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltL1sMu20EG10IorMu23EG10', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLDZFilter', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltL1sMu5EG20IorMu5IsoEG18IorMu5IsoEG20IorMu5EG23', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLElectronlegTrackIsoFilter', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter', 
        'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v.*:hltEle24Ele22WPLooseGsfleg1TrackIsoFilter', 
        'HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v.*:hltEle24Ele22WPLooseGsfleg2TrackIsoFilter', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v.*:hltDiEle33CaloIdLGsfTrkIdVLMWPMS2UnseededFilter', 
        'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v.*:hltDiEle33CaloIdLPixelMatchUnseededFilter', 
        'HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL_v.*:hltEle37CaloIdLGsfTrkIdVLDPhiUnseededFilter', 
        'HLT_DoubleEle37_Ele27_CaloIdL_GsfTrkIdVL_v.*:hltDiEle27CaloIdLGsfTrkIdVLDPhiUnseededFilter', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltEle17Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltEle17Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltEle17Ele12CaloIdLTrackIdLIsoVLDZFilter', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltEle17Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter', 
        'HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltEle17Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltEle23Ele12CaloIdLTrackIdLIsoVLDZFilter', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter', 
        'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter'),
    RecElectronNum = cms.untracked.int32(0),
    RecElectronPtMin = cms.untracked.double(8.0),
    RecJet = cms.untracked.bool(True),
    RecJetBtagDiscriminators = cms.untracked.vstring('pfCombinedInclusiveSecondaryVertexV2BJetTags', 
        'pfJetProbabilityBJetTags'),
    RecJetEtaMax = cms.untracked.double(5.2),
    RecJetHLTriggerMatching = cms.untracked.vstring('HLT_PFJet60_v.*:hltSinglePFJet60', 
        'HLT_PFJet80_v.*:hltSinglePFJet80', 
        'HLT_PFJet140_v.*:hltSinglePFJet140'),
    RecJetNum = cms.untracked.int32(0),
    RecJetPtMin = cms.untracked.double(18.0),
    RecMuon = cms.untracked.bool(True),
    RecMuonEtaMax = cms.untracked.double(2.5),
    RecMuonHLTriggerMatching = cms.untracked.vstring('HLT_IsoMu18_v.*:hltL3crIsoL1sMu16L1f0L2f10QL3f18QL3trkIsoFiltered0p09', 
        'HLT_IsoMu20_v.*:hltL3crIsoL1sMu18L1f0L2f10QL3f20QL3trkIsoFiltered0p09', 
        'HLT_IsoMu22_v.*:hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09', 
        'HLT_IsoMu22_eta2p1_v.*:hltL3crIsoL1sSingleMu20erL1f0L2f10QL3f22QL3trkIsoFiltered0p09', 
        'HLT_IsoMu24_v.*:hltL3crIsoL1sMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p09', 
        'HLT_IsoMu27_v.*:hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p09', 
        'HLT_IsoTkMu18_v.*:hltL3fL1sMu16L1f0Tkf18QL3trkIsoFiltered0p09', 
        'HLT_IsoTkMu20_v.*:hltL3fL1sMu18L1f0Tkf20QL3trkIsoFiltered0p09', 
        'HLT_IsoTkMu22_v.*:hltL3fL1sMu20L1f0Tkf22QL3trkIsoFiltered0p09', 
        'HLT_IsoTkMu22_eta2p1_v.*:hltL3fL1sMu20erL1f0Tkf22QL3trkIsoFiltered0p09', 
        'HLT_IsoTkMu24_v.*:hltL3fL1sMu22L1f0Tkf24QL3trkIsoFiltered0p09', 
        'HLT_IsoTkMu27_v.*:hltL3fL1sMu22Or25L1f0Tkf27QL3trkIsoFiltered0p09', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltL1sSingleMu16er', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltL3crIsoL1sSingleMu16erL1f0L2f10QL3f17QL3trkIsoFiltered0p09', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoMu17LooseIsoPFTau20', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v.*:hltL1sMu16erTau20er', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v.*:hltL3crIsoL1sMu16erTauJet20erL1f0L2f10QL3f17QL3trkIsoFiltered0p09', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v.*:hltOverlapFilterIsoMu17LooseIsoPFTau20', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltL1sSingleMu18erIorSingleMu20er', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltL3crIsoL1sSingleMu18erIorSingleMu20erL1f0L2f10QL3f19QL3trkIsoFiltered0p09', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoMu19LooseIsoPFTau20', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v.*:hltL1sMu18erTau20er', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v.*:hltL3crIsoL1sMu18erTauJet20erL1f0L2f10QL3f19QL3trkIsoFiltered0p09', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v.*:hltOverlapFilterIsoMu19LooseIsoPFTau20', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltL1sSingleMu20erIorSingleMu22er', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltL3crIsoL1sSingleMu20erIorSingleMu22erL1f0L2f10QL3f21QL3trkIsoFiltered0p09', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoMu21LooseIsoPFTau20', 
        'HLT_Mu20_v.*:hltL3fL1sMu18L1f0L2f10QL3Filtered20Q', 
        'HLT_Mu24_eta2p1_v.*:hltL3fL1sMu20Eta2p1Or22L1f0L2f10QL3Filtered24Q', 
        'HLT_Mu27_v.*:hltL3fL1sMu22Or25L1f0L2f10QL3Filtered27Q', 
        'HLT_Mu45_eta2p1_v.*:hltL3fL1sMu22Or25L1f0L2f10QL3Filtered45e2p1Q', 
        'HLT_Mu50_v.*:hltL3fL1sMu22Or25L1f0L2f10QL3Filtered50Q', 
        'HLT_Mu17_TrkIsoVVL_v.*:hltL3fL1sMu1lqL1f0L2f10L3Filtered17TkIsoFiltered0p4', 
        'HLT_Mu17_TrkIsoVVL_v.*:hltL3fL1sMu10lqL1f0L2f10L3Filtered17', 
        'HLT_Mu8_TrkIsoVVL_v.*:hltL3fL1sMu5L1f0L2f5L3Filtered8TkIsoFiltered0p4', 
        'HLT_Mu8_TrkIsoVVL_v.*:hltL3fL1sMu5L1f0L2f5L3Filtered8', 
        'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sMu12EG10', 
        'HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltMu17TrkIsoVVLEle12CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered17', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sMu20EG10,hltL1sMu20EG10IorMu23EG10', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v.*:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered23', 
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sSingleMu20erIorSingleMu22IorSingleMu25,hltL1sSingleMu20erlorSingleMu22lorSingleMu25,hltL1sSingleMu20erIorSingleMu22IorSingleMu25IorMu20IsoEG6', 
        'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v.*:hltMu23TrkIsoVVLEle8CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered23', 
        'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sMu5EG15', 
        'HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v.*:hltMu8TrkIsoVVLEle17CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered8', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v.*:hltL1sMu5EG20IorMu5IsoEG18,hltL1sMu5EG20IorMu5IsoEG18IorMu5IsoEG20IorMu5EG23', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v.*:hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered8', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltL1sMu20EG10IorMu23EG10', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered23', 
        'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltMu23TrkIsoVVLEle12CaloIdLTrackIdLIsoVLDZFilter', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLDZFilter', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltL1sMu5EG20IorMu5IsoEG18IorMu5IsoEG20IorMu5EG23', 
        'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v.*:hltMu8TrkIsoVVLEle23CaloIdLTrackIdLIsoVLMuonlegL3IsoFiltered8', 
        'HLT_Mu17_Mu8_DZ_v.*:hltL3pfL1sDoubleMu114ORDoubleMu125L1f0L2pf0L3PreFiltered8,hltL3pfL1sDoubleMu114L1f0L2pf0L3PreFiltered8', 
        'HLT_Mu17_Mu8_DZ_v.*:hltL3fL1sDoubleMu114L1f0L2f10OneMuL3Filtered17', 
        'HLT_Mu17_Mu8_DZ_v.*:hltDiMuonGlb17Glb8DzFiltered0p2', 
        'HLT_Mu17_Mu8_SameSign_DZ_v.*:hltL3pfL1sDoubleMu114ORDoubleMu125L1f0L2pf0L3PreFiltered8,hltL3pfL1sDoubleMu114L1f0L2pf0L3PreFiltered8', 
        'HLT_Mu17_Mu8_SameSign_DZ_v.*:hltL3fL1sDoubleMu114L1f0L2f10OneMuL3Filtered17', 
        'HLT_Mu17_Mu8_SameSign_DZ_v.*:hltDiMuonGlb17Glb8DzFiltered0p2', 
        'HLT_Mu17_Mu8_SameSign_DZ_v.*:hltDiMuonGlb17Glb8DzFiltered0p2SameSign', 
        'HLT_Mu17_Mu8_SameSign_v.*:hltL3pfL1sDoubleMu114ORDoubleMu125L1f0L2pf0L3PreFiltered8,hltL3pfL1sDoubleMu114L1f0L2pf0L3PreFiltered8', 
        'HLT_Mu17_Mu8_SameSign_v.*:hltL3fL1sDoubleMu114L1f0L2f10OneMuL3Filtered17', 
        'HLT_Mu17_Mu8_SameSign_v.*:hltDiMuonGlb17Glb8SameSign', 
        'HLT_Mu17_Mu8_v.*:hltL3pfL1sDoubleMu114ORDoubleMu125L1f0L2pf0L3PreFiltered8,hltL3pfL1sDoubleMu114L1f0L2pf0L3PreFiltered8', 
        'HLT_Mu17_Mu8_v.*:hltL3fL1sDoubleMu114L1f0L2f10OneMuL3Filtered17', 
        'HLT_Mu17_TkMu8_DZ_v.*:hltL3fL1sDoubleMu114L1f0L2f10L3Filtered17', 
        'HLT_Mu17_TkMu8_DZ_v.*:hltDiMuonGlbFiltered17TrkFiltered8', 
        'HLT_Mu17_TkMu8_DZ_v.*:hltDiMuonGlb17Trk8DzFiltered0p2', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v.*:hltL3pfL1sDoubleMu114L1f0L2pf0L3PreFiltered8,hltL3pfL1sDoubleMu114ORDoubleMu125L1f0L2pf0L3PreFiltered8', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v.*:hltL3fL1sDoubleMu114L1f0L2f10OneMuL3Filtered17', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v.*:hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v.*:hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4DzFiltered0p2', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v.*:hltL3pfL1sDoubleMu114L1f0L2pf0L3PreFiltered8,hltL3pfL1sDoubleMu114ORDoubleMu125L1f0L2pf0L3PreFiltered8', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v.*:hltL3fL1sDoubleMu114L1f0L2f10OneMuL3Filtered17', 
        'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v.*:hltDiMuonGlb17Glb8RelTrkIsoFiltered0p4', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v.*:hltL3fL1sDoubleMu114L1f0L2f10L3Filtered17', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v.*:hltDiMuonGlbFiltered17TrkFiltered8', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v.*:hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v.*:hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4DzFiltered0p2', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v.*:hltL3fL1sDoubleMu114L1f0L2f10L3Filtered17', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v.*:hltDiMuonGlbFiltered17TrkFiltered8', 
        'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v.*:hltDiMuonGlb17Trk8RelTrkIsoFiltered0p4', 
        'HLT_DoubleMu18NoFiltersNoVtx_v.*:hltL3fDimuonL1f0L2NVf10L3NoFiltersNoVtxFiltered18', 
        'HLT_DoubleMu23NoFiltersNoVtxDisplaced_v.*:hltL3fDimuonL1f0L2NVf10L3NoFiltersNoVtxDisplacedFiltered23', 
        'HLT_DoubleMu28NoFiltersNoVtxDisplaced_v.*:hltL3fDimuonL1f0L2NVf16L3NoFiltersNoVtxDisplacedFiltered28', 
        'HLT_DoubleMu33NoFiltersNoVtx_v.*:hltL3fDimuonL1f0L2NVf10L3NoFiltersNoVtxFiltered33', 
        'HLT_DoubleMu38NoFiltersNoVtx_v.*:hltL3fDimuonL1f0L2NVf16L3NoFiltersNoVtxFiltered38', 
        'HLT_TripleMu_12_10_5_v.*:hltL1TripleMu553L2TriMuFiltered3L3TriMuFiltered5', 
        'HLT_TripleMu_12_10_5_v.*:hltL1TripleMu553L2TriMuFiltered3L3TriMuFiltered10105', 
        'HLT_TripleMu_12_10_5_v.*:hltL1TripleMu553L2TriMuFiltered3L3TriMuFiltered12105', 
        'HLT_TripleMu_5_3_3_v.*:hltL1TripleMu0L2TriMuFiltered0L3TriMuFiltered533,hltL1TripleMu500L2TriMuFiltered0L3TriMuFiltered533', 
        'HLT_TripleMu_5_3_3_v.*:hltL1TripleMu0L2TriMuFiltered0L3TriMuFiltered3,hltL1TripleMu500L2TriMuFiltered0L3TriMuFiltered3', 
        'HLT_DoubleIsoMu17_eta2p1_noDzCut_v.*:hltL3crIsoL1sDoubleMu125L1f16erL2f10QL3f17QL3L3crIsoRhoFiltered0p15IterTrk02', 
        'HLT_DoubleIsoMu17_eta2p1_v.*:hltL3crIsoL1sDoubleMu125L1f16erL2f10QL3f17QL3Dz0p2L3crIsoRhoFiltered0p15IterTrk02'),
    RecMuonNum = cms.untracked.int32(0),
    RecMuonPtMin = cms.untracked.double(5.0),
    RecMvaMet = cms.untracked.bool(True),
    RecPFMet = cms.untracked.bool(True),
    RecPFMetCorr = cms.untracked.bool(True),
    RecPhoton = cms.untracked.bool(False),
    RecPhotonEtaMax = cms.untracked.double(10000.0),
    RecPhotonHLTriggerMatching = cms.untracked.vstring(),
    RecPhotonNum = cms.untracked.int32(0),
    RecPhotonPtMin = cms.untracked.double(20.0),
    RecPrimVertex = cms.untracked.bool(True),
    RecPuppiMet = cms.untracked.bool(True),
    RecTau = cms.untracked.bool(True),
    RecTauBinaryDiscriminators = cms.untracked.vstring(),
    RecTauEtaMax = cms.untracked.double(2.5),
    RecTauFloatDiscriminators = cms.untracked.vstring(),
    RecTauHLTriggerMatching = cms.untracked.vstring('HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltPFTau20TrackLooseIsoAgainstMuon', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoMu17LooseIsoPFTau20', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v.*:hltPFTau20TrackLooseIsoAgainstMuon', 
        'HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v.*:hltOverlapFilterIsoMu17LooseIsoPFTau20', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltPFTau20TrackLooseIsoAgainstMuon', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoMu19LooseIsoPFTau20', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v.*:hltPFTau20TrackLooseIsoAgainstMuon', 
        'HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v.*:hltOverlapFilterIsoMu19LooseIsoPFTau20', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltPFTau20TrackLooseIsoAgainstMuon', 
        'HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoMu21LooseIsoPFTau20', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltPFTau20TrackLooseIso', 
        'HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoEle22WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltPFTau20TrackLooseIso', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterSingleIsoEle24WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v.*:hltPFTau20TrackLooseIso', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v.*:hltOverlapFilterIsoEle24WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltPFTau20TrackLooseIso', 
        'HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterIsoEle27WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltPFTau20TrackLooseIso', 
        'HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v.*:hltOverlapFilterIsoEle32WPLooseGsfLooseIsoPFTau20', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v.*:hltOverlapFilterIsoEle24WPLooseGsfLooseIsoPFTau30', 
        'HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v.*:hltPFTau30TrackLooseIso', 
        'HLT_DoubleMediumIsoPFTau32_Trk1_eta2p1_Reg_v.*:hltDoublePFTau32TrackPt1MediumIsolationDz02Reg', 
        'HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v.*:hltDoublePFTau35TrackPt1MediumIsolationDz02Reg', 
        'HLT_DoubleMediumIsoPFTau40_Trk1_eta2p1_Reg_v.*:hltDoublePFTau40TrackPt1MediumIsolationDz02Reg'),
    RecTauNum = cms.untracked.int32(0),
    RecTauPtMin = cms.untracked.double(15),
    RecTrack = cms.untracked.bool(False),
    RecTrackDxyMax = cms.untracked.double(1.0),
    RecTrackDzMax = cms.untracked.double(1.0),
    RecTrackEtaMax = cms.untracked.double(2.4),
    RecTrackNum = cms.untracked.int32(0),
    RecTrackPtMin = cms.untracked.double(0.5),
    SampleName = cms.untracked.string('Data'),
    Skim = cms.untracked.uint32(0),
    SusyInfo = cms.untracked.bool(True),
    SusyLSPMassTag = cms.InputTag("susyInfo","SusyLSPMass"),
    SusyMotherMassTag = cms.InputTag("susyInfo","SusyMotherMass"),
    TauCollectionTag = cms.InputTag("slimmedTaus"),
    TrackCollectionTag = cms.InputTag("generalTracks"),
    Trigger = cms.untracked.bool(True),
    TriggerObjectCollectionTag = cms.InputTag("selectedPatTrigger"),
    TriggerProcess = cms.untracked.string('HLT'),
    Year = cms.untracked.uint32(2016),
    eleLooseIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
    eleLooseIdSummer16Map = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
    eleMediumIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
    eleMediumIdSummer16Map = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
    eleMvaNonTrigIdWP80Map = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring15-25ns-nonTrig-V1-wp80"),
    eleMvaNonTrigIdWP90Map = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring15-25ns-nonTrig-V1-wp90"),
    eleMvaTrigIdWP80Map = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring15-25ns-Trig-V1-wp80"),
    eleMvaTrigIdWP90Map = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring15-25ns-Trig-V1-wp90"),
    eleMvaWP80GeneralMap = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp80"),
    eleMvaWP90GeneralMap = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp90"),
    eleTightIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
    eleTightIdSummer16Map = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
    eleVetoIdMap = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
    eleVetoIdSummer16Map = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto"),
    mvaCategoriesMapSpring16 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
    mvaNonTrigCategoriesMap = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Categories"),
    mvaNonTrigValuesMap = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15NonTrig25nsV1Values"),
    mvaTrigCategoriesMap = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Categories"),
    mvaTrigValuesMap = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring15Trig25nsV1Values"),
    mvaValuesMapSpring16 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values")
)


process.output = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('p')
    ),
    fileName = cms.untracked.string('output_particles_MC.root'),
    outputCommands = cms.untracked.vstring('keep *_slimmedMETs_*_*', 
        'keep *_MVAMET_*_*', 
        'keep *_patpfMETT1_*_*', 
        'keep *_*MET*_*_*')
)


process.type0PFMEtCorrectionPFCandToVertexAssociationForValidation = cms.Sequence(cms.ignore(process.selectedVerticesForPFMEtCorrType0)+cms.ignore(process.selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0)+process.particleFlowDisplacedVertex+process.pfCandidateToVertexAssociation)


process.pfMEtSysShiftCorrSequence = cms.Sequence(process.pfMEtMultShiftCorr)


process.ak4L1JPTOffsetCorrectorChain = cms.Sequence(process.ak4CaloL1OffsetCorrector+process.ak4L1JPTOffsetCorrector)


process.patPFMetT1T2CorrSequence = cms.Sequence(process.patPFMetT1T2Corr)


process.ak4PFL1L2L3CorrectorChain = cms.Sequence(process.ak4PFL1OffsetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL1L2L3Corrector)


process.ak4PFCHSL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1FastjetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSResidualCorrector+process.ak4PFCHSL1FastL2L3ResidualCorrector)


process.type0PFMEtCorrectionPFCandToVertexAssociation = cms.Sequence(process.selectedVerticesForPFMEtCorrType0+process.selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0+process.particleFlowDisplacedVertex+process.pfCandidateToVertexAssociation)


process.ak4PFCHSL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1FastjetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSL1FastL2L3Corrector)


process.ak4CaloL1L2L3CorrectorChain = cms.Sequence(process.ak4CaloL1OffsetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL1L2L3Corrector)


process.ak4PFL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFL1FastjetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL1FastL2L3Corrector)


process.patMetModuleSequence = cms.Sequence(process.pfMet+process.genMetExtractor+process.patJetCorrFactorsReapplyJEC+process.patJetsReapplyJEC+process.basicJetsForMet+process.jetSelectorForMet+process.cleanedPatJets+process.metrawCalo+process.patPFMet)


process.ak4TrackL2L3CorrectorChain = cms.Sequence(process.ak4TrackL2RelativeCorrector+process.ak4TrackL3AbsoluteCorrector+process.ak4TrackL2L3Corrector)


process.patPFMetT1SmearpatShiftedModuleSequence = cms.Sequence(process.patPFMetT1SmearJetResDown+process.patPFMetT1SmearJetResUp+process.patPFMetT1SmearMuonEnUp+process.patPFMetT1SmearMuonEnDown+process.patPFMetT1SmearJetEnUp+process.patPFMetT1SmearJetEnDown+process.patPFMetT1SmearTauEnUp+process.patPFMetT1SmearTauEnDown+process.patPFMetT1SmearPhotonEnUp+process.patPFMetT1SmearPhotonEnDown+process.patPFMetT1SmearElectronEnDown+process.patPFMetT1SmearElectronEnUp+process.patPFMetT1SmearUnclusteredEnUp+process.patPFMetT1SmearUnclusteredEnDown)


process.correctionTermsPfMetType0PFCandidate = cms.Sequence(process.type0PFMEtCorrectionPFCandToVertexAssociation+process.corrPfMetType0PfCand)


process.ak4PFL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1FastjetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFResidualCorrector+process.ak4PFL1FastL2L3ResidualCorrector)


process.ak4JPTL1L2L3CorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTL1L2L3Corrector)


process.patPFMetSmearCorrSequencePuppi = cms.Sequence(process.patSmearedJetsPuppi+process.selectedPatJetsForMetT1T2SmearCorrPuppi+process.patPFMetT1T2SmearCorrPuppi)


process.ak4PFPuppiL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastjetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiResidualCorrector+process.ak4PFPuppiL1FastL2L3ResidualCorrector)


process.patPFMetT2SmearCorrSequencePuppi = cms.Sequence(process.patSmearedJetsPuppi+process.selectedPatJetsForMetT1T2SmearCorrPuppi+process.selectedPatJetsForMetT2SmearCorrPuppi+process.patPFMetT1T2SmearCorrPuppi+process.patPFMetT2SmearCorrPuppi)


process.patPFMetTxyCorrSequencePuppi = cms.Sequence(process.patPFMetTxyCorrPuppi)


process.ak4PFCHSL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSResidualCorrector+process.ak4PFCHSL2L3ResidualCorrector)


process.patPFMetT1SmearPuppipatShiftedModuleSequencePuppi = cms.Sequence(process.patPFMetT1SmearJetResDownPuppi+process.patPFMetT1SmearJetResUpPuppi+process.patPFMetT1SmearMuonEnUpPuppi+process.patPFMetT1SmearMuonEnDownPuppi+process.patPFMetT1SmearJetEnUpPuppi+process.patPFMetT1SmearJetEnDownPuppi+process.patPFMetT1SmearTauEnDownPuppi+process.patPFMetT1SmearTauEnUpPuppi+process.patPFMetT1SmearPhotonEnUpPuppi+process.patPFMetT1SmearPhotonEnDownPuppi+process.patPFMetT1SmearElectronEnDownPuppi+process.patPFMetT1SmearElectronEnUpPuppi+process.patPFMetT1SmearUnclusteredEnUpPuppi+process.patPFMetT1SmearUnclusteredEnDownPuppi)


process.ak4CaloL2L3CorrectorChain = cms.Sequence(process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL2L3Corrector)


process.ak4JPTL1FastL2L3CorrectorChain = cms.Sequence(process.ak4JPTL1FastjetCorrector+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTL1FastL2L3Corrector)


process.ak4PFCHSL2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSL2L3Corrector)


process.patPFMetT0CorrSequence = cms.Sequence(process.type0PFMEtCorrectionPFCandToVertexAssociation+process.patPFMetT0Corr)


process.patPFMetT2CorrSequencePuppi = cms.Sequence(process.patPFMetT2CorrPuppi)


process.patPFMetSmearCorrSequence = cms.Sequence(process.patSmearedJets+process.selectedPatJetsForMetT1T2SmearCorr+process.patPFMetT1T2SmearCorr)


process.ak4CaloL1FastL2L3CorrectorChain = cms.Sequence(process.ak4CaloL1FastjetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL1FastL2L3Corrector)


process.patPFMetT2CorrSequence = cms.Sequence(process.patPFMetT2Corr)


process.producePatPFMETCorrectionsPuppi = cms.Sequence(process.patPFMetPuppi+process.pfCandsNotInJetsForMetCorrPuppi+process.selectedPatJetsForMetT1T2CorrPuppi+process.selectedPatJetsForMetT2CorrPuppi+process.patPFMetT1T2CorrPuppi+process.patPFMetT2CorrPuppi+process.selectedVerticesForPFMEtCorrType0Puppi+process.selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0Puppi+process.particleFlowDisplacedVertex+process.pfCandidateToVertexAssociation+process.patPFMetT0CorrPuppi+process.pfCandMETcorrPuppi+process.patPFMetT1Puppi+process.patPFMetT1T2Puppi+process.patPFMetT0pcT1Puppi+process.patPFMetT0pcT1T2Puppi)


process.ak4PFL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL1OffsetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFResidualCorrector+process.ak4PFL1L2L3ResidualCorrector)


process.ak4JPTL2L3ResidualCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTResidualCorrector+process.ak4JPTL2L3ResidualCorrector)


process.ak4PFL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL1FastjetCorrector+process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL6SLBCorrector+process.ak4PFL1FastL2L3L6Corrector)


process.patPFMetT1SmearpatMetUncertaintySequence = cms.Sequence(process.shiftedPatSmearedJetResDown+process.shiftedPatMETCorrSmearedJetResDown+process.shiftedPatSmearedJetResUp+process.shiftedPatMETCorrSmearedJetResUp)


process.patMetModuleSequencePuppi = cms.Sequence(process.pfMetPuppi+process.patJetCorrFactorsReapplyJECPuppi+process.patJetsReapplyJECPuppi+process.basicJetsForMetPuppi+process.jetSelectorForMetPuppi+process.cleanedPatJetsPuppi+process.metrawCaloPuppi+process.genMetExtractorPuppi+process.patPFMetPuppi)


process.ak4PFPuppiL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiResidualCorrector+process.ak4PFPuppiL2L3ResidualCorrector)


process.ak4JPTL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4JPTL1FastjetCorrector+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTResidualCorrector+process.ak4JPTL1FastL2L3ResidualCorrector)


process.ak4PFL2L3L6CorrectorChain = cms.Sequence(process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL6SLBCorrector+process.ak4PFL2L3L6Corrector)


process.noBadGlobalMuonsMAOD = cms.Sequence(~process.cloneGlobalMuonTaggerMAOD+~process.badGlobalMuonTaggerMAOD)


process.ak4PFPuppiL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFPuppiL1OffsetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiResidualCorrector+process.ak4PFPuppiL1L2L3ResidualCorrector)


process.ak4PFCHSL1L2L3CorrectorChain = cms.Sequence(process.ak4PFCHSL1OffsetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSL1L2L3Corrector)


process.patMETCorrectionsPuppi = cms.Sequence(process.ak4CaloL2RelativeCorrectorPuppi+process.ak4CaloL3AbsoluteCorrectorPuppi+process.ak4CaloL2L3CorrectorPuppi+process.corrCaloMetType1Puppi+process.muCaloMetCorrPuppi+process.corrCaloMetType2Puppi+process.caloMetT1Puppi+process.caloMetT1T2Puppi+process.pfJetsPtrForMetCorrPuppi+process.particleFlowPtrsPuppi+process.pfCandsNotInJetsPtrForMetCorrPuppi+process.pfCandsNotInJetsForMetCorrPuppi+process.pfCandMETcorrPuppi+process.ak4PFCHSL1FastjetCorrectorPuppi+process.ak4PFCHSL2RelativeCorrectorPuppi+process.ak4PFCHSL3AbsoluteCorrectorPuppi+process.ak4PFCHSResidualCorrectorPuppi+process.ak4PFCHSL1FastL2L3ResidualCorrectorPuppi+process.ak4PFCHSL1FastL2L3CorrectorPuppi+process.corrPfMetType1Puppi+process.corrPfMetType2Puppi+process.pfMetT1Puppi+process.pfMetT1T2Puppi)


process.ak4CaloL1FastL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1FastjetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloResidualCorrector+process.ak4CaloL1FastL2L3ResidualCorrector)


process.ak4CaloL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL6SLBCorrector+process.ak4CaloL2L3L6Corrector)


process.ak4PFPuppiL1FastL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1FastjetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiL1FastL2L3Corrector)


process.patPFMetT2SmearCorrSequence = cms.Sequence(process.patSmearedJets+process.selectedPatJetsForMetT1T2SmearCorr+process.selectedPatJetsForMetT2SmearCorr+process.patPFMetT1T2SmearCorr+process.patPFMetT2SmearCorr)


process.ak4JPTL2L3CorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTL2L3Corrector)


process.puppiMETSequence = cms.Sequence(process.puppi+process.pfLeptonsPUPPET+process.pfNoLepPUPPI+process.puppiNoLep+process.puppiMerged+process.puppiForMET)


process.ak4JPTL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4L1JPTOffsetCorrectorChain+process.ak4JPTL2RelativeCorrector+process.ak4JPTL3AbsoluteCorrector+process.ak4JPTResidualCorrector+process.ak4JPTL1L2L3ResidualCorrector)


process.patPFMetTxyCorrSequence = cms.Sequence(process.patPFMetTxyCorr)


process.producePatPFMETCorrectionsUnc = cms.Sequence(process.patPFMet+process.pfCandsNotInJetsForMetCorr+process.selectedPatJetsForMetT1T2Corr+process.selectedPatJetsForMetT2Corr+process.patPFMetT1T2Corr+process.patPFMetT2Corr+process.type0PFMEtCorrectionPFCandToVertexAssociation+process.patPFMetT0Corr+process.pfCandMETcorr)


process.rerunMvaIsolation2SeqRun2 = cms.Sequence(process.rerunDiscriminationByIsolationMVArun2v1raw+process.rerunDiscriminationByIsolationMVArun2v1VLoose+process.rerunDiscriminationByIsolationMVArun2v1Loose+process.rerunDiscriminationByIsolationMVArun2v1Medium+process.rerunDiscriminationByIsolationMVArun2v1Tight+process.rerunDiscriminationByIsolationMVArun2v1VTight+process.rerunDiscriminationByIsolationMVArun2v1VVTight)


process.BadGlobalMuonFilter = cms.Sequence(process.cloneGlobalMuonTagger+process.badGlobalMuonTagger)


process.patPFMetT0CorrSequencePuppi = cms.Sequence(process.selectedVerticesForPFMEtCorrType0Puppi+process.selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0Puppi+process.particleFlowDisplacedVertex+process.pfCandidateToVertexAssociation+process.patPFMetT0CorrPuppi)


process.patPFMetT1SmearPuppipatMetUncertaintySequencePuppi = cms.Sequence(process.shiftedPatSmearedJetResDownPuppi+process.shiftedPatMETCorrSmearedJetResDownPuppi+process.shiftedPatSmearedJetResUpPuppi+process.shiftedPatMETCorrSmearedJetResUpPuppi)


process.producePatPFMETCorrections = cms.Sequence(process.patPFMet+process.pfCandsNotInJetsForMetCorr+process.selectedPatJetsForMetT1T2Corr+process.selectedPatJetsForMetT2Corr+process.patPFMetT1T2Corr+process.patPFMetT2Corr+process.type0PFMEtCorrectionPFCandToVertexAssociation+process.patPFMetT0Corr+process.pfCandMETcorr+process.patPFMetT1+process.patPFMetT1T2+process.patPFMetT0pcT1+process.patPFMetT0pcT1T2)


process.patPFMetT1T2CorrSequencePuppi = cms.Sequence(process.patPFMetT1T2CorrPuppi)


process.type0PFMEtCorrection = cms.Sequence(process.type0PFMEtCorrectionPFCandToVertexAssociation+process.pfMETcorrType0)


process.egmGsfElectronIDSequence = cms.Sequence(process.electronMVAValueMapProducer+process.egmGsfElectronIDs+process.electronRegressionValueMapProducer)


process.egmPhotonIsolationMiniAODSequence = cms.Sequence(process.egmPhotonIsolation)


process.ak4CaloL1FastL2L3L6CorrectorChain = cms.Sequence(process.ak4CaloL1FastjetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloL6SLBCorrector+process.ak4CaloL1FastL2L3L6Corrector)


process.type0PFMEtCorrectionPFCandToVertexAssociationForValidationMiniAOD = cms.Sequence(cms.ignore(process.selectedVerticesForPFMEtCorrType0)+cms.ignore(process.selectedPrimaryVertexHighestPtTrackSumForPFMEtCorrType0)+process.particleFlowDisplacedVertex+process.pfCandidateToVertexAssociation)


process.ak4PFPuppiL2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiL2L3Corrector)


process.ak4CaloL2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloResidualCorrector+process.ak4CaloL2L3ResidualCorrector)


process.ak4PFCHSL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFCHSL1OffsetCorrector+process.ak4PFCHSL2RelativeCorrector+process.ak4PFCHSL3AbsoluteCorrector+process.ak4PFCHSResidualCorrector+process.ak4PFCHSL1L2L3ResidualCorrector)


process.ak4PFL2L3CorrectorChain = cms.Sequence(process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFL2L3Corrector)


process.ak4CaloL1L2L3ResidualCorrectorChain = cms.Sequence(process.ak4CaloL1OffsetCorrector+process.ak4CaloL2RelativeCorrector+process.ak4CaloL3AbsoluteCorrector+process.ak4CaloResidualCorrector+process.ak4CaloL1L2L3ResidualCorrector)


process.correctionTermsPfMetType0PFCandidateForValidation = cms.Sequence(process.type0PFMEtCorrectionPFCandToVertexAssociationForValidation+process.corrPfMetType0PfCand)


process.ak4PFL2L3ResidualCorrectorChain = cms.Sequence(process.ak4PFL2RelativeCorrector+process.ak4PFL3AbsoluteCorrector+process.ak4PFResidualCorrector+process.ak4PFL2L3ResidualCorrector)


process.ak4PFPuppiL1L2L3CorrectorChain = cms.Sequence(process.ak4PFPuppiL1OffsetCorrector+process.ak4PFPuppiL2RelativeCorrector+process.ak4PFPuppiL3AbsoluteCorrector+process.ak4PFPuppiL1L2L3Corrector)


process.patMetUncertaintySequencePuppi = cms.Sequence(process.ak4PFPuppiL1FastL2L3CorrectorChain+process.ak4PFPuppiL1FastL2L3ResidualCorrectorChain+(process.shiftedPatJetResDownPuppi+process.shiftedPatMETCorrJetResDownPuppi+process.shiftedPatJetResUpPuppi+process.shiftedPatMETCorrJetResUpPuppi+process.pfCandsNoJetsPuppi+process.pfCandsNoJetsNoElePuppi+process.pfCandsNoJetsNoEleNoMuPuppi+process.pfCandsNoJetsNoEleNoMuNoTauPuppi+process.pfCandsForUnclusteredUncPuppi+process.shiftedPatMuonEnDownPuppi+process.shiftedPatMETCorrMuonEnDownPuppi+process.shiftedPatMuonEnUpPuppi+process.shiftedPatMETCorrMuonEnUpPuppi+process.shiftedPatJetEnDownPuppi+process.shiftedPatMETCorrJetEnDownPuppi+process.shiftedPatJetEnUpPuppi+process.shiftedPatMETCorrJetEnUpPuppi+process.shiftedPatTauEnDownPuppi+process.shiftedPatMETCorrTauEnDownPuppi+process.shiftedPatTauEnUpPuppi+process.shiftedPatMETCorrTauEnUpPuppi+process.shiftedPatPhotonEnDownPuppi+process.shiftedPatMETCorrPhotonEnDownPuppi+process.shiftedPatPhotonEnUpPuppi+process.shiftedPatMETCorrPhotonEnUpPuppi+process.shiftedPatElectronEnDownPuppi+process.shiftedPatMETCorrElectronEnDownPuppi+process.shiftedPatElectronEnUpPuppi+process.shiftedPatMETCorrElectronEnUpPuppi+process.shiftedPatUnclusteredEnDownPuppi+process.shiftedPatMETCorrUnclusteredEnDownPuppi+process.shiftedPatUnclusteredEnUpPuppi+process.shiftedPatMETCorrUnclusteredEnUpPuppi)+process.patPFMetT1SmearPuppipatMetUncertaintySequencePuppi)


process.patMetUncertaintySequence = cms.Sequence(process.ak4PFCHSL1FastL2L3CorrectorChain+process.ak4PFCHSL1FastL2L3ResidualCorrectorChain+(process.shiftedPatJetResDown+process.shiftedPatMETCorrJetResDown+process.shiftedPatJetResUp+process.shiftedPatMETCorrJetResUp+process.pfCandsNoJets+process.pfCandsNoJetsNoEle+process.pfCandsNoJetsNoEleNoMu+process.pfCandsNoJetsNoEleNoMuNoTau+process.pfCandsForUnclusteredUnc+process.shiftedPatMuonEnDown+process.shiftedPatMETCorrMuonEnDown+process.shiftedPatMuonEnUp+process.shiftedPatMETCorrMuonEnUp+process.shiftedPatJetEnDown+process.shiftedPatMETCorrJetEnDown+process.shiftedPatJetEnUp+process.shiftedPatMETCorrJetEnUp+process.shiftedPatTauEnDown+process.shiftedPatMETCorrTauEnDown+process.shiftedPatTauEnUp+process.shiftedPatMETCorrTauEnUp+process.shiftedPatPhotonEnDown+process.shiftedPatMETCorrPhotonEnDown+process.shiftedPatPhotonEnUp+process.shiftedPatMETCorrPhotonEnUp+process.shiftedPatElectronEnDown+process.shiftedPatMETCorrElectronEnDown+process.shiftedPatElectronEnUp+process.shiftedPatMETCorrElectronEnUp+process.shiftedPatUnclusteredEnDown+process.shiftedPatMETCorrUnclusteredEnDown+process.shiftedPatUnclusteredEnUp+process.shiftedPatMETCorrUnclusteredEnUp)+process.patPFMetT1SmearpatMetUncertaintySequence)


process.patShiftedModuleSequencePuppi = cms.Sequence(process.patPFMetT1JetResDownPuppi+process.patPFMetT1JetResUpPuppi+process.patPFMetT1MuonEnUpPuppi+process.patPFMetT1MuonEnDownPuppi+process.patPFMetT1JetEnUpPuppi+process.patPFMetT1JetEnDownPuppi+process.patPFMetT1TauEnDownPuppi+process.patPFMetT1TauEnUpPuppi+process.patPFMetT1PhotonEnDownPuppi+process.patPFMetT1PhotonEnUpPuppi+process.patPFMetT1ElectronEnUpPuppi+process.patPFMetT1ElectronEnDownPuppi+process.patPFMetT1UnclusteredEnUpPuppi+process.patPFMetT1UnclusteredEnDownPuppi+process.patPFMetT1SmearPuppipatShiftedModuleSequencePuppi)


process.correctionTermsPfMetType1Type2 = cms.Sequence(process.pfJetsPtrForMetCorr+process.particleFlowPtrs+process.pfCandsNotInJetsPtrForMetCorr+process.pfCandsNotInJetsForMetCorr+process.pfCandMETcorr+process.ak4PFCHSL1FastL2L3ResidualCorrectorChain+process.ak4PFCHSL1FastL2L3Corrector+process.corrPfMetType1+process.corrPfMetType2)


process.correctionTermsCaloMet = cms.Sequence(process.ak4CaloL2L3CorrectorChain+process.corrCaloMetType1+process.muCaloMetCorr+process.corrCaloMetType2)


process.patShiftedModuleSequence = cms.Sequence(process.patPFMetT1JetResUp+process.patPFMetT1JetResDown+process.patPFMetT1MuonEnUp+process.patPFMetT1MuonEnDown+process.patPFMetT1JetEnUp+process.patPFMetT1JetEnDown+process.patPFMetT1TauEnDown+process.patPFMetT1TauEnUp+process.patPFMetT1PhotonEnUp+process.patPFMetT1PhotonEnDown+process.patPFMetT1ElectronEnUp+process.patPFMetT1ElectronEnDown+process.patPFMetT1UnclusteredEnUp+process.patPFMetT1UnclusteredEnDown+process.patPFMetT1SmearpatShiftedModuleSequence)


process.patMetCorrectionSequence = cms.Sequence(process.patPFMetT1T2CorrSequence+process.patPFMetT1+process.patPFMetTxyCorrSequence+process.patPFMetT1Txy+process.patPFMetTxy+process.patPFMetSmearCorrSequence+process.patPFMetT1Smear)


process.patMetCorrectionSequencePuppi = cms.Sequence(process.patPFMetT1T2CorrSequencePuppi+process.patPFMetT1Puppi+process.patPFMetTxyCorrSequencePuppi+process.patPFMetT1TxyPuppi+process.patPFMetTxyPuppi+process.patPFMetSmearCorrSequencePuppi+process.patPFMetT1SmearPuppi)


process.egmPhotonIDSequence = cms.Sequence(process.egmPhotonIsolationMiniAODSequence+process.photonIDValueMapProducer+process.photonMVAValueMapProducer+process.egmPhotonIDs+process.photonRegressionValueMapProducer)


process.patMETCorrections = cms.Sequence(process.correctionTermsCaloMet+process.caloMetT1+process.caloMetT1T2+process.correctionTermsPfMetType1Type2+process.pfMetT1+process.pfMetT1T2)


process.fullPatMetSequence = cms.Sequence(process.patMetModuleSequence+process.patMetCorrectionSequence+process.patMetUncertaintySequence+process.patShiftedModuleSequence+process.patCaloMet+process.slimmedMETs)


process.makePatMETs = cms.Sequence(process.patMETCorrections+process.patMETs)


process.fullPatMetSequencePuppi = cms.Sequence(process.patMetModuleSequencePuppi+process.patMetCorrectionSequencePuppi+process.patMetUncertaintySequencePuppi+process.patShiftedModuleSequencePuppi+process.patCaloMet+process.slimmedMETsPuppi)


process.p = cms.Path(process.initroottree+process.BadChargedCandidateFilter+process.BadPFMuonFilter+process.BadGlobalMuonFilter+process.pileupJetIdUpdated+process.patJetCorrFactorsReapplyJEC+process.patJetsReapplyJEC+process.fullPatMetSequence+process.egmPhotonIDSequence+process.puppiMETSequence+process.fullPatMetSequencePuppi+process.egmGsfElectronIDSequence+process.rerunMvaIsolation2SeqRun2+process.makeroottree)


process.AdaptorConfig = cms.Service("AdaptorConfig",
    enable = cms.untracked.bool(True),
    stats = cms.untracked.bool(True)
)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(500)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10),
            timespan = cms.untracked.int32(60)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(187627949)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(680368709)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(134160106)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(643240878)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(594308844)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(78443563)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(299709853)
    ),
    famosSimHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(775550011)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(389967541)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(487970066)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(744216813)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(678119483)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(444491675)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(694470990)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(667513881)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(636821157)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(783434209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(141865767)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(571720817)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(185754574)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(387212232)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(714234730)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(638585258)
    ),
    saveFileName = cms.untracked.string(''),
    siTrackerGaussianSmearingRecHits = cms.PSet(
        engineName = cms.untracked.string('TRandom3'),
        initialSeed = cms.untracked.uint32(178881989)
    ),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(149051161)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(678225201)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(189313156)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(352448271)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('HepJamesRandom'),
        initialSeed = cms.untracked.uint32(343910304)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('output_MC.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring('HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER')
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer")


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True),
    hcalTopologyConstants = cms.PSet(
        maxDepthHB = cms.int32(2),
        maxDepthHE = cms.int32(3),
        mode = cms.string('HcalTopologyMode::LHC')
    )
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(18268),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(18268)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelQualityFromDbRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        ))
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(cms.PSet(
        Label = cms.untracked.string(''),
        NormalizationFactor = cms.untracked.double(1.0),
        Record = cms.string('SiStripApvGainRcd')
    ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(cms.PSet(
        record = cms.string('SiStripDetVOffRcd'),
        tag = cms.string('')
    ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v8'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HERecalibration = cms.bool(False),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalibration = cms.bool(False),
    iLumi = cms.double(-1.0),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths')
)


process.loadRecoTauTagMVAsFromPrepDB = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string(''),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet(cms.PSet(
        label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1'),
        record = cms.string('GBRWrapperRcd'),
        tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1')
    ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwoLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwoLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAoldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAoldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAnewDMwoLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAnewDMwoLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBoldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBoldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBnewDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBnewDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWoldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWnewDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAPWdR03oldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVADBdR03oldDMwLTv1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBnewDMwLT2016v1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff50'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff50')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff70'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff70')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff60'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff60')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff80'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff80')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff40'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff40')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff90'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_WPEff90')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_tauIdMVAIsoDBoldDMwLT2016v1_mvaOutput_normalization')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_wGwoGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_woGwoGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_wGwoGSF_BL_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA5v1_gbr_NoEleMatch_woGwoGSF_EC_WPeff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_EC_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_BL_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_EC_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_BL_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_woGwGSF_BL_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_wGwGSF_BL_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_wGwoGSF_EC_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff99'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff99')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff96'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff96')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff91'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff91')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff85'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff85')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff79'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_antiElectronMVA6v1_gbr_NoEleMatch_woGwoGSF_EC_WPEff79')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1'),
            record = cms.string('GBRWrapperRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_WPeff99_5'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_WPeff99_5')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_WPeff99_0'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_WPeff99_0')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_WPeff98_0'),
            record = cms.string('PhysicsTGraphPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_WPeff98_0')
        ), 
        cms.PSet(
            label = cms.untracked.string('RecoTauTag_againstMuonMVAv1_mvaOutput_normalization'),
            record = cms.string('PhysicsTFormulaPayloadRcd'),
            tag = cms.string('RecoTauTag_againstMuonMVAv1_mvaOutput_normalization')
        ))
)


process.prefer("es_hardcode")

