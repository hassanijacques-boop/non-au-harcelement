# -*- coding: utf-8 -*-
"""Fiche de fusion — une page, à garder à côté du PC de référence."""
from fpdf import FPDF
import os

FONT = "/home/hermeswebui/.fonts/DejaVuSans.ttf"
FONTB = "/home/hermeswebui/.fonts/DejaVuSans-Bold.ttf"
VERSION = "20261027-9"

INK = (18, 22, 32)
GREY = (95, 100, 112)
LINE = (205, 210, 218)
IND = (58, 48, 176)
IND_C = (235, 236, 251)
VERT = (22, 132, 76)
VERT_C = (233, 248, 239)
ROUGE = (192, 38, 44)
ROUGE_C = (254, 236, 236)
LM = 12
W = 186


class PDF(FPDF):
    def __init__(self):
        super().__init__(format="A4")
        self.add_font("D", "", FONT)
        self.add_font("D", "B", FONTB)
        self.set_auto_page_break(False)
        self.set_margins(LM, 10, LM)


pdf = PDF()
pdf.add_page()

# ---------------------------------- BANDEAU ----------------------------------
pdf.set_fill_color(*IND)
pdf.rect(0, 0, 210, 26, style="F")
pdf.set_xy(LM, 5)
pdf.set_font("D", "", 7.4)
pdf.set_text_color(206, 209, 246)
pdf.cell(0, 4, "JOURNÉE DU 5 NOVEMBRE  ·  ENQUÊTE « NON AU HARCÈLEMENT »")
pdf.set_xy(LM, 10)
pdf.set_font("D", "B", 15)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 7, "Fusionner les sept fichiers")
pdf.set_xy(LM, 18)
pdf.set_font("D", "", 8.4)
pdf.set_text_color(216, 219, 249)
pdf.cell(0, 4.6, "À garder à côté du PC de référence  ·  cocher au fur et à mesure")

pdf.set_xy(LM, 30)
pdf.set_font("D", "", 8.4)
pdf.set_text_color(*GREY)
pdf.cell(120, 5, "École : ......................................................")
pdf.set_x(LM + 122)
pdf.cell(64, 5, "Date de la fusion : ...... / ...... / 2026")


def etape(pdf, n, titre, detail, y, col=IND):
    # case à cocher
    pdf.set_draw_color(*GREY)
    pdf.set_line_width(0.45)
    pdf.rect(LM, y + 0.9, 4.2, 4.2)
    pdf.set_font("D", "B", 8.6)
    pdf.set_text_color(*col)
    pdf.set_xy(LM + 7, y)
    pdf.cell(6, 6, str(n))
    pdf.set_xy(LM + 14, y)
    pdf.set_font("D", "B", 8.7)
    pdf.set_text_color(*INK)
    pdf.cell(0, 6, titre)
    x0 = LM + 14 + pdf.get_string_width(titre) + 1.6
    if detail:
        pdf.set_xy(x0, y)
        pdf.set_font("D", "", 8.4)
        pdf.set_text_color(*GREY)
        pdf.multi_cell(210 - LM - x0, 4.5, detail, align="L")
        return max(pdf.get_y(), y + 5.6)
    return y + 5.6


def sous_titre(pdf, txt, y, col=IND):
    pdf.set_y(y)
    pdf.set_font("D", "B", 9.6)
    pdf.set_text_color(*col)
    pdf.set_x(LM)
    pdf.cell(0, 5.4, txt)
    pdf.set_draw_color(*col)
    pdf.set_line_width(0.5)
    pdf.line(LM, y + 5.9, LM + W, y + 5.9)
    return y + 8.4


# ------------------------------- AVANT (3) -------------------------------
y = sous_titre(pdf, "Avant de commencer", 40)
for n, t, d in [
    (1, "Un seul PC de référence", "celui de la direction ou le vôtre, mais toujours le même."),
    (2, "Chrome, jamais en navigation privée", "en privé, les données disparaissent à la fermeture."),
    (3, "Le dossier des sept fichiers", "un .json par enseignant, reçu à la fin de sa saisie."),
]:
    y = etape(pdf, n, t, d, y) + 0.6

# ------------------------------- LA FUSION (5) -------------------------------
y = sous_titre(pdf, "La fusion, sur ce PC", y + 2.6)
for n, t, d in [
    (4, "Ouvrir le lien de l’application", "en bas de l’écran d’accueil : Version " + VERSION),
    (5, "Espace adulte, puis le code", "2026, sauf si vous l’avez changé."),
    (6, "Onglet Données", "c’est là que tout se passe."),
    (7, "Descendre sous « Postes de saisie »", "jusqu’à la zone pointillée « Fusionner plusieurs postes de saisie »."),
    (8, "Cliquer dans la zone pointillée", "la fenêtre de fichiers s’ouvre."),
    (9, "Sélectionner les sept fichiers d’un coup", "Ctrl + clic sur chacun, puis « Ouvrir »."),
    (10, "Lire le message de fin", "« X ajouté(s), Y doublon(s) ignoré(s) » : les doublons sont normaux."),
]:
    y = etape(pdf, n, t, d, y) + 0.6

