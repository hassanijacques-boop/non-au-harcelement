# -*- coding: utf-8 -*-
"""Mode d'emploi PDF de l'application « Non au harcèlement » (fpdf2 + DejaVu)."""
from fpdf import FPDF
import os

FONT = "/home/hermeswebui/.fonts/DejaVuSans.ttf"
FONTB = "/home/hermeswebui/.fonts/DejaVuSans-Bold.ttf"
SH = "/workspace/nah"
URL = "https://hassanijacques-boop.github.io/non-au-harcelement/"

IND = (67, 56, 202)
IND_L = (238, 242, 255)
INK = (15, 23, 42)
GREY = (90, 100, 120)
ROUGE = (200, 30, 30)
ORANGE = (170, 75, 5)
VERT = (20, 140, 70)
LINE = (222, 227, 238)
LM = 18          # marge gauche
W = 174          # largeur utile


class PDF(FPDF):
    def __init__(self):
        super().__init__(format="A4")
        self.add_font("D", "", FONT)
        self.add_font("D", "B", FONTB)
        self.set_auto_page_break(True, margin=17)
        self.set_margins(LM, 16, LM)

    def footer(self):
        self.set_y(-13)
        self.set_font("D", "", 7.5)
        self.set_text_color(*GREY)
        self.cell(0, 6, "Non au harcèlement — enquête école élémentaire · " + URL)
        self.set_y(-13)
        self.cell(0, 6, "page %d" % self.page_no(), align="R")


def h1(pdf, txt):
    pdf.set_font("D", "B", 15)
    pdf.set_text_color(*IND)
    pdf.multi_cell(0, 8, txt, align="L")
    pdf.ln(1.5)


def h2(pdf, txt, color=INK, avant=3):
    if pdf.get_y() > 245:
        pdf.add_page()
    pdf.ln(avant)
    pdf.set_font("D", "B", 11)
    pdf.set_text_color(*color)
    pdf.set_x(LM)
    pdf.multi_cell(W, 6.2, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)
    pdf.ln(1.2)


def para(pdf, txt, size=9.4, color=INK, lh=5.3):
    pdf.set_font("D", "", size)
    pdf.set_text_color(*color)
    pdf.set_x(LM)
    pdf.multi_cell(W, lh, txt, align="L")
    pdf.set_x(LM)
    pdf.set_text_color(*INK)


def puce(pdf, titre, txt, color=IND, size=9.3):
    if pdf.get_y() > 266:
        pdf.add_page()
    contenu = ("**" + titre + "** : " + txt) if titre else txt
    pdf.set_font("D", "", size)
    pdf.set_text_color(*INK)
    pdf.set_x(LM)
    pdf.multi_cell(W, 5.3, "•  " + contenu, align="L", markdown=True)
    pdf.set_x(LM)
    pdf.ln(1.3)


