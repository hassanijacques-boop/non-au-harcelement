# -*- coding: utf-8 -*-
"""Note aux professeurs — une page, à distribuer aux collègues."""
from fpdf import FPDF
import os

FONT = "/home/hermeswebui/.fonts/DejaVuSans.ttf"
FONTB = "/home/hermeswebui/.fonts/DejaVuSans-Bold.ttf"
SH = "/workspace/nah"
URL = "https://hassanijacques-boop.github.io/non-au-harcelement/"
VERSION = "20261027-9"

IND = (67, 56, 202)
IND_L = (238, 242, 255)
INK = (15, 23, 42)
GREY = (90, 100, 120)
ROUGE = (190, 30, 30)
VERT = (18, 130, 65)
LINE = (222, 227, 238)
LM = 18
W = 174


class PDF(FPDF):
    def __init__(self):
        super().__init__(format="A4")
        self.add_font("D", "", FONT)
        self.add_font("D", "B", FONTB)
        self.set_auto_page_break(False)
        self.set_margins(LM, 14, LM)

    def footer(self):
        self.set_draw_color(*LINE)
        self.set_line_width(0.4)
        self.line(LM, 284, 210 - LM, 284)
        self.set_y(285)
        self.set_font("D", "", 7.0)
        self.set_text_color(*GREY)
        self.set_x(LM)
        self.cell(130, 4.6, "Enquête « Non au harcèlement » · école élémentaire CE2-CM2 · année scolaire 2026-2027")
        self.set_x(LM + 130)
        self.cell(44, 4.6, "v" + VERSION, align="R")


def para(pdf, txt, y, size=9.3, lh=5.1, color=INK):
    pdf.set_y(y)
    pdf.set_font("D", "", size)
    pdf.set_text_color(*color)
    pdf.set_x(LM)
    pdf.multi_cell(W, lh, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)
    return pdf.get_y()


def etape(pdf, n, titre, lignes, y):
    pdf.set_fill_color(*IND)
    pdf.ellipse(LM, y + 0.3, 7.4, 7.4, style="F")
    pdf.set_font("D", "B", 9.8)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(LM, y + 1.4)
    pdf.cell(7.4, 5, str(n), align="C")
    pdf.set_xy(LM + 11, y)
    pdf.set_text_color(*IND)
    pdf.set_font("D", "B", 10.1)
    pdf.cell(0, 5.4, titre)
    y += 6.6
    pdf.set_text_color(*INK)
    for l in lignes:
        pdf.set_xy(LM + 11, y)
        pdf.set_font("D", "", 9.0)
        pdf.multi_cell(W - 11, 4.85, l, align="L")
        y = pdf.get_y()
    return y + 2.4


def encadre(pdf, titre, lignes, y, bg, bord, tc, size=8.8, largeur=W - 6):
    h = 7.4
    for l in lignes:
        h += 4.75 * max(1, len(l) // 92 + (1 if len(l) % 92 else 0))
    h += 1.6
    pdf.set_fill_color(*bg)
    pdf.set_draw_color(*bord)
    pdf.set_line_width(0.5)
    pdf.rect(LM, y, W, h, style="DF")
    pdf.set_xy(LM + 3, y + 2.3)
    pdf.set_font("D", "B", 9.1)
    pdf.set_text_color(*tc)
    pdf.cell(0, 5, titre)
    yy = y + 8.0
    pdf.set_font("D", "", size)
    pdf.set_text_color(*INK)
    for l in lignes:
        pdf.set_xy(LM + 3, yy)
        pdf.multi_cell(largeur, 4.75, l, align="L")
        yy = pdf.get_y()
    return y + h


pdf = PDF()
pdf.add_page()

# ------------------------------- BANDEAU -------------------------------
pdf.set_fill_color(*IND)
pdf.rect(0, 0, 210, 32, style="F")
pdf.set_xy(LM, 6.5)
pdf.set_font("D", "B", 16.5)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 8, "Note aux professeurs")
pdf.set_xy(LM, 15)
pdf.set_font("D", "", 9.5)
pdf.cell(0, 5, "Enquête « Non au harcèlement » · grille d’auto-évaluation · année scolaire 2026-2027")
pdf.set_xy(LM, 20.8)
pdf.set_font("D", "", 8.3)
pdf.cell(0, 5, "École primaire publique La Rose · circonscription IEN Bandraboua · du CP au CM2")

# ------------------------------- INTRO -------------------------------
y = para(pdf,
         "Le 5 novembre, toute l’école participe à la journée nationale de lutte contre le harcèlement : les "
         "élèves du CE2 au CM2 remplissent la grille officielle, les CP et les CE1 mènent des activités "
         "adaptées, sans questionnaire.", 36)
y = para(pdf,
         "La passation ne change pas : la grille reste remplie sur papier. Ce qui change, c’est la suite — vos "
         "résultats sont saisis dans l’application, qui calcule les indices officiels et rédige "
         "l’interprétation. Plus de dépouillement à la main, des résultats lisibles par classe.",
         y + 1.2, color=IND)

# échéance
pdf.set_y(y + 2.4)
pdf.set_font("D", "B", 9.4)
pdf.set_text_color(*ROUGE)
pdf.set_x(LM)
pdf.cell(0, 5.2, "Tout doit être passé, saisi et exporté avant le vendredi 11 décembre 2026.")

