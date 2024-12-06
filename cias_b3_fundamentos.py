import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta

st.set_page_config(layout="wide")

#--------------------------------------------------------------------------------------
codigo = ['BRAV', 'CSAN', 'RPMG', 'PETR', 'RECV', 'PRIO', 'RAIZ', 'UGPA', 'VBBR', 'LUPA', 'OPCT', 'OSXB', 'AURA', 'BRAP', 'CBAV', 'CMIN', 'LTEL', 'LTLA', 'VALE', 'FESA', 'GGBR', 'GOAU', 'CSNA', 'USIM', 'MGEL', 'PATI', 'TKNO', 'PMAM', 'BRKM', 'DEXP', 'FHER', 'NUTR', 'VITT', 'CRPG', 'UNIP', 'DXCO', 'EUCA', 'KLBN', 'MSPA', 'NEMO', 'SUZB', 'RANI', 'SNSY', 'ETER', 'HAGA', 'PTBL', 'AZEV', 'SOND', 'EMBR', 'FRAS', 'POMO', 'RAPT', 'RCSL', 'RSUL', 'TUPY', 'MWET', 'SHUL', 'WEGE', 'EALT', 'AERI', 'ARML', 'BDLL', 'INEP', 'KEPL', 'FRIO', 'MILS', 'NORD', 'PTCA', 'ROMI', 'MTSA', 'TASA', 'AZUL', 'GOLL', 'FRRN', 'VSPT', 'MRSA', 'RAIL', 'HBSA', 'LOGN', 'LUXM', 'JSLG', 'TGMA', 'CCRO', 'CRTE', 'ECOR', 'RDVT', 'TPIS', 'AGRU', 'HMOB', 'IVPR', 'PSVM', 'STBP', 'PORT', 'ATMP', 'BBML', 'DTCY', 'ALPK', 'GGPS', 'PRNR', 'SEQL', 'VLID', 'EPAR', 'MMAQ', 'RBNS', 'WLMM', 'TTEN', 'GRAO', 'AGXY', 'APTI', 'SOJA', 'AGRO', 'CTCA', 'EGGY', 'SLCE', 'LAND', 'JALL', 'SMTO', 'BRFS', 'BAUH', 'JBSS', 'MRFG', 'BEEF', 'MNPR', 'CAML', 'JOPA', 'MDIA', 'ODER', 'ABEV', 'NTCO', 'BOBR', 'ASAI', 'CRFB', 'EXCO', 'GMAT', 'PCAR', 'AVLL', 'CALI', 'CURY', 'CYRE', 'DIRR', 'EVEN', 'EZTC', 'FIEI', 'GFSA', 'HBOR', 'INNC', 'JHSF', 'JFEN', 'KLAS', 'LAVV', 'MELK', 'MTRE', 'MDNE', 'MRVE', 'PDGR', 'PLPL', 'RDNI', 'RSID', 'TCSA', 'TEGA', 'TEND', 'TRIS', 'VIVR', 'CEDO', 'CTNM', 'DOHL', 'CATA', 'CTKA', 'PTNT', 'CTSA', 'SGPS', 'TEKA', 'TXRX', 'TFCO', 'ALPA', 'CAMB', 'GRND', 'VULC', 'MNDL', 'TECN', 'VIVA', 'WHRL', 'MBLY', 'UCAS', 'WEST', 'HETA', 'MYPK', 'LEVE', 'PLAS', 'HOOT', 'MEAL', 'ZAMP', 'BMKS', 'ESTR', 'AHEB', 'SHOW', 'CVCB', 'SMFT', 'ANIM', 'BAHI', 'COGN', 'CSED', 'SEER', 'VTRU', 'YDUQ', 'RENT', 'MOVI', 'VAMO', 'DOTZ', 'AZZA', 'CEAB', 'CGRA', 'GUAR', 'AMAR', 'LREN', 'VSTE', 'ALLD', 'BHIA', 'MGLU', 'AMER', 'ESPA', 'SBFG', 'LLBI', 'PETZ', 'LJQQ', 'BIOM', 'NRTQ', 'OFSA', 'AALR', 'DASA', 'FLRY', 'HAPV', 'KRSA', 'MATD', 'ODPV', 'ONCO', 'QUAL', 'RDOR', 'BALM', 'LMED', 'BLAU', 'DMVF', 'PNVL', 'EUFA', 'HYPE', 'PGMN', 'PFRM', 'RADL', 'VVEO', 'INTB', 'MLAS', 'POSI', 'BMOB', 'BRQB', 'ENJU', 'NINJ', 'IFCM', 'LWSA', 'CASH', 'NGRD', 'PDTC', 'QUSW', 'TRAD', 'TOTS', 'LVTC', 'BRIT', 'DESK', 'OIBR', 'TELB', 'VIVT', 'TIMS', 'FIQE', 'ELMD', 'AESO', 'AFLT', 'ALUP', 'CBEE', 'AURE', 'CEBR', 'CEED', 'CLSC', 'GPAR', 'CMIG', 'CEEB', 'COCE', 'COMR', 'CPLE', 'CPFE', 'EKTR', 'ELET', 'LIPR', 'EMAE', 'ENGI', 'ENMT', 'ENEV', 'EGIE', 'EQPA', 'EQMA', 'EQTL', 'GEPA', 'LIGH', 'LIGT', 'NEOE', 'SRNA', 'PRMN', 'REDE', 'RNEW', 'SAEN', 'TAEE', 'TRPL', 'UPKP', 'AMBP', 'CASN', 'CSMG', 'IGSN', 'ORVR', 'SBSP', 'SAPR', 'CEGR', 'CGAS', 'PASS', 'ABCB', 'RPAD', 'BAZA', 'BMGB', 'BPAN', 'BGIP', 'BEES', 'BPAR', 'BRSR', 'BRBI', 'BBDC', 'BBAS', 'BSLI', 'BPAC', 'INBR', 'ITUB', 'BMEB', 'BMIN', 'BNBR', 'PINE', 'SANB', 'DMFN', 'MERC', 'BSCS', 'RBRA', 'PLSC', 'G2DI', 'GPIV', 'PPLA', 'B3SA', 'CLSA', 'CSUD', 'EFXB', 'EVTC', 'STOC', 'XPBR', 'BBSE', 'CXSE', 'PSSA', 'IRBR', 'WIZC', 'ALOS', 'GSHP', 'HBTS', 'HBRE', 'IGTI', 'LOGG', 'MNZC', 'MULT', 'PEAB', 'SCAR', 'SYNE', 'LPSB', 'NEXP', 'ITSA', 'MOAR', 'SIMH', 'CTBA', 'MCRJ', 'PMSP', 'QVQP', 'ATOM', 'BETP', 'MAPT', 'CMSA', 'OPGM', 'FIGE', 'PPAR', 'PRPT', 'OPSE', 'OPTS', 'YBRA']
nome = ['BRAVA', 'COSAN', 'PET MANGUINH', 'PETROBRAS', 'PETRORECSA', 'PETRORIO', 'RAIZEN', 'ULTRAPAR', 'VIBRA', 'LUPATECH', 'OCEANPACT', 'OSX BRASIL', 'AURA 360', 'BRADESPAR', 'CBA', 'CSNMINERACAO', 'LITEL', 'LITELA', 'VALE', 'FERBASA', 'GERDAU', 'GERDAU MET', 'SID NACIONAL', 'USIMINAS', 'MANGELS INDL', 'PANATLANTICA', 'TEKNO', 'PARANAPANEMA', 'BRASKEM', 'DEXXOS PAR', 'FER HERINGER', 'NUTRIPLANT', 'VITTIA', 'CRISTAL', 'UNIPAR', 'DEXCO', 'EUCATEX', 'KLABIN S/A', 'MELHOR SP', 'SUZANO HOLD', 'SUZANO S.A.', 'IRANI', 'SANSUY', 'ETERNIT', 'HAGA S/A', 'PORTOBELLO', 'AZEVEDO', 'SONDOTECNICA', 'EMBRAER', 'FRAS-LE', 'MARCOPOLO', 'RANDON PART', 'RECRUSUL', 'RIOSULENSE', 'TUPY', 'WETZEL S/A', 'SCHULZ', 'WEG', 'ACO ALTONA', 'AERIS', 'ARMAC', 'BARDELLA', 'INEPAR', 'KEPLER WEBER', 'METALFRIO', 'MILLS', 'NORDON MET', 'PRATICA', 'ROMI', 'METISA', 'TAURUS ARMAS', 'AZUL', 'GOL', 'ALL NORTE', 'FER C ATLANT', 'MRS LOGIST', 'RUMO S.A.', 'HIDROVIAS', 'LOG-IN', 'TREVISA', 'JSL', 'TEGMA', 'CCR SA', 'CONC RIO TER', 'ECORODOVIAS', 'ROD TIETE', 'TRIUNFO PART', 'GRUAIRPORT', 'HMOBI S.A', 'INVEPAR', 'PORTO VM', 'SANTOS BRP', 'WILSON SONS', 'ATMASA', 'BBMLOGISTICA', 'DTCOM-DIRECT', 'ESTAPAR', 'GPS', 'PRINER', 'SEQUOIA LOG', 'VALID', 'EMBPAR S/A', 'MINASMAQUINA', 'RODOBENS', 'WLM IND COM', '3TENTOS', 'AGRIBRASIL', 'AGROGALAXY', 'ALIPERTI', 'BOA SAFRA', 'BRASILAGRO', 'CTC S.A.', 'GRANJA FARIA', 'SLC AGRICOLA', 'TERRASANTAPA', 'JALLESMACHAD', 'SAO MARTINHO', 'BRF SA', 'EXCELSIOR', 'JBS', 'MARFRIG', 'MINERVA', 'MINUPAR', 'CAMIL', 'JOSAPAR', 'M.DIASBRANCO', 'ODERICH', 'AMBEV S/A', 'GRUPO NATURA', 'BOMBRIL', 'ASSAI', 'CARREFOUR BR', 'EXITO', 'GRUPO MATEUS', 'P.ACUCAR-CBD', 'ALPHAVILLE', 'CONST A LIND', 'CURY S/A', 'CYRELA REALT', 'DIRECIONAL', 'EVEN', 'EZTEC', 'FICA', 'GAFISA', 'HELBOR', 'INC SA', 'JHSF PART', 'JOAO FORTES', 'KALLAS', 'LAVVI', 'MELNICK', 'MITRE REALTY', 'MOURA DUBEUX', 'MRV', 'PDG REALT', 'PLANOEPLANO', 'RNI', 'ROSSI RESID', 'TECNISA', 'TEGRA INCORP', 'TENDA', 'TRISUL', 'VIVER', 'CEDRO', 'COTEMINAS', 'DOHLER', 'IND CATAGUAS', 'KARSTEN', 'PETTENATI', 'SANTANENSE', 'SPRINGS', 'TEKA', 'TEX RENAUX', 'TRACK FIELD', 'ALPARGATAS', 'CAMBUCI', 'GRENDENE', 'VULCABRAS', 'MUNDIAL', 'TECHNOS', 'VIVARA S.A.', 'WHIRLPOOL', 'MOBLY', 'UNICASA', 'WESTWING', 'HERCULES', 'IOCHP-MAXION', 'METAL LEVE', 'PLASCAR PART', 'HOTEIS OTHON', 'IMC S/A', 'ZAMP S.A.', 'BIC MONARK', 'ESTRELA', 'SPTURIS', 'TIME FOR FUN', 'CVC BRASIL', 'SMART FIT', 'ANIMA', 'BAHEMA', 'COGNA ON', 'CRUZEIRO EDU', 'SER EDUCA', 'VITRUEDUCA', 'YDUQS PART', 'LOCALIZA', 'MOVIDA', 'VAMOS', 'DOTZ SA', 'AZZAS 2154', 'CEA MODAS', 'GRAZZIOTIN', 'GUARARAPES', 'LOJAS MARISA', 'LOJAS RENNER', 'VESTE', 'ALLIED', 'CASAS BAHIA', 'MAGAZ LUIZA', 'AMERICANAS', 'ESPACOLASER', 'GRUPO SBF', 'LE BISCUIT', 'PETZ', 'QUERO-QUERO', 'BIOMM', 'NORTCQUIMICA', 'OUROFINO S/A', 'ALLIAR', 'DASA', 'FLEURY', 'HAPVIDA', 'KORA SAUDE', 'MATER DEI', 'ODONTOPREV', 'ONCOCLINICAS', 'QUALICORP', 'REDE D OR', 'BAUMER', 'LIFEMED', 'BLAU', 'D1000VFARMA', 'DIMED', 'EUROFARMA SA', 'HYPERA', 'PAGUE MENOS', 'PROFARMA', 'RAIADROGASIL', 'VIVEO', 'INTELBRAS', 'MULTILASER', 'POSITIVO TEC', 'BEMOBI TECH', 'BRQ', 'ENJOEI', 'GETNINJAS', 'INFRACOMM', 'LWSA', 'MELIUZ', 'NEOGRID', 'PADTEC', 'QUALITY SOFT', 'TC', 'TOTVS', 'WDC NETWORKS', 'BRISANET', 'DESKTOP', 'OI', 'TELEBRAS', 'TELEF BRASIL', 'TIM', 'UNIFIQUE', 'ELETROMIDIA', 'AESOPERACOES', 'AFLUENTE T', 'ALUPAR', 'AMPLA ENERG', 'AUREN', 'CEB', 'CEEE-D', 'CELESC', 'CELGPAR', 'CEMIG', 'COELBA', 'COELCE', 'COMERC PAR', 'COPEL', 'CPFL ENERGIA', 'ELEKTRO', 'ELETROBRAS', 'ELETROPAR', 'EMAE', 'ENERGISA', 'ENERGISA MT', 'ENEVA', 'ENGIE BRASIL', 'EQTL PARA', 'EQTLMARANHAO', 'EQUATORIAL', 'GER PARANAP', 'LIGHT', 'LIGHT S/A', 'NEOENERGIA', 'SERENA', 'PROMAN', 'REDE ENERGIA', 'RENOVA', 'SAFIRA ENERG', 'TAESA', 'TRAN PAULIST', 'UPTICK', 'AMBIPAR', 'CASAN', 'COPASA', 'IGUA SA', 'ORIZON', 'SABESP', 'SANEPAR', 'CEG', 'COMGAS', 'COMPASS', 'ABC BRASIL', 'ALFA HOLDING', 'AMAZONIA', 'BANCO BMG', 'BANCO PAN', 'BANESE', 'BANESTES', 'BANPARA', 'BANRISUL', 'BR PARTNERS', 'BRADESCO', 'BRASIL', 'BRB BANCO', 'BTGP BANCO', 'INTER CO', 'ITAUUNIBANCO', 'MERCANTIL', 'MERC INVEST', 'NORD BRASIL', 'PINE', 'SANTANDER BR', 'DMFINANCEIRA', 'MERC FINANC', 'BRAZILIAN SC', 'OPEA', 'POLO CAP SEC', 'G2D INVEST', 'GP INVEST', 'PPLA', 'B3', 'CLEARSALE', 'CSU DIGITAL', 'EQUIFAXBRL', 'EVERTEC INC', 'STONE CO', 'XP INC', 'BBSEGURIDADE', 'CAIXA SEGURI', 'PORTO SEGURO', 'IRBBRASIL RE', 'WIZ CO', 'ALLOS', 'GENERALSHOPP', 'HABITASUL', 'HBR REALTY', 'IGUATEMI S.A', 'LOG COM PROP', 'MENEZES CORT', 'MULTIPLAN', 'PAR AL BAHIA', 'SAO CARLOS', 'SYN PROP TEC', 'LOPES BRASIL', 'NEXPE', 'ITAUSA', 'MONT ARANHA', 'SIMPAR', 'CEPAC - CTBA', 'CEPAC - MCRJ', 'CEPAC - PMSP', '524 PARTICIP', 'ATOMPAR', 'BETAPART', 'CEMEPE', 'CIMS', 'GAMA PART', 'INVEST BEMGE', 'POLPAR', 'PROMPT PART', 'SUDESTE S/A', 'SUL 116 PART', 'YBYRA S/A']
segmento = ['Exploração, Refino e Distribuição', 'Exploração, Refino e Distribuição', 'Exploração, Refino e Distribuição', 'Exploração, Refino e Distribuição', 'Exploração, Refino e Distribuição', 'Exploração, Refino e Distribuição', 'Exploração, Refino e Distribuição', 'Exploração, Refino e Distribuição', 'Exploração, Refino e Distribuição', 'Equipamentos e Serviços', 'Equipamentos e Serviços', 'Equipamentos e Serviços', 'Minerais Metálicos', 'Minerais Metálicos', 'Minerais Metálicos', 'Minerais Metálicos', 'Minerais Metálicos', 'Minerais Metálicos', 'Minerais Metálicos', 'Siderurgia', 'Siderurgia', 'Siderurgia', 'Siderurgia', 'Siderurgia', 'Artefatos de Ferro e Aço', 'Artefatos de Ferro e Aço', 'Artefatos de Ferro e Aço', 'Artefatos de Cobre', 'Petroquímicos', 'Petroquímicos', 'Fertilizantes e Defensivos', 'Fertilizantes e Defensivos', 'Fertilizantes e Defensivos', 'Químicos Diversos', 'Químicos Diversos', 'Madeira', 'Madeira', 'Papel e Celulose', 'Papel e Celulose', 'Papel e Celulose', 'Papel e Celulose', 'Embalagens', 'Materiais Diversos', 'Produtos para Construção', 'Produtos para Construção', 'Produtos para Construção', 'Construção Pesada', 'Engenharia Consultiva', 'Material Aeronáutico e de Defesa', 'Material Rodoviário', 'Material Rodoviário', 'Material Rodoviário', 'Material Rodoviário', 'Material Rodoviário', 'Material Rodoviário', 'Material Rodoviário', 'Motores, Compressores e Outros', 'Motores, Compressores e Outros', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Industriais', 'Máq. e Equip. Construção e Agrícolas', 'Armas e Munições', 'Linhas Aéreas de Passageiros', 'Linhas Aéreas de Passageiros', 'Transporte Ferroviário', 'Transporte Ferroviário', 'Transporte Ferroviário', 'Transporte Ferroviário', 'Transporte Hidroviário', 'Transporte Hidroviário', 'Transporte Hidroviário', 'Transporte Rodoviário', 'Transporte Rodoviário', 'Exploração de Rodovias', 'Exploração de Rodovias', 'Exploração de Rodovias', 'Exploração de Rodovias', 'Exploração de Rodovias', 'Serviços de Apoio e Armazenagem', 'Serviços de Apoio e Armazenagem', 'Serviços de Apoio e Armazenagem', 'Serviços de Apoio e Armazenagem', 'Serviços de Apoio e Armazenagem', 'Serviços de Apoio e Armazenagem', 'Serviços Diversos', 'Serviços Diversos', 'Serviços Diversos', 'Serviços Diversos', 'Serviços Diversos', 'Serviços Diversos', 'Serviços Diversos', 'Serviços Diversos', 'Material de Transporte', 'Material de Transporte', 'Material de Transporte', 'Material de Transporte', 'Agricultura', 'Agricultura', 'Agricultura', 'Agricultura', 'Agricultura', 'Agricultura', 'Agricultura', 'Agricultura', 'Agricultura', 'Agricultura', 'Açucar e Alcool', 'Açucar e Alcool', 'Carnes e Derivados', 'Carnes e Derivados', 'Carnes e Derivados', 'Carnes e Derivados', 'Carnes e Derivados', 'Carnes e Derivados', 'Alimentos Diversos', 'Alimentos Diversos', 'Alimentos Diversos', 'Alimentos Diversos', 'Cervejas e Refrigerantes', 'Produtos de Cuidado Pessoal', 'Produtos de Limpeza', 'Alimentos', 'Alimentos', 'Alimentos', 'Alimentos', 'Alimentos', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Incorporações', 'Fios e Tecidos', 'Fios e Tecidos', 'Fios e Tecidos', 'Fios e Tecidos', 'Fios e Tecidos', 'Fios e Tecidos', 'Fios e Tecidos', 'Fios e Tecidos', 'Fios e Tecidos', 'Fios e Tecidos', 'Vestuário', 'Calçados', 'Calçados', 'Calçados', 'Calçados', 'Acessórios', 'Acessórios', 'Acessórios', 'Eletrodomésticos', 'Móveis', 'Móveis', 'Móveis', 'Utensílios Domésticos', 'Automóveis e Motocicletas', 'Automóveis e Motocicletas', 'Automóveis e Motocicletas', 'Hotelaria', 'Restaurante e Similares', 'Restaurante e Similares', 'Bicicletas', 'Brinquedos e Jogos', 'Produção de Eventos e Shows', 'Produção de Eventos e Shows', 'Viagens e Turismo', 'Atividades Esportivas', 'Serviços Educacionais', 'Serviços Educacionais', 'Serviços Educacionais', 'Serviços Educacionais', 'Serviços Educacionais', 'Serviços Educacionais', 'Serviços Educacionais', 'Aluguel de carros', 'Aluguel de carros', 'Aluguel de carros', 'Programas de Fidelização', 'Tecidos, Vestuário e Calçados', 'Tecidos, Vestuário e Calçados', 'Tecidos, Vestuário e Calçados', 'Tecidos, Vestuário e Calçados', 'Tecidos, Vestuário e Calçados', 'Tecidos, Vestuário e Calçados', 'Tecidos, Vestuário e Calçados', 'Eletrodomésticos', 'Eletrodomésticos', 'Eletrodomésticos', 'Produtos Diversos', 'Produtos Diversos', 'Produtos Diversos', 'Produtos Diversos', 'Produtos Diversos', 'Produtos Diversos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Serviços Médico - Hospitalares, Análises e Diagnósticos', 'Equipamentos', 'Equipamentos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Medicamentos e Outros Produtos', 'Computadores e Equipamentos', 'Computadores e Equipamentos', 'Computadores e Equipamentos', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Programas e Serviços', 'Telecomunicações', 'Telecomunicações', 'Telecomunicações', 'Telecomunicações', 'Telecomunicações', 'Telecomunicações', 'Telecomunicações', 'Publicidade e Propaganda', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Energia Elétrica', 'Água e Saneamento', 'Água e Saneamento', 'Água e Saneamento', 'Água e Saneamento', 'Água e Saneamento', 'Água e Saneamento', 'Água e Saneamento', 'Gás', 'Gás', 'Gás', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Bancos', 'Soc. Crédito e Financiamento', 'Soc. Crédito e Financiamento', 'Securitizadoras de Recebíveis', 'Securitizadoras de Recebíveis', 'Securitizadoras de Recebíveis', 'Gestão de Recursos e Investimentos', 'Gestão de Recursos e Investimentos', 'Gestão de Recursos e Investimentos', 'Serviços Financeiros Diversos', 'Serviços Financeiros Diversos', 'Serviços Financeiros Diversos', 'Serviços Financeiros Diversos', 'Serviços Financeiros Diversos', 'Serviços Financeiros Diversos', 'Serviços Financeiros Diversos', 'Seguradoras', 'Seguradoras', 'Seguradoras', 'Resseguradoras', 'Corretoras de Seguros e Resseguros', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Exploração de Imóveis', 'Intermediação Imobiliária', 'Intermediação Imobiliária', 'Holdings Diversificadas', 'Holdings Diversificadas', 'Holdings Diversificadas', 'Outros Títulos', 'Outros Títulos', 'Outros Títulos', 'Outros', 'Outros', 'Outros', 'Outros', 'Outros', 'Outros', 'Outros', 'Outros', 'Outros', 'Outros', 'Outros', 'Outros']

