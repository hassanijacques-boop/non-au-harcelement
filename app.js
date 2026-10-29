/* =========================================================================
   NON AU HARCÈLEMENT — Enquête d’auto-évaluation, école élémentaire
   Grille officielle 2025 (CE2-CM2) — passation sur tablette + interprétation
   Tout est local : aucune donnée ne quitte l’appareil.
   ========================================================================= */
var VERSION = '20261027-8';

/* ------------------------------- DONNÉES -------------------------------- */
/* d : total auquel la question appartient (A, B, C) — null = non comptée.
   Le seuil de comptage : 3 ou 4 pour A et B, 2 à 4 pour C (grille officielle). */
var Q = [
 {n:1,  e:'\uD83D\uDEB6', d:null, c:'Peur sur le trajet',
  t:'As-tu peur sur le trajet de l’école à cause d’un ou plusieurs élèves ?',
  s:'Sur le chemin de l’école, tu as peur à cause d’autres élèves.'},

 {n:2,  e:'\uD83C\uDFEB', d:'A', c:'Peur d’aller à l’école',
  t:'As-tu peur d’aller à l’école à cause d’un ou plusieurs élèves ?',
  s:'Tu as peur d’aller à l’école à cause d’autres élèves.'},

 {n:3,  e:'\uD83E\uDD12', d:'A', c:'Mentir pour rester',
  t:'As-tu menti pour rester chez toi par peur de retrouver un ou plusieurs élèves à l’école ?',
  s:'Tu as déjà dit que tu étais malade pour rester à la maison, parce que tu avais peur d’un élève.'},

 {n:4,  e:'\uD83D\uDCDA', d:'A', c:'Devoirs difficiles',
  t:'As-tu du mal à faire tes devoirs à cause de ce que tu vis à l’école ?',
  s:'Tu n’arrives pas à faire tes devoirs parce que tu penses à ce qui se passe à l’école.'},

 {n:5,  e:'\uD83D\uDE34', d:'A', c:'Sommeil, cauchemars',
  t:'As-tu du mal à t’endormir ou fais-tu des cauchemars à cause de ce que tu vis à l’école ?',
  s:'Tu as du mal à t’endormir, ou tu fais des cauchemars, à cause de l’école.'},

 {n:6,  e:'\uD83E\uDD12', d:'A', c:'Maux de ventre, tête',
  t:'As-tu mal au ventre ou à la tête à cause de ce que tu vis à l’école ?',
  s:'Tu as mal au ventre ou à la tête quand tu penses à l’école.'},

 {n:7,  e:'\uD83D\uDE22', d:'A', c:'Tristesse',
  t:'Est-ce que tu te sens triste à cause de ce que tu vis à l’école ?',
  s:'Tu es triste à cause de ce qui se passe à l’école.'},

 {n:8,  e:'\uD83D\uDE14', d:'A', c:'Sentiment de solitude',
  t:'Est-ce que tu te sens seul(e) à l’école ?',
  s:'À l’école, tu te sens seul ou seule.'},

 {n:9,  e:'\uD83D\uDE20', d:null, c:'Colère, agressivité',
  t:'Te mets-tu en colère ou es-tu agressif(ve) sans savoir pourquoi ?',
  s:'Tu te fâches très vite, ou tu deviens méchant, sans savoir pourquoi.'},

 {n:10, e:'\u26BD', d:null, c:'Peur de la récréation',
  t:'As-tu peur d’aller en récréation à cause d’un ou plusieurs élèves ?',
  s:'Tu as peur d’aller dans la cour à cause d’autres élèves.'},

 {n:11, e:'\uD83D\uDEAB', d:'B', c:'Mise à l’écart',
  t:'As-tu été mis(e) à l’écart dans la classe ou à la récréation par un ou plusieurs élèves ?',
  s:'Des élèves t’ont laissé de côté, en classe ou dans la cour.'},

 {n:12, e:'\uD83C\uDF7D', d:'B', c:'Cantine',
  t:'Est-ce qu’un ou plusieurs élèves t’empêchent de déjeuner tranquillement à la cantine ?',
  s:'Des élèves t’empêchent de manger tranquillement à la cantine.'},

 {n:13, e:'\uD83D\uDDE3', d:'B', c:'Rumeurs, choses fausses',
  t:'Est-ce qu’un ou plusieurs élèves racontent des choses fausses ou méchantes sur toi ?',
  s:'Des élèves racontent des choses fausses ou méchantes sur toi.'},

 {n:14, e:'\uD83C\uDFF7', d:'B', c:'Surnom méchant',
  t:'Est-ce qu’un ou plusieurs élèves t’ont donné un surnom méchant ?',
  s:'Des élèves t’ont donné un surnom méchant.'},

 {n:15, e:'\uD83D\uDE1D', d:'B', c:'Moqueries, insultes',
  t:'Est-ce qu’un ou plusieurs élèves se moquent de toi ou t’insultent (par exemple, à propos de la couleur de ta peau, de tes origines ou de ton physique) ?',
  s:'Des élèves se moquent de toi ou t’insultent : ta peau, ton origine, ton corps.'},

 {n:16, e:'\uD83D\uDC4A', d:'B', c:'Bagarres',
  t:'T’es-tu bagarré(e) avec un ou plusieurs élèves ?',
  s:'Tu t’es bagarré avec des élèves.'},

 {n:17, e:'\uD83D\uDCA5', d:'B', c:'Coups, bousculades',
  t:'Est-ce qu’un ou plusieurs élèves t’ont fait du mal exprès (par exemple, en te bousculant ou en te lançant un objet) ?',
  s:'Des élèves t’ont fait mal exprès : bousculé, lancé un objet…'},

 {n:18, e:'\uD83C\uDF92', d:'B', c:'Vols, menaces',
  t:'Est-ce qu’un ou plusieurs élèves t’ont volé des affaires ou ont menacé de le faire ?',
  s:'Des élèves t’ont pris des affaires, ou ils ont menacé de le faire.'},

 {n:19, e:'\uD83D\uDEBB', d:'B', c:'Toilettes',
  t:'As-tu été embêté(e) quand tu étais aux toilettes par un ou plusieurs élèves ?',
  s:'Des élèves t’embêtent quand tu es aux toilettes.'},

 {n:20, e:'\uD83D\uDCF1', d:'B', c:'Messages insultants (cyber)', grave:true,
  t:'As-tu vu ou reçu des messages sur toi, insultants ou menaçants, venant d’un ou plusieurs élèves, sur un téléphone portable, sur les réseaux sociaux ou sur une plateforme de jeux en ligne ?',
  s:'Tu as reçu, ou tu as vu, des messages méchants ou menaçants sur toi : téléphone, réseaux sociaux, jeu en ligne.'},

 {n:21, e:'\uD83C\uDFAE', d:'C', c:'Jeu dangereux',
  t:'As-tu participé à un jeu qui te semble dangereux à la demande d’un ou plusieurs élèves ?',
  s:'Des élèves t’ont demandé de faire un jeu dangereux, et tu l’as fait.'},

 {n:22, e:'\uD83D\uDC55', d:'C', c:'Retirer les habits', grave:true,
  t:'Est-ce qu’un ou plusieurs élèves ont essayé de te retirer tes habits ?',
  s:'Des élèves ont essayé de te retirer tes habits.'},

 {n:23, e:'\u270B', d:'C', c:'Attouchements, baisers', grave:true,
  t:'Est-ce qu’un ou plusieurs élèves ont essayé de toucher des parties de ton corps ou de t’embrasser sans que tu dises oui ?',
  s:'Des élèves ont essayé de toucher ton corps ou de t’embrasser alors que tu n’as pas dit oui.'},

 {n:24, e:'\uD83D\uDCF8', d:'C', c:'Photos diffusées', grave:true,
  t:'Un ou plusieurs élèves font-ils circuler sur toi, sans ton accord, des photos ou messages sur un téléphone portable, sur les réseaux sociaux ou sur une plateforme de jeux en ligne ?',
  s:'Des élèves font passer des photos ou des messages sur toi sans ton accord.'}
];

var REP = ['Jamais', 'Parfois', 'Souvent', 'Très souvent'];
var EMO = ['\uD83D\uDE42', '\uD83D\uDE15', '\uD83D\uDE1F', '\uD83D\uDE22'];

/* Questions « pour en savoir plus » — oui / non */
var PLUS = [
 {k:'memes',  t:'Est-ce toujours par le ou les mêmes élèves ?',
  s:'Si on t’embête souvent, est-ce toujours la même personne ?', cond:'embete'},
 {k:'aideEleve', t:'As-tu déjà demandé de l’aide à un(e) autre élève ?',
  s:'Tu as déjà demandé de l’aide à un autre élève.'},
 {k:'aideParent', t:'As-tu déjà demandé de l’aide à tes parents ?',
  s:'Tu as déjà parlé de ce problème à tes parents.'},
 {k:'aideAdulte', t:'As-tu déjà demandé de l’aide à un adulte de l’école ?',
  s:'Tu as déjà demandé de l’aide à un adulte de l’école : maître, maîtresse, directeur.'},
 {k:'ami',    t:'As-tu au moins un(e) ami(e) dans ton école ?',
  s:'Tu as au moins un ami ou une amie dans l’école.'},
 {k:'n3018',  t:'Connais-tu le numéro de téléphone contre le harcèlement 3018 ?',
  s:'Tu connais le numéro 3018 : le numéro gratuit contre le harcèlement.'},
 {k:'auteur', t:'As-tu déjà, avec d’autres élèves, embêté un(e) autre élève en te moquant de lui ou d’elle, en répétant des rumeurs à son sujet, en le ou la bousculant ou en le ou la mettant à l’écart ?',
  s:'Tu as déjà embêté un élève avec d’autres : moqué, rumeurs, bousculé, mis de côté.'},
 {k:'temEcole', t:'Connais-tu un(e) élève harcelé(e) dans ton école ?',
  s:'Tu connais un élève harcelé dans l’école.'},
 {k:'temClasse', t:'Connais-tu un(e) élève harcelé(e) dans ta classe ?',
  s:'Tu connais un élève harcelé dans ta classe.'}
];

var ANNEES = ['2018 ou après', '2017', '2016', '2015', '2014 ou avant'];
var CLE = 'nah_v1';

/* Les classes de l’école, pré-remplies : ainsi les 10 tablettes sont prêtes
   sans réglage. Modifiable dans Réglages (le « ; » sépare nom et effectif). */
var CLASSES_DEFAUT = 'CE2 A ; 0\nCE2 B ; 0\nCE2/CM1 ; 0\nCM1 A ; 0\nCM1 B ; 0\nCM1/CM2 ; 0\nCM2 ; 0';
/* anciennes listes par défaut : une tablette déjà ouverte bascule sur la nouvelle */
var ANCIENS = [
  'CE2 ; 0\nCM1 ; 0\nCM2 ; 0',
  'CE2 A ; 0\nCE2 B ; 0\nCM1 A ; 0\nCM1 B ; 0\nCM1 C ; 0\nCM2 ; 0\nCM1/CM2 ; 0'
];

/* ------------------------------- STOCKAGE -------------------------------- */
var DB = {
  cfg: {
    nom: 'École primaire publique La Rose',
    circo: 'IEN Bandraboua — Mayotte Nord',
    classesTxt: CLASSES_DEFAUT,
    pin: '2026',
    auto: false,
    resp: '',
    dev: ''
  },
  rep: []
};

function charger() {
  try {
    var s = localStorage.getItem(CLE);
    if (s) {
      var o = JSON.parse(s);
      if (o && o.cfg) {
        for (var k in DB.cfg) { if (o.cfg[k] !== undefined) DB.cfg[k] = o.cfg[k]; }
      }
      if (o && o.rep && o.rep.length !== undefined) DB.rep = o.rep;
      for (var m = 0; m < ANCIENS.length; m++) {
        if (DB.cfg.classesTxt === ANCIENS[m]) DB.cfg.classesTxt = CLASSES_DEFAUT;
      }
      /* « CM1 C » n’existe pas dans l’école : toute tablette qui la porte
         reçoit la liste réelle, quels que soient les effectifs saisis. */
      if (DB.cfg.classesTxt.indexOf('CM1 C') >= 0 && DB.cfg.classesTxt.indexOf('CE2/CM1') < 0) {
        DB.cfg.classesTxt = CLASSES_DEFAUT;
      }
    }
  } catch (e) {}
}
function sauver() {
  try { localStorage.setItem(CLE, JSON.stringify(DB)); return true; }
  catch (e) { alert('Mémoire pleine : exportez vos données puis effacez-les.'); return false; }
}