def encadre(pdf, titre, lignes, bg=(255, 251, 235), bord=(253, 230, 138), tc=ORANGE, size=8.9):
    pdf.ln(1)
    # mesure
    pdf.set_font("D", "", size)
    h = 8.0
    for l in lignes:
        h += 5.0 * max(1, len(l) // 92 + (1 if len(l) % 92 else 0))
    h += 2
    y0 = pdf.get_y()
    if y0 + h > 272:
        pdf.add_page()
        y0 = pdf.get_y()
    pdf.set_fill_color(*bg)
    pdf.set_draw_color(*bord)
    pdf.set_line_width(0.5)
    pdf.rect(LM, y0, W, h, style="DF")
    pdf.set_xy(LM + 3, y0 + 2.6)
    pdf.set_font("D", "B", 9.3)
    pdf.set_text_color(*tc)
    pdf.cell(0, 5, titre)
    pdf.set_xy(LM + 3, y0 + 8.6)
    pdf.set_font("D", "", size)
    pdf.set_text_color(*INK)
    for l in lignes:
        pdf.set_x(LM + 3)
        pdf.multi_cell(W - 6, 5.0, l, align="L")
    pdf.set_y(y0 + h + 3)


def etape(pdf, num, titre, lignes):
    y = pdf.get_y()
    pdf.set_fill_color(*IND)
    pdf.ellipse(LM, y + 0.6, 7.5, 7.5, style="F")
    pdf.set_font("D", "B", 10)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(LM, y + 1.7)
    pdf.cell(7.5, 5, str(num), align="C")
    pdf.set_xy(LM + 11, y)
    pdf.set_text_color(*IND)
    pdf.set_font("D", "B", 10.3)
    pdf.cell(0, 5.5, titre)
    pdf.ln(6.6)
    pdf.set_text_color(*INK)
    for l in lignes:
        pdf.set_x(LM + 11)
        pdf.set_font("D", "", 9.2)
        pdf.multi_cell(W - 11, 5.1, l, align="L")
    pdf.ln(1.8)


pdf = PDF()

# ============================== PAGE 1 ==============================
pdf.add_page()
pdf.set_fill_color(*IND)
pdf.rect(0, 0, 210, 36, style="F")
pdf.set_xy(LM, 8.5)
pdf.set_font("D", "B", 19)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 9, "Non au harcèlement")
pdf.set_xy(LM, 18.5)
pdf.set_font("D", "", 10)
pdf.cell(0, 5, "Enquête d’auto-évaluation · école élémentaire CE2-CM2 · 2026-2027")
pdf.set_xy(LM, 24.5)
pdf.set_font("D", "", 8.5)
pdf.cell(0, 5, "Mode d’emploi — passation sur tablette, lecture des résultats, rapport")

pdf.set_y(42)
pdf.set_font("D", "B", 11)
pdf.set_text_color(*INK)
pdf.cell(0, 6, "Ouvrir l’application")
pdf.ln(7.5)
pdf.set_font("D", "", 9.3)
pdf.set_text_color(*INK)
pdf.set_x(LM)
pdf.multi_cell(108, 5.2,
    "Sur chaque tablette : ouvrir Chrome, taper l’adresse ci-dessous, ou scanner le QR code.\n"
    "Une fois la page ouverte, appuyer sur les trois points en haut à droite de Chrome puis "
    "« Ajouter à l’écran d’accueil » : l’application s’installe comme une vraie application et "
    "fonctionne ensuite sans connexion Internet.", align="L")

pdf.ln(2.5)
pdf.set_font("D", "B", 9.2)
pdf.set_text_color(*IND)
pdf.set_x(LM)
pdf.multi_cell(108, 4.8, "hassanijacques-boop.github.io/", align="L")
pdf.set_x(LM)
pdf.multi_cell(108, 4.8, "non-au-harcelement/", align="L")
pdf.ln(1)
pdf.set_font("D", "", 8.4)
pdf.set_text_color(*GREY)
pdf.set_x(LM)
pdf.multi_cell(108, 4.6, "Aucun compte, aucun magasin d’applications, aucun paiement.", align="L")

pdf.image(SH + "/qr-code.png", x=138, y=44, w=36)
pdf.set_xy(138, 81)
pdf.set_font("D", "", 7.4)
pdf.set_text_color(*GREY)
pdf.multi_cell(36, 4.2, "À scanner avec l’appareil photo de la tablette", align="C")

pdf.set_y(105)
h1(pdf, "À quoi ça sert")
para(pdf,
     "Chaque élève répond aux 24 questions de la grille officielle, puis aux 9 questions complémentaires. "
     "L’application calcule elle-même les trois indices officiels, situe chaque élève dans la table de "
     "croisement, rédige l’interprétation et produit le rapport à imprimer pour la circonscription. "
     "Les années précédentes, les grilles étaient remplies mais les résultats n’étaient pas interprétés : "
     "ici, l’interprétation est automatique.")
pdf.ln(1.5)