cias = pd.DataFrame({'Código': codigo,
                    'Nome':  nome,
                    'Segmento':  segmento})
#--------------------------------------------------------------------------------------

# Configuração do cabeçalho para simular um navegador
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml;application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'close'
}

# URL do site Fundamentus
url_1 = 'https://fundamentus.com.br/resultado.php'

# Fazer a requisição
st.title("Filtro de ações B3")
# st.write("Buscando dados do site Fundamentus...")

try:
    request_1 = requests.get(url_1, headers=header)
    request_1.raise_for_status()  # Verifica se houve algum erro na requisição

    # Lê a tabela usando pandas
    colunas = ["Papel", "Cotação", "P/VP", "P/L", "LPA", "PSR", "Div.Yield", "EV/EBIT", "EV/EBITDA",
               "Mrg. Líq.", "ROE", "ROIC", "Cresc. Rec.5a"]

    tabela = pd.DataFrame(pd.read_html(request_1.text)[0], columns=colunas)

    tabela['Código'] = tabela['Papel'].str[:-1]

    fundamentos = pd.merge(cias, tabela, on='Código', how='inner')

    #---------------------------------------------------------------------------
    # Tratamento.

    # Modificar o nome das Colunas e definir index.

    fundamentos.columns = fundamentos.columns.str.replace('/', '_').str.replace(' ', '_').str.replace('.', '_')
    fundamentos = fundamentos.set_index('Papel')

    # Modificar formato % e converter valores para numéricos.

    fundamentos['Div_Yield'] = (fundamentos['Div_Yield'].str.replace('%', '').str.replace(',', '.')).apply(pd.to_numeric, errors='coerce')/100
    fundamentos['Cresc__Rec_5a'] = (fundamentos['Cresc__Rec_5a'].str.replace('%', '').str.replace(',', '.')).apply(pd.to_numeric, errors='coerce')/100
    fundamentos['Mrg__Líq_'] = (fundamentos['Mrg__Líq_'].str.replace('%', '').str.replace(',', '.')).apply(pd.to_numeric, errors='coerce')/100
    fundamentos['ROE'] = (fundamentos['ROE'].str.replace('%', '').str.replace(',', '.')).apply(pd.to_numeric, errors='coerce')/100
    fundamentos['ROIC'] = (fundamentos['ROIC'].str.replace('%', '').str.replace(',', '.')).apply(pd.to_numeric, errors='coerce')/100

    # Converter colunas para valores numéricos.

    colunas_numericas = ['Cotação', 'P_VP', 'P_L', 'PSR', 'EV_EBIT', 'EV_EBITDA'] 
    fundamentos[colunas_numericas] = fundamentos[colunas_numericas].apply(pd.to_numeric, errors='coerce')

    # Cálculo dos indicadores.

    fundamentos = fundamentos[fundamentos["P_L"] > 0]

    fundamentos['VPA'] = fundamentos['Cotação']/fundamentos['P_VP']
    fundamentos['LPA'] = fundamentos['Cotação']/fundamentos['P_L']

    fundamentos['Cotação'] = fundamentos['Cotação']/100
    fundamentos['P_VP'] = fundamentos['P_VP']/100
    fundamentos['P_L'] = fundamentos['P_L']/100
    fundamentos['PSR'] = fundamentos['PSR']/1000
    fundamentos['EV_EBIT'] = fundamentos['EV_EBIT']/100
    fundamentos['EV_EBITDA'] = fundamentos['EV_EBITDA']/100

    fundamentos['Dividend_Yield_%'] = fundamentos['Div_Yield']*100
    fundamentos['Div_Yield'] = fundamentos['Div_Yield'].astype(float).map('{:.2%}'.format)

    fundamentos['Margem_Líq_%'] = fundamentos['Mrg__Líq_']*100
    fundamentos['Mrg__Líq_'] = fundamentos['Mrg__Líq_'].astype(float).map('{:.2%}'.format)

    fundamentos['ROIC_%'] = fundamentos['ROIC']*100
    fundamentos['ROIC'] = fundamentos['ROIC'].astype(float).map('{:.2%}'.format)

    fundamentos['ROE_%'] = fundamentos['ROE']*100
    fundamentos['ROE'] = fundamentos['ROE'].astype(float).map('{:.2%}'.format)

    fundamentos['Cresc__Rec_5_anos_%'] = fundamentos['Cresc__Rec_5a']*100
    fundamentos['Cresc__Rec_5a'] = fundamentos['Cresc__Rec_5a'].astype(float).map('{:.2%}'.format)

    #---------------------------------------------------------------------------

    # Exibindo os dados no Streamlit

    st.success("Dados carregados com sucesso!")
    # st.dataframe(fundamentos)

    # Opcional: salvar os dados em um arquivo Excel.

    # save_excel = st.button("Salvar dados .xlsx")

    # if save_excel:

    #     try:

    #         # Salvando o DataFrame em um arquivo Excel.

    #         fundamentos.to_excel("C:/Users/pccli/Downloads/dados_fundamentus.xlsx", index=False)
    #         st.success("Arquivo salvo como 'dados_fundamentus.xlsx'.")

    #     except Exception as e:

    #         st.error(f"Erro ao salvar o arquivo: {e}")