function classes() {
  var out = [];
  var lignes = String(DB.cfg.classesTxt || '').split('\n');
  for (var i = 0; i < lignes.length; i++) {
    var l = lignes[i].replace(/^\s+|\s+$/g, '');
    if (!l) continue;
    var p = l.split(';');
    var nom = (p[0] || '').replace(/^\s+|\s+$/g, '');
    var eff = parseInt((p[1] || '0'), 10);
    if (!nom) continue;
    out.push({ n: nom, eff: isNaN(eff) ? 0 : eff });
  }
  if (!out.length) out.push({ n: 'CM2', eff: 0 });
  return out;
}

/* --------------------------------- ÉTAT ---------------------------------- */
var vue = 'accueil';
var cur = null;
var ad = { tab: 'vue' };
var pinBuf = '';
var attente = null;
var flash = '';

/* -------------------------------- OUTILS --------------------------------- */
function $(id) { return document.getElementById(id); }
function esc(s) {
  return String(s === undefined || s === null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function pct(a, b) { return b > 0 ? (a * 100 / b) : 0; }
function nf(x, d) {
  d = (d === undefined) ? 1 : d;
  var s = Number(x).toFixed(d);
  return s.replace('.', ',');
}
function nfc(x) { var s = Number(x).toFixed(1); return s.replace(/\.0$/, ''); }
function barre(num, label, p, col) {
  var corps = (p > 0)
    ? '<div class="t"><i style="width:' + nfc(p) + '%;min-width:3px' + (col ? ';background:' + col : '') + '"></i></div>'
    : '<div class="t"><i class="vide" style="width:0"></i></div>';
  return '<div class="bar"><div class="lb"><span class="qn">' + num + '</span>' +
    '<span class="sp">' + esc(label) + '</span><span class="p">' + nf(p) + ' %</span></div>' +
    corps + '</div>';
}
function arr(n) { var a = []; for (var i = 0; i < n; i++) a.push(i); return a; }
function somme(a) { var t = 0; for (var i = 0; i < a.length; i++) t += a[i]; return t; }

/* Tablettes d’origine des réponses (pour vérifier qu’aucune n’a été oubliée à la fusion) */
function appareils(reps) {
  var vus = {}, out = [], i;
  for (i = 0; i < reps.length; i++) {
    var d = reps[i].dev || 'origine';
    if (!vus[d]) { vus[d] = { id: d, n: 0, dernier: '' }; out.push(vus[d]); }
    vus[d].n++;
    if (reps[i].ts && reps[i].ts > vus[d].dernier) vus[d].dernier = reps[i].ts;
  }
  return out;
}

/* Niveau déduit du nom de la classe : « CM1/CM2 B » → « CM1/CM2 » */
function niveauDe(nom) {
  var t = String(nom || '').toUpperCase(), lv = [];
  if (t.indexOf('CE1') !== -1) lv.push('CE1');
  if (t.indexOf('CE2') !== -1) lv.push('CE2');
  if (t.indexOf('CM1') !== -1) lv.push('CM1');
  if (t.indexOf('CM2') !== -1) lv.push('CM2');
  if (!lv.length) return 'Autre';
  return lv.join('/');
}

/* -------------------------------- SCORES --------------------------------- */
function seuil(q) { return q.d === 'C' ? 2 : 3; }

function calc(r) {
  var A = 0, B = 0, C = 0, graves = [];
  for (var i = 0; i < Q.length; i++) {
    var v = r.q[i] || 0;
    if (!v) continue;
    var q = Q[i];
    if (q.d === 'A' && v >= 3) A++;
    if (q.d === 'B' && v >= 3) B++;
    if (q.d === 'C' && v >= 2) C++;
    if (q.grave && v >= 2) graves.push(q.n);
  }
  var BC = B + C;
  return { A: A, B: B, C: C, BC: BC, statut: statut(A, BC), graves: graves };
}

/* Table officielle de croisement A × (B+C)
   pois = harcèlement · vagues = à surveiller · vide = rien */
function statut(A, BC) {
  var r = A === 0 ? 0 : (A <= 2 ? 1 : (A <= 4 ? 2 : 3));
  var c = BC === 0 ? 0 : (BC <= 2 ? 1 : (BC <= 4 ? 2 : (BC <= 7 ? 3 : 4)));
  var T = [
    ['rien', 'rien', 'surv', 'surv', 'harc'],
    ['rien', 'rien', 'surv', 'surv', 'harc'],
    ['surv', 'surv', 'surv', 'surv', 'harc'],
    ['harc', 'harc', 'harc', 'harc', 'harc']
  ];
  return T[r][c];
}
var LIB_STATUT = { harc: 'Harcèlement', surv: 'À surveiller', rien: 'Pas de difficulté' };
var CLS_STATUT = { harc: 'b-h', surv: 'b-s', rien: 'b-r' };

/* ------------------------------- ANALYSE --------------------------------- */
function analyse() {
  var rep = [], i, j;
  for (i = 0; i < DB.rep.length; i++) if (DB.rep[i].fini) rep.push(DB.rep[i]);
  var n = rep.length;
  var res = {
    n: n, harc: 0, surv: 0, rien: 0, incomplets: 0,
    rep: rep, q: [], clim: {}, alertes: [], parClasse: [],
    tauxH: 0, tauxS: 0, effectif: 0, part: 0, graves: 0
  };
  res.incomplets = DB.rep.length - n;

  var stats = [];
  for (i = 0; i < n; i++) {
    var s = calc(rep[i]);
    stats.push(s);
    if (s.statut === 'harc') res.harc++;
    else if (s.statut === 'surv') res.surv++;
    else res.rien++;
    if (s.graves.length) res.graves++;
    if (s.statut !== 'rien') {
      res.alertes.push({ r: rep[i], s: s });
    }
  }
  // tri : les plus préoccupants d’abord
  res.alertes.sort(function (a, b) {
    var d = (b.s.statut === 'harc' ? 1 : 0) - (a.s.statut === 'harc' ? 1 : 0);
    if (d) return d;
    return (b.s.BC + b.s.A) - (a.s.BC + a.s.A);
  });

  res.tauxH = pct(res.harc, n);
  res.tauxS = pct(res.surv, n);

  // par question
  for (i = 0; i < Q.length; i++) {
    var c = 0, c34 = 0;
    for (j = 0; j < n; j++) {
      var v = rep[j].q[i] || 0;
      if (!v) continue;
      if (v >= seuil(Q[i])) c++;
      if (v >= 3) c34++;
    }
    res.q.push({ n: Q[i].n, c: c, c34: c34, p: pct(c, n) });
  }

  // climat (oui / non)
  for (i = 0; i < PLUS.length; i++) {
    var oui = 0, non = 0;
    for (j = 0; j < n; j++) {
      var p = rep[j].plus || {};
      if (p[PLUS[i].k] === 'oui') oui++;
      else if (p[PLUS[i].k] === 'non') non++;
    }
    res.clim[PLUS[i].k] = { oui: oui, non: non, p: pct(oui, oui + non) };
  }

  // par classe
  var cs = classes();
  for (i = 0; i < cs.length; i++) {
    var e = { n: cs[i].n, eff: cs[i].eff, tot: 0, h: 0, s: 0, r: 0 };
    for (j = 0; j < n; j++) {
      if (rep[j].classe === cs[i].n) {
        e.tot++;
        if (stats[j].statut === 'harc') e.h++;
        else if (stats[j].statut === 'surv') e.s++;
        else e.r++;
      }
    }
    res.effectif += e.eff;
    res.parClasse.push(e);
  }
  // classes présentes dans les réponses mais absentes du réglage
  for (j = 0; j < n; j++) {
    var connu = false;
    for (i = 0; i < res.parClasse.length; i++) if (res.parClasse[i].n === rep[j].classe) connu = true;
    if (!connu) {
      var e2 = { n: rep[j].classe, eff: 0, tot: 0, h: 0, s: 0, r: 0 };
      for (var k = 0; k < n; k++) if (rep[k].classe === rep[j].classe) {
        e2.tot++;
        if (stats[k].statut === 'harc') e2.h++;
        else if (stats[k].statut === 'surv') e2.s++;
        else e2.r++;
      }
      res.parClasse.push(e2);
    }
  }
  // par niveau (CE2 / CM1 / CM2), déduit du nom de la classe
  var niv = {}, ordre = ['CE1', 'CE2', 'CM1', 'CM2'];
  res.parNiveau = [];
  for (j = 0; j < n; j++) {
    var lv = niveauDe(rep[j].classe);
    if (!niv[lv]) { niv[lv] = { n: lv, tot: 0, h: 0, s: 0, r: 0 }; res.parNiveau.push(niv[lv]); }
    niv[lv].tot++;
    if (stats[j].statut === 'harc') niv[lv].h++;
    else if (stats[j].statut === 'surv') niv[lv].s++;
    else niv[lv].r++;
  }
  res.parNiveau.sort(function (x, y) {
    var ix = ordre.indexOf(x.n), iy = ordre.indexOf(y.n);
    if (ix < 0) ix = 9;
    if (iy < 0) iy = 9;
    if (ix !== iy) return ix - iy;
    return x.n > y.n ? 1 : (x.n < y.n ? -1 : 0);
  });
  res.appareils = appareils(rep).length;

  res.part = pct(n, res.effectif);
  return res;
}

function topQ(a, max) {
  var t = a.q.slice(0);
  t.sort(function (x, y) { return y.p - x.p || y.c - x.c; });
  var out = [];
  for (var i = 0; i < t.length && out.length < (max || 5); i++) {
    if (t[i].c > 0) out.push(t[i]);
  }
  return out;
}

/* Texte d’interprétation automatique */
function interpretation(a) {
  var L = [];
  if (!a.n) {
    L.push({ t: 'p', x: 'Aucun questionnaire n’a encore été enregistré. Les résultats apparaîtront ici dès la première passation.' });
    return L;
  }
  var H = a.tauxH, S = a.tauxS;
  L.push({ t: 'p', x: 'Sur les ' + a.n + ' élèves interrogés, ' + a.harc + ' se situent dans la zone « harcèlement » (' + nf(H) + ' %) et ' + a.surv + ' dans la zone « à surveiller » (' + nf(S) + ' %). ' + a.rien + ' élèves ne présentent pas de difficulté particulière.' });

  // comparaison nationale
  var cmp = '';
  if (H >= 6) cmp = 'Ce niveau est nettement supérieur au repère national (3 % des écoliers en novembre 2025).';
  else if (H >= 2) cmp = 'Ce niveau est proche du repère national (3 % des écoliers en novembre 2025).';
  else cmp = 'Ce niveau est inférieur au repère national (3 % des écoliers en novembre 2025), mais chaque situation signalée reste à traiter individuellement.';
  if (S >= 20) cmp += ' La part d’élèves « à surveiller » est très élevée (repère national : 13 %) : elle traduit un climat scolaire dégradé qui appelle des actions de prévention sur l’ensemble de l’école, et pas seulement des réponses individuelles.';
  else if (S >= 10) cmp += ' La part d’élèves « à surveiller » (' + nf(S) + ' %) est comparable au repère national (13 %).';
  else cmp += ' La part d’élèves « à surveiller » est inférieure au repère national (13 %).';
  L.push({ t: 'p', x: cmp });

  if (a.n < 30) {
    L.push({ t: 'n', x: 'Prudence d’interprétation : avec ' + a.n + ' questionnaires, un seul élève représente ' + nf(pct(1, a.n)) + ' points de pourcentage. Les écarts de quelques points ne sont pas significatifs ; les situations individuelles, elles, se lisent une par une.' });
  }

  // dimensions
  var dA = 0, dB = 0, dC = 0;
  for (var i = 0; i < a.rep.length; i++) {
    var s = calc(a.rep[i]);
    if (s.A >= 3) dA++;
    if (s.B >= 5) dB++;
    if (s.C >= 1) dC++;
  }
  L.push({ t: 'h', x: 'Les trois dimensions de la grille' });
  L.push({ t: 'p', x: '• Qualité de vie à l’école (total A) : ' + dA + ' élève(s) cumulent au moins 3 réponses « souvent » ou « très souvent » — c’est la traduction d’une souffrance installée (peur, sommeil, douleurs, tristesse).' });
  L.push({ t: 'p', x: '• Atteintes subies de façon répétée (total B) : ' + dB + ' élève(s) en déclarent 5 ou plus. C’est le cœur de l’indice de multivictimation.' });
  L.push({ t: 'p', x: '• Atteintes graves (total C) : ' + dC + ' élève(s) déclarent au moins un fait relevant de la violence physique, sexuelle ou du cyberharcèlement. Ces faits, même isolés, ne se traitent pas par la prévention : ils se signalent.' });

  // atteintes principales
  var tp = topQ(a, 4);
  if (tp.length) {
    L.push({ t: 'h', x: 'Ce que les élèves déclarent le plus' });
    var phrase = [];
    for (i = 0; i < tp.length; i++) {
      phrase.push('« ' + Q[tp[i].n - 1].c + ' » (' + nf(tp[i].p) + ' % des élèves)');
    }
    L.push({ t: 'p', x: 'Les faits les plus rapportés sont : ' + phrase.join(' ; ') + '. Ce sont les thèmes à traiter en priorité dans les séances de prévention.' });
  }

  // climat
  var nc = a.clim;
  var sansAmi = nc.ami ? nc.ami.non : 0;
  var sansAide = 0;
  for (i = 0; i < a.rep.length; i++) {
    var p = a.rep[i].plus || {};
    if (p.aideEleve !== 'oui' && p.aideParent !== 'oui' && p.aideAdulte !== 'oui') sansAide++;
  }
  var conn3018 = nc.n3018 ? nc.n3018.oui : 0;
  var auteurs = nc.auteur ? nc.auteur.oui : 0;
  var temoins = nc.temClasse ? nc.temClasse.oui : 0;

  L.push({ t: 'h', x: 'Le climat, vu par les élèves' });
  L.push({ t: 'p', x: '• ' + sansAmi + ' élève(s) déclarent n’avoir aucun ami dans l’école (' + nf(pct(sansAmi, a.n)) + ' %). L’isolement est le premier facteur de vulnérabilité.' });
  L.push({ t: 'p', x: '• ' + sansAide + ' élève(s) n’ont demandé d’aide à personne — ni à un camarade, ni à leurs parents, ni à un adulte de l’école (' + nf(pct(sansAide, a.n)) + ' %). C’est le principal obstacle à la révélation : il indique où porter l’effort en premier.' });
  L.push({ t: 'p', x: '• ' + conn3018 + ' élève(s) connaissent le 3018 (' + nf(pct(conn3018, a.n)) + ' %) : le numéro doit être connu de tous, c’est un objectif simple et mesurable de la journée du 5 novembre.' });
  L.push({ t: 'p', x: '• ' + auteurs + ' élève(s) reconnaissent avoir déjà embêté un autre élève (' + nf(pct(auteurs, a.n)) + ' %). Ce chiffre mesure la banalisation des faits dans le groupe, pas la culpabilité individuelle : il justifie un travail sur les normes du groupe.' });
  L.push({ t: 'p', x: '• ' + temoins + ' élève(s) disent connaître un élève harcelé dans leur classe (' + nf(pct(temoins, a.n)) + ' %). Un écart important avec le nombre de victimes déclarées signifie que des situations sont vues mais non dites.' });

  return L;
}

/* Recommandations déduites des réponses */
function recommandations(a) {
  var r = [];
  if (!a.n) return r;
  var idx = {};
  for (var i = 0; i < a.q.length; i++) idx[a.q[i].n] = a.q[i].p;

  function fort(n) { return (idx[n] || 0) >= 20; }
  function moyen(n) { return (idx[n] || 0) >= 10; }

  if (a.graves > 0) r.push('Signaler sans délai : ' + a.graves + ' questionnaire(s) révèlent des faits graves (violence à caractère sexuel, violences physiques ou cyberviolence). Mettre en œuvre le protocole national de traitement des situations de harcèlement et informer l’équipe ressource Phare.');
  if (fort(23) || fort(22)) r.push('Atteintes à caractère sexuel : entretien individuel obligatoire avec chaque élève concerné, information immédiate du directeur et de l’IEN, protection de l’élève. Aucun traitement collectif ne remplace cette démarche.');
  if (fort(15)) r.push('Moqueries et insultes : séquence d’EMC sur les préjugés (couleur de peau, origine, physique), affiches produites par les élèves, rappel explicite que « une insulte n’est jamais pour rire ».');
  if (fort(11)) r.push('Mise à l’écart : jeux coopératifs en EPS et en récréation, brassage régulier des groupes, conseil des élèves où les exclus ont une place nominative.');
  if (fort(13) || fort(14)) r.push('Rumeurs et surnoms : séance sur la mécanique de la rumeur (théâtre-forum), travail sur le nom des personnes comme marque de respect.');
  if (fort(17) || fort(16)) r.push('Violences physiques : présence active et visible des adultes aux points chauds (couloir, terrain, escaliers), protocole clair de signalement, médiation par les pairs.');
  if (fort(12)) r.push('Cantine : surveillance renforcée et places attribuées, pour que le repas ne soit plus un moment à risque.');
  if (fort(19)) r.push('Toilettes : contrôle aux intercours, affichage du 3018 et du nom des adultes référents, accès au signalement facilité.');
  if (fort(20) || fort(24)) r.push('Cyberharcèlement : atelier « écrans et réseaux » avec les familles, charte du numérique signée, rappel du 3018 et du droit à l’image.');
  if (fort(8)) r.push('Isolement : parrainage des élèves seuls par des élèves ambassadeurs, observation des récréations pour identifier les élèves qui restent à l’écart.');
  if (fort(7) || fort(5) || fort(6)) r.push('Souffrance exprimée : entretiens individuels rapides, lien avec les familles, appui du RASED et du psychologue scolaire.');
  if (fort(2) || fort(10) || fort(1)) r.push('Peur à l’école et dans la cour : sécuriser les espaces et les temps non surveillés, montrer aux élèves où et à qui parler.');
  if (moyen(3) || moyen(4)) r.push('Absentéisme et décrochage : surveiller les élèves qui manquent ou qui n’arrivent plus à travailler, et les recevoir avant que la situation ne s’installe.');

  r.push('Restitution : présenter les grandes tendances aux élèves et aux parents (réunion ou atelier), sans jamais donner le détail des réponses individuelles.');
  r.push('Suite de l’année : refaire passer la grille en fin d’année pour mesurer l’effet des actions engagées — c’est ce suivi qui fait la différence dans un dossier de labellisation.');
  return r;
}

/* Synthèse courte, copiable pour l’IEN */
function syntheseTexte(a) {
  var t = '';
  t += 'ENQUÊTE « NON AU HARCÈLEMENT » — ' + (DB.cfg.nom || '') + '\n';
  t += 'Circonscription : ' + (DB.cfg.circo || '') + '\n';
  t += 'Grille d’auto-évaluation officielle (CE2-CM2), passation du ' + (DB.cfg.resp || new Date().toLocaleDateString('fr-FR')) + '\n\n';
  if (!a.n) { t += 'Aucune réponse enregistrée.\n'; return t; }
  t += 'Participation : ' + a.n + ' questionnaires exploités';
  if (a.effectif) t += ' (' + nf(a.part) + ' % des ' + a.effectif + ' élèves de l’école)';
  t += '\n\n';
  t += 'RÉSULTATS (croisement des indices A et B+C)\n';
  t += '- Zone harcèlement : ' + a.harc + ' élèves (' + nf(a.tauxH) + ' %) — repère national 3 %\n';
  t += '- Zone à surveiller : ' + a.surv + ' élèves (' + nf(a.tauxS) + ' %) — repère national 13 %\n';
  t += '- Sans difficulté : ' + a.rien + ' élèves (' + nf(pct(a.rien, a.n)) + ' %)\n';
  t += '- Faits graves déclarés : ' + a.graves + ' élève(s)\n\n';
  t += 'THÈMES LES PLUS DÉCLARÉS\n';
  var tp = topQ(a, 4);
  for (var i = 0; i < tp.length; i++) {
    t += '- ' + Q[tp[i].n - 1].c + ' : ' + nf(tp[i].p) + ' %\n';
  }
  t += '\nCLASSE PAR CLASSE\n';
  for (i = 0; i < a.parClasse.length; i++) {
    var c = a.parClasse[i];
    if (!c.tot) continue;
    t += '- ' + c.n + ' : ' + c.tot + ' réponses, ' + c.h + ' harcèlement, ' + c.s + ' à surveiller\n';
  }
  if (a.parNiveau && a.parNiveau.length) {
    t += '\nPAR NIVEAU\n';
    for (i = 0; i < a.parNiveau.length; i++) {
      var nvp = a.parNiveau[i];
      t += '- ' + nvp.n + ' : ' + nvp.tot + ' réponses, ' + nvp.h + ' harcèlement, ' + nvp.s + ' à surveiller\n';
    }
  }
  t += '\nINTERPRÉTATION\n';
  var L = interpretation(a);
  for (i = 0; i < L.length; i++) {
    if (L[i].t === 'h') t += '\n' + L[i].x.toUpperCase() + '\n';
    else t += L[i].x.replace(/^• /, '- ') + '\n';
  }
  var R = recommandations(a);
  t += '\nACTIONS PRIORITAIRES\n';
  for (i = 0; i < R.length; i++) t += '- ' + R[i] + '\n';
  return t;
}

/* --------------------------------- AUDIO --------------------------------- */
function voixFr() {
  try {
    var vs = window.speechSynthesis.getVoices() || [];
    for (var i = 0; i < vs.length; i++) {
      if (vs[i].lang && vs[i].lang.toLowerCase().indexOf('fr') === 0) return vs[i];
    }
  } catch (e) {}
  return null;
}
function lire(txt) {
  try {
    if (!window.speechSynthesis) return;
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance(txt);
    u.lang = 'fr-FR';
    u.rate = 0.92;
    u.pitch = 1;
    var v = voixFr();
    if (v) u.voice = v;
    window.speechSynthesis.speak(u);
  } catch (e) {}
}
function stopLire() { try { window.speechSynthesis.cancel(); } catch (e) {} }
function txtDit(q) {
  return String(q.t).replace(/\(e\)/g, '').replace(/’/g, ' ');
}

/* ------------------------------- RENDU ----------------------------------- */
function dessiner() {
  var h = '';
  stopLire();
  if (vue === 'accueil') h = vAccueil();
  else if (vue === 'ident') h = vIdent();
  else if (vue === 'consignes') h = vConsignes();
  else if (vue === 'q') h = vQ();
  else if (vue === 'plus') h = vPlus();
  else if (vue === 'prenom') h = vPrenom();
  else if (vue === 'merci') h = vMerci();
  else if (vue === 'saisieClasse') h = vSaisieClasse();
  else if (vue === 'saisie') h = vSaisie();
  else if (vue === 'pin') h = vPin();
  else if (vue === 'adulte') h = vAdulte();
  else if (vue === 'aide') h = vAide();
  else h = vAccueil();

  var el = $('app');
  el.className = (vue === 'adulte' || vue === 'pin') ? 'adm' : '';
  el.innerHTML = h;
  if (vue !== 'rapport') window.scrollTo(0, 0);

  if (vue === 'q' && DB.cfg.auto) {
    setTimeout(function () { lire(txtDit(Q[cur.i])); }, 260);
  }
}

function aller(v) { vue = v; dessiner(); }

/* ------------------------------- ACCUEIL --------------------------------- */
function vAccueil() {
  var a = analyse();
  var t = '';
  t += '<div class="wrap narrow kid"><div class="home">';
  t += '<div class="logo">\uD83D\uDEE1\uFE0F</div>';
  t += '<div><span class="pill">Enquête 2026 — 2027</span></div>';
  t += '<h1>Non au harcèlement</h1>';
  t += '<p class="sub">' + esc(DB.cfg.nom || 'Mon école') + '</p>';
  t += '<button class="btn" onclick="ouvrirSaisie()">\uD83D\uDCC4 Saisir les réponses (enseignant)</button>';
  t += '<button class="btn gris" onclick="commencer()">\uD83D\uDCDD Répondre au questionnaire (élève)</button>';
  t += '<button class="btn gris" onclick="aller(\'pin\')">\uD83D\uDD12 Espace adulte (résultats)</button>';
  t += '<button class="btn gris" onclick="aller(\'aide\')">\u2139\uFE0F Aide</button>';
  t += '<p class="tiny muted" style="margin-top:10px">';
  if (a.n) t += a.n + ' questionnaire(s) déjà enregistré(s) sur cet appareil · ';
  t += 'rien n’est envoyé sur Internet</p>';
  t += '<p class="tiny muted">Version ' + VERSION + '</p>';
  t += '</div></div>';
  return t;
}

function vAide() {
  var t = '<div class="wrap"><h1 style="margin-bottom:12px">Comment ça se passe</h1>';

  t += '<div class="card"><h2>Deux façons de faire passer</h2>';
  t += '<p><b>1. Sur papier, puis saisie par l’enseignant.</b> C’est la méthode retenue pour l’école : '
     + 'les élèves remplissent la grille imprimée en classe, puis chaque enseignant recopie les résultats '
     + 'de sa classe dans l’application. Un fichier par enseignant, fusionnés ensuite.</p>';
  t += '<p><b>2. Directement sur tablette.</b> Chaque élève répond seul, une question par écran, avec la '
     + 'lecture audio. Utile pour un petit groupe ou un élève absent le jour de la passation.</p>';
  t += '</div>';

  t += '<div class="card"><h2>Saisir les réponses papier</h2>';
  t += '<p>Bouton « Saisir les réponses (enseignant) », puis choisir sa classe : elle est mémorisée pour '
     + 'toute la série, inutile de la ressaisir à chaque élève.</p>';
  t += '<p>Chaque questionnaire tient sur un écran : 24 lignes de questions et 9 lignes oui/non, dans le '
     + 'même ordre que la grille papier.</p>';
  t += '<div class="info small"><b>Au clavier, c’est beaucoup plus rapide :</b> les touches <b>1</b> à '
     + '<b>4</b> remplissent la ligne surlignée et passent à la suivante, <b>Entrée</b> enregistre et '
     + 'prépare l’élève suivant. Un questionnaire se recopie en une minute environ.</div>';
  t += '<p class="small muted">Une erreur ? « Annuler le dernier » supprime le questionnaire qui vient '
     + 'd’être enregistré pour cette classe. Une ligne laissée vide n’est pas comptée.</p>';
  t += '</div>';

  t += '<div class="card"><h2>Ce que deviennent les réponses</h2>';
  t += '<p>Elles restent <b>dans l’appareil</b>. Rien n’est envoyé sur Internet, aucun compte n’est '
     + 'nécessaire. Seuls les adultes de l’école les lisent, pour aider les élèves qui en ont besoin.</p>';
  t += '<p class="small">À la fin de la campagne : exporter chaque poste de saisie (onglet Données), '
     + 'puis fusionner les fichiers sur le poste de référence. L’onglet Données indique le nombre de '
     + 'postes fusionnés : il doit correspondre au nombre d’enseignants.</p>';
  t += '</div>';

  t += '<div class="card"><h2>Pour l’élève qui répond sur tablette</h2>';
  t += '<p>Le questionnaire contient 24 questions et 9 questions oui/non. Il choisit sa classe, puis '
     + 'répond par <b>Jamais</b>, <b>Parfois</b>, <b>Souvent</b> ou <b>Très souvent</b>.</p>';
  t += '<p>Le bouton <b>\uD83D\uDD0A Écouter</b> lit la question à voix haute, autant de fois que '
     + 'nécessaire. La ligne bleue « En clair » la reformule simplement.</p>';
  t += '<p class="small muted">Il n’est pas obligé de répondre, et il peut passer une question. Le prénom '
     + 'n’est demandé qu’à la fin, et reste facultatif.</p>';
  t += '</div>';

  t += '<button class="btn gris" onclick="aller(\'accueil\')">\u2190 Retour</button></div>';
  return t;
}

/* ------------------------------- IDENTITÉ -------------------------------- */
function commencer() {
  var cs = classes();
  cur = { classe: '', sexe: '', annee: '', q: [], plus: {}, prenom: '', i: 0, pg: 0, fini: false, debut: Date.now() };
  for (var i = 0; i < Q.length; i++) cur.q.push(0);
  attente = cs;
  aller('ident');
}

function vIdent() {
  var cs = classes();
  var t = '<div class="wrap narrow kid"><h1 style="margin-bottom:6px">Avant de commencer</h1>';
  t += '<p class="sub" style="margin-bottom:18px">Ces trois informations servent seulement à ranger les réponses. Ton nom n’est pas demandé.</p>';
  t += '<div class="card">';

  t += '<div class="grp"><label>1. Ta classe</label><div class="chips">';
  for (var i = 0; i < cs.length; i++) {
    t += '<button class="chip' + (cur.classe === cs[i].n ? ' on' : '') + '" onclick="setClasse(' + i + ')">' + esc(cs[i].n) + '</button>';
  }
  t += '</div></div>';

  t += '<div class="grp"><label>2. Tu es</label><div class="chips">';
  t += '<button class="chip' + (cur.sexe === 'fille' ? ' on' : '') + '" onclick="setSexe(\'fille\')">\uD83D\uDC67 Une fille</button>';
  t += '<button class="chip' + (cur.sexe === 'garcon' ? ' on' : '') + '" onclick="setSexe(\'garcon\')">\uD83D\uDC66 Un garçon</button>';
  t += '</div></div>';

  t += '<div class="grp"><label>3. Ton année de naissance</label><div class="chips">';
  for (i = 0; i < ANNEES.length; i++) {
    t += '<button class="chip' + (cur.annee === ANNEES[i] ? ' on' : '') + '" onclick="setAnnee(' + i + ')">' + ANNEES[i] + '</button>';
  }
  t += '</div></div>';

  t += '<button class="btn" id="btnGo" onclick="versConsignes()"' + (cur.classe && cur.sexe && cur.annee ? '' : ' disabled') + '>Continuer \u2192</button>';
  t += '</div>';
  t += '<button class="lnk" onclick="aller(\'accueil\')">\u2190 Annuler</button></div>';
  return t;
}

function setClasse(i) { cur.classe = classes()[i].n; dessiner(); }
function setSexe(s) { cur.sexe = s; dessiner(); }
function setAnnee(i) { cur.annee = ANNEES[i]; dessiner(); }

/* ------------------------------- CONSIGNES -------------------------------- */
function versConsignes() {
  if (!cur.classe || !cur.sexe || !cur.annee) return;
  aller('consignes');
}

function vConsignes() {
  var t = '<div class="wrap narrow kid">';
  t += '<div class="card">';
  t += '<div class="qico">\uD83D\uDC4B</div>';
  t += '<h2 style="font-size:1.35rem;margin-bottom:10px">Comment répondre ?</h2>';
  t += '<p>Pour chaque question, tu choisis une seule réponse :</p>';
  t += '<div class="opts" style="margin:14px 0">';
  for (var i = 0; i < 4; i++) {
    t += '<div class="opt o' + (i + 1) + '"><span class="em">' + EMO[i] + '</span><span class="lb">' + REP[i] + '</span></div>';
  }
  t += '</div>';
  t += '<p class="small muted">Pense à <b>depuis le début de l’année scolaire</b>, pas seulement à aujourd’hui.</p>';
  t += '<hr>';
  t += '<p class="small"><b>Ce que tu dis reste confidentiel.</b> Ton nom n’est pas demandé. Tu peux passer une question si tu ne veux pas répondre.</p>';
  t += '<p class="small">À la fin, si tu veux qu’un adulte t’aide, tu pourras écrire ton prénom.</p>';
  t += '<label class="small" style="display:flex;gap:10px;align-items:center;margin-top:14px;background:#f4f7fd;padding:11px 13px;border-radius:12px">';
  t += '<input type="checkbox" id="autoCb" ' + (DB.cfg.auto ? 'checked' : '') + ' onchange="setAuto(this.checked)" style="width:22px;height:22px">';
  t += '<span>Lire les questions à voix haute automatiquement</span></label>';
  t += '</div>';
  t += '<button class="btn" onclick="demarrer()">Je commence \u2192</button>';
  t += '<button class="lnk" onclick="aller(\'ident\')">\u2190 Retour</button>';
  t += '</div>';
  return t;
}
function setAuto(v) { DB.cfg.auto = !!v; sauver(); }

function demarrer() { cur.i = 0; aller('q'); }

/* ------------------------------- QUESTIONS -------------------------------- */
function vQ() {
  var q = Q[cur.i];
  var t = '<div class="wrap narrow kid">';
  t += '<div class="qtop"><span class="lab">' + (cur.i + 1) + ' / ' + Q.length + '</span>';
  t += '<div class="pbar"><i style="width:' + nfc(pct(cur.i + 1, Q.length)) + '%"></i></div></div>';
  t += '<div class="card">';
  t += '<div class="qico">' + q.e + '</div>';
  t += '<p class="qtxt">' + esc(q.t) + '</p>';
  t += '<div class="qsim"><b>\uD83D\uDCA1 En clair :</b> ' + esc(q.s) + '</div>';
  t += '<button class="audio" onclick="ecouter()">\uD83D\uDD0A Écouter la question</button>';
  t += '<div class="opts">';
  for (var i = 0; i < 4; i++) {
    t += '<button class="opt o' + (i + 1) + (cur.q[cur.i] === i + 1 ? ' sel' : '') + '" onclick="rep(' + (i + 1) + ')">';
    t += '<span class="em">' + EMO[i] + '</span><span class="lb">' + REP[i] + '</span>';
    t += '</button>';
  }
  t += '</div>';
  t += '<div class="qfoot">';
  t += '<button class="lnk" onclick="prec()">\u2190 Retour</button>';
  t += '<button class="lnk" onclick="passer()">Je préfère ne pas répondre</button>';
  t += '</div>';
  t += '</div></div>';
  return t;
}

function ecouter() { lire(txtDit(Q[cur.i])); }
function rep(v) {
  cur.q[cur.i] = v;
  setTimeout(function () { suivant(); }, 90);
}
function passer() { cur.q[cur.i] = 0; suivant(); }
function prec() { if (cur.i > 0) { cur.i--; aller('q'); } else { aller('consignes'); } }
function suivant() {
  if (cur.i < Q.length - 1) { cur.i++; aller('q'); }
  else { cur.pg = 0; aller('plus'); }
}

/* --------------------------- QUESTIONS OUI / NON --------------------------- */
function vPlus() {
  var g = cur.pg;
  var debut = g * 3;
  var t = '<div class="wrap narrow kid">';
  t += '<div class="qtop"><span class="lab">Pour en savoir plus</span>';
  t += '<div class="pbar"><i style="width:' + nfc(pct(g + 1, 3)) + '%"></i></div></div>';
  t += '<div class="card">';
  t += '<h2 style="font-size:1.12rem;margin-bottom:4px">' + (g === 0 ? 'Si on t’embête souvent…' : 'Encore quelques questions') + '</h2>';
  t += '<p class="small muted" style="margin-bottom:6px">Réponds par oui ou par non.</p>';

  for (var k = debut; k < debut + 3 && k < PLUS.length; k++) {
    var p = PLUS[k];
    if (p.cond === 'embete') {
      t += '<p class="tiny muted" style="margin:16px 0 2px">Si tu as l’impression d’être embêté(e) souvent dans ton école ou sur Internet :</p>';
    }
    t += '<div style="margin:14px 0 6px">';
    t += '<p style="font-weight:700;font-size:1.02rem;margin:0 0 4px">' + esc(p.t) + '</p>';
    t += '<p class="small muted" style="margin:0 0 9px">' + esc(p.s) + '</p>';
    t += '<div class="yesno">';
    t += '<button class="yn' + (cur.plus[p.k] === 'oui' ? ' on' : '') + '" onclick="setPlus(\'' + p.k + '\',\'oui\')">\uD83D\uDC4D Oui</button>';
    t += '<button class="yn' + (cur.plus[p.k] === 'non' ? ' on' : '') + '" onclick="setPlus(\'' + p.k + '\',\'non\')">\uD83D\uDC4E Non</button>';
    t += '</div></div>';
  }
  t += '</div>';
  t += '<button class="btn" onclick="plusSuivant()">' + (g < 2 ? 'Continuer \u2192' : 'Terminer \u2192') + '</button>';
  t += '<button class="lnk" onclick="plusPrec()">\u2190 Retour</button>';
  t += '</div>';
  return t;
}

function setPlus(k, v) {
  cur.plus[k] = v;
  dessiner();
  // avance auto si les 3 de la page sont remplies
  var debut = cur.pg * 3, tous = true;
  for (var i = debut; i < debut + 3 && i < PLUS.length; i++) {
    if (!cur.plus[PLUS[i].k]) tous = false;
  }
  if (tous) setTimeout(function () { plusSuivant(); }, 320);
}
function plusSuivant() {
  if (cur.pg < 2) { cur.pg++; aller('plus'); }
  else aller('prenom');
}
function plusPrec() {
  if (cur.pg > 0) { cur.pg--; aller('plus'); }
  else { cur.i = Q.length - 1; aller('q'); }
}

/* -------------------------------- PRÉNOM ---------------------------------- */
function vPrenom() {
  var t = '<div class="wrap narrow kid">';
  t += '<div class="card" style="text-align:center">';
  t += '<div class="qico" style="margin:0 auto 14px">\uD83D\uDC64</div>';
  t += '<h2>Tu peux écrire ton prénom</h2>';
  t += '<p class="small">Ce n’est <b>pas obligatoire</b>. Si tu l’écris et que tes réponses montrent que tu souffres à l’école, un adulte viendra te parler pour t’aider.</p>';
  t += '<p class="small muted">Si tu préfères rester anonyme, laisse vide : cela ne change rien pour toi.</p>';
  t += '<input id="pn" value="' + esc(cur.prenom) + '" placeholder="Prénom (facultatif)" autocomplete="off" ';
  t += 'style="width:100%;margin:14px 0;padding:15px 16px;border:2px solid #dde3ee;border-radius:13px;font-family:inherit;font-size:1.1rem;text-align:center">';
  t += '</div>';
  t += '<button class="btn vert" onclick="terminer()">Envoyer mes réponses</button>';
  t += '<button class="lnk" onclick="terminer()">Non merci, rester anonyme</button>';
  t += '</div>';
  return t;
}

function terminer() {
  var el = $('pn');
  cur.prenom = el ? String(el.value || '').replace(/^\s+|\s+$/g, '').slice(0, 30) : '';
  cur.fini = true;
  cur.id = 'R' + Date.now() + Math.floor(Math.random() * 900 + 100);
  cur.dev = DB.cfg.dev || '';
  cur.ts = new Date().toISOString();
  cur.duree = Math.round((Date.now() - cur.debut) / 1000);
  DB.rep.push(cur);
  sauver();
  aller('merci');
}

function vMerci() {
  var a = analyse();
  var t = '<div class="wrap narrow" style="justify-content:center">';
  t += '<div class="card" style="text-align:center">';
  t += '<div class="bigok">\u2705</div>';
  t += '<h2 style="font-size:1.4rem">Merci !</h2>';
  t += '<p>Tes réponses sont enregistrées. Elles vont aider les adultes de l’école à mieux comprendre ce qui se passe entre les élèves.</p>';
  t += '<div class="num3618"><div style="font-size:30px">\uD83D\uDCDE</div><div style="text-align:left">';
  t += '<div class="n">3018</div><div class="small">Numéro gratuit contre le harcèlement.<br>7 jours sur 7, de 9 h à 23 h. Anonyme.</div></div></div>';
  t += '<p class="small">Si tu as besoin de parler, tu peux t’adresser à n’importe quel adulte de l’école : ton maître ou ta maîtresse, le directeur, la personne qui s’occupe de la santé.</p>';
  t += '</div>';
  t += '<button class="btn gris" onclick="suivantEleve()">\uD83D\uDC65 Élève suivant</button>';
  t += '<p class="tiny muted" style="text-align:center">' + a.n + ' questionnaire(s) enregistré(s) sur cet appareil</p>';
  t += '</div>';
  return t;
}

function suivantEleve() { cur = null; aller('accueil'); }


/* --------------------------- SAISIE ENSEIGNANT ---------------------------- */
/* Les questionnaires sont remplis sur papier, puis recopiés ici par
   l’enseignant. Classe choisie une fois, puis une ligne par question. */
var sais = null;
var toastT = null;

function toast(msg) {
  var d = document.getElementById('toast');
  if (!d) {
    d = document.createElement('div');
    d.id = 'toast';
    document.body.appendChild(d);
  }
  d.className = 'toast on';
  d.textContent = msg;
  clearTimeout(toastT);
  toastT = setTimeout(function () { d.className = 'toast'; }, 2800);
}

function nbSaisisClasse() {
  var n = 0;
  for (var i = 0; i < DB.rep.length; i++) {
    if (DB.rep[i].fini && DB.rep[i].classe === sais.classe) n++;
  }
  return n;
}

function ouvrirSaisie() {
  var cs = classes(), i;
  sais = { classe: '', sexe: '', annee: '', prenom: '', q: [], plus: {}, i: 0 };
  for (i = 0; i < Q.length; i++) sais.q.push(0);
  if (cs.length === 1) sais.classe = cs[0].n;
  aller(sais.classe ? 'saisie' : 'saisieClasse');
}

function vSaisieClasse() {
  var cs = classes();
  var t = '<div class="wrap narrow kid">';
  t += '<div class="card">';
  t += '<h2 style="font-size:1.3rem">Saisie des questionnaires</h2>';
  t += '<p class="small muted">Choisissez la classe dont vous recopiez les résultats. Elle restera '
     + 'la même pour toute la série : inutile de la ressaisir à chaque élève.</p>';
  t += '<div class="chips" style="margin-top:12px">';
  for (var i = 0; i < cs.length; i++) {
    t += '<button class="chip" onclick="choixClasseSaisie(' + i + ')">' + esc(cs[i].n) + '</button>';
  }
  t += '</div></div>';
  t += '<button class="lnk" onclick="aller(\'accueil\')">\u2190 Retour</button></div>';
  return t;
}

function choixClasseSaisie(i) { sais.classe = classes()[i].n; aller('saisie'); }

function vSaisie() {
  var a = analyse(), i, k;
  var t = '<div class="wrap"><div class="sais">';

  t += '<div class="shead"><div class="t">Saisie \u2014 ' + esc(sais.classe) + '</div>';
  t += '<div class="s">' + nbSaisisClasse() + ' questionnaire(s) recopi\u00e9(s) pour cette classe \u00b7 '
     + a.n + ' au total sur cet appareil</div></div>';

  /* identité, tout est facultatif sauf la classe déjà fixée */
  t += '<div class="sid">';
  t += '<button class="sx' + (sais.sexe === 'fille' ? ' on' : '') + '" onclick="saisSexe(\'fille\')">Fille</button>';
  t += '<button class="sx' + (sais.sexe === 'garcon' ? ' on' : '') + '" onclick="saisSexe(\'garcon\')">Gar\u00e7on</button>';
  t += '<select id="sannee" onchange="saisAnnee(this.value)"><option value="">Ann\u00e9e Naiss.</option>';
  for (i = 0; i < ANNEES.length; i++) {
    t += '<option' + (sais.annee === ANNEES[i] ? ' selected' : '') + '>' + ANNEES[i] + '</option>';
  }
  t += '</select>';
  t += '<input id="sprenom" placeholder="Pr\u00e9nom (facultatif)" autocomplete="off" value="' + esc(sais.prenom) + '">';
  t += '</div>';

  /* les 24 questions */
  for (i = 0; i < Q.length; i++) {
    t += '<div class="srow' + (sais.i === i ? ' cur' : '') + '" id="sr' + i + '">';
    t += '<div class="sn">' + Q[i].n + '</div>';
    t += '<div class="st">' + esc(Q[i].c) + '</div>';
    t += '<div class="sv">';
    for (k = 1; k <= 4; k++) {
      t += '<button class="sbn' + (sais.q[i] === k ? ' sel' + k : '') + '" title="' + REP[k - 1] +
           '" onclick="saisRep(' + i + ',' + k + ')">' + k + '</button>';
    }
    t += '</div></div>';
  }

  /* les 9 questions oui / non */
  for (i = 0; i < PLUS.length; i++) {
    var idx = Q.length + i;
    var val = sais.plus[PLUS[i].k];
    t += '<div class="srow' + (sais.i === idx ? ' cur' : '') + '" id="sr' + idx + '">';
    t += '<div class="sn">' + (i + 1) + '</div>';
    t += '<div class="st">' + esc(PLUS[i].t) + '</div>';
    t += '<div class="sv">';
    t += '<button class="sbn w' + (val === 'oui' ? ' selo' : '') + '" onclick="saisPlus(' + i + ',\'oui\')">Oui</button>';
    t += '<button class="sbn w' + (val === 'non' ? ' selo' : '') + '" onclick="saisPlus(' + i + ',\'non\')">Non</button>';
    t += '</div></div>';
  }

  t += '<div class="sbar"><div class="tiny muted">Touches <b>1</b> \u00e0 <b>4</b> : remplir et passer \u00e0 la ligne suivante \u00b7 <b>Entr\u00e9e</b> : enregistrer</div>';
  t += '<div style="display:flex;gap:8px;flex-wrap:wrap">';
  t += '<button class="btn mini gris" onclick="annulerDernier()">Annuler le dernier</button>';
  t += '<button class="btn mini gris" onclick="aller(\'accueil\')">Terminer</button>';
  t += '<button class="btn mini" onclick="enregistrerSaisie()">Enregistrer et continuer</button>';
  t += '</div></div>';

  t += '</div>';
  t += '<p class="tiny muted" style="text-align:center;margin-top:10px">Les r\u00e9ponses vides restent non compt\u00e9es, comme sur le papier.</p>';
  t += '</div>';
  return t;
}

function saisSexe(v) { sais.sexe = v; dessiner(); }
function saisAnnee(v) { sais.annee = v; }

function majSaisRow(i) {
  var row = document.getElementById('sr' + i);
  if (!row) return;
  var bs = row.querySelectorAll('.sbn');
  if (i < Q.length) {
    for (var k = 0; k < 4; k++) bs[k].className = 'sbn' + (sais.q[i] === k + 1 ? ' sel' + (k + 1) : '');
  } else {
    var v = sais.plus[PLUS[i - Q.length].k];
    bs[0].className = 'sbn w' + (v === 'oui' ? ' selo' : '');
    bs[1].className = 'sbn w' + (v === 'non' ? ' selo' : '');
  }
}

function setCurSais(i) {
  var old = document.getElementById('sr' + sais.i);
  if (old) old.className = 'srow';
  sais.i = i;
  var row = document.getElementById('sr' + i);
  if (!row) return;
  row.className = 'srow cur';
  if (row.scrollIntoView) row.scrollIntoView({ block: 'nearest' });
}

function saisRep(i, v) {
  sais.q[i] = v;
  majSaisRow(i);
  setCurSais(Math.min(i + 1, Q.length + PLUS.length - 1));
}
function saisPlus(i, v) {
  sais.plus[PLUS[i].k] = v;
  majSaisRow(Q.length + i);
  setCurSais(Math.min(Q.length + i + 1, Q.length + PLUS.length - 1));
}

function annulerDernier() {
  for (var i = DB.rep.length - 1; i >= 0; i--) {
    if (DB.rep[i].classe === sais.classe) {
      if (!confirm('Supprimer le dernier questionnaire enregistr\u00e9 pour ' + sais.classe + ' ?\n\n'
        + 'Les r\u00e9ponses de cet \u00e9l\u00e8ve seront perdues.')) return;
      DB.rep.splice(i, 1);
      sauver();
      dessiner();
      toast('Dernier questionnaire supprim\u00e9.');
      return;
    }
  }
  toast('Aucun questionnaire \u00e0 annuler pour cette classe.');
}

function enregistrerSaisie() {
  var n = 0, i, k;
  for (i = 0; i < Q.length; i++) if (sais.q[i]) n++;
  if (!n) { toast('Aucune r\u00e9ponse coch\u00e9e : rien \u00e0 enregistrer.'); return; }
  var pn = document.getElementById('sprenom');
  var r = {
    id: 'R' + Date.now() + Math.floor(Math.random() * 900 + 100),
    dev: DB.cfg.dev || '',
    ts: new Date().toISOString(),
    classe: sais.classe, sexe: sais.sexe, annee: sais.annee,
    prenom: pn ? String(pn.value).replace(/^\s+|\s+$/g, '').slice(0, 30) : '',
    q: sais.q.slice(0), plus: {}, fini: true, source: 'papier'
  };
  for (k in sais.plus) r.plus[k] = sais.plus[k];
  DB.rep.push(r);
  sauver();
  sais.q = [];
  for (i = 0; i < Q.length; i++) sais.q.push(0);
  sais.plus = {}; sais.prenom = ''; sais.sexe = ''; sais.annee = ''; sais.i = 0;
  dessiner();
  window.scrollTo(0, 0);
  toast('Enregistr\u00e9 \u2014 ' + nbSaisisClasse() + ' questionnaire(s) pour ' + sais.classe);
}

document.addEventListener('keydown', function (e) {
  if (vue !== 'saisie' || !sais) return;
  var tag = (e.target && e.target.tagName) ? e.target.tagName.toUpperCase() : '';
  if (tag === 'INPUT' || tag === 'SELECT' || tag === 'TEXTAREA') return;
  var k = e.key;
  if (k >= '1' && k <= '4') {
    if (sais.i < Q.length) {
      saisRep(sais.i, parseInt(k, 10));
    } else if (k === '1' || k === '2') {
      saisPlus(sais.i - Q.length, k === '1' ? 'oui' : 'non');
    }
    e.preventDefault();
  } else if (k === 'ArrowDown') {
    setCurSais(Math.min(sais.i + 1, Q.length + PLUS.length - 1));
    e.preventDefault();
  } else if (k === 'ArrowUp') {
    setCurSais(Math.max(sais.i - 1, 0));
    e.preventDefault();
  } else if (k === 'Enter') {
    enregistrerSaisie();
    e.preventDefault();
  }
});

/* ---------------------------------- PIN ----------------------------------- */
function vPin() {
  var t = '<div class="wrap narrow" style="justify-content:center">';
  t += '<div class="card" style="text-align:center">';
  t += '<div class="qico" style="margin:0 auto 12px">\uD83D\uDD12</div>';
  t += '<h2>Espace adulte</h2>';
  t += '<p class="small muted">Réservé aux adultes de l’école.</p>';
  t += '<div class="dots">';
  for (var i = 0; i < 4; i++) t += '<i class="' + (pinBuf.length > i ? 'on' : '') + '"></i>';
  t += '</div>';
  if (flash) t += '<p class="small" style="color:#dc2626;font-weight:700">' + esc(flash) + '</p>';
  t += '<div class="pinpad">';
  var k = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '\u232B', '0', '\u2713'];
  for (i = 0; i < k.length; i++) {
    t += '<button onclick="pinTouche(\'' + k[i] + '\')">' + k[i] + '</button>';
  }
  t += '</div>';
  if (DB.cfg.pin === '2026') t += '<p class="tiny muted" style="margin-top:14px">Code initial : 2026 — à changer dans Réglages.</p>';
  t += '</div>';
  t += '<button class="lnk" onclick="aller(\'accueil\')">\u2190 Retour</button></div>';
  return t;
}

function pinTouche(c) {
  flash = '';
  if (c === '\u232B') { pinBuf = pinBuf.slice(0, -1); dessiner(); return; }
  if (c === '\u2713') { validerPin(); return; }
  if (pinBuf.length < 4) pinBuf += c;
  if (pinBuf.length === 4) { setTimeout(validerPin, 140); return; }
  dessiner();
}
function validerPin() {
  if (pinBuf === DB.cfg.pin) { pinBuf = ''; ad.tab = 'vue'; aller('adulte'); }
  else { pinBuf = ''; flash = 'Code incorrect.'; dessiner(); }
}

/* ------------------------------ ESPACE ADULTE ------------------------------ */
function onglet(t) { ad.tab = t; dessiner(); }

function vAdulte() {
  var t = '<div class="wrap"><div class="noprint" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">';
  t += '<div><div style="font-weight:900;font-size:1.05rem">Espace adulte</div>';
  t += '<div class="tiny muted">' + esc(DB.cfg.nom || '') + '</div></div>';
  t += '<button class="btn mini gris" onclick="aller(\'accueil\')">Quitter</button>';
  t += '</div>';

  var tabs = [['vue', 'Vue d’ensemble'], ['classes', 'Par classe'], ['questions', 'Par question'],
              ['eleves', 'Élèves à recevoir'], ['rapport', 'Rapport'], ['donnees', 'Données'], ['config', 'Réglages']];
  t += '<div class="tabs noprint">';
  for (var i = 0; i < tabs.length; i++) {
    t += '<button class="tab' + (ad.tab === tabs[i][0] ? ' on' : '') + '" onclick="onglet(\'' + tabs[i][0] + '\')">' + tabs[i][1] + '</button>';
  }
  t += '</div>';

  if (ad.tab === 'vue') t += tabVue();
  else if (ad.tab === 'classes') t += tabClasses();
  else if (ad.tab === 'questions') t += tabQuestions();
  else if (ad.tab === 'eleves') t += tabEleves();
  else if (ad.tab === 'rapport') t += tabRapport();
  else if (ad.tab === 'donnees') t += tabDonnees();
  else t += tabConfig();

  t += '</div>';
  return t;
}

function tabVue() {
  var a = analyse();
  var t = '';
  if (!a.n) {
    t += '<div class="info">Aucun questionnaire enregistré pour l’instant. Faites passer la grille sur les tablettes, puis revenez ici : les résultats se calculent automatiquement.</div>';
    return t;
  }
  if (a.graves) {
    t += '<div class="alerte"><h3>\u26A0\uFE0F ' + a.graves + ' questionnaire(s) avec faits graves</h3>';
    t += '<p>Violence à caractère sexuel, violences physiques ou cyberviolence déclarées. Le guide de passation impose un signalement immédiat à la direction et la mise en œuvre du protocole national. Voir l’onglet « Élèves à recevoir ».</p></div>';
  }
  if (a.harc) {
    t += '<div class="warn"><b>' + a.harc + ' élève(s) en zone harcèlement.</b> Le protocole de traitement doit être ouvert : entretien avec l’élève, mesures de protection, information des familles. Voir l’onglet « Élèves à recevoir ».</div>';
  }

  t += '<div class="kpis">';
  t += '<div class="kpi p"><div class="v">' + a.n + '</div><div class="l">Questionnaires exploités' + (a.effectif ? '<br>' + nf(a.part) + ' % des ' + a.effectif + ' élèves' : '') + '</div></div>';
  t += '<div class="kpi h"><div class="v">' + nf(a.tauxH) + '<span style="font-size:1rem"> %</span></div><div class="l">Zone harcèlement<br>' + a.harc + ' élève(s) · repère national 3 %</div></div>';
  t += '<div class="kpi s"><div class="v">' + nf(a.tauxS) + '<span style="font-size:1rem"> %</span></div><div class="l">À surveiller<br>' + a.surv + ' élève(s) · repère national 13 %</div></div>';
  t += '<div class="kpi g"><div class="v">' + nf(pct(a.rien, a.n)) + '<span style="font-size:1rem"> %</span></div><div class="l">Sans difficulté<br>' + a.rien + ' élève(s)</div></div>';
  t += '</div>';

  t += '<p class="tiny muted" style="margin:-4px 0 12px 2px">' +
       (a.appareils > 1
         ? '\uD83D\uDCF1 Résultats fusionnés de <b>' + a.appareils + ' postes de saisie</b> — vérifiez que c’est bien le nombre attendu.'
         : '\uD83D\uDCF1 Réponses enregistrées sur cet appareil uniquement (aucune fusion).') + '</p>';

  // comparaison visuelle
  t += '<div class="card"><h2>Comparaison avec le baromètre national 2025</h2>';
  t += '<div class="comp">';
  t += '<div class="c"><div class="v" style="color:#dc2626">' + nf(a.tauxH) + ' %</div><div class="l">École<br>(national : 3 %)</div></div>';
  t += '<div class="c"><div class="v" style="color:#b45309">' + nf(a.tauxS) + ' %</div><div class="l">À surveiller<br>(national : 13 %)</div></div>';
  t += '</div>';
  t += '<p class="tiny muted" style="margin-top:10px">Repères nationaux : baromètre harcèlement 2025, écoliers du CE2 au CM2. Un écart sur un petit effectif se lit avec prudence : 1 élève = ' + nf(pct(1, a.n)) + ' points ici.</p>';
  t += '</div>';

  // interprétation
  t += '<div class="card"><h2>Interprétation</h2>';
  var L = interpretation(a);
  for (var i = 0; i < L.length; i++) {
    if (L[i].t === 'h') t += '<h3>' + esc(L[i].x) + '</h3>';
    else if (L[i].t === 'n') t += '<div class="warn small">' + esc(L[i].x) + '</div>';
    else t += '<p class="small">' + esc(L[i].x) + '</p>';
  }
  t += '</div>';

  // top atteintes
  var tp = topQ(a, 6);
  if (tp.length) {
    t += '<div class="card"><h2>Faits les plus déclarés</h2><div class="bars">';
    for (i = 0; i < tp.length; i++) {
      t += barre('Q' + tp[i].n, Q[tp[i].n - 1].c, tp[i].p);
    }
    t += '</div><p class="tiny muted" style="margin-top:10px">Pourcentage d’élèves ayant répondu « souvent » ou « très souvent » (ou « parfois » et plus pour les questions 21 à 24).</p></div>';
  }
  return t;
}

function tabClasses() {
  var a = analyse();
  var t = '<div class="card"><h2>Résultats par classe</h2>';
  if (!a.n) return t + '<p class="muted">Pas encore de réponses.</p></div>';
  t += '<div class="tbl"><table><thead><tr><th>Classe</th><th class="num">Effectif</th><th class="num">Réponses</th><th class="num">Harcèl.</th><th class="num">À surveiller</th><th class="num">Sans diff.</th></tr></thead><tbody>';
  var th = 0, ts = 0, tr = 0, tt = 0;
  for (var i = 0; i < a.parClasse.length; i++) {
    var c = a.parClasse[i];
    th += c.h; ts += c.s; tr += c.r; tt += c.tot;
    t += '<tr><td><b>' + esc(c.n) + '</b></td>';
    t += '<td class="num">' + (c.eff || '—') + '</td>';
    t += '<td class="num">' + c.tot + (c.eff ? ' <span class="tiny muted">(' + nf(pct(c.tot, c.eff), 0) + ' %)</span>' : '') + '</td>';
    t += '<td class="num">' + (c.h ? '<span class="badge b-h">' + c.h + '</span>' : '0') + '</td>';
    t += '<td class="num">' + (c.s ? '<span class="badge b-s">' + c.s + '</span>' : '0') + '</td>';
    t += '<td class="num">' + c.r + '</td></tr>';
  }
  t += '<tr class="tot"><td>École</td><td class="num">' + (a.effectif || '—') + '</td><td class="num">' + tt + '</td><td class="num">' + th + '</td><td class="num">' + ts + '</td><td class="num">' + tr + '</td></tr>';
  t += '</tbody></table></div>';
  if (a.incomplets) t += '<p class="small muted">' + a.incomplets + ' questionnaire(s) commencé(s) mais non terminé(s) — non comptés.</p>';

  if (a.parNiveau.length) {
    t += '<h3 style="margin-top:22px">Résultats par niveau</h3>';
    t += '<div class="tbl"><table><thead><tr><th>Niveau</th><th class="num">Réponses</th><th class="num">Harcèl.</th><th class="num">À surveiller</th><th class="num">Sans diff.</th><th class="num">% harcèl.</th></tr></thead><tbody>';
    for (var k = 0; k < a.parNiveau.length; k++) {
      var nv = a.parNiveau[k];
      t += '<tr><td><b>' + esc(nv.n) + '</b></td><td class="num">' + nv.tot + '</td>';
      t += '<td class="num">' + (nv.h ? '<span class="badge b-h">' + nv.h + '</span>' : '0') + '</td>';
      t += '<td class="num">' + (nv.s ? '<span class="badge b-s">' + nv.s + '</span>' : '0') + '</td>';
      t += '<td class="num">' + nv.r + '</td>';
      t += '<td class="num">' + nf(pct(nv.h, nv.tot)) + ' %</td></tr>';
    }
    t += '</tbody></table></div>';
    t += '<p class="tiny muted" style="margin-top:8px">Le niveau est déduit du nom de la classe : une classe à cours multiple apparaît sous son niveau réel, par exemple « CM1/CM2 ».</p>';
  }
  t += '<p class="tiny muted" style="margin-top:12px">Renseignez les effectifs dans l’onglet Réglages pour obtenir les taux de participation.</p>';

  t += '</div>';
  return t;
}

function tabQuestions() {
  var a = analyse();
  var t = '<div class="card"><h2>Réponses question par question</h2>';
  if (!a.n) return t + '<p class="muted">Pas encore de réponses.</p></div>';
  t += '<p class="small muted" style="margin-bottom:14px">Part des élèves ayant déclaré le fait de façon répétée. Les questions 2 à 8 forment le total A, les questions 11 à 20 le total B, les questions 21 à 24 le total C.</p>';
  t += '<div class="bars">';
  for (var i = 0; i < a.q.length; i++) {
    var q = a.q[i];
    var col = q.n >= 21 ? '#db2777' : (q.n >= 11 ? '#4338ca' : '#0ea5e9');
    t += barre(q.n, Q[i].c, q.p, col);
  }
  t += '</div>';
  t += '<p class="tiny muted" style="margin-top:12px"><span style="color:#0ea5e9">\u25A0</span> qualité de vie (A) · <span style="color:#4338ca">\u25A0</span> atteintes (B) · <span style="color:#db2777">\u25A0</span> atteintes graves (C)</p>';
  t += '</div>';

  // climat
  t += '<div class="card"><h2>Climat et ressources des élèves</h2><div class="tbl"><table><thead><tr><th>Question</th><th class="num">Oui</th><th class="num">%</th></tr></thead><tbody>';
  for (i = 0; i < PLUS.length; i++) {
    var p = a.clim[PLUS[i].k];
    if (!p) continue;
    var bon = (PLUS[i].k === 'ami' || PLUS[i].k === 'n3018' || PLUS[i].k.indexOf('aide') === 0);
    var col = p.p >= 50 ? (bon ? '#16a34a' : '#dc2626') : (bon ? '#b45309' : '#64748b');
    t += '<tr><td>' + esc(PLUS[i].t) + '</td><td class="num">' + p.oui + '</td>';
    t += '<td class="num" style="color:' + col + ';font-weight:800">' + nf(p.p) + ' %</td></tr>';
  }
  t += '</tbody></table></div>';
  t += '<p class="tiny muted" style="margin-top:10px">Lecture : pour « au moins un ami » et « connaît le 3018 », un pourcentage élevé est une bonne nouvelle. Pour les autres, un pourcentage élevé signale un point de vigilance.</p></div>';
  return t;
}

function tabEleves() {
  var a = analyse();
  var t = '<div class="card"><h2>Élèves à recevoir</h2>';
  if (!a.alertes.length) return t + '<div class="okbox">Aucun élève en zone harcèlement ou à surveiller. Cela ne dispense pas de rester attentif : un questionnaire peut ne pas tout dire.</div></div>';
  t += '<p class="small muted" style="margin-bottom:12px">Classés du plus préoccupant au moins préoccupant. Les questionnaires sans prénom restent anonymes : ils servent à l’analyse collective, pas au suivi individuel.</p>';
  t += '<div class="tbl"><table><thead><tr><th>Élève</th><th>Classe</th><th class="num">A</th><th class="num">B+C</th><th>Statut</th><th>Signal</th></tr></thead><tbody>';
  for (var i = 0; i < a.alertes.length; i++) {
    var r = a.alertes[i].r, s = a.alertes[i].s;
    t += '<tr><td>' + (r.prenom ? '<b>' + esc(r.prenom) + '</b>' : '<span class="muted">Anonyme</span> <span class="tiny muted">' + esc(String(r.id).slice(-4)) + '</span>') + '</td>';
    t += '<td>' + esc(r.classe) + '</td>';
    t += '<td class="num">' + s.A + '</td><td class="num">' + s.BC + '</td>';
    t += '<td><span class="badge ' + CLS_STATUT[s.statut] + '">' + LIB_STATUT[s.statut] + '</span></td>';
    t += '<td>' + (s.graves.length ? '<span class="badge b-h">Q' + s.graves.join(', Q') + '</span>' : '') + '</td></tr>';
  }
  t += '</tbody></table></div>';
  t += '<div class="warn small" style="margin-top:14px"><b>Protocole :</b> si un questionnaire nominatif révèle une situation de harcèlement, entretien obligatoire avec l’élève victime et mesures conservatoires. Si le questionnaire est anonyme, l’école doit tout de même organiser une action d’information et de sensibilisation dans la classe concernée.</div>';
  t += '</div>';
  return t;
}

/* --------------------------------- RAPPORT -------------------------------- */
function tabRapport() {
  var a = analyse();
  var t = '<div class="noprint" style="display:flex;gap:9px;flex-wrap:wrap;margin-bottom:14px">';
  t += '<button class="btn mini" onclick="window.print()">\uD83D\uDDA8\uFE0F Imprimer / Enregistrer en PDF</button>';
  t += '<button class="btn mini gris" onclick="copierSynthese()">\uD83D\uDCCB Copier la synthèse</button>';
  t += '</div>';
  if (!a.n) {
    return t + '<div class="info">Le rapport s’édite à partir des réponses enregistrées. Aucune réponse pour l’instant.</div>';
  }
  var d = new Date();
  var dateStr = DB.cfg.resp || (d.toLocaleDateString('fr-FR'));

  t += '<div class="card"><div class="prp-head"><div>';
  t += '<p class="t">Enquête « Non au harcèlement »</p>';
  t += '<p class="s">Grille d’auto-évaluation officielle — école élémentaire (CE2-CM2)</p>';
  t += '<p class="s"><b>' + esc(DB.cfg.nom || '') + '</b> · ' + esc(DB.cfg.circo || '') + '</p>';
  t += '</div><div style="text-align:right;font-size:9pt;color:#475569">';
  t += 'Passation : ' + esc(dateStr) + '<br>Année scolaire 2026-2027<br>Version ' + VERSION;
  t += '</div></div>';

  t += '<p class="small">Ce document présente les résultats de la grille d’auto-évaluation passée par les élèves, leur interprétation et les actions retenues. Il est destiné à l’équipe pédagogique, au conseil d’école et à la circonscription.</p>';

  t += '<div class="kpis" style="margin-top:12px">';
  t += '<div class="kpi p"><div class="v">' + a.n + '</div><div class="l">Questionnaires' + (a.effectif ? '<br>' + nf(a.part) + ' % de participation' : '') + '</div></div>';
  t += '<div class="kpi h"><div class="v">' + a.harc + '</div><div class="l">Harcèlement<br><span style="white-space:nowrap">' + nf(a.tauxH) + ' % · nat. 3 %</span></div></div>';
  t += '<div class="kpi s"><div class="v">' + a.surv + '</div><div class="l">À surveiller<br><span style="white-space:nowrap">' + nf(a.tauxS) + ' % · nat. 13 %</span></div></div>';
  t += '<div class="kpi g"><div class="v">' + a.rien + '</div><div class="l">Sans difficulté<br>' + nf(pct(a.rien, a.n)) + ' %</div></div>';
  t += '</div>';

  t += '<h3>1. Résultats par classe</h3><div class="tbl"><table><thead><tr><th>Classe</th><th class="num">Effectif</th><th class="num">Réponses</th><th class="num">Harcèlement</th><th class="num">À surveiller</th><th class="num">Sans difficulté</th></tr></thead><tbody>';
  for (var i = 0; i < a.parClasse.length; i++) {
    var c = a.parClasse[i];
    if (!c.tot && !c.eff) continue;
    t += '<tr><td>' + esc(c.n) + '</td><td class="num">' + (c.eff || '—') + '</td><td class="num">' + c.tot + '</td><td class="num">' + c.h + '</td><td class="num">' + c.s + '</td><td class="num">' + c.r + '</td></tr>';
  }
  t += '<tr class="tot"><td>École</td><td class="num">' + (a.effectif || '—') + '</td><td class="num">' + a.n + '</td><td class="num">' + a.harc + '</td><td class="num">' + a.surv + '</td><td class="num">' + a.rien + '</td></tr>';
  t += '</tbody></table></div>';

  if (a.parNiveau.length) {
    t += '<h3>Résultats par niveau</h3><div class="tbl"><table><thead><tr><th>Niveau</th><th class="num">Réponses</th><th class="num">Harcèlement</th><th class="num">À surveiller</th><th class="num">Sans difficulté</th></tr></thead><tbody>';
    for (var w = 0; w < a.parNiveau.length; w++) {
      var np = a.parNiveau[w];
      t += '<tr><td>' + esc(np.n) + '</td><td class="num">' + np.tot + '</td><td class="num">' + np.h + '</td><td class="num">' + np.s + '</td><td class="num">' + np.r + '</td></tr>';
    }
    t += '</tbody></table></div>';
  }
  t += '</div>';

  // page 2
  t += '<div class="card page"><h3 style="margin-top:0">2. Interprétation</h3>';
  var L = interpretation(a);
  for (i = 0; i < L.length; i++) {
    if (L[i].t === 'h') t += '<h3>' + esc(L[i].x) + '</h3>';
    else if (L[i].t === 'n') t += '<div class="warn small">' + esc(L[i].x) + '</div>';
    else t += '<p class="small" style="margin:0 0 7px">' + esc(L[i].x) + '</p>';
  }
  t += '</div>';

  t += '<div class="card"><h3 style="margin-top:0">3. Thèmes les plus déclarés</h3><div class="bars">';
  var tp = topQ(a, 8);
  for (i = 0; i < tp.length; i++) {
    t += barre('Q' + tp[i].n, Q[tp[i].n - 1].c, tp[i].p);
  }
  t += '</div></div>';

  t += '<div class="card page"><h3 style="margin-top:0">4. Actions retenues</h3>';
  var R = recommandations(a);
  t += '<ol class="small" style="margin:0;padding-left:18px;line-height:1.6">';
  for (i = 0; i < R.length; i++) t += '<li style="margin-bottom:6px">' + esc(R[i]) + '</li>';
  t += '</ol>';
  t += '<h3>5. Ce que cette enquête apporte au dossier de labellisation (niveau 1)</h3>';
  t += '<table><tbody>';
  t += '<tr><td style="width:26%"><b>Axe 1 — S’engager</b></td><td class="small">Enquête réalisée auprès de ' + a.n + ' élèves, résultats interprétés et partagés avec l’équipe : la preuve d’un diagnostic local, pas seulement d’une intention.</td></tr>';
  t += '<tr><td><b>Axe 2 — Prévenir</b></td><td class="small">Thèmes prioritaires identifiés par les élèves eux-mêmes (' + (tp.length ? esc(Q[tp[0].n - 1].c) : '—') + ' en tête) : les séances de prévention sont ciblées et évaluables.</td></tr>';
  t += '<tr><td><b>Axe 3 — Former</b></td><td class="small">Support de passation homogène pour tous les collègues, réutilisable d’une année sur l’autre.</td></tr>';
  t += '<tr><td><b>Axe 4 — Prendre en charge</b></td><td class="small">' + a.alertes.length + ' situation(s) identifiée(s) et orientée(s) vers l’équipe ressource ; faits graves : ' + a.graves + '.</td></tr>';
  t += '</tbody></table>';
  t += '<p class="tiny muted" style="margin-top:10px">Suivi proposé : nouvelle passation en fin d’année scolaire pour mesurer l’évolution des indicateurs.</p>';
  t += '</div>';

  t += '<div class="card"><p class="tiny muted" style="margin:0">Données anonymes agrégées. Les questionnaires individuels sont conservés par l’école jusqu’à la fin de l’année scolaire, et trois ans pour les questionnaires nominatifs révélant une situation de harcèlement, conformément au guide de passation 2026.</p></div>';
  return t;
}

function copierSynthese() {
  var txt = syntheseTexte(analyse());
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(txt).then(function () { alert('Synthèse copiée. Vous pouvez la coller dans un mail à l’IEN.'); },
      function () { secours(txt); });
  } else secours(txt);
}
function secours(txt) {
  var ta = document.createElement('textarea');
  ta.value = txt;
  document.body.appendChild(ta);
  ta.select();
  try { document.execCommand('copy'); alert('Synthèse copiée.'); } catch (e) { alert('Copie impossible. Utilisez Imprimer / PDF.'); }
  document.body.removeChild(ta);
}

