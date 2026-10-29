# -*- coding: utf-8 -*-
"""Dossier de présentation — CPC, IEN, archivage et transfert à d'autres écoles."""
from fpdf import FPDF
import os

FONT = "/home/hermeswebui/.fonts/DejaVuSans.ttf"
FONTB = "/home/hermeswebui/.fonts/DejaVuSans-Bold.ttf"
SH = "/workspace/nah"
URL = "hassanijacques-boop.github.io/non-au-harcelement"
VERSION = "20261027-7"

INK = (18, 22, 32)
GREY = (92, 98, 110)
MGREY = (176, 181, 190)
LINE = (203, 208, 216)
IND = (58, 48, 176)
IND_C = (233, 234, 251)
BLEU = (16, 106, 200)
BLEU_C = (229, 241, 252)
TEAL = (12, 122, 130)
TEAL_C = (226, 244, 245)
VERT = (22, 132, 76)
VERT_C = (231, 247, 238)
AMBRE = (176, 106, 8)
AMBRE_C = (253, 246, 228)
ROUGE = (192, 38, 44)
ROUGE_C = (253, 233, 233)
LM = 12
W = 186


class PDF(FPDF):
    def __init__(self):
        super().__init__(format="A4")
        self.add_font("D", "", FONT)
        self.add_font("D", "B", FONTB)
        self.set_auto_page_break(False)
        self.set_margins(LM, 10, LM)

    def pied(self, txt):
        self.set_y(-9)
        self.set_font("D", "", 6.6)
        self.set_text_color(*GREY)
        self.set_x(LM)
        self.cell(150, 4, txt)
        self.set_x(LM + 148)
        self.cell(38, 4, "%d" % self.page_no(), align="R")


def entete(pdf, surtitre, titre, sous="", col=IND):
    pdf.set_fill_color(*col)
    pdf.rect(0, 0, 210, 21, style="F")
    pdf.set_xy(LM, 4)
    pdf.set_font("D", "", 7.2)
    pdf.set_text_color(226, 228, 240)
    pdf.cell(0, 4, surtitre.upper())
    pdf.set_xy(LM, 8.4)
    pdf.set_font("D", "B", 13.6)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 7, titre)
    pdf.set_y(25)
    if sous:
        pdf.set_font("D", "", 8.5)
        pdf.set_text_color(*GREY)
        pdf.set_x(LM)
        pdf.multi_cell(W, 4.5, sous, align="L")
        pdf.set_y(pdf.get_y() + 2.4)


def h2(pdf, txt, y=None, size=10.2, col=INK):
    pdf.set_y(y if y is not None else pdf.get_y() + 2)
    pdf.set_font("D", "B", size)
    pdf.set_text_color(*col)
    pdf.set_x(LM)
    pdf.cell(0, 5.6, txt)
    pdf.set_y(pdf.get_y() + 6.8)


def para(pdf, txt, size=8.8, lh=4.65, color=INK, indent=0):
    pdf.set_font("D", "", size)
    pdf.set_text_color(*color)
    pdf.set_x(LM + indent)
    pdf.multi_cell(W - indent, lh, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)


def puce(pdf, a, b=None, size=8.7, lh=4.6):
    head, txt = (None, a) if b is None else (a, b)
    pdf.set_x(LM + 1)
    pdf.set_text_color(*INK)
    if head:
        pdf.set_font("D", "B", size)
        pdf.write(lh, "\u2022  " + head + "  ")
        pdf.set_font("D", "", size)
        pdf.write(lh, txt)
    else:
        pdf.set_font("D", "", size)
        pdf.write(lh, "\u2022  " + txt)
    pdf.ln(lh + 1.1)
    pdf.set_x(LM)


def cellule(pdf, x, y, w, h, txt, size=7.5, gras=False, centre=False, pad=2.0, fill=None):
    if fill:
        pdf.set_fill_color(*fill)
        pdf.rect(x, y, w, h, style="F")
    pdf.set_draw_color(*LINE)
    pdf.set_line_width(0.3)
    pdf.rect(x, y, w, h)
    pdf.set_font("D", "B" if gras else "", size)
    pdf.set_text_color(*INK)
    if centre:
        pdf.set_xy(x, y + h / 2 - 2)
        pdf.cell(w, 4, txt, align="C")
    else:
        pdf.set_xy(x + pad, y + 1.5)
        pdf.multi_cell(w - 2 * pad, 3.9, txt, align="L")


def ligne(pdf, y, h, cols):
    x = LM
    for w, txt, sz, gr, ce in cols:
        cellule(pdf, x, y, w, h, txt, sz, gr, ce)
        x += w
    return y + h