except Exception as e:

    st.error(f"Erro ao carregar dados: {e}")
    st.write("Verifique sua conexão ou tente novamente mais tarde.")

#-------------------------------------------------------------------------------------------------
# Sliders no painel lateral.

st.sidebar.title("**Indicadores**")
st.sidebar.write("Use os sliders na barra lateral para ajustar os valores dos indicadores.")

col1_slider = st.sidebar.slider("**P_VP:**  menor que 1 é melhor.", 0.0, 5.0, value=(0.0, 2.0), step=0.1)
col2_slider = st.sidebar.slider("**PSR:**  menor que 1 é melhor.", 0.0, 5.0, value=(0.0, 2.0), step=0.1)
col3_slider = st.sidebar.slider("**P_L:**  aproximadamente igual a 10.", 0.0, 20.0, value=(0.0, 10.0), step=0.1)
col4_slider = st.sidebar.slider("**Dividend_Yield_%:**  maior ou igual a 10 é melhor.", 0.0, 30.0, value=(0.0, 20.0), step=1.0)
col5_slider = st.sidebar.slider("**EV_EBIT:**  menor ou igual a 3 é melhor.", 0.0, 20.0, value=(0.0, 10.0), step=0.5)
col6_slider = st.sidebar.slider("**EV_EBITDA:**  menor ou igual a 3 é melhor.", 0.0, 20.0, value=(0.0, 10.0), step=0.5)
col7_slider = st.sidebar.slider("**Margem_Líq_%:**  quanto maior melhor.", 0, 100, value=(0, 50), step=5)
col8_slider = st.sidebar.slider("**ROIC_%:**  quanto maior melhor.", 0, 100, value=(0, 50), step=5)
col9_slider = st.sidebar.slider("**ROE_%:**  quanto maior melhor.", 0, 100, value=(0, 50), step=5)
col10_slider = st.sidebar.slider("**Cresc__Rec_5_anos_%:**  quanto maior melhor.", -100, 100, value=(-50, 100), step=5)