# ------------------------------- ÉTAPES -------------------------------
pdf.set_y(y + 10.5)
pdf.set_font("D", "B", 11.1)
pdf.set_text_color(*INK)
pdf.set_x(LM)
pdf.cell(0, 6, "Ce que vous avez à faire")

y = etape(pdf, 1, "Faire passer la grille en classe", [
    "Comme d’habitude : présenter la grille, lire aux élèves la mention informative figurant au dos, "
    "expliquer les quatre réponses (Jamais, Parfois, Souvent, Très souvent), laisser remplir, ramasser "
    "les copies."], y + 16.5)

y = etape(pdf, 2, "Saisir les résultats de votre classe — 30 minutes", [
    "Ouvrir le lien ci-dessous, puis « Saisir les réponses (enseignant) ». Votre classe est déjà dans la "
    "liste : choisissez-la une seule fois, elle est mémorisée. Un élève par écran ; les touches 1 à 4 "
    "remplissent chaque ligne, Entrée enregistre et passe à l’élève suivant.",
    "Avant de commencer, vérifier en bas de l’écran d’accueil : Version " + VERSION + ". Sur une version "
    "plus ancienne, la liste des classes est fausse : fermer l’application et la rouvrir."], y)

y = etape(pdf, 3, "Exporter votre fichier et le transmettre", [
    "Espace adulte → code 2026 → onglet Données → « Sauvegarde complète (.json) ». Renommer le fichier au "
    "nom de votre classe (CM1-B.json) et le transmettre à la direction.",
    "Si vous partagez la tablette avec un collègue, exportez avant de la lui passer : sinon vos réponses "
    "partent dans son fichier."], y)

# ------------------------------- LIEN + QR -------------------------------
ybox = y + 1.5
pdf.set_fill_color(248, 250, 252)
pdf.set_draw_color(*LINE)
pdf.set_line_width(0.5)
pdf.rect(LM, ybox, W, 32, style="DF")
pdf.set_xy(LM + 4, ybox + 2.4)
pdf.set_font("D", "B", 9.4)
pdf.set_text_color(*IND)
pdf.cell(0, 5, "Le lien")
pdf.set_xy(LM + 4, ybox + 8.2)
pdf.set_font("D", "B", 9.2)
pdf.set_text_color(*INK)
pdf.cell(0, 5, "hassanijacques-boop.github.io/non-au-harcelement/")
pdf.set_xy(LM + 4, ybox + 15.0)
pdf.set_font("D", "", 8.4)
pdf.multi_cell(128, 4.5, "Code adulte : 2026   ·   rien à installer   ·   fonctionne sans connexion",
               align="L")
pdf.set_xy(LM + 4, ybox + 21.2)
pdf.set_font("D", "", 8.0)
pdf.set_text_color(*GREY)
pdf.multi_cell(128, 4.3, "Sur téléphone ou tablette : menu de Chrome → « Ajouter à l’écran d’accueil ».",
               align="L")

pdf.image(SH + "/qr-code.png", x=152, y=ybox + 3, w=26)
pdf.set_xy(146, ybox + 30.2)
pdf.set_font("D", "", 6.0)
pdf.set_text_color(*GREY)
pdf.multi_cell(38, 3.0, "à scanner", align="C")

# --------------------------- POINTS DE VIGILANCE ---------------------------
y = encadre(pdf, "Quatre points de vigilance",
            ["Conservez les grilles papier : c’est la pièce de référence, la saisie ne les remplace pas.",
             "N’attendez pas la fin de la période : une classe oubliée fausse les résultats de l’école.",
             "Ne videz pas l’historique de Chrome : cela effacerait vos réponses avant l’export.",
             "Liste incorrecte ? Espace adulte → Réglages → « Rétablir la liste des 7 classes »."],
            ybox + 35, (254, 242, 242), (254, 202, 202), ROUGE)

# ------------------------------ CE QUE VOUS RECEVEZ ------------------------------
y = encadre(pdf, "Ce que vous recevez en retour",
            ["Les résultats de votre classe, élève par élève, avec la liste des élèves à recevoir et les "
             "faits déclarés — de quoi préparer vos entretiens.",
             "Les résultats de l’école par niveau et les thèmes qui ressortent : ce n’est pas une évaluation "
             "de votre travail, ni un classement des classes, mais le point de départ des séances de l’année."],
            y + 3.5, (240, 253, 244), (187, 247, 208), VERT)

# -------------------------------- CONTACT --------------------------------
pdf.set_y(y + 4.5)
pdf.set_font("D", "", 8.7)
pdf.set_text_color(*INK)
pdf.set_x(LM)
pdf.cell(0, 5, "Une question, un problème de connexion, une situation à signaler ?")
pdf.set_y(y + 9.5)
pdf.set_x(LM)
pdf.cell(0, 5, "Contact : .....................................................................        "
               "Le protocole complet est sur le lien, page « Aide ».")

pdf.output("/workspace/nah/note-aux-professeurs.pdf")
print("note:", os.path.getsize("/workspace/nah/note-aux-professeurs.pdf"), "octets,", pdf.page_no(), "page(s)")
