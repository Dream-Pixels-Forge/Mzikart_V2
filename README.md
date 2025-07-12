# 🎶 Mzikart V2 — Générateur de chansons IA

Mzikart V2 est une application web Python/Flask qui permet de générer automatiquement des chansons complètes (lyrics, voix IA, instru, mix) à partir de simples champs : paroles et tags.

### ✨ Fonctionnalités
- Générateur de paroles personnalisé (Verse / Chorus / Bridge)
- Voix IA réaliste (XTTS multilingue)
- Instrumental généré avec MusicGen (Meta)
- Mix audio automatique en `.mp3`
- Interface web moderne en Tailwind CSS

---

## 🚀 Démarrage

### 1. Cloner le dépôt

```bash
git clone https://github.com/Dream-Pixels-Forge/Mzikart_V2.git
cd Mzikart_V2
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt

# Installer MusicGen
git clone https://github.com/facebookresearch/audiocraft
cd audiocraft && pip install -e .
cd ..
```

> MusicGen nécessite PyTorch + CUDA pour les performances optimales.

### 3. Lancer l'application

```bash
python main.py
```

Rendez-vous ensuite sur [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 Structure

```
Mzikart_V2/
│
├── main.py                  # App Flask
├── voice_generator.py       # Génération voix IA
├── instru_generator.py      # Génération instru avec MusicGen
├── mixer.py                 # Mix final .mp3
├── requirements.txt         # Dépendances
├── templates/
│   └── index.html           # Interface web
└── static/                  # Fichiers audio générés
```

---

## 📜 Licence
MIT — libre de modifier, étendre et partager.

---

## ❤️ Projet par Dream Pixels Forge
Made with Python, Music & Magic.