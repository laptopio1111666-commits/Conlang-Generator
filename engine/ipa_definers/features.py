from enum import Enum

class Voicing(Enum):
    VOICELESS           = "VCLS"
    BREATHY_VOICE       = "BRVC"
    SLACK_VOICE         = "SLVC"
    MODAL_VOICE         = "MDVC"
    VOICED              = "VCED"
    STIFF_VOICE         = "STVC"
    CREAKY_VOICE        = "CRVC"
    GLOTTAL_CLOSURE     = "GLCL"

class PlaceBroad(Enum):
    LABIAL              = "LABL"
    CORONAL             = "CRNL"
    DORSAL              = "DRSL"
    LARYNGEAL           = "LRGL"

class PlaceSpecific(Enum):
    BILABIAL            = "BLBL"
    LABIODENTAL         = "LBDN"
    LINGUOLABIAL        = "LGLB"
    DENTAL              = "DNTL"
    ALVEOLAR            = "ALVR"
    POST_ALVEOLAR       = "PALV"
    RETROFLEX           = "RTFL"
    ALVEOLOPALATAL      = "ALPL"
    PALATAL             = "PLTL"
    VELAR               = "VELR"
    UVULAR              = "UVLR"
    PHARYNGEAL          = "PHGL"
    EPIGLOTTAL          = "EPGL"
    GLOTTAL             = "GLTL"

PLACE_GROUPS = {
    PlaceBroad.LABIAL    : {PlaceSpecific.BILABIAL, PlaceSpecific.LABIODENTAL, PlaceSpecific.LINGUOLABIAL},
    PlaceBroad.CORONAL   : {PlaceSpecific.DENTAL, PlaceSpecific.ALVEOLAR, PlaceSpecific.POST_ALVEOLAR, PlaceSpecific.RETROFLEX, PlaceSpecific.ALVEOLOPALATAL},
    PlaceBroad.DORSAL    : {PlaceSpecific.PALATAL, PlaceSpecific.VELAR, PlaceSpecific.UVULAR},
    PlaceBroad.LARYNGEAL : {PlaceSpecific.PHARYNGEAL, PlaceSpecific.EPIGLOTTAL, PlaceSpecific.GLOTTAL}
}

class Manner(Enum):
    NASAL                   = "NSAL"
    PLOSIVE                 = "PLSV"
    SIBILANT_FRICATIVE      = "SBFR"
    NONSIBILANT_FRICATIVE   = "NSFR"
    LATERAL_FRICATIVE       = "LAFR"
    APPROXIMANT             = "APPR"
    LATERAL_APPROXIMANT     = "LAPR"
    TAP_FLAP                = "TPFL" 
    TRILL                   = "TRLL"
    LATERAL_TAP_FLAP        = "LTPF"
    IMPLOSIVE               = "IMPL"
    EJECTIVE                = "EJTV"
    CLICK                   = "CLCK"
    AFFRICATE               = "AFFR"
    SIBILANT_AFFRICATE      = "SBAF"
    NONSIBILANT_AFFRICATE   = "NSAF"
    LATERAL_AFFRICATE       = "LAAF"
    EJECTIVE_AFFRICATE      = "EJAF"
    LATERAL_EJECTIVE_AFFRICATE = "LEAF"

class Height(Enum):
    CLOSE               = "CLSE"  
    NEAR_CLOSE          = "NRCL" 
    CLOSE_MID           = "CLMD"
    MID                 = "MIDE"
    OPEN_MID            = "OPMD"
    NEAR_OPEN           = "NROP"
    OPEN                = "OPEN"

class Backness(Enum):
    FRONT               = "FRNT"
    CENTRAL             = "CNTR"
    BACK                = "BACK"

class Roundness(Enum):
    ROUNDED             = "VWRN"
    UNROUNDED           = "VWUN"
    
class Nasalization(Enum):
    NASALIZED           = "NZLD"
    UNNASALIZED         = "UNNZ"

class Length(Enum):
    SHORT               = "SHRT"
    LONG                = "LONG"
    OVERLONG            = "OVLG"