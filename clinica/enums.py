from django.db import models

class SexoPaciente(models.TextChoices):
    masculino = 'M'
    feminino = 'F'
    outro = 'O'

class SimOuNao(models.TextChoices):
    sim = 'Sim'
    nao = 'Não'

class ParticularOuConvenio(models.TextChoices):
    particular = 'Particular'
    convenio = 'Convênio'

class PlanosDeSaude(models.TextChoices):
    bradesco = 'Bradesco'

class ConsultaRealizada(models.TextChoices):
    sim = 'Sim'
    cancelou = 'Cancelou'
    faltou = 'Faltou'
    desistiu = 'Desistiu'

class Exames(models.TextChoices):
    tc_de_maxila_tipo_cone_beam = "TC DE MAXILA - TIPO CONE BEAM"
    tc_de_mandibula_tipo_cone_beam_virtual = "TC DE MANDÍBULA - TIPO CONE BEAM POR MEIO VIRTUAL OU POR E-MAIL"
    tc_cone_beam_com_tracado_para_implantes = "TC CONE BEAM COM TRAÇADO PARA IMPLANTES"
    rx_de_face_po = "RX DE FACE PO"
    radiografia_oclusal = "RADIOGRAFIA OCLUSAL"
    radiografia_periapical = "RADIOGRAFIA PERIAPICAL"
    radiografia_panoramica_sem_laudo = "RADIOGRAFIA PANORÂMICA SEM LAUDO"
    radiografia_panoramica_com_laudo = "RADIOGRAFIA PANORÂMICA COM LAUDO"
    rx_perfil_de_face = "RX PERFIL DE FACE"
    rx_pa_de_mandibula = "RX PA DE MANDÍBULA"
    rx_waters = "RX WATER'S"
    ressonancia_magnetica_de_atm = "RESSONÂNCIA MAGNÉTICA DE ATM"
    ressonancia_magnetica_de_maxila = "RESSONÂNCIA MAGNÉTICA DE MAXILA"
    ressonancia_magnetica_de_mandibula = "RESSONÂNCIA MAGNÉTICA DE MANDÍBULA"
    ultrassonografia_de_glandula_submandibular = "ULTRASSONOGRAFIA DE GLÂNDULA SUBMANDIBULAR"
    ultrassonografia_de_glandula_parotida = "ULTRASSONOGRAFIA DE GLÂNDULA PARÓTIDA"
    tc_de_seios_da_face = "TC DE SEIOS DA FACE"
    tc_de_face = "TC DE FACE"
    tc_de_face_em_3d = "TC DE FACE EM 3D"
    tc_de_maxila = "TC DE MAXILA"
    tc_de_mandibula = "TC DE MANDÍBULA"
    tc_de_mandibula_atm = "TC DE MANDÍBULA - ATM"
    exames_solicitados_por_outro_profissional = "EXAMES SOLICITADOS POR OUTRO PROFISSIONAL"
    exames_ortognatica_usp_mcnamara_unicamp = "EXAMES ORTOGNÁTICA - USP/MC NAMARA/ UNICAMP"
    ultrassonografia = "ULTRASSONOGRAFIA"



class ProfissionaisParaEncaminhar(models.TextChoices):
    nao = "NÃO"
    endodontia = "ENDODONTIA"
    fisioterapia = "FISIOTERAPIA"
    cirurgiao_plastico = "CIRURGIÃO PLÁSTICO"
    otorrino = "OTORRINO"
    neuroclinico = "NEUROCLÍNICO"
    neurocirurgia = "NEUROCIRURGIA"
    psicologo = "PSICÓLOGO"
    psiquiatra = "PSIQUIATRA"
    nefrologista = "NEFROLOGISTA"
    cardiologista = "CARDIOLOGISTA"
    protesista = "PROTESISTA"
    fono = "FONO"
    ortodontista = "ORTODONTISTA"
    dra_samya_cabral = "DRA. SÂMYA CABRAL"
    dra_monica_taira = "DRA. MÔNICA TAIRA"
    dra_hosana_baima = "DRA. HOSANA BAIMA"
    dra_gisele_gonzaga = "DRA. GISELE GONZAGA"
    dentistica_estetica = "DENTÍSTICA - ESTÉTICA"
    dr_antonio_jorge = "DR. ANTÔNIO JORGE"
    dr_miguel_ledo = "DR. MIGUEL LEDO"