/* --------------------------------- DONNÉES -------------------------------- */
function tabDonnees() {
  var a = analyse();
  var t = '<div class="warn"><b>Sauvegardez après chaque séance.</b> Les réponses sont stockées dans la mémoire du navigateur de cet appareil. Si quelqu’un vide l’historique de Chrome, tout est perdu. Un export = un fichier que vous gardez.</div>';

  t += '<div class="card"><h2>Exporter</h2>';
  t += '<p class="small">' + a.n + ' questionnaire(s) ' + (a.appareils > 1
        ? 'au total, issus de ' + a.appareils + ' postes de saisie.'
        : 'sur cet appareil.') + '</p>';
  t += '<div style="display:grid;gap:9px">';
  t += '<button class="btn" onclick="exportJSON()">\uD83D\uDCBE Sauvegarde complète (.json)</button>';
  t += '<p class="tiny muted" style="margin:-2px 0 6px 2px">À garder et à réutiliser pour fusionner plusieurs postes de saisie.</p>';
  t += '<button class="btn gris" onclick="exportCSV()">\uD83D\uDCCA Tableau anonyme (.csv)</button>';
  t += '<p class="tiny muted" style="margin:-2px 0 0 2px">Pour Excel ou LibreOffice. Sans prénom.</p>';
  t += '</div></div>';

  var ap = appareils(DB.rep);
  t += '<div class="card"><h2>Postes de saisie</h2>';
  if (!ap.length) {
    t += '<p class="small muted">Aucune réponse pour l’instant.</p></div>';
  } else {
    t += '<div class="tbl"><table><thead><tr><th>Poste</th><th class="num">Questionnaires</th></tr></thead><tbody>';
    for (var q = 0; q < ap.length; q++) {
      t += '<tr><td>' + (ap[q].id === 'origine' ? '<span class="muted">Avant le suivi</span>' : esc(ap[q].id)) +
           '</td><td class="num">' + ap[q].n + '</td></tr>';
    }
    t += '<tr class="tot"><td>Total</td><td class="num">' + ap.length + ' poste(s)</td></tr>';
    t += '</tbody></table></div>';
    t += '<p class="tiny muted" style="margin-top:8px">Après fusion, cette liste doit contenir tous les postes utilisés (un par enseignant en général). S’il en manque un, importez son fichier .json ci-dessous.</p></div>';
  }

  t += '<div class="card"><h2>Fusionner plusieurs postes de saisie</h2>';
  t += '<p class="small">Si plusieurs enseignants ont saisi les résultats, choisissez le fichier .json exporté par chacun. Les doublons sont automatiquement écartés : on peut réimporter sans risque.</p>';
  t += '<input type="file" id="fj" accept=".json,application/json" multiple onchange="importer(this)" style="width:100%;padding:12px;border:2px dashed #c7d2fe;border-radius:12px;background:#f8faff">';
  t += '</div>';

  t += '<div class="card"><h2>Effacer</h2>';
  t += '<p class="small muted">À ne faire qu’après avoir exporté la sauvegarde.</p>';
  t += '<button class="btn rouge" onclick="effacer()">\uD83D\uDDD1\uFE0F Effacer les réponses de cet appareil</button>';
  t += '</div>';
  return t;
}