# Lista suspensa tipo escolha múltipla.

st.markdown("<h3 style='font-size:24px;'>Segmentos</h3>", unsafe_allow_html=True)

opcoes = sorted(fundamentos['Segmento'].unique())
lista_susp = st.multiselect("Selecione os segmentos:", opcoes)

# Copia o DataFrame para aplicar filtros.

data_filtered = fundamentos.sort_values(by='P_VP').copy()

# Filtra os valores o DataFrame com base nos limites dos sliders.

data_filtered = data_filtered[(data_filtered['P_VP'] >= col1_slider[0]) & (data_filtered['P_VP'] <= col1_slider[1])]
data_filtered = data_filtered[(data_filtered['PSR'] >= col2_slider[0]) & (data_filtered['PSR'] <= col2_slider[1])]
data_filtered = data_filtered[(data_filtered['P_L'] >= col3_slider[0]) & (data_filtered['P_L'] <= col3_slider[1])]
data_filtered = data_filtered[(data_filtered['Dividend_Yield_%'] >= col4_slider[0]) & (data_filtered['Dividend_Yield_%'] <= col4_slider[1])]
data_filtered = data_filtered[(data_filtered['EV_EBIT'] >= col5_slider[0]) & (data_filtered['EV_EBIT'] <= col5_slider[1])]
data_filtered = data_filtered[(data_filtered['EV_EBITDA'] >= col6_slider[0]) & (data_filtered['EV_EBITDA'] <= col6_slider[1])]
data_filtered = data_filtered[(data_filtered['Margem_Líq_%'] >= col7_slider[0]) & (data_filtered['Margem_Líq_%'] <= col7_slider[1])]
data_filtered = data_filtered[(data_filtered['ROIC_%'] >= col8_slider[0]) & (data_filtered['ROIC_%'] <= col8_slider[1])]
data_filtered = data_filtered[(data_filtered['ROE_%'] >= col9_slider[0]) & (data_filtered['ROE_%'] <= col9_slider[1])]
data_filtered = data_filtered[(data_filtered['Cresc__Rec_5_anos_%'] >= col10_slider[0]) & (data_filtered['Cresc__Rec_5_anos_%'] <= col10_slider[1])]

