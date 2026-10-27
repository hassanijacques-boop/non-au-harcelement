# -*- coding: utf-8 -*-
"""Sept enveloppes prêtes à distribuer — une par classe."""
from fpdf import FPDF
import os

FONT = "/home/hermeswebui/.fonts/DejaVuSans.ttf"
FONTB = "/home/hermeswebui/.fonts/DejaVuSans-Bold.ttf"

INK = (20, 25, 35)
GREY = (95, 100, 110)
MGREY = (176, 181, 190)
LINE = (200, 205, 214)
LM = 12
W = 186
VERSION = "20261027-6"


class PDF(FPDF):
    def __init__(self):
        super().__init__(format="A4")
        self.add_font("D", "", FONT)
        self.add_font("D", "B", FONTB)
        self.set_auto_page_break(False)
        self.set_margins(LM, 10, LM)

    def pied(self):
        self.set_y(-9)
        self.set_font("D", "", 6.8)
        self.set_text_color(*GREY)
        self.set_x(LM)
        self.cell(150, 4, "Enveloppes de la journée du 5 novembre · à découper et à coller sur les pochettes")
        self.set_x(LM + 150)
        self.cell(36, 4, "%d" % self.page_no(), align="R")


CLASSES = [
    ("CE2 A", "CE2", 1),
    ("CE2 B", "CE2", 2),
    ("CM1 A", "CM1", 3),
    ("CM1 B", "CM1", 4),
    ("CM1 C", "CM1", 5),
    ("CM2", "CM2", 6),
    ("CM1/CM2", "CM2", 7),
]

DETAIL = {
    "CE2": {
        "imprimer": "pages 2 à 5  +  page 15",
        "dedans": [
            "1 fiche animateur (p. 2)",
            "16 cartes « situations » (p. 3 et 4) — prévoir 3 jeux, soit 6 pages",
            "4 en-têtes de familles (p. 5) — un jeu par groupe",
            "1 affiche de classe à compléter (p. 15)",
            "1 fiche adulte : pièges et contacts (p. 17) — à garder, ne pas afficher",
        ],
        "commun": "À ajouter : bandelettes du mur des alliés (p. 14), mur des mots, boîte et quiz 3018 (p. 16).",
        "duree": "45 minutes d’activités, puis 30 minutes de questionnaire.",
        "ordre": "Rituel commun (10 min)  ·  les 4 visages (25 min)  ·  la feuille froissée (10 min)  ·  "
                 "le questionnaire papier (30 min)  ·  l’affiche (25 min)  ·  clôture (10 min).",
    },
    "CM1": {
        "imprimer": "pages 6 à 8  +  page 15",
        "dedans": [
            "1 fiche animateur (p. 6)",
            "fiches élève « thermomètre » (p. 7) — une pour deux élèves",
            "fiches élève « plan du témoin » (p. 8) — une par élève",
            "1 affiche de classe à compléter (p. 15)",
            "1 fiche adulte : pièges et contacts (p. 17) — à garder, ne pas afficher",
        ],
        "commun": "À ajouter : bandelettes du mur des alliés (p. 14), mur des mots, boîte et quiz 3018 (p. 16).",
        "duree": "45 minutes d’activités, puis 30 minutes de questionnaire.",
        "ordre": "Rituel commun (10 min)  ·  le thermomètre (20 min)  ·  le plan du témoin (25 min)  ·  "
                 "le questionnaire papier (30 min)  ·  le mur des mots (15 min)  ·  clôture (10 min).",
    },
    "CM2": {
        "imprimer": "pages 9 à 12  +  page 15",
        "dedans": [
            "1 fiche animateur débat mouvant (p. 9)",
            "8 affirmations à découper + les 2 affiches D’ACCORD / PAS D’ACCORD (p. 10)",
            "3 saynètes de théâtre-forum (p. 11)",
            "règles du joker + grille d’observation (p. 12) — une grille par observateur",
            "1 affiche de classe à compléter (p. 15)",
            "1 fiche adulte : pièges et contacts (p. 17) — à garder, ne pas afficher",
        ],
        "commun": "À ajouter : bandelettes du mur des alliés (p. 14), mur des mots, boîte et quiz 3018 (p. 16).",
        "duree": "50 minutes d’activités, puis 30 minutes de questionnaire.",
        "ordre": "Rituel commun (10 min)  ·  le débat mouvant (25 min)  ·  le questionnaire papier (30 min)  ·  "
                 "le théâtre-forum (30 min)  ·  l’affiche (15 min)  ·  clôture (10 min).",
    },
}


