
from pathlib import Path

BASE_DIR = Path('.').absolute()

CACHE_DIR = BASE_DIR / 'cache'
CACHE_DIR.mkdir(exist_ok=True)

URL_DATOS_ISCIII = 'https://cnecovid.isciii.es/covid19/resources/casos_hosp_uci_def_sexo_edad_provres.csv'
ORIG_SEX_COL = 'sexo'
ORIG_DATE_COL = 'fecha'
ORIG_PROVINCE_COL = 'provincia_iso'
ORIG_AGE_GROUP_COL = 'grupo_edad'
ORIG_CASES_COL = 'num_casos'
ORIG_HOSP_COL = 'num_hosp'
ORIG_ICU_COL = 'num_uci'
ORIG_DEATHS_COL = 'num_def'

PLOT_PARAM_DESCRIPTIONS = {ORIG_CASES_COL : 'Num. casos',
                           ORIG_HOSP_COL: 'Num. hosp',
                           ORIG_ICU_COL: 'Num. uci',
                           ORIG_DEATHS_COL: 'Num. fallecidos'}

MALE = 'H'
FEMALE = 'M'

PROVINCE = 'province'
COMMUNITY = 'community'

ORIG_COUNT_COLS = [ORIG_HOSP_COL, ORIG_ICU_COL, ORIG_DEATHS_COL, ORIG_CASES_COL]

PLOT_DIR = BASE_DIR / 'plots'
PLOT_DIR.mkdir(exist_ok=True)
SPAIN_PLOT_DIR = PLOT_DIR / 'spain'
SPAIN_PLOT_DIR.mkdir(exist_ok=True)
COMMUNITY_PLOT_DIR = PLOT_DIR / 'communities'
COMMUNITY_PLOT_DIR.mkdir(exist_ok=True)
PROVINCE_PLOT_DIR = PLOT_DIR / 'provinces'
PROVINCE_PLOT_DIR.mkdir(exist_ok=True)
AGE_GROUP_PLOT_DIR = PLOT_DIR / 'age_groups'
AGE_GROUP_PLOT_DIR.mkdir(exist_ok=True)

FOR_PANEL_EVOLUTION_FIG_SIZE = (8, 11)

MAIN_EVOLUTION_COLOR = '#DC143C'
REFERENCE_EVOLUTION_COLOR = '#A9A9A9'

DATA_DIR = BASE_DIR / 'datos'
DEMOGRAPHIC_CSV = DATA_DIR / 'datos_demograficos_ine.csv.gz'