# Lista suspensa para seleção de carteiras.

# fazer ...

# Filtra o DataFrame de acordo com a seleção na coluna Segmento.

if lista_susp:
    data_filtered = data_filtered[data_filtered['Segmento'].isin(lista_susp)]

#-------------------------------------------------------------------------------------------------

st.data_editor(data_filtered[['Nome', 'Segmento', 'Cotação', 'VPA', 'P_VP', 'LPA', 'P_L', 'PSR', 'Div_Yield',
                                    'EV_EBIT', 'EV_EBITDA',
                                    'Mrg__Líq_', 'ROIC', 'ROE',
                                    'Cresc__Rec_5a']], use_container_width=True)

st.write(f'{len(data_filtered)} ações filtradas.')

#-------------------------------------------------------------------------------------------------

# Proventos.

st.title("Proventos")

proventos = pd.DataFrame(columns = ['Data', 'Valor', 'Tipo','Data de pagamento', 'Por quantas ações'])

acao = st.selectbox("Selecione uma ação", sorted(data_filtered.index.tolist())) # lista suspensa

url_2 = f'https://fundamentus.com.br/proventos.php?papel={acao}&tipo=2'

#---------------------------------------------------------------------------------------------------

request_2 = requests.get(url_2, headers = header).text
soup = BeautifulSoup(request_2, 'html.parser')
table = soup.find('table')