h2(pdf, "Ce que produit l’application", avant=1)
puce(pdf, "Un résultat par élève", "« harcèlement », « à surveiller » ou « pas de difficulté », selon la table officielle.")
puce(pdf, "Des résultats par classe et par question", "pour savoir quels faits reviennent le plus : moqueries, mise à l’écart, cantine, cyberharcèlement…")
puce(pdf, "Une interprétation rédigée", "comparée aux repères nationaux du baromètre 2025 (3 % en harcèlement, 13 % à surveiller).")
puce(pdf, "Un rapport A4", "avec les tableaux, les thèmes prioritaires, les actions retenues et la contribution au dossier de labellisation.")
puce(pdf, "Une synthèse à copier", "pour le courrier ou le mail à l’inspecteur de circonscription.")

encadre(pdf, "Code d’accès adulte : 2026",
        ["Les résultats sont protégés par un code à 4 chiffres, pour que les élèves ne puissent pas les ouvrir.",
         "Pour le changer : Espace adulte → onglet Réglages → « Code d’accès adulte »."],
        bg=IND_L, bord=(199, 210, 254), tc=IND)

pdf.set_y(243)
h2(pdf, "Le déroulé de l’opération", avant=0)
pdf.set_font("D", "", 8.8)
pdf.set_draw_color(*LINE)
blocs = [("Novembre 2026", "passation dans toutes les classes, du 5 novembre au 11 décembre"),
         ("Décembre 2026", "dépouillement, conseil des maîtres, restitution aux familles"),
         ("Janvier-mai 2027", "actions ciblées sur les thèmes sortis en tête"),
         ("Juin 2027", "seconde passation pour mesurer l’évolution")]
x = LM
for t, d in blocs:
    pdf.set_xy(x, 254)
    pdf.set_font("D", "B", 8.4)
    pdf.set_text_color(*IND)
    pdf.multi_cell(41, 4.2, t, align="L")
    pdf.set_x(x)
    pdf.set_font("D", "", 8.2)
    pdf.set_text_color(*INK)
    pdf.multi_cell(41, 4.2, d, align="L")
    pdf.set_draw_color(*IND)
    pdf.set_line_width(0.8)
    pdf.line(x, 252, x, 253.2)
    x += 43.5

# ============================== PAGE 2 ==============================
pdf.add_page()
h1(pdf, "Pendant la séance, pas à pas")
para(pdf, "Deux heures sont banalisées entre le jeudi 5 novembre et le vendredi 11 décembre 2026. "
          "Compter 10 à 15 minutes de questionnaire par élève.", color=GREY, size=9)
pdf.ln(1.5)

etape(pdf, 1, "Expliquer avant de lancer", [
    "Rappeler ce qu’est le harcèlement, que les réponses ne sont pas obligatoires, que le prénom n’est "
    "pas demandé et que les adultes sont là pour aider."])
etape(pdf, 2, "Chaque élève commence", [
    "Bouton « Je réponds au questionnaire ». L’élève indique sa classe, fille ou garçon, son année de naissance.",
    "Une question par écran. Le bouton « Écouter la question » la lit à voix haute : à utiliser sans compter, "
    "c’est ce qui rend le questionnaire accessible aux élèves qui lisent difficilement.",
    "La ligne bleue « En clair » reformule la question en français simple. Le texte officiel reste affiché "
    "au-dessus : la question n’est jamais modifiée."])
etape(pdf, 3, "À la fin de chaque élève", [
    "Écran de remerciement avec le numéro 3018. L’élève appuie sur « Élève suivant » : la tablette est "
    "prête pour le camarade suivant."])
etape(pdf, 4, "Surveiller les réactions", [
    "Un élève qui pleure, qui se bloque ou qui reste silencieux : c’est déjà une information. Prévoir un "
    "adulte disponible pour l’écouter tout de suite, sans attendre la fin de la séance."])

y = pdf.get_y() + 2
pdf.image(SH + "/shots/crop-question.png", x=LM, y=y, w=68)
pdf.set_xy(LM + 74, y + 1)
pdf.set_font("D", "B", 9.8)
pdf.set_text_color(*IND)
pdf.cell(0, 5, "L’écran de question")
pdf.ln(6)
pdf.set_x(LM + 74)
pdf.set_font("D", "", 8.9)
pdf.set_text_color(*INK)
pdf.multi_cell(W - 74, 5.0,
    "La reformulation « En clair » est un ajout, placé sous le texte officiel. Elle sert aux élèves en "
    "difficulté de lecture et aux élèves allophones, sans changer le sens de la question.", align="L")
