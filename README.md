# 📈 QGIS-Plugin: Longitudinal

![QGIS Version](https://img.shields.io/badge/QGIS-3.x-green.svg)
![Status](https://img.shields.io/badge/Status-Experimental-yellow.svg)
![Version](https://img.shields.io/badge/Version-0.8-blue.svg)

**Longitudinal** ist ein spezialisiertes QGIS-Werkzeug zur Erzeugung von Längsschnitten (Profilen) entlang von Linien- und Punktdaten. Es eignet sich hervorragend für die Visualisierung von Höhenverläufen, Trassierungen oder Leitungsverläufen direkt in QGIS.

---

## 📖 Überblick

Das Plugin ermöglicht es, Höhendaten entlang einer definierten Achse (Linie) auszuwerten und grafisch darzustellen. Es wurde speziell für Anwender entwickelt, die schnell und unkompliziert Profilschnitte ohne komplexe externe Software erstellen möchten.

* **Entwickler:** Gerd Dreier (g3er geoplaning GmbH) / [Amphibitus](https://github.com/Amphibitus)
* **Kategorie:** Vermessung / Analyse / Wasserbau

---

## ✨ Features

* **Profilauswertung:** Erstellt Längsschnitte basierend auf Liniengeometrien und zugehörigen Punkten.
* **Zweite Höhenlinie:** Unterstützung für eine zweite Höhenlinie (z.B. Gelände vs. Sohle/Rohroberkante).
* **Dynamische Anpassung:** Die Höhe der zweiten Profillinie kann direkt im Tool angepasst werden (neu in v0.8).
* **Flexibilität:** Funktioniert sowohl mit Punktwolken/Punkten als auch mit interpolierten Linendaten.
* **Integration:** Nahtlose Arbeit innerhalb der QGIS-Oberfläche.

---

## 🚀 Installation & Nutzung

### Installation
1. Lade das Repository als ZIP herunter oder klone es in deinen QGIS Plugin-Ordner:
   ```bash
   git clone [https://github.com/Amphibitus/longitudinal.git](https://github.com/Amphibitus/longitudinal.git)