for linha in table.tbody.find_all('tr'):
  columns = linha.find_all('td')
  if (columns != []):
    data = columns[0].text.strip(' ')
    valor = columns[1].text.strip(' ')
    tipo = columns[2].text.strip(' ')
    data_pagamento = columns[3].text.strip(' ')
    quantidade_acoes = columns[4].text.strip(' ')
    proventos = pd.concat(([proventos, pd.DataFrame.from_records([{'Data': data,
                                                     'Valor': valor,
                                                     'Tipo': tipo,
                                                     'Data de pagamento': data_pagamento,
                                                     'Por quantas ações': quantidade_acoes}])]))

#---------------------------------------------------------------------------------------------------

proventos['Data'] = pd.to_datetime(proventos['Data'], format = '%d/%m/%Y', errors = 'ignore')

proventos['Valor'] =[x.replace(',', '.') for x in proventos['Valor']]
proventos = proventos.astype({'Valor': float})

temp = pd.to_datetime(proventos['Data de pagamento'], format = '%d/%m/%Y', errors = 'coerce')
proventos['Data de pagamento'] = proventos['Data de pagamento'].where(temp.isna(), temp.dt.date)

proventos['Tipo'] = proventos['Tipo'].str.upper()

proventos = proventos.astype({'Por quantas ações': int})