pdf.ln(2.4)
pdf.set_x(LM + 74)
pdf.multi_cell(W - 74, 5.0,
    "Les quatre réponses sont toujours dans le même ordre et de la même couleur : vert, jaune, orange, "
    "rouge. Un élève se trompe rarement.", align="L")
pdf.ln(2.4)
pdf.set_x(LM + 74)
pdf.multi_cell(W - 74, 5.0,
    "« Je préfère ne pas répondre » laisse la question vide : elle n’est comptée ni pour ni contre l’élève.",
    align="L")

pdf.set_y(max(pdf.get_y(), y + 92) + 4)
encadre(pdf, "À dire aux élèves avant de ranger les tablettes",
        ["La violence, sous toutes ses formes, est inacceptable à l’école comme en dehors. Une moquerie, "
         "une insulte, un coup ne sont jamais « pour rire ».",
         "Tous les adultes de l’école sont disponibles pour écouter, à tout moment de l’année, même si "
         "l’élève n’a pas écrit son prénom.",
         "3018 : numéro gratuit, anonyme et confidentiel, 7 jours sur 7 de 9 h à 23 h."],
        bg=(240, 253, 244), bord=(187, 247, 208), tc=VERT)

# ============================== PAGE 3 ==============================
pdf.add_page()
h1(pdf, "Après la séance : lire les résultats")
para(pdf, "Espace adulte → code 2026. L’onglet « Vue d’ensemble » donne les chiffres et l’interprétation ; "
          "l’onglet « Rapport » produit le document à imprimer ou à enregistrer en PDF.")
pdf.ln(2)

h2(pdf, "Comment sont calculés les scores (règles officielles)", avant=1)
pdf.set_draw_color(*LINE)
pdf.set_font("D", "B", 8.6)
pdf.set_fill_color(*IND_L)
pdf.set_text_color(*INK)
pdf.cell(64, 7, "Indice", border=1, fill=True)
pdf.cell(88, 7, "Ce qui est compté", border=1, fill=True)
pdf.cell(22, 7, "Étendue", border=1, fill=True, align="C")
pdf.ln()
rows = [
    ("Total A — qualité de vie", "réponses 3 ou 4 aux questions 2 à 8", "0 à 7"),
    ("Total B — atteintes subies", "réponses 3 ou 4 aux questions 11 à 20", "0 à 10"),
    ("Total C — atteintes graves", "réponses 2, 3 ou 4 aux questions 21 à 24", "0 à 4"),
    ("Score de victimation", "total B + total C", "0 à 14"),
]
pdf.set_font("D", "", 8.5)
for a, b, c in rows:
    pdf.cell(64, 7, a, border=1)
    pdf.cell(88, 7, b, border=1)
    pdf.cell(22, 7, c, border=1, align="C")
    pdf.ln()

pdf.ln(3)
para(pdf, "Le croisement du total A et de la somme B + C place ensuite chaque élève dans la table "
          "officielle : les deux indices élevés, la situation est retenue comme du harcèlement ; un seul "
          "indice élevé, l’élève est « à surveiller ». L’application applique cette table à la lettre et "
          "le montre élève par élève.", size=9)

h2(pdf, "Comment lire les chiffres", avant=2)
puce(pdf, "Le pourcentage compte des élèves, pas des faits",
     "12 % en zone harcèlement sur 33 élèves, cela fait 4 élèves. Sur un petit effectif, un seul élève "
     "pèse 3 points : c’est pourquoi l’application affiche cette prudence.")
puce(pdf, "3 % et 13 % sont des repères, pas des objectifs",
     "ce sont les résultats nationaux 2025 pour les écoliers du CE2 au CM2. Être au-dessus ne veut pas "
     "dire « école en échec » : cela veut dire « il y a du travail, et on sait lequel ».", color=ORANGE)
