
from collections import defaultdict


PROVINCES = '''ES-C	La Coruña	GA
ES-VI	Álava	PV
ES-AB	Albacete	CM
ES-A	Alicante	VC
ES-AL	Almería	AN
ES-O	Asturias	AS
ES-AV	Ávila	CL
ES-BA	Badajoz	EX
ES-PM	Baleares	IB
ES-B	Barcelona	CT
ES-BI	Vizcaya	PV
ES-BU	Burgos	CL
ES-CC	Cáceres	EX
ES-CA	Cádiz	AN
ES-S	Cantabria	CB
ES-CS	Castellón	VC
ES-CR	Ciudad Real	CM
ES-CO	Córdoba	AN
ES-CU	Cuenca	CM
ES-SS	Guipúzcoa	PV
ES-GI	Gerona	CT
ES-GR	Granada	AN
ES-GU	Guadalajara	CM
ES-H	Huelva	AN
ES-HU	Huesca	AR
ES-J	Jaén	AN
ES-LO	La Rioja	RI
ES-GC	Las Palmas	CN
ES-LE	León	CL
ES-L	Lérida	CT
ES-LU	Lugo	GA
ES-M	Madrid	MD
ES-MA	Málaga	AN
ES-MU	Murcia	MC
ES-NC	Navarra	NC
ES-OR	Orense	GA
ES-P	Palencia	CL
ES-PO	Pontevedra	GA
ES-SA	Salamanca	CL
ES-TF	Santa Cruz de Tenerife	CN
ES-SG	Segovia	CL
ES-SE	Sevilla	AN
ES-SO	Soria	CL
ES-T	Tarragona	CT
ES-TE	Teruel	AR
ES-TO	Toledo	CM
ES-V	Valencia	VC
ES-VA	Valladolid	CL
ES-ZA	Zamora	CL
ES-Z	Zaragoza	AR
ES-CE\tCeuta\tCE
ES-ML\tMelilla\tML'''

CCAA = '''ES-AN 	Andalucía
ES-AR 	Aragón
ES-AS 	Asturias
ES-CN 	Canarias
ES-CB 	Cantabria
ES-CM 	Castilla-La Mancha
ES-CL 	Castilla y León
ES-CT 	Cataluña
ES-EX 	Extremadura
ES-GA 	Galicia
ES-IB 	Baleares
ES-RI 	La Rioja
ES-MD 	Madrid
ES-MC 	Murcia
ES-NC 	Navarra
ES-PV 	País Vasco
ES-VC 	Comunidad Valenciana
ES-CE\tCeuta
ES-ML\tMelilla'''


def _get_province_names():
    names = {}
    ccaa = {}
    for line in PROVINCES.splitlines():
        province_iso, name, ca_iso = line.split('\t')
        province_iso = province_iso[3:]
        names[province_iso] = name
        ccaa[province_iso] = ca_iso
    return names, ccaa


PROVINCE_NAMES_PER_ISO_CODE, CA_PER_PROVINCE = _get_province_names()
PROVINCE_ISO_PER_NAME = {name: iso for iso, name in PROVINCE_NAMES_PER_ISO_CODE.items()}


def _get_ccaa_names():
    ccaa_names = {}
    for line in CCAA.splitlines():
        ca_iso, name = line.split('\t')
        ca_iso = ca_iso[3:].strip()
        ccaa_names[ca_iso] = name
    return ccaa_names

CA_NAMES_PER_ISO_CODE = _get_ccaa_names()
ISO_CODES_PER_CA_NAME = {ca_name: ca for ca, ca_name in CA_NAMES_PER_ISO_CODE.items()}