proventos = proventos.set_index('Data')

#---------------------------------------------------------------------------------------------------

# Gráfico.

# Entrada de anos pelo usuário

ano_atual = datetime.today().year
ano_inicial = st.number_input("Ano Inicial", min_value=2000, max_value=datetime.today().year, value=ano_atual-5)
ano_final = st.number_input("Ano Final", min_value=2000, max_value=datetime.today().year, value=ano_atual)

# Filtrando os dados com base nos anos escolhidos

proventos.index = pd.to_datetime(proventos.index)
prov = proventos[(proventos.index.year >= ano_inicial) & (proventos.index.year <= ano_final)]

# Cálculo dos proventos anuais

prov_anual = (prov['Valor'] / prov['Por quantas ações']).resample('Y').sum()

# Média dos proventos anuais

media_prov = prov_anual.mean()

# Gráfico

plt.figure(figsize=(15, 8))

# Adicionando rótulos nas barras

for i, valor in enumerate(prov_anual):
    plt.text(prov_anual.index.year[i], valor, f'{valor:.2f}', ha='center', va='bottom', fontsize=14)

# Plotando as barras

plt.bar(prov_anual.index.year, prov_anual)
plt.axhline(y=media_prov, color='red', linestyle='--')

# Texto sobre a linha da média

plt.text(plt.xlim()[1], media_prov, f'Média dos proventos: R$ {media_prov:.2f}', va='bottom', color='black', fontsize=14)

# Título e rótulos

plt.title(f'Proventos por ação {acao} entre {ano_inicial} e {ano_final}', fontsize=20)
# plt.xlabel('Ano', fontsize=16)
plt.ylabel('Proventos (R$)', fontsize=16)

# Exibindo o gráfico no Streamlit

st.pyplot(plt)

# Exibindo a média dos proventos

# st.write(f'Média dos proventos: R$ {media_prov:.2f}')

st.markdown(
    f'<a href="https://statusinvest.com.br/acoes/{acao}" target="_blank" style="color:blue; font-size:20px; text-decoration:none;">Mais detalhes de {acao} aqui!</a>',
    unsafe_allow_html=True
)