puce(pdf, "La part « à surveiller » décrit le climat",
     "quand elle est haute, le problème n’est pas seulement individuel : il porte sur les relations dans "
     "l’école, donc sur les actions collectives.")
puce(pdf, "Les faits graves ne se discutent pas",
     "violence sexuelle, violences physiques, cyberviolence : l’application les signale nommément "
     "(questions 20 à 24) et les place en tête de la liste des élèves à recevoir.", color=ROUGE)

y = pdf.get_y() + 3
pdf.image(SH + "/shots/crop-rap.png", x=LM, y=y, w=94)
pdf.set_xy(LM + 100, y + 1)
pdf.set_font("D", "B", 9.6)
pdf.set_text_color(*IND)
pdf.cell(0, 5, "Le rapport à transmettre")
pdf.ln(6)
pdf.set_x(LM + 100)
pdf.set_font("D", "", 8.8)
pdf.set_text_color(*INK)
pdf.multi_cell(W - 100, 4.9,
    "Onglet Rapport → « Imprimer / Enregistrer en PDF ». Le document reprend les effectifs, les résultats "
    "par classe, l’interprétation, les thèmes prioritaires et les actions retenues.", align="L")
pdf.ln(2.2)
pdf.set_x(LM + 100)
pdf.multi_cell(W - 100, 4.9,
    "« Copier la synthèse » met le même contenu en texte : il se colle directement dans un mail à "
    "l’inspecteur.", align="L")

# ============================== PAGE 4 ==============================
pdf.add_page()
h1(pdf, "Que faire des élèves repérés")
para(pdf, "C’est le point que le guide de passation impose, et celui que la circonscription regardera.")
puce(pdf, "Questionnaire nominatif en situation de harcèlement",
     "entretien obligatoire avec l’élève, mesures conservatoires, information de la famille, ouverture du "
     "protocole national de traitement.")
puce(pdf, "Questionnaire anonyme en situation de harcèlement",
     "l’élève ne peut pas être identifié, mais une action d’information et de sensibilisation doit être "
     "organisée dans la classe concernée.")
puce(pdf, "Faits graves",
     "signalement immédiat à la direction et à l’équipe ressource Phare, sans attendre l’analyse collective.",
     color=ROUGE)
puce(pdf, "Élèves « à surveiller »",
     "pas de protocole, mais une vigilance : les revoir, les observer en récréation, parler avec eux avant "
     "que la situation ne s’installe.", color=ORANGE)

h2(pdf, "Plusieurs tablettes : récupérer les données")
para(pdf, "Les réponses restent dans la tablette qui les a reçues. Il faut donc les rapatrier.")
etape(pdf, 1, "Sur chaque tablette, à la fin de la séance", [
    "Espace adulte → onglet Données → « Sauvegarde complète (.json) ». Le fichier se range dans les "
    "téléchargements de la tablette. C’est la sauvegarde : à faire à chaque séance, sans exception."])
etape(pdf, 2, "Sur la tablette de référence", [
    "Onglet Données → « Fusionner plusieurs tablettes » → choisir les fichiers récupérés. Les doublons "
    "sont écartés automatiquement.",
    "L’onglet Données affiche alors le nombre de tablettes fusionnées : il doit correspondre au nombre "
    "de tablettes qui ont servi. S’il en manque une, c’est que son fichier n’a pas été importé."])
etape(pdf, 3, "Si une seule tablette a servi", [
    "Rien à fusionner : les résultats sont déjà complets dans l’onglet Vue d’ensemble."])

encadre(pdf, "À ne pas faire",
        ["Vider l’historique ou les données de Chrome sur la tablette : cela effacerait les réponses.",
         "Changer de tablette en cours de route sans exporter : les réponses resteraient dans l’ancienne.",
         "Laisser un élève répondre deux fois : il compterait deux fois dans les statistiques."],
        bg=(254, 242, 242), bord=(254, 202, 202), tc=ROUGE)

# ============================== PAGE 5 ==============================
pdf.add_page()
h1(pdf, "Le dossier de labellisation (niveau 1)")
para(pdf, "Le rapport produit par l’application contient une section qui relie les résultats aux quatre "
          "axes attendus. Voici ce que l’enquête apporte, axe par axe.")