function telecharger(nom, contenu, type) {
  var b = new Blob([contenu], { type: type || 'application/octet-stream' });
  var u = URL.createObjectURL(b);
  var a = document.createElement('a');
  a.href = u; a.download = nom;
  document.body.appendChild(a); a.click();
  setTimeout(function () { document.body.removeChild(a); URL.revokeObjectURL(u); }, 400);
}
function dateNom() {
  var d = new Date();
  function p(x) { return (x < 10 ? '0' : '') + x; }
  return d.getFullYear() + p(d.getMonth() + 1) + p(d.getDate()) + '-' + p(d.getHours()) + p(d.getMinutes());
}

function exportJSON() {
  var o = { app: 'NAH-ELEMENTAIRE', v: 1, version: VERSION, cfg: DB.cfg, rep: DB.rep, export: new Date().toISOString() };
  telecharger('harcelement-sauvegarde-' + dateNom() + '.json', JSON.stringify(o), 'application/json');
}

function exportCSV() {
  var sep = ';';
  var l = [];
  l.push(['id', 'classe', 'sexe', 'annee_naissance', 'total_A', 'total_B', 'total_C', 'total_BC', 'statut', 'faits_graves'].concat(arr(24).map(function (i) { return 'Q' + (i + 1); })));
  var lignes = [l[0].join(sep)];
  for (var i = 0; i < DB.rep.length; i++) {
    var r = DB.rep[i];
    if (!r.fini) continue;
    var s = calc(r);
    var row = [r.id, r.classe, r.sexe, r.annee, s.A, s.B, s.C, s.BC, LIB_STATUT[s.statut], s.graves.join(' ')].concat(r.q);
    lignes.push(row.join(sep));
  }
  telecharger('harcelement-donnees-' + dateNom() + '.csv', '\uFEFF' + lignes.join('\r\n'), 'text/csv;charset=utf-8');
}