# --------------------------- LES TROIS CONTROLES ---------------------------
y = sous_titre(pdf, "Les trois contrôles — dans cet ordre", y + 2.6, VERT)
pdf.set_fill_color(*VERT_C)
pdf.rect(LM, y, W, 4, style="F")
y += 1.2
for t, d in [
    ("1. Tableau « Postes de saisie »", "sept lignes, une par enseignant, et un total « 7 poste(s) »."),
    ("2. Onglet « Par classe »", "sept lignes, une par classe, avec son nombre de questionnaires."),
    ("3. Le volume", "le total doit correspondre au nombre de grilles ramassées."),
]:
    pdf.set_xy(LM + 3, y)
    pdf.set_font("D", "B", 8.6)
    pdf.set_text_color(*INK)
    pdf.cell(54, 5, t)
    pdf.set_font("D", "", 8.4)
    pdf.set_text_color(*GREY)
    pdf.set_x(LM + 58)
    pdf.multi_cell(210 - LM - 58 - 3, 4.5, d, align="L")
    y = max(pdf.get_y(), y + 5) + 1.2

pdf.set_xy(LM, y + 0.4)
pdf.set_font("D", "", 8.2)
pdf.set_text_color(*INK)
pdf.multi_cell(W, 4.5,
    "Deux collègues ont partagé une tablette ? Le tableau n’affichera que six postes, alors que les "
    "sept classes sont bien là : dans ce cas, c’est le contrôle 2 qui fait foi.", align="L")
y = pdf.get_y() + 2

# ------------------------------- APRES (2) -------------------------------
print("AVANT Juste apres, y =", round(y,1)); y = sous_titre(pdf, "Juste après", y + 1.6); print("  ->", round(y,1))
for n, t, d in [
    (11, "Réglages → les sept effectifs", "puis « Enregistrer les réglages » : les taux se calculent."),
    (12, "Données → Sauvegarde complète (.json)", "c’est l’archive de l’école. Garder aussi les sept fichiers."),
]:
    y = etape(pdf, n, t, d, y, VERT) + 0.6; print("   etape", n, "->", round(y,1))

# ----------------------------- LES CINQ ERREURS -----------------------------
print("AVANT erreurs, y =", round(y,1)); y = sous_titre(pdf, "Les cinq erreurs qui coûtent la campagne", y + 5.4, ROUGE); print("  ->", round(y,1))
for t in ["Fusionner sur deux postes différents, ou sur une tablette.",
          "Travailler en navigation privée : tout disparaît à la fermeture.",
          "Vider l’historique de Chrome avant d’avoir exporté la sauvegarde complète.",
          "Écraser un fichier en le renommant : garder les sept originaux.",
          "Croire que la fusion se fait toute seule : c’est un geste manuel, une fois."]:
    pdf.set_x(LM + 2)
    pdf.set_font("D", "", 8.3)
    pdf.set_text_color(*INK)
    pdf.multi_cell(W - 2, 4.4, "\u2022  " + t, align="L")
    pdf.set_x(LM)
    y = pdf.get_y() + 0.4

# ------------------------- LA PHRASE A DIRE AUX AUTRES -------------------------
y = max(y + 3, 232)
pdf.set_fill_color(*IND_C)
pdf.set_draw_color(*IND)
pdf.set_line_width(0.6)
pdf.rect(LM, y, W, 40, style="DF")
pdf.set_xy(LM + 4, y + 2.6)
pdf.set_font("D", "B", 8.8)
pdf.set_text_color(*IND)
pdf.cell(0, 4.6, "À dire aux collègues, en trois phrases")
pdf.set_xy(LM + 4, y + 8.6)
pdf.set_font("D", "", 8.3)
pdf.set_text_color(*INK)
pdf.multi_cell(W - 8, 4.6,
    "Chacun exporte un fichier à la fin de sa saisie : sept fichiers, sept classes. Ces fichiers ne "
    "contiennent que les réponses des élèves, jamais les réglages — donc personne n’a d’effectif à "
    "saisir. Sur le PC de la direction, on les importe tous d’un coup : l’application écarte les "
    "doublons, l’ordre des fichiers n’a aucune importance, et on peut recommencer sans risque.",
    align="L")

pdf.set_y(-9)
pdf.set_font("D", "", 6.6)
pdf.set_text_color(*GREY)
pdf.set_x(LM)
pdf.cell(150, 4, "Fusion des sept fichiers · journée du 5 novembre 2026 · application v" + VERSION)
pdf.set_x(LM + 150)
pdf.cell(36, 4, "1", align="R")

out = "/tmp/f.pdf"
pdf.output(out)
print("fiche:", os.path.getsize(out), "octets,", pdf.page_no(), "page(s)")