h2(pdf, "Les quatre axes", avant=1)
pdf.set_draw_color(*LINE)
rows2 = [
    ("Axe 1 — S’engager", "Une enquête menée auprès de tous les élèves, des résultats interprétés et "
     "partagés en conseil des maîtres : un diagnostic local, pas une intention."),
    ("Axe 2 — Prévenir", "Des thèmes prioritaires désignés par les élèves eux-mêmes, donc des séances de "
     "prévention ciblées, et un indicateur pour mesurer leur effet."),
    ("Axe 3 — Former", "Un support de passation commun à tous les collègues, réutilisable chaque année, "
     "accessible aux élèves à besoins particuliers (lecture audio, français simple)."),
    ("Axe 4 — Prendre en charge", "Les situations identifiées, nominatives ou non, avec la trace des "
     "élèves reçus et des faits graves signalés."),
]
for a, b in rows2:
    y = pdf.get_y()
    hb = 4.9 * max(1, len(b) // 84 + (1 if len(b) % 84 else 0)) + 5
    pdf.set_fill_color(248, 250, 252)
    pdf.rect(LM, y, 40, hb, style="DF")
    pdf.rect(LM + 40, y, W - 40, hb)
    pdf.set_xy(LM + 2, y + 2.2)
    pdf.set_font("D", "B", 9)
    pdf.set_text_color(*INK)
    pdf.multi_cell(36, 4.7, a, align="L")
    pdf.set_xy(LM + 42, y + 2.2)
    pdf.set_font("D", "", 8.7)
    pdf.multi_cell(W - 44, 4.7, b, align="L")
    pdf.set_y(y + hb + 1.5)

h2(pdf, "Ce qui fait la différence dans un dossier", avant=2)
puce(pdf, "Une mesure avant, une mesure après",
     "refaire passer la grille en juin avec la même application. La comparaison des deux mesures est la "
     "preuve qu’un dispositif fonctionne, et c’est ce qui manque le plus souvent aux dossiers.", color=VERT)
puce(pdf, "Une trace écrite du suivi",
     "l’onglet « Élèves à recevoir » garde la liste des élèves repérés et le numéro des questions en jeu : "
     "elle documente la prise en charge.")
puce(pdf, "Une restitution aux familles",
     "réunion ou atelier, avec les grandes tendances seulement, jamais le détail des réponses.")

h2(pdf, "Données personnelles et conservation")
para(pdf, "Les réponses ne quittent pas la tablette : aucun serveur, aucun envoi sur Internet, aucun compte. "
          "Le prénom est facultatif et n’apparaît jamais dans l’export CSV, seulement dans la sauvegarde "
          "que vous gardez. Comme le prévoit le guide de passation : questionnaires conservés jusqu’à la fin "
          "de l’année scolaire puis détruits ; questionnaires nominatifs révélant une situation de "
          "harcèlement conservés trois ans au maximum, dans des conditions garantissant leur confidentialité.",
     size=9)

pdf.ln(2)
y = pdf.get_y()
pdf.set_draw_color(*IND)
pdf.set_line_width(0.7)
pdf.rect(LM, y, W, 24)
pdf.set_xy(LM + 3, y + 3)
pdf.set_font("D", "B", 9.6)
pdf.set_text_color(*IND)
pdf.cell(0, 5, "En une phrase")
pdf.set_xy(LM + 3, y + 9)
pdf.set_font("D", "", 9.2)
pdf.set_text_color(*INK)
pdf.multi_cell(W - 6, 5.0, "Le jour de la passation : ouvrir le lien, laisser chaque élève répondre, puis "
                           "exporter la sauvegarde. Le soir, l’onglet Rapport donne l’interprétation et le "
                           "document à transmettre.", align="L")

out = "/workspace/nah/mode-emploi-non-au-harcelement.pdf"
pdf.output(out)
print("PDF:", out, os.path.getsize(out), "octets,", pdf.page_no(), "pages")
