
from pathlib import Path

BASE_DIR = Path('.').absolute()

CACHE_DIR = BASE_DIR / 'cache'
CACHE_DIR.mkdir(exist_ok=True)

URL_DATOS_ISCIII = 'https://cnecovid.isciii.es/covid19/resources/casos_hosp_uci_def_sexo_edad_provres.csv'
ORIG_SEX_COL = 'sexo'
ORIG_DATE_COL = 'fecha'
ORIG_PROVINCE_COL = 'provincia_iso'
ORIG_AGE_GROUP_COL = 'grupo_edad'
