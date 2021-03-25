
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

POPULATION_PER_PROVINCE = '''Madrid	6 779 888
Barcelona	5 743 402
Valencia	2 591 875
Sevilla	1 950 219
Alicante	1 879 888
Málaga	1 685 920
Murcia	1 511 251
Cádiz	1 244 049
Baleares	1 171 543
Vizcaya	1 159 443
Las Palmas	1 131 065
La Coruña	1 121 815
Santa Cruz de Tenerife	1 044 887
Asturias	1 018 784
Zaragoza	972 528
Pontevedra	945 408
Granada	919 168
Tarragona	816 772
Gerona	781 788
Córdoba	781 451
Almería	727 945
Guipúzcoa	727 121
Toledo	703 772
Badajoz	672 137
Navarra	661 197
Jaén	631 381
Castellón	585 590
Cantabria	582 905
Huelva	524 278
Valladolid	520 649
Ciudad Real	495 045
León	456 439
Lérida	438 517
Cáceres	391 850
Albacete	388 270
Burgos	357 650
Álava	333 940
Salamanca	329 245
Lugo	327 946
La Rioja	319 914
Orense	306 650
Guadalajara	261 955
Huesca	222 687
Cuenca	196 139
Zamora	170 588
Palencia	160 321
Ávila	157 664
Segovia	153 478
Teruel	134 176
Soria	88 884
Melilla	87 076
Ceuta	84 202'''


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


def _get_province_population():
    pops = {}
    for line in POPULATION_PER_PROVINCE.splitlines():
        name, pop = line.split('\t')
        pop = int(pop.replace(' ', ''))
        pops[PROVINCE_ISO_PER_NAME[name]] = pop
    return pops

POPULATIONS_PER_PROVINCE = _get_province_population()

def _get_provinces_per_ca():
    provinces_per_ca = defaultdict(list)
    for province, ca in CA_PER_PROVINCE.items():
        provinces_per_ca[ca].append(province)
    return provinces_per_ca


def _get_ca_population():
    pops_per_ca = {}
    for ca, provinces in _get_provinces_per_ca().items():
        pops_per_ca[ca] = sum([POPULATIONS_PER_PROVINCE[province] for province in provinces])
    return pops_per_ca

POPULATIONS_PER_CA = _get_ca_population()