function importer(inp) {
  var fs = inp.files;
  if (!fs || !fs.length) return;
  var aFaire = fs.length, ok = 0, dbl = 0, err = 0;
  var vus = {};
  for (var i = 0; i < DB.rep.length; i++) vus[DB.rep[i].id] = true;

  function fini() {
    aFaire--;
    if (aFaire > 0) return;
    sauver();
    alert('Fusion terminée.\n\n' + ok + ' questionnaire(s) ajouté(s)\n' + dbl + ' doublon(s) ignoré(s)' + (err ? '\n' + err + ' fichier(s) illisible(s)' : ''));
    dessiner();
  }

  for (var f = 0; f < fs.length; f++) {
    (function (file) {
      var rd = new FileReader();
      rd.onload = function () {
        try {
          var o = JSON.parse(rd.result);
          var rep = o.rep || (o.reponses || []);
          for (var k = 0; k < rep.length; k++) {
            var r = rep[k];
            if (!r || !r.id) { err++; continue; }
            if (vus[r.id]) { dbl++; continue; }
            vus[r.id] = true;
            DB.rep.push(r); ok++;
          }
        } catch (e) { err++; }
        fini();
      };
      rd.onerror = function () { err++; fini(); };
      rd.readAsText(file);
    })(fs[f]);
  }
}