def bloc(pdf, titre, lignes, y, size=8.5, fill=None, accent=None):
    hh = 6.2
    for l in lignes:
        hh += 4.55 * max(1, -(-len(l) // 96))
    hh += 2
    if fill:
        pdf.set_fill_color(*fill)
        pdf.set_draw_color(*LINE)
        pdf.set_line_width(0.3)
        pdf.rect(LM, y, W, hh, style="DF")
    else:
        pdf.set_draw_color(*LINE)
        pdf.set_line_width(0.3)
        pdf.rect(LM, y, W, hh)
    if accent:
        pdf.set_fill_color(*accent)
        pdf.rect(LM, y, 2.4, hh, style="F")
    pdf.set_xy(LM + 5, y + 2)
    pdf.set_font("D", "B", 8.7)
    pdf.set_text_color(*(accent or INK))
    pdf.cell(0, 4.4, titre)
    yy = y + 7.2
    pdf.set_font("D", "", size)
    pdf.set_text_color(*INK)
    for l in lignes:
        pdf.set_xy(LM + 5, yy)
        pdf.multi_cell(W - 9, 4.55, l, align="L")
        yy = pdf.get_y()
    return y + hh


pdf = PDF()

# ============================== 1. COUVERTURE ==============================
pdf.add_page()
pdf.set_fill_color(*IND)
pdf.rect(0, 0, 210, 104, style="F")
pdf.set_xy(LM, 15)
pdf.set_font("D", "", 8.2)
pdf.set_text_color(198, 201, 244)
pdf.cell(0, 5, "DOSSIER DE PRÉSENTATION  ·  CONSEILLER PÉDAGOGIQUE  ·  INSPECTEUR DE CIRCONSCRIPTION")
pdf.set_xy(LM, 26)
pdf.set_font("D", "B", 29)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 12, "Journée du 5 novembre 2026")
pdf.set_xy(LM, 41)
pdf.set_font("D", "B", 14.5)
pdf.set_text_color(224, 226, 250)
pdf.cell(0, 8, "Lutte contre le harcèlement scolaire, du CP au CM2")
pdf.set_xy(LM, 52)
pdf.set_font("D", "", 10)
pdf.set_text_color(214, 217, 249)
pdf.cell(0, 6, "École primaire publique La Rose  ·  circonscription IEN Bandraboua")
pdf.set_fill_color(255, 255, 255)
pdf.rect(LM, 63, 46, 0.9, style="F")
pdf.set_xy(LM, 68)
pdf.set_font("D", "", 8.6)
pdf.set_text_color(206, 210, 248)
pdf.multi_cell(155, 5,
    "18 classes  ·  335 élèves  ·  2 cycles  ·  9 activités  ·  7 classes enquêtées. "
    "Document conçu pour être présenté, archivé, et transmis à d’autres écoles.", align="L")
pdf.set_xy(LM, 86)
pdf.set_font("D", "", 8)
pdf.set_text_color(184, 189, 242)
pdf.cell(0, 4.6, "Version %s  ·  27 octobre 2026" % VERSION)
pdf.set_xy(LM, 91)
pdf.set_font("D", "", 7.6)
pdf.set_text_color(166, 172, 236)
pdf.cell(0, 4.6, "Application, kit et protocole : " + URL)

# sommaire
pdf.set_y(112)
pdf.set_font("D", "B", 12)
pdf.set_text_color(*IND)
pdf.set_x(LM)
pdf.cell(0, 6, "Sommaire")
somm = [
    ("1", "Note de synthèse à l’attention de l’inspecteur", "2"),
    ("2", "Le dispositif en un coup d’œil", "3"),
    ("3", "Cycle 2 : ce que font les CP et les CE1", "4"),
    ("4", "Cycle 3 : ce que font les CE2, CM1 et CM2", "5"),
    ("5", "Le questionnaire et ce que l’outil calcule", "6"),
    ("6", "Cadre réglementaire, données et droit à l’image", "7"),
    ("7", "Organiser la journée dans une école de 18 classes", "8"),
    ("8", "Après la journée : saisir, consolider, rapporter", "9"),
    ("9", "Restitution et labellisation niveau 1", "10"),
    ("10", "Le prix Non au harcèlement", "11"),
    ("11", "Transmettre à une autre école", "12"),
    ("12", "Rétroplanning de la campagne", "13"),
    ("13", "Inventaire des pièces et contacts", "14"),
]
y = 122
for i, (n, t, p) in enumerate(somm):
    col = LM if i < 7 else LM + 96
    yy = y + (i % 7) * 9.2
    pdf.set_xy(col, yy)
    pdf.set_font("D", "B", 8.4)
    pdf.set_text_color(*IND)
    pdf.cell(6, 5, n + ".")
    pdf.set_font("D", "", 8.6)
    pdf.set_text_color(*INK)
    pdf.cell(80, 5, t)
    pdf.set_font("D", "", 8)
    pdf.set_text_color(*GREY)
    pdf.cell(6, 5, p, align="R")
    pdf.set_draw_color(*MGREY)
    pdf.set_dash_pattern(dash=0.6, gap=1.4)
    pdf.line(col + 6, yy + 4.6, col + 86, yy + 4.6)
    pdf.set_dash_pattern()

pdf.set_y(190)
pdf.set_fill_color(*IND_C)
pdf.rect(LM, 190, W, 34, style="F")
pdf.set_xy(LM + 5, 193)
pdf.set_font("D", "B", 8.8)
pdf.set_text_color(*IND)
pdf.cell(0, 4.6, "Comment lire ce dossier")
pdf.set_xy(LM + 5, 199)
pdf.set_font("D", "", 8.4)
pdf.set_text_color(*INK)
pdf.multi_cell(W - 10, 4.6,
    "Les pages 2 et 3 portent la demande et le dispositif. Les pages 4 et 5 disent précisément ce que fait "
    "chaque niveau, cycle par cycle. Les pages 6 à 10 traitent de la mise en œuvre et des suites. Les pages "
    "11 à 14 servent à transmettre : le prix, le transfert à une autre école, le calendrier et l’inventaire "
    "des pièces à archiver.", align="L")

# resume en trois phrases
pdf.set_y(232)
pdf.set_draw_color(*IND)
pdf.set_line_width(0.9)
pdf.rect(LM, 232, W, 44)
pdf.set_xy(LM + 5, 235)
pdf.set_font("D", "B", 9.2)
pdf.set_text_color(*IND)
pdf.cell(0, 5, "En trois phrases")
pdf.set_xy(LM + 5, 242)
pdf.set_font("D", "", 8.6)
pdf.set_text_color(*INK)
pdf.multi_cell(W - 10, 5.1,
    "1.  Le 5 novembre, les 18 classes de l’école mènent une activité de lutte contre le harcèlement, "
    "adaptée à leur âge ; les 7 classes de CE2, de CM1 et de CM2 remplissent en plus la grille "
    "officielle.\n"
    "2.  Les résultats sont saisis, calculés et interprétés selon la table de croisement du guide : "
    "l’école sait enfin combien d’élèves sont concernés, et lesquels recevoir.\n"
    "3.  Tout est gratuit, sans serveur, sans donnée en ligne, et transférable tel quel à une autre école.",
    align="L")
pdf.pied("Dossier de présentation · journée du 5 novembre 2026")

# ============================== 2. NOTE DE SYNTHESE ==============================
pdf.add_page()
entete(pdf, "1 · Note de synthèse", "Ce que je soumets à votre examen",
       "Objet : une journée de lutte contre le harcèlement outillée pour les 18 classes de l’école, "
       "du CP au CM2, dont l’exploitation des résultats est désormais interprétée.")

h2(pdf, "Le problème que ce dispositif résout", 40)
para(pdf, "Les années précédentes, la grille d’auto-évaluation a été remplie dans les classes, mais les "
          "résultats n’ont pas été exploités : les questionnaires étaient dépouillés à la main, ou pas du "
          "tout. Une école qui fait remplir la grille sans en tirer d’enseignements ne peut ni cibler ses "
          "actions, ni documenter sa démarche dans un dossier de labellisation.")
para(pdf, "Le dispositif proposé ne change pas la passation : la grille reste remplie sur papier, pendant "
          "les deux heures banalisées, sous la responsabilité du professeur. Il ajoute l’exploitation — "
          "saisie, calcul des indices officiels, lecture de la table de croisement, rapport par classe et "
          "par niveau — et il outille les dix classes de CP et de CE1, qui ne passent pas le questionnaire "
          "mais participent à la journée.", indent=0)

h2(pdf, "Ce que cela produit, concrètement")
for a, b in [
    ("Un état des lieux daté", "nombre d’élèves en situation de harcèlement et en zone à surveiller, "
     "calculé selon la table officielle, avec les repères nationaux (3 % / 13 %) en regard."),
    ("Une liste d’élèves à recevoir", "nominative, par classe, avec les faits déclarés et leur gravité. "
     "C’est la pièce qui transforme une enquête en prise en charge."),
    ("Des traces pédagogiques", "une affiche par classe, un mur de mots, des fiches élèves : les pièces "
     "attendues à l’axe « prévenir » du dossier de labellisation."),
    ("Un dossier transférable", "l’application ne contient aucune donnée d’élève en ligne, et les "
     "documents sont génériques : une autre école peut s’en saisir sans rien réécrire."),
]:
    puce(pdf, a, b)

h2(pdf, "Ce que je demande")
pdf.set_fill_color(*IND_C)
pdf.rect(LM, pdf.get_y(), W, 30, style="F")
pdf.set_xy(LM + 5, pdf.get_y() + 3)
pdf.set_font("D", "", 8.6)
pdf.set_text_color(*INK)
pdf.multi_cell(W - 10, 4.7,
    "1.  Valider le principe d’une exploitation des résultats par l’école elle-même, sur la base de la "
    "table de croisement officielle et sans modification de l’instrument.\n"
    "2.  Autoriser la diffusion du dispositif aux autres écoles de la circonscription, si vous le jugez "
    "utile, le dossier étant conçu pour cela (pages 13 et 14).\n"
    "3.  Désigner, si le dispositif est étendu, un référent de circonscription pour l’agrégation des "
    "résultats d’école — étape non prévue cette année.", align="L")
pdf.set_y(pdf.get_y() + 6)

h2(pdf, "Trois réserves que je formule moi-même")
for t in ["L’outil n’est adossé à aucun serveur : il n’existe pas de base de données académique. La trace "
          "est constituée par les fichiers exportés. Il faut donc désigner qui les conserve, et les "
          "détruire à l’échéance.",
          "La fidélité de l’instrument n’est pas modifiée, mais l’ajout d’une lecture audio et d’une "
          "reformulation en français simple peut modifier le taux de réponses chez les élèves en "
          "difficulté de lecture. C’est assumé, et signalé dans le protocole.",
          "L’interprétation reste un outil de pilotage : elle ne remplace ni l’entretien, ni le signalement "
          "au titre du protocole national."]:
    puce(pdf, t)
pdf.pied("Dossier de présentation · note de synthèse")

# ============================== 3. LE DISPOSITIF ==============================
pdf.add_page()
entete(pdf, "2 · Le dispositif", "Un seul jour, deux parcours, une exploitation commune",
       "Ce que fait chaque classe le 5 novembre, et ce que l’école en tire.")

# schema
y = 40
pdf.set_fill_color(*IND)
pdf.rect(LM, y, 52, 20, style="F")
pdf.set_xy(LM + 2, y + 2.5)
pdf.set_font("D", "B", 9.4)
pdf.set_text_color(255, 255, 255)
pdf.multi_cell(48, 4.6, "18 classes\n335 élèves", align="C")
# fleches et deux branches
for i, (col, colc, titre, sous) in enumerate([
        (VERT, VERT_C, "Cycle 2  ·  11 classes", "CP et CE1 : activités seules, 45 min"),
        (BLEU, BLEU_C, "Cycle 3  ·  7 classes", "CE2 à CM2 : activités puis questionnaire")]):
    yy = y - 4 + i * 26
    pdf.set_fill_color(*colc)
    pdf.set_draw_color(*col)
    pdf.set_line_width(0.9)
    pdf.rect(LM + 60, yy, 76, 22, style="DF")
    pdf.set_xy(LM + 63, yy + 3)
    pdf.set_font("D", "B", 9.2)
    pdf.set_text_color(*col)
    pdf.cell(0, 4.6, titre)
    pdf.set_xy(LM + 63, yy + 9.4)
    pdf.set_font("D", "", 8)
    pdf.set_text_color(*INK)
    pdf.cell(0, 4.4, sous)
    pdf.set_draw_color(*col)
    pdf.set_line_width(1)
    pdf.line(LM + 52, y + 10, LM + 60, yy + 11)

pdf.set_fill_color(*IND_C)
pdf.rect(LM + 142, y, 44, 46, style="F")
pdf.set_xy(LM + 145, y + 3)
pdf.set_font("D", "B", 8.8)
pdf.set_text_color(*IND)
pdf.multi_cell(38, 4.6, "Saisie\nexport\nconsolidation", align="L")
pdf.set_draw_color(*IND)
pdf.set_line_width(1)
pdf.line(LM + 136, y + 10, LM + 142, y + 10)
pdf.line(LM + 136, y + 32, LM + 142, y + 14)

pdf.set_y(y + 50)
h2(pdf, "Les six temps du dispositif")
tps = [("1", "Préparer", "18 enveloppes, 20 minutes en conseil des maîtres, aucune formation.", "octobre"),
       ("2", "Faire", "2 h banalisées : activités, puis questionnaire pour le cycle 3.", "5 nov. – 11 déc."),
       ("3", "Saisir", "Chaque professeur recopie sa classe : 30 minutes, au clavier.", "avant le 11 déc."),
       ("4", "Consolider", "7 fichiers fusionnés sur un poste ; effectifs ; rapport.", "décembre"),
       ("5", "Restituer", "Conseil des maîtres, familles, élèves à recevoir.", "décembre"),
       ("6", "Documenter", "4 axes de labellisation, prix Non au harcèlement.", "janv. – printemps")]
yy = pdf.get_y()
for n, t, d, q in tps:
    pdf.set_font("D", "B", 8)
    pdf.set_text_color(*IND)
    pdf.set_xy(LM, yy)
    pdf.cell(5, 5, n)
    pdf.set_font("D", "B", 8.4)
    pdf.set_text_color(*INK)
    pdf.cell(24, 5, t)
    pdf.set_font("D", "", 8.2)
    pdf.multi_cell(W - 52, 4.4, d, align="L")
    pdf.set_xy(LM + W - 22, yy)
    pdf.set_font("D", "", 7.6)
    pdf.set_text_color(*GREY)
    pdf.cell(22, 5, q, align="R")
    yy = max(pdf.get_y(), yy + 5) + 1.6

bloc(pdf, "Ce qui change par rapport aux années précédentes", [
    "Les résultats ne restent pas dans un carton : ils sont calculés selon la table de croisement "
    "officielle, et donnent une liste d’élèves à recevoir par classe.",
    "Les CP et les CE1 ne sont plus laissés de côté : ils ont leur propre parcours, sans questionnaire.",
    "Rien n’est stocké en ligne : chaque poste garde ses données, la consolidation se fait par fichiers."],
    yy + 3, fill=IND_C, accent=IND)

bloc(pdf, "Ce que l’école saura le 12 décembre 2026, et qu’elle ne savait pas le 4 novembre", [
    "Combien d’élèves sont en situation de harcèlement, combien sont en zone à surveiller, et où cela se "
    "situe par rapport aux repères nationaux.",
    "Quelles classes sont les plus concernées, et quels thèmes ressortent des questions de contexte : "
    "c’est ce qui fixera les séances de l’année.",
    "Quels élèves doivent être reçus, individuellement, avec les faits qu’ils ont déclarés et leur "
    "gravité — la seule information qui déclenche une action.",
    "Ce que l’école peut joindre à son dossier de labellisation, et sur quelle mesure de départ elle "
    "s’appuiera l’an prochain."],
    yy + 47, fill=VERT_C, accent=VERT)
pdf.pied("Dossier de présentation · le dispositif")

# ============================== 4. CYCLE 2 ==============================
pdf.add_page()
entete(pdf, "3 · Cycle 2", "CP et CE1 : nommer, se protéger, dire à un adulte",
       "Onze classes, environ 165 élèves. À cet âge, le mot « harcèlement » est trop abstrait : on travaille "
       "sur « ça fait mal », « tous les jours », « on le dit à un adulte ». Aucun questionnaire.", VERT)

h2(pdf, "Les activités, par niveau", 40)
y = pdf.get_y() - 2
hdr = [(22, "Niveau", 7.4, True, False), (52, "Activité", 7.4, True, False),
       (16, "Durée", 7.4, True, True), (0, "Ce que la classe produit", 7.4, True, False)]
x = LM
for w, t, sz, gr, ce in [(22, "Niveau", 0, 1, 0), (54, "Activité", 0, 1, 0), (16, "Durée", 0, 1, 1), (94, "Ce que la classe produit", 0, 1, 0)]:
    cellule(pdf, x, y, w, 7, t, 7.4, True, ce, fill=VERT_C)
    x += w
y += 7
rows = [
    ("CP", "Ça fait mal, ou pas ?", "15 min", "Une liste de ce qui fait mal et de ce qui ne fait pas mal"),
    ("CP", "La forêt de mains", "10 min", "Un grand STOP fait de toutes les mains de la classe"),
    ("CP", "Les trois mots", "10 min", "Tous les jours · exprès · toujours le même, au tableau"),
    ("CE1", "Les quatre images", "15 min", "Quatre affiches : conflit, moquerie, harcèlement, violence"),
    ("CE1", "Les trois rôles", "10 min", "Le rôle de celui qui regarde, nommé et discuté"),
    ("CE1", "La scène à rejouer", "15 min", "Un enfant remplace le témoin : la classe compare"),
    ("CE1", "La comptine à gestes", "5 min", "Une phrase mémorisée, dite devant les autres classes"),
]
for i, (nv, act, dur, tr) in enumerate(rows):
    x = LM
    for w, t, sz, gr, ce in [(22, nv, 7.5, 1, 0), (54, act, 7.5, 0, 0), (16, dur, 7.5, 0, 1), (94, tr, 7.3, 0, 0)]:
        cellule(pdf, x, y, w, 11, t, sz, gr, ce, fill=(VERT_C if i % 2 == 0 else None))
        x += w
    y += 11

h2(pdf, "Ce que l’on vise, et pourquoi cela sert le questionnaire", y + 4)
para(pdf, "Un élève de CP qui n’a jamais entendu dire qu’« embêter tous les jours, exprès, toujours la même "
          "personne » n’est pas la même chose qu’« embêter une fois » répond « jamais » au questionnaire "
          "trois ans plus tard sans mentir. Les activités du cycle 2 préparent donc la compréhension des "
          "notions que la grille du CE2 suppose déjà acquises.")
puce(pdf, "Nommer", "distinguer ce qui blesse de ce qui n’est qu’un désaccord.")
puce(pdf, "Se protéger", "savoir que le recours existe : un adulte nommé, pas une consigne abstraite.")
puce(pdf, "Dire", "une phrase simple et répétable : « si c’est tous les jours, je le dis ».")
puce(pdf, "Ne pas exposer", "aucun élève ne parle de sa propre situation devant la classe. À cet âge, on "
     "parle de situations inventées ou d’une marionnette, jamais de soi.")

bloc(pdf, "Deux outils de détection à installer le jour même, et à garder toute l’année", [
    "La météo du cœur : chaque matin, l’élève place son étiquette sous un soleil, un nuage ou un orage. "
    "Dix secondes par jour. Un enfant en orage tous les lundis matin dit quelque chose que la grille ne "
    "dira jamais.",
    "Le dessin « moi et mes copains » : vingt minutes, puis l’enseignant regarde seul qui s’est dessiné "
    "isolé. Ce n’est pas une preuve, c’est un signal.",
    "Ces deux outils n’ont de valeur que si l’adulte qui les reçoit fait quelque chose. Une étiquette "
    "laissée trois semaines sous l’orage apprend à l’enfant que parler ne sert à rien."],
    pdf.get_y() + 3, fill=VERT_C, accent=VERT)
pdf.pied("Dossier de présentation · cycle 2")

# ============================== 5. CYCLE 3 ==============================
pdf.add_page()
entete(pdf, "4 · Cycle 3", "CE2, CM1 et CM2 : comprendre, agir, argumenter",
       "Sept classes, environ 170 élèves. Chaque classe mène deux ou trois activités, puis remplit la "
       "grille officielle pendant trente minutes.", BLEU)

h2(pdf, "Les activités, par niveau", 40)
y = pdf.get_y() - 2
x = LM
for w, t, ce in [(22, "Niveau", 0), (58, "Activité", 0), (16, "Durée", 1), (90, "Ce que la classe produit", 0)]:
    cellule(pdf, x, y, w, 7, t, 7.4, True, ce, fill=BLEU_C)
    x += w
y += 7
rows = [
    ("CE2", "Les 4 visages", "25 min", "16 situations triées en 4 familles, tableau affiché"),
    ("CE2", "La feuille froissée", "10 min", "L’image des traces que laissent les mots"),
    ("CE2", "L’affiche de la classe", "25 min", "Une affiche par classe, exposée dans le couloir"),
    ("CM1", "Le thermomètre", "20 min", "Les trois critères : répétition, intention, rapport de force"),
    ("CM1", "Le plan du témoin", "25 min", "Ce que je peux dire, à qui, et ce que je ne fais pas"),
    ("CM1", "Le mur des mots", "15 min", "Cinq mots par classe sur le rouleau collectif"),
    ("CM2", "Débat mouvant", "25 min", "Huit affirmations départagées, trois engagements écrits"),
    ("CM2", "Théâtre-forum", "30 min", "Trois saynètes, un joker, des solutions trouvées"),
    ("CM2", "Les ambassadeurs", "15 min", "Deux élèves par classe désignés et briefés"),
]
for i, (nv, act, dur, tr) in enumerate(rows):
    x = LM
    for w, t, sz, gr, ce in [(22, nv, 7.5, 1, 0), (58, act, 7.5, 0, 0), (16, dur, 7.5, 0, 1), (90, tr, 7.3, 0, 0)]:
        cellule(pdf, x, y, w, 10.6, t, sz, gr, ce, fill=(BLEU_C if i % 2 == 0 else None))
        x += w
    y += 10.6

h2(pdf, "Puis le questionnaire, dans la même séance", y + 4)
para(pdf, "Trente minutes, sur papier, après un retour au calme. Le professeur lit la mention informative "
          "figurant au verso de la grille, explique les quatre modalités de réponse, laisse le temps "
          "nécessaire, et ramasse lui-même les copies. Aucune activité ne se déroule pendant la passation.")
puce(pdf, "Après l’explication, avant l’activité créative", "c’est l’ordre qui donne les réponses les plus "
     "fiables : après une séance émotionnelle, les élèves répondent moins justement ; après une activité "
     "créative, ils sont dispersés.")
puce(pdf, "Le double niveau CE2/CM1", "suit le menu CE2, accessible aux deux ; les CM1 enchaînent sur le "
     "thermomètre. Le double niveau CM1/CM2 suit le menu CM2.")

bloc(pdf, "Ce que l’on vise au cycle 3, et qui ne s’acquiert pas en une séance", [
    "Comprendre que le harcèlement se définit par trois critères cumulés, et pas par la gravité d’un "
    "geste isolé : c’est ce que le thermomètre installe.",
    "Passer du statut de témoin à celui d’acteur : les trois rôles et le théâtre-forum y travaillent, "
    "parce que c’est le groupe des témoins qui fait cesser ou durer la situation.",
    "Argumenter sans disqualifier l’autre : le débat mouvant installe la controverse réglée, qui est "
    "aussi un objectif d’EMC."],
    pdf.get_y() + 3, fill=BLEU_C, accent=BLEU)
pdf.pied("Dossier de présentation · cycle 3")

# ============================== 6. LE QUESTIONNAIRE ==============================
pdf.add_page()
entete(pdf, "5 · L’enquête", "Ce que mesure la grille, et ce que l’outil en fait",
       "La grille officielle n’est pas modifiée. Ce qui est ajouté, c’est le calcul et la lecture des "
       "résultats, selon la table de croisement du guide de passation.", IND)

h2(pdf, "Les trois indices", 40)
y = pdf.get_y() - 2
x = LM
for w, t, ce in [(22, "Indice", 0), (104, "Ce qu’il compte", 0), (60, "Plage", 0)]:
    cellule(pdf, x, y, w, 7, t, 7.4, True, ce, fill=IND_C)
    x += w
y += 7
for i, (ind, txt, plage) in enumerate([
        ("A", "les réponses 3 ou 4 aux questions 2 à 8 : les atteintes subies", "0 à 7"),
        ("B", "les réponses 3 ou 4 aux questions 11 à 20 : les atteintes répétées", "0 à 10"),
        ("C", "les réponses 2, 3 ou 4 aux questions 21 à 24 : les atteintes graves", "0 à 4")]):
    x = LM
    for w, t, sz, gr, ce in [(22, ind, 8, 1, 1), (104, txt, 7.4, 0, 0), (60, plage, 7.4, 0, 1)]:
        cellule(pdf, x, y, w, 10, t, sz, gr, ce, fill=(IND_C if i % 2 == 0 else None))
        x += w
    y += 10

h2(pdf, "Puis la table de croisement : A croisé avec B + C", y + 4)
y = pdf.get_y() - 2
w1, w2 = 34, 38
cellule(pdf, LM, y, w1, 9, "Total A  /  B + C", 7, True, True, fill=IND_C)
for j, c in enumerate(["0", "1 à 4", "5 à 7", "8 et +"]):
    cellule(pdf, LM + w1 + j * w2, y, w2, 9, c, 7.4, True, True, fill=IND_C)
y += 9
grille = [
    ("0", ["", "", "surv", "harc"]),
    ("1 à 2", ["", "", "surv", "harc"]),
    ("3 à 4", ["surv", "surv", "surv", "harc"]),
    ("5 et +", ["harc", "harc", "harc", "harc"]),
]
for i, (a, cases) in enumerate(grille):
    cellule(pdf, LM, y, w1, 9, a, 7.4, True, True)
    for j, c in enumerate(cases):
        if c == "harc":
            cellule(pdf, LM + w1 + j * w2, y, w2, 9, "HARCÈLEMENT", 7, True, True, fill=ROUGE_C)
        elif c == "surv":
            cellule(pdf, LM + w1 + j * w2, y, w2, 9, "à surveiller", 7, True, True, fill=AMBRE_C)
        else:
            cellule(pdf, LM + w1 + j * w2, y, w2, 9, "rien", 7, False, True)
    y += 9

pdf.set_y(y + 3)
para(pdf, "Repères nationaux 2025 : environ 3 % des élèves en situation de harcèlement, 13 % en zone à "
          "surveiller. Ces repères servent à situer une école, pas à la juger.", size=8.2, color=GREY)

h2(pdf, "Exemple de lecture, de bout en bout", pdf.get_y() + 2)
para(pdf, "Un élève répond « souvent » aux questions 3, 7 et 8, et « très souvent » à la question 2 : "
          "total A = 4. Il déclare six atteintes répétées aux questions 11 à 20 : total B = 6 ; aucune "
          "atteinte grave : total C = 0, soit B + C = 6. Ligne « 3 à 4 », colonne « 5 à 7 » : zone "
          "« à surveiller ». La souffrance est réelle et les faits sont répétés ; l’élève doit être revu, "
          "même si la situation n’est pas un harcèlement au sens de la grille.")

bloc(pdf, "Ce que l’outil produit à partir de ces chiffres", [
    "Une vue d’ensemble : nombre d’élèves, taux de participation, comparaison aux repères nationaux.",
    "Un tableau par classe, puis un tableau par niveau (CE2, CE2/CM1, CM1, CM1/CM2, CM2).",
    "Une liste nominative d’élèves à recevoir, avec les faits déclarés et les atteintes graves distinguées.",
    "Un rapport imprimable de cinq pages, et une synthèse d’une page pour la circonscription.",
    "Un point de méthode : l’indice ne dit pas qui. Le nom vient du questionnaire papier, que le "
    "professeur a ramassé et conservé."],
    pdf.get_y() + 3, fill=IND_C, accent=IND)

bloc(pdf, "Les limites du questionnaire, à connaître avant de lire les chiffres", [
    "Il interroge l’élève sur ce qu’il subit, jamais sur ce qu’il fait : il ne mesure pas les auteurs et "
    "ne permet pas de les identifier. C’est le papier, et l’entretien, qui le permettent.",
    "Un taux bas ne prouve pas l’absence de harcèlement. Il peut signaler des élèves qui ne se sentent pas "
    "autorisés à répondre, ou qui ne reconnaissent pas les faits comme du harcèlement.",
    "Il ne dit rien du climat de classe ni de la qualité des relations entre adultes et élèves.",
    "Il photographie une période, pas une année : c’est pourquoi il doit être repassé chaque année, avec "
    "le même outil, pour que la comparaison ait un sens."],
    pdf.get_y() + 4, fill=(248, 249, 252))
pdf.pied("Dossier de présentation · l’enquête")

# ============================== 7. CADRE ==============================
pdf.add_page()
entete(pdf, "6 · Cadre et conformité", "Textes, données personnelles, droit à l’image",
       "Ce que le dispositif respecte, ce qu’il n’altère pas, et ce qu’il ne fait pas.")

h2(pdf, "Les textes dans lesquels il s’inscrit", 40)
for t in ["La journée nationale de lutte contre le harcèlement, fixée au premier jeudi de novembre.",
          "Le guide de passation de la grille d’auto-évaluation 2026-2027, qui fixe la période, le "
          "déroulé et les conditions de recueil.",
          "Le programme pHARe et son dispositif de labellisation, qui demande des actions tracées.",
          "Le protocole national de traitement des faits de harcèlement, qui reste le seul cadre de "
          "traitement des situations individuelles."]:
    puce(pdf, t)

h2(pdf, "Ce qui n’est pas modifié")
para(pdf, "Les 24 questions et les 9 questions de contexte sont reproduites mot pour mot, dans le même "
          "ordre, avec la même échelle de réponse et les mêmes règles de comptage. La table de croisement "
          "est celle du guide. Aucun item n’est ajouté, retiré ou reformulé dans le corps de la grille.")

h2(pdf, "Les deux seuls ajouts, et pourquoi ils sont assumés")
puce(pdf, "La lecture audio de chaque question", "pour les élèves non lecteurs. Elle ne change pas le "
     "texte, elle le dit à voix haute.")
puce(pdf, "Une reformulation « en clair » sous le texte officiel", "en français simple, jamais à la place "
     "du texte officiel. Elle vise les élèves allophones et les élèves en grande difficulté de lecture, "
     "nombreux dans l’école. C’est un choix pédagogique explicite, à signaler si les résultats sont "
     "comparés d’une école à l’autre.")

h2(pdf, "Les données personnelles")
y = pdf.get_y()
puce(pdf, "Aucune donnée ne quitte l’appareil", "l’application n’envoie rien sur Internet : il n’existe "
     "ni serveur, ni base de données académique, ni compte. Chaque poste conserve ses réponses dans le "
     "navigateur.")
puce(pdf, "La consolidation se fait par fichiers", "chaque classe exporte un fichier, réuni sur un poste "
     "de référence. La fusion écarte les doublons.")
puce(pdf, "Les prénoms restent sur les postes de passation", "l’export peut être fait sans prénom : le "
     "traitement statistique n’en a pas besoin, seule la liste des élèves à recevoir en a besoin, et elle "
     "reste interne à l’école.")
puce(pdf, "Conservation et destruction", "les fichiers consolidés doivent être conservés le temps de "
     "l’exploitation, puis détruits. Cette durée doit être fixée par l’école et écrite noir sur blanc : "
     "c’est la seule pièce que le dispositif ne peut pas fournir à votre place.")

h2(pdf, "Le droit à l’image, si l’école candidate au prix")
para(pdf, "Toute image d’élève identifiable diffusée hors de l’école exige une autorisation écrite des "
          "parents, mentionnant la diffusion et son support. Deux précautions simples évitent le problème : "
          "filmer de dos ou en amorce, et privilégier les mains, les objets, les dessins et les "
          "silhouettes. Les productions collectives — affiches, mur de mots, mains découpées — ne "
          "nécessitent aucune autorisation.")

bloc(pdf, "Ce que le dispositif ne fait pas", [
    "Il ne modifie pas le protocole : la grille est remplie sur papier, pendant les heures banalisées, "
    "sous la responsabilité du professeur de la classe.",
    "Il ne se substitue ni à l’entretien, ni au signalement, ni à l’équipe ressource : les situations "
    "individuelles suivent le circuit habituel.",
    "Il ne compare pas les écoles entre elles : il n’existe pas de collecte de circonscription cette "
    "année, et l’agrégation n’est pas prévue."],
    pdf.get_y() + 3, fill=(248, 249, 252))
pdf.pied("Dossier de présentation · cadre et conformité")

# ============================== 8. ORGANISER ==============================
pdf.add_page()
entete(pdf, "7 · Mise en œuvre", "Organiser la journée dans une école de 18 classes",
       "Cinq CP, un CP/CE1, cinq CE1, deux CE2, un CE2/CM1, deux CM1, un CM1/CM2, un CM2 : environ 335 élèves, dont "
       "sept classes passent le questionnaire.")

h2(pdf, "Qui fait quoi", 40)
y = pdf.get_y() - 2
x = LM
for w, t, ce in [(24, "Niveau", 0), (12, "Nb", 1), (100, "Ce que fait la classe", 0), (50, "Durée", 1)]:
    cellule(pdf, x, y, w, 7, t, 7.4, True, ce, fill=IND_C)
    x += w
y += 7
lignes = [("CP", "5", "Ça fait mal ou pas ? + forêt de mains", "45 min"),
          ("CP/CE1", "1", "Menu CP, puis les quatre images pour les CE1", "45 min"),
          ("CE1", "5", "Les quatre images + les trois rôles + la comptine", "50 min"),
          ("CE2", "2", "Les 4 visages + feuille froissée + affiche", "45 min + 30"),
          ("CE2/CM1", "1", "Menu CE2, puis thermomètre pour les CM1", "45 min + 30"),
          ("CM1", "2", "Thermomètre + plan du témoin + mur des mots", "45 min + 30"),
          ("CM1/CM2", "1", "Menu CM2", "50 min + 30"),
          ("CM2", "1", "Débat mouvant + théâtre-forum + ambassadeurs", "50 min + 30")]
for i, (a, b, c, d) in enumerate(lignes):
    x = LM
    for w, t, sz, gr, ce in [(24, a, 7.5, 1, 0), (12, b, 7.5, 0, 1), (100, c, 7.3, 0, 0), (50, d, 7.4, 0, 1)]:
        cellule(pdf, x, y, w, 9, t, sz, gr, ce, fill=(IND_C if i % 2 == 0 else None))
        x += w
    y += 9

h2(pdf, "Trois points de vigilance propres à une école de cette taille", y + 4)
puce(pdf, "Les circulations", "dix-huit classes qui changent de salle en même temps, c’est le premier "
     "risque de la journée. Un seul niveau circule à la fois, et les CP restent dans leur classe.")
puce(pdf, "Les grands et les petits dans la même cour", "plus longtemps que d’habitude, ce jour-là. "
     "Renforcer la présence adulte aux récréations, sans l’annoncer.")
puce(pdf, "Une seule parole publique", "à dix-huit classes, il y aura une ou deux confidences. Prévoir un "
     "adulte disponible et un lieu pour écouter, sinon les élèves parleront dans le couloir.")

h2(pdf, "Le rituel de 10 h — ce qui fait tenir l’école ensemble")
for t in ["La même lecture courte dans toutes les classes, à la même heure. Cinq lignes, lues par le "
          "maître, jamais par un élève.",
          "Chaque classe choisit trois mots et les écrit sur une bande. Les dix-huit bandes sont "
          "accrochées ensemble dans le hall : le mur de l’école est fait de dix-huit classes.",
          "Les CP et les CE1 récitent leur comptine pendant que les autres accrochent : c’est le seul "
          "moment où toute l’école regarde la même chose.",
          "Une photo à 10 h 30, un seul appareil, un seul adulte."]:
    puce(pdf, t)

bloc(pdf, "Le rôle de la personne ressource, et ce qu’elle ne peut pas faire", [
    "Avant : vingt minutes en conseil des maîtres, dix-huit enveloppes préparées, aucune formation.",
    "Le jour même : elle circule, elle ne remplace personne, elle prend trois photos et récupère les "
    "traces.",
    "Après : elle rassemble les affiches et le mur, consolide les sept fichiers, et écrit les cinq lignes "
    "du bilan.",
    "Ce qui décide de la réussite n’est pas la qualité de l’activité : c’est que chaque professeur ait, "
    "sur son bureau, une fiche qui tient debout toute seule."],
    pdf.get_y() + 3, fill=IND_C, accent=IND)
pdf.pied("Dossier de présentation · mise en œuvre")

# ============================== 9. APRES ==============================
pdf.add_page()
entete(pdf, "8 · Après la journée", "Saisir, consolider, rapporter",
       "C’est l’étape qui n’existait pas les années précédentes. Elle prend trente minutes par classe et "
       "une heure pour l’école.")

h2(pdf, "Les quatre temps", 40)
etapes = [
    ("1. Saisir", "Chaque professeur recopie sa classe dans l’application, au clavier : les touches 1 à 4 "
     "remplissent une ligne et passent à la suivante, Entrée enregistre. Une minute par questionnaire, "
     "trente minutes pour une classe de 25. La classe est choisie une seule fois."),
    ("2. Exporter", "Espace adulte, onglet Données, « Sauvegarde complète ». Le fichier est renommé avec "
     "le nom de la classe (CM1-B.json). Chaque professeur transmet son fichier à la direction : sept "
     "fichiers, sept classes."),
    ("3. Consolider", "Sur un poste qui n’a pas servi à la saisie, on importe les sept fichiers. La fusion "
     "écarte les doublons. L’onglet Données doit afficher sept postes : c’est le seul contrôle qui révèle "
     "une classe oubliée."),
    ("4. Renseigner et rapporter", "Les effectifs des sept classes sont saisis dans Réglages : ce sont eux "
     "qui donnent le taux de participation. Le rapport de cinq pages et la synthèse d’une page "
     "s’impriment directement."),
]
y = pdf.get_y() - 2
for t, d in etapes:
    pdf.set_font("D", "B", 8.8)
    pdf.set_text_color(*IND)
    pdf.set_xy(LM, y)
    pdf.cell(0, 5, t)
    y += 5.2
    pdf.set_font("D", "", 8.5)
    pdf.set_text_color(*INK)
    pdf.set_y(y)
    pdf.set_x(LM)
    pdf.multi_cell(W, 4.6, d, align="L")
    y = pdf.get_y() + 3

bloc(pdf, "Les trois pièges de cette étape", [
    "Un poste personnalisé : si la liste des classes a été modifiée sur une tablette avant la mise à jour, "
    "elle n’est pas remplacée automatiquement. Vérifier une fois, dans Réglages.",
    "L’historique du navigateur vidé avant l’export : tout est perdu, sans recours. Exporter dès la fin de "
    "la saisie, ne jamais attendre.",
    "La classe oubliée : rien ne le signale dans les résultats. La fiche de suivi, avec une ligne par "
    "classe et une case par étape, est la seule protection."],
    y + 2, fill=ROUGE_C, accent=ROUGE)
pdf.pied("Dossier de présentation · après la journée")

# ============================== 10. RESTITUTION ==============================
pdf.add_page()
entete(pdf, "9 · Restitution et labellisation", "Rendre les résultats utiles, et documenter la démarche",
       "Une enquête qui n’est pas restituée ne produit aucun effet, même si ses chiffres sont exacts.")

h2(pdf, "Le conseil des maîtres, dans cet ordre", 40)
for t in ["Les résultats de l’école : combien d’élèves, quelle comparaison aux repères nationaux. "
          "Présenter les chiffres, pas les noms.",
          "Les résultats par niveau : ce que disent les CE2, les CM1, les CM2 — c’est là que se voient les "
          "besoins de reprise.",
          "Les thèmes qui ressortent des questions de contexte : c’est ce qui détermine les séances de "
          "l’année, pas le chiffre global.",
          "Le circuit des situations individuelles : qui reçoit, qui suit, dans quel délai. À décider en "
          "séance, pas après."]:
    puce(pdf, t)

h2(pdf, "Les familles")
para(pdf, "Un courrier court, en décembre : la journée a eu lieu, voici ce que l’école a fait, voici ce "
          "qu’elle a retenu, voici où l’on s’adresse. Ne pas communiquer de chiffres par classe — un "
          "effectif de trois élèves dans une classe de 25 permet d’identifier les enfants.")

h2(pdf, "Les élèves à recevoir")
para(pdf, "La liste produite par l’application est nominative. Elle ne circule pas : elle est remise à la "
          "direction et à l’équipe ressource, et le circuit est celui du protocole national. Un entretien "
          "n’est pas une sanction : il sert à entendre, à vérifier, et à décider d’une suite.")

h2(pdf, "Les quatre axes de la labellisation niveau 1")
y = pdf.get_y() - 2
x = LM
for w, t, ce in [(46, "Axe", 0), (86, "Ce que le dispositif apporte", 0), (54, "La pièce à joindre", 0)]:
    cellule(pdf, x, y, w, 7, t, 7.4, True, ce, fill=IND_C)
    x += w
y += 7
axes = [
    ("1 · S’engager", "Une action commune aux 18 classes, à une date unique", "Les photos et le mur du hall"),
    ("2 · Prévenir", "Des séances par niveau, avant le questionnaire", "Les 18 affiches, les fiches élèves"),
    ("3 · Former", "Un kit qui ne demande ni formation ni matériel", "Les fiches animateur, les enveloppes"),
    ("4 · Prendre en charge", "Une conduite à tenir écrite pour l’adulte", "La fiche adulte, la liste des élèves"),
]
for i, (a, b, c) in enumerate(axes):
    x = LM
    for w, t, sz, gr, ce in [(46, a, 7.4, 1, 0), (86, b, 7.3, 0, 0), (54, c, 7.3, 0, 0)]:
        cellule(pdf, x, y, w, 11, t, sz, gr, ce, fill=(IND_C if i % 2 == 0 else None))
        x += w
    y += 11

bloc(pdf, "Ce que l’enquête apporte au dossier, et que rien d’autre ne remplace", [
    "Un état des lieux daté et chiffré, avant les actions : c’est ce qui distingue un projet d’une "
    "intention.",
    "Une mesure de départ, qui permet de recommencer l’an prochain et de comparer. Sans mesure initiale, "
    "aucune action de prévention ne peut être évaluée.",
    "La preuve que les élèves ont été entendus : la grille remplie par 170 élèves est une pièce plus "
    "solide qu’un compte rendu de réunion."],
    y + 3, fill=VERT_C, accent=VERT)
pdf.pied("Dossier de présentation · restitution et labellisation")

# ============================== 11. LE PRIX ==============================
pdf.add_page()
entete(pdf, "10 · Le prix Non au harcèlement", "Candidater sans ajouter un projet au projet",
       "Deux catégories, l’affiche et la vidéo. Vérifier le règlement de l’année avant de produire : "
       "catégories, dates et formats changent.", AMBRE)

h2(pdf, "Les trois pièges qui éliminent une candidature", 40)
puce(pdf, "La musique commerciale", "une vidéo avec une chanson connue est disqualifiée, même très "
     "réussie. Musique libre de droits, ou aucune musique, ou les voix des élèves.")
puce(pdf, "Le droit à l’image", "autorisation écrite des parents pour toute image d’élève identifiable, "
     "mentionnant la diffusion. Filmer de dos, ou les mains seulement.")
puce(pdf, "Le générique absent", "les noms des élèves, de la classe et de l’école doivent apparaître.")

h2(pdf, "Quatre idées d’affiche")
for t in ["« Il manque quelqu’un » — trente silhouettes, une seule absente. Personne ne l’a vue partir.",
          "« Une phrase, quatre langues » — Arrête, en français, en shimaoré, en kibushi et en arabe, puis : "
          "on a tous compris, pourquoi personne n’a rien dit ?",
          "« Le sac qu’on ne voit pas » — un cartable dont chaque mot blessant pend comme une étiquette.",
          "« Avant / après » — la même cour à cinq minutes d’écart, une silhouette en moins."]:
    puce(pdf, t)

h2(pdf, "Quatre idées de vidéo, une minute, un téléphone")
for t in ["Le téléphone posé — les notifications arrivent, une main le retourne face contre table, le "
          "bruit continue. Aucun visage.",
          "La chaîne des mots — une phrase chuchotée par vingt élèves filmés de dos, elle arrive déformée.",
          "Le stop-motion de Post-it — des mots qui se déplacent image par image : « c’était pour rire », "
          "« c’était tous les jours ».",
          "Le banc en accéléré — un plan fixe sur un banc de la cour, une journée entière."]:
    puce(pdf, t)

bloc(pdf, "Le levier : ne pas ajouter un projet, prolonger celui du 5 novembre", [
    "Les dix-huit affiches de classe, le mur de mots et les photos existent déjà à la fin de la journée. "
    "Photographiés et réunis, ils forment l’affiche collective de l’école : c’est la candidature, et elle "
    "ne coûte rien de plus.",
    "La vidéo, si l’école en fait une, filme la fabrication — les mains, les Post-it, le mur qui se "
    "construit. Un making-of de soixante secondes est souvent plus juste qu’une mise en scène.",
    "Un seul angle à retenir : ne pas faire une affiche sur le harcèlement, faire une affiche sur celui "
    "qui regarde. C’est ce qui distingue, et c’est ce que le kit travaille déjà."],
    pdf.get_y() + 3, fill=AMBRE_C, accent=AMBRE)
pdf.pied("Dossier de présentation · le prix")

# ============================== 12. TRANSMETTRE ==============================
pdf.add_page()
entete(pdf, "11 · Transmettre", "Comment une autre école s’en saisit en une heure",
       "Le dispositif a été construit pour être repris : l’application ne contient aucune donnée d’élève, "
       "et les documents ne dépendent pas de cette école.")

h2(pdf, "Les cinq étapes", 40)
for n, t, d in [
    ("1", "Ouvrir le lien", "sur un ordinateur, puis « Ajouter à l’écran d’accueil » sur chaque tablette. "
     "L’application fonctionne ensuite sans connexion."),
    ("2", "Adapter la liste des classes", "dans Réglages, à raison d’une ligne par classe au format "
     "« nom ; effectif ». C’est la seule configuration, et elle prend cinq minutes."),
    ("3", "Imprimer par niveau", "chaque professeur imprime les pages de son niveau depuis le kit. "
     "L’enveloppe collée sur la pochette dit exactement quoi imprimer."),
    ("4", "Faire la journée", "deux heures banalisées : activités, puis questionnaire pour le cycle 3."),
    ("5", "Saisir et consolider", "trente minutes par classe, puis fusion des fichiers sur un poste."),
]:
    pdf.set_fill_color(*IND)
    pdf.ellipse(LM, pdf.get_y() + 0.4, 5.4, 5.4, style="F")
    pdf.set_font("D", "B", 7.6)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(LM, pdf.get_y() + 1.1)
    pdf.cell(5.4, 4, n, align="C")
    yy = pdf.get_y()
    pdf.set_xy(LM + 8, yy)
    pdf.set_font("D", "B", 8.6)
    pdf.set_text_color(*INK)
    pdf.cell(0, 5, t)
    pdf.set_xy(LM + 8, yy + 5)
    pdf.set_font("D", "", 8.4)
    pdf.multi_cell(W - 8, 4.5, d, align="L")
    pdf.set_y(max(pdf.get_y(), yy + 10) + 1.6)

h2(pdf, "Ce qui est générique, ce qu’il faut adapter")
y = pdf.get_y() - 2
x = LM
for w, t, ce in [(88, "Générique : rien à changer", 0), (98, "À adapter en une heure", 0)]:
    cellule(pdf, x, y, w, 7, t, 7.4, True, ce, fill=VERT_C)
    x += w
y += 7
gauche = ["L’application et ses 24 questions", "Les 9 activités du cycle 2 et du cycle 3",
          "Les fiches animateur", "Le protocole et la fiche de suivi", "Les enveloppes (le nom change)"]
droite = ["Le nom de l’école sur les 3 couvertures", "La liste des classes dans Réglages",
          "Les effectifs de chaque classe", "Les noms des adultes référents (page 17)",
          "Le nom du référent harcèlement"]
hmax = 5 * 8.6
pdf.set_draw_color(*LINE)
pdf.set_line_width(0.3)
pdf.rect(LM, y, 88, hmax)
pdf.rect(LM + 88, y, 98, hmax)
pdf.set_font("D", "", 7.4)
pdf.set_text_color(*INK)
for k, g in enumerate(gauche):
    pdf.set_xy(LM + 3, y + 2.4 + k * 8.6)
    pdf.cell(84, 5, "\u2022  " + g)
for k, d in enumerate(droite):
    pdf.set_xy(LM + 91, y + 2.4 + k * 8.6)
    pdf.cell(94, 5, "\u2022  " + d)

bloc(pdf, "Ce que cela coûte, et ce qui ne se transfère pas", [
    "Temps : vingt minutes de présentation en conseil des maîtres, deux heures par classe, trente minutes "
    "de saisie par classe. Environ quatre heures par enseignant sur la période.",
    "Photocopies : environ 340 pages pour une école de 18 classes ; sous 150 avec les trois leviers "
    "(thermomètre à deux, plan du témoin recopié, cartes CP remplacées par le pouce levé).",
    "Ce qui ne se transfère pas : les données. Aucune réponse d’élève ne circule avec les documents. Une "
    "école qui reprend le dispositif repart d’une base vide, et c’est voulu."],
    y + hmax + 5, fill=IND_C, accent=IND)
pdf.pied("Dossier de présentation · transfert")

# ============================== 13. RETROPLANNING ==============================
pdf.add_page()
entete(pdf, "12 · Rétroplanning", "De la préparation au dossier de labellisation",
       "Ce que fait l’école, et quand. Les dates de la période de passation sont celles du guide.")

h2(pdf, "Le calendrier", 40)
y = pdf.get_y() - 2
x = LM
for w, t, ce in [(30, "Période", 0), (106, "Ce qui se fait", 0), (50, "Qui", 0)]:
    cellule(pdf, x, y, w, 7, t, 7.4, True, ce, fill=IND_C)
    x += w
y += 7
cal = [
    ("Sept. – oct.", "Préparation : enveloppes, impression par niveau, 20 min en conseil des maîtres",
     "Référent"),
    ("Jeudi 5 nov.", "Journée banalisée : rituel de 10 h, activités, questionnaire pour le cycle 3",
     "Toutes les classes"),
    ("5 nov. – 11 déc.", "Passation dans les classes qui ne l’ont pas faite le 5",
     "Professeurs"),
    ("Dès la fin de la saisie", "Export du fichier de classe, renommé au nom de la classe", "Professeurs"),
    ("Décembre", "Consolidation des 7 fichiers, effectifs, rapport de 5 pages", "Direction"),
    ("Décembre", "Conseil des maîtres, courrier aux familles, entretiens des élèves repérés", "Équipe"),
    ("Janvier", "Séances de reprise sur les thèmes ressortis de l’enquête", "Professeurs"),
    ("Janv. – printemps", "Dossier de labellisation niveau 1 ; candidature au prix", "Référent"),
    ("Juin", "Bilan : ce qui a changé, ce qui reste à faire, destruction des fichiers", "Équipe"),
]
for i, (a, b, c) in enumerate(cal):
    x = LM
    for w, t, sz, gr, ce in [(30, a, 7.4, 1, 0), (106, b, 7.2, 0, 0), (50, c, 7.2, 0, 0)]:
        cellule(pdf, x, y, w, 9.6, t, sz, gr, ce, fill=(IND_C if i % 2 == 0 else None))
        x += w
    y += 9.6

h2(pdf, "Les trois échéances à ne pas manquer", y + 4)
puce(pdf, "Le 11 décembre 2026", "fin de la période de passation : toutes les grilles doivent être "
     "remplies, saisies et exportées. Une classe non saisie fausse les résultats de toute l’école.")
puce(pdf, "La fin du trimestre", "le courrier aux familles et les entretiens des élèves repérés. Une "
     "enquête dont les résultats ne sont pas suivis d’effet apprend aux élèves que parler ne sert à rien.")
puce(pdf, "Le printemps", "le dépôt du dossier de labellisation et, si l’école le souhaite, la "
     "candidature au prix. Les deux s’appuient sur les mêmes pièces.")

bloc(pdf, "Ce que le dispositif ne décide pas à votre place", [
    "La durée de conservation des fichiers, et leur lieu de stockage.",
    "Le circuit exact des situations individuelles, qui relève du protocole national et de l’équipe "
    "ressource.",
    "L’opportunité d’étendre l’enquête à la circonscription, qui supposerait un code école par "
    "établissement et une agrégation : ce n’est pas prévu cette année."],
    pdf.get_y() + 3, fill=(248, 249, 252))
pdf.pied("Dossier de présentation · rétroplanning")

# ============================== 14. INVENTAIRE ==============================
pdf.add_page()
entete(pdf, "13 · Inventaire", "Les pièces du dossier, et où les trouver",
       "Tout est au même endroit, sans compte ni mot de passe. Les liens sont aussi dans le pied de page "
       "de l’application.")

h2(pdf, "Les documents", 40)
y = pdf.get_y() - 2
x = LM
for w, t, ce in [(74, "Document", 0), (16, "Pages", 1), (96, "À quoi il sert", 0)]:
    cellule(pdf, x, y, w, 7, t, 7.4, True, ce, fill=IND_C)
    x += w
y += 7
docs = [
    ("mode-emploi-non-au-harcelement.pdf", "9", "Le protocole : passation papier, saisie, consolidation"),
    ("kit-journee-5-novembre.pdf", "17", "Le kit des activités, CE2 à CM2"),
    ("kit-cycle-2.pdf", "6", "Le complément CP, CP/CE1 et CE1, plus l’organisation à 18 classes"),
    ("kit-journee-5-novembre-couleur.pdf", "19", "La version couleur, pour la présentation"),
    ("kit-journee-5-novembre-econome.pdf", "17", "La même chose, pour la photocopieuse"),
    ("enveloppes-journee-5-novembre.pdf", "9", "Les 17 fiches de pochette, à coller et distribuer"),
    ("note-aux-professeurs.pdf", "1", "La note à distribuer aux collègues"),
    ("dossier-presentation.pdf", "14", "Ce document"),
]
for i, (a, b, c) in enumerate(docs):
    x = LM
    for w, t, sz, gr, ce in [(74, a, 7.2, 0, 0), (16, b, 7.4, 0, 1), (96, c, 7.2, 0, 0)]:
        cellule(pdf, x, y, w, 8.6, t, sz, gr, ce, fill=(IND_C if i % 2 == 0 else None))
        x += w
    y += 8.6

yb = bloc(pdf, "Comment archiver ce dossier", [
    "Un dossier daté, avec la version de l’application (%s) : une version différente de celle des "
    "tablettes explique la plupart des difficultés." % VERSION,
    "Les fichiers exportés (.json) de l’année, un par classe, et le fichier consolidé.",
    "Les photos de la journée, les affiches scannées ou photographiées, et la fiche de suivi signée.",
    "Les grilles papier des sept classes enquêtées : ce sont les pièces de référence, elles ne sont pas remplacées par la saisie."],
    y + 3, fill=(248, 249, 252))

h2(pdf, "Contacts et suivi", yb + 5)
for l in ["Référent harcèlement de l’école : ..............................................................................",
          "Directeur de l’école : ......................................................................................",
          "Référent de circonscription, si le dispositif est étendu : ..............................."]:
    pdf.set_font("D", "", 8.4)
    pdf.set_text_color(*INK)
    pdf.set_x(LM)
    pdf.cell(0, 7.4, l)
    pdf.set_y(pdf.get_y() + 7.4)

yy = pdf.get_y() + 6
pdf.set_draw_color(*LINE)
pdf.set_line_width(0.4)
pdf.line(LM, yy - 3, LM + W, yy - 3)
for q, r in [
    ("Faut-il un compte, une connexion, un abonnement ?",
     "Non. L’application s’installe depuis un lien, fonctionne hors connexion, et n’envoie aucune donnée."),
    ("Peut-on l’utiliser au collège ?",
     "Non : la grille reproduite est celle du premier degré (CE2-CM2). Le second degré dispose de sa "
     "propre grille, avec d’autres seuils."),
    ("Et si un élève ne veut pas répondre ?",
     "Il rend une grille vierge. Elle compte comme non-répondant, jamais comme « rien à signaler » : "
     "c’est une distinction qui change le taux de participation."),
]:
    pdf.set_font("D", "B", 8.2)
    pdf.set_text_color(*IND)
    pdf.set_xy(LM, yy)
    pdf.cell(0, 4.8, q)
    yy += 4.9
    pdf.set_font("D", "", 8.1)
    pdf.set_text_color(*INK)
    pdf.set_xy(LM, yy)
    pdf.multi_cell(W, 4.5, r, align="L")
    yy = pdf.get_y() + 3

pdf.set_y(258)
pdf.set_font("D", "", 7.6)
pdf.set_text_color(*GREY)
pdf.set_x(LM)
pdf.multi_cell(W, 4.4, "Historique des versions de l’application : 20261027-7 (liste réelle des sept "
                       "classes concernées, 18 classes au total, double niveau CE2/CM1) · 20261027-6 (saisie "
                       "au clavier, résultats par niveau) · 20261027-4 (sept classes pré-remplies) · "
                       "20261027-1 (première version).", align="L")
pdf.pied("Dossier de présentation · inventaire")

out = "/workspace/nah/dossier-presentation.pdf"
pdf.output(out)
print("dossier:", os.path.getsize(out), "octets,", pdf.page_no(), "pages")
