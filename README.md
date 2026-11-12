# Pinball Spatial

Un flipper dans l'espace qu'on construit soi-même. Pensé pour les enfants d'environ 8 ans, jouable sur ordinateur et sur mobile.

## Jouer

Ouvre `index.html` dans un navigateur. Aucune installation : tout tient dans ce seul fichier.

Pour le mettre en ligne gratuitement, active **GitHub Pages** dans les réglages du dépôt (Settings → Pages → branche `main`, dossier racine). Le jeu sera alors accessible à `https://noemilag.github.io/pinballspatial/`.

## Comment ça marche

- **Accueil** : choisis une table dans le carrousel (une table vide ou 5 tables prêtes), puis touche **Jouer**.
- **Créer** : glisse des pièces depuis le tiroir du bas, déplace-les, tourne-les et change leur taille. Tire la barre « Ambiance » vers le haut pour changer le décor et la musique.
- **Jouer** : 3 billes. Garde la barre d'espace (ou le bouton LANCER) enfoncée, puis lâche. Les flèches ← → (ou les deux moitiés de l'écran) bougent les batteurs.

### Les pièces

Bumper, paroi, arc, cible, batteurs gauche et droit, trou noir, portail, planète (avec gravité), propulseur et astéroïde.

### Les ambiances

Cosmique, Futuriste, Apocalyptique et Mission spatiale. Chacune a son décor, ses couleurs, ses bruitages et sa musique générée en direct.

## Sauvegarde

- Dans la version publiée sur claude.ai, les tables sauvées sont gardées en ligne et on peut les partager avec un code.
- Ouvert directement depuis ce dépôt (ou GitHub Pages), le jeu sauve les tables dans le navigateur de l'appareil seulement. Le partage par code n'est pas disponible dans ce cas.

## Technique

Un seul fichier HTML avec du CSS et du JavaScript intégrés, sans dépendance. Le rendu et la physique utilisent Canvas 2D, et la musique la Web Audio API. Les polices viennent de Google Fonts (Orbitron et Exo 2).