function effacer() {
  if (!confirm('Effacer définitivement les ' + DB.rep.length + ' questionnaire(s) de cet appareil ?\n\nAssurez-vous d’avoir exporté la sauvegarde.')) return;
  DB.rep = [];
  sauver();
  dessiner();
}

/* -------------------------------- RÉGLAGES -------------------------------- */
function tabConfig() {
  var t = '<div class="card"><h2>École</h2>';
  t += '<div class="grp"><label>Nom de l’école</label>';
  t += '<input id="cnom" value="' + esc(DB.cfg.nom) + '" style="width:100%;padding:13px;border:2px solid #dde3ee;border-radius:12px;font-family:inherit;font-size:1rem"></div>';
  t += '<div class="grp"><label>Circonscription</label>';
  t += '<input id="ccirco" value="' + esc(DB.cfg.circo) + '" style="width:100%;padding:13px;border:2px solid #dde3ee;border-radius:12px;font-family:inherit;font-size:1rem"></div>';
  t += '<div class="grp"><label>Date de passation (pour le rapport)</label>';
  t += '<input id="cresp" value="' + esc(DB.cfg.resp) + '" placeholder="' + new Date().toLocaleDateString('fr-FR') + '" style="width:100%;padding:13px;border:2px solid #dde3ee;border-radius:12px;font-family:inherit;font-size:1rem"></div>';
  t += '</div>';

  t += '<div class="card"><h2>Classes et effectifs</h2>';
  t += '<p class="small muted">Une classe par ligne, au format <b>Nom ; effectif</b>. Les effectifs servent au taux de participation.</p>';
  t += '<textarea id="ccls" rows="6" style="width:100%;padding:13px;border:2px solid #dde3ee;border-radius:12px;font-family:inherit;font-size:1rem;line-height:1.7">' + esc(DB.cfg.classesTxt) + '</textarea>';
  t += '<p class="tiny muted">Exemple : <b>CM1/CM2 B ; 27</b></p>';
  t += '<button class="btn mini" style="margin-top:10px" onclick="listeEcole()">Rétablir la liste des 7 classes de l\u2019école</button>';
  t += '<p class="tiny muted" style="margin-top:6px">Cette liste doit être la même sur toutes les tablettes, sinon les élèves ne choisiront pas la même classe. Elle est déjà pré-remplie pour les 7 classes concernées par le questionnaire (CE2 A, CE2 B, CE2/CM1, CM1 A, CM1 B, CM1/CM2, CM2).</p></div>';

  t += '<div class="card"><h2>Code d’accès adulte</h2>';
  t += '<p class="small muted">4 chiffres. Il empêche les élèves d’ouvrir les résultats.</p>';
  t += '<input id="cpin" value="' + esc(DB.cfg.pin) + '" inputmode="numeric" maxlength="4" style="width:140px;padding:13px;border:2px solid #dde3ee;border-radius:12px;font-family:inherit;font-size:1.2rem;text-align:center;letter-spacing:6px"></div>';

  t += '<button class="btn" onclick="saveCfg()">Enregistrer les réglages</button>';
  t += '<p class="tiny muted" style="text-align:center;margin-top:14px">Version ' + VERSION + ' · ' + DB.rep.length + ' questionnaire(s) en mémoire</p>';
  return t;
}