def carte(pdf, x, y, w, h, nom, niveau, num):
    d = DETAIL[niveau]
    pdf.set_draw_color(*INK)
    pdf.set_line_width(1.0)
    pdf.rect(x, y, w, h)

    # en-tête
    pdf.set_xy(x + 5, y + 4)
    pdf.set_font("D", "", 7.2)
    pdf.set_text_color(*GREY)
    pdf.cell(60, 4, "ENVELOPPE %d sur 7" % num)
    pdf.set_xy(x + 5, y + 8)
    pdf.set_font("D", "B", 17)
    pdf.set_text_color(*INK)
    pdf.cell(90, 8, nom)
    pdf.set_xy(x + w - 52, y + 9)
    pdf.set_font("D", "", 7.6)
    pdf.set_text_color(*GREY)
    pdf.cell(47, 4, "menu " + niveau, align="R")
    # case préparée
    pdf.set_draw_color(*MGREY)
    pdf.set_line_width(0.4)
    pdf.rect(x + w - 52, y + 3.6, 4.6, 4.6)
    pdf.set_xy(x + w - 46, y + 3)
    pdf.set_font("D", "", 6.8)
    pdf.cell(0, 4, "préparée")
    pdf.set_draw_color(*INK)
    pdf.set_line_width(0.7)
    pdf.line(x + 5, y + 18, x + w - 5, y + 18)

    # à imprimer
    pdf.set_xy(x + 5, y + 21)
    pdf.set_font("D", "B", 8.4)
    pdf.cell(0, 4.4, "Ce que tu imprimes : " + d["imprimer"])
    pdf.set_xy(x + 5, y + 26.4)
    pdf.set_font("D", "", 7.4)
    pdf.set_text_color(*GREY)
    pdf.cell(0, 4.2, "À télécharger ici :  hassanijacques-boop.github.io/non-au-harcelement/kit-journee-5-novembre.pdf")
    pdf.set_text_color(*INK)

    # ce qu'il y a dedans
    yy = y + 33
    pdf.set_xy(x + 5, yy)
    pdf.set_font("D", "B", 8.2)
    pdf.cell(0, 4.2, "Ce qu’il y a dans l’enveloppe")
    yy += 5.4
    pdf.set_font("D", "", 7.5)
    for it in d["dedans"]:
        pdf.set_xy(x + 7, yy)
        pdf.multi_cell(w - 14, 4.1, "\u2022  " + it, align="L")
        yy = pdf.get_y() + 0.4

    # ordre de la séance
    yo = y + 70
    pdf.set_xy(x + 5, yo)
    pdf.set_font("D", "B", 8.2)
    pdf.cell(0, 4.2, "L’ordre de la séance")
    pdf.set_xy(x + 5, yo + 5.2)
    pdf.set_font("D", "", 7.5)
    pdf.multi_cell(w - 10, 4.2, d["ordre"], align="L")

    # bas de carte
    yy = y + h - 26
    pdf.set_draw_color(*LINE)
    pdf.set_line_width(0.3)
    pdf.line(x + 5, yy - 2, x + w - 5, yy - 2)
    pdf.set_xy(x + 5, yy)
    pdf.set_font("D", "B", 7.6)
    pdf.cell(0, 4, d["duree"])
    pdf.set_xy(x + 5, yy + 4.6)
    pdf.set_font("D", "", 7.2)
    pdf.set_text_color(*GREY)
    pdf.multi_cell(w - 10, 3.9, d["commun"], align="L")
    pdf.set_xy(x + 5, y + h - 9)
    pdf.set_font("D", "", 7.2)
    pdf.set_text_color(*INK)
    pdf.cell(0, 4, "À rendre à la personne ressource : l’affiche de la classe et les traces produites.")
    pdf.set_xy(x + w - 62, y + h - 4.6)
    pdf.set_font("D", "", 6.6)
    pdf.set_text_color(*GREY)
    pdf.cell(57, 3.6, "préparée le ......../........ par ............................")


pdf = PDF()
pdf.add_page()

for i, (nom, niveau, num) in enumerate(CLASSES):
    pos = i % 2
    if pos == 0 and i:
        pdf.add_page()
    x = LM
    y = 10 if pos == 0 else 10 + 128 + 8
    carte(pdf, x, y, W, 128, nom, niveau, num)
    if pos == 1:
        pdf.pied()

pdf.pied()

out = "/workspace/nah/enveloppes-journee-5-novembre.pdf"
pdf.output(out)
print("enveloppes:", os.path.getsize(out), "octets,", pdf.page_no(), "pages")