/* Remet la liste officielle des 7 classes concernées par le questionnaire.
   Utile sur une tablette qui aurait gardé une ancienne liste. */
function listeEcole() {
  if (!confirm('Remplacer la liste actuelle par les 7 classes de l\u2019école ?\n\n' +
               'CE2 A · CE2 B · CE2/CM1 · CM1 A · CM1 B · CM1/CM2 · CM2\n\n' +
               'Les effectifs repasseront à 0 : ils sont à ressaisir.')) return;
  DB.cfg.classesTxt = CLASSES_DEFAUT;
  sauver();
  dessiner();
  toast('Liste des 7 classes rétablie');
}

function saveCfg() {
  DB.cfg.nom = $('cnom').value;
  DB.cfg.circo = $('ccirco').value;
  DB.cfg.resp = $('cresp').value;
  DB.cfg.classesTxt = $('ccls').value;
  var p = String($('cpin').value || '').replace(/[^0-9]/g, '').slice(0, 4);
  if (p.length === 4) DB.cfg.pin = p;
  sauver();
  alert('Réglages enregistrés.');
  dessiner();
}

/* ------------------------------- DÉMARRAGE -------------------------------- */
charger();
if (!DB.cfg.dev) {
  DB.cfg.dev = 'D' + Math.random().toString(36).slice(2, 5).toUpperCase();
  sauver();
}
if (window.speechSynthesis) {
  try { window.speechSynthesis.onvoiceschanged = function () {}; } catch (e) {}
}
dessiner();

/* installation sur l’écran d’accueil + marche hors connexion */
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function () {
    try { navigator.serviceWorker.register('sw.js'); } catch (e) {}
  });
}

/* mise à jour automatique (une seule fois) */
(function () {
  try {
    fetch('version.txt?t=' + Date.now(), { cache: 'no-store' })
      .then(function (r) { return r.text(); })
      .then(function (v) {
        v = (v || '').replace(/^\s+|\s+$/g, '');
        if (!v || v === VERSION) return;
        if (sessionStorage.getItem('maj_' + v)) return;
        sessionStorage.setItem('maj_' + v, '1');
        location.replace(location.pathname + '?v=' + encodeURIComponent(v));
      })
      .catch(function () {});
  } catch (e) {}
})();
