# 📈 QGIS-Plugin: Longitudinal

![QGIS Version](https://img.shields.io/badge/QGIS-3.x-green.svg)
![Status](https://img.shields.io/badge/Status-Experimental-yellow.svg)
![Version](https://img.shields.io/badge/Version-0.8-blue.svg)

**Longitudinal** ist ein spezialisiertes QGIS-Werkzeug zur Erzeugung von Längsschnitten (Profilen) entlang von Linien- und Punktdaten. Ideal für die Visualisierung von Höhenverläufen, Trassierungen oder Leitungsverläufen.

---

## 📖 Überblick

Das Plugin ermöglicht es, Höhendaten entlang einer definierten Achse (Linie) auszuwerten und grafisch darzustellen. Es wurde entwickelt, um Profile effizient und direkt innerhalb der QGIS-Umgebung zu generieren.

* **Kategorie:** Vermessung / Analyse / Wasserbau

---

## 🛠 Installation

### Der einfache Weg (Empfohlen)
1. Öffne **QGIS**.
2. Gehe im Menü auf **Erweiterungen** > **Erweiterungen verwalten und installieren...**.
3. Suche im Reiter "Alle" nach **"Longitudinal"**.
4. Klicke auf **Erweiterung installieren**.
   *(Hinweis: Da das Plugin teils als "Experimental" markiert ist, stelle sicher, dass in den Einstellungen "Auch experimentelle Erweiterungen anzeigen" aktiviert ist.)*

### Manuelle Installation (für Entwickler)
Falls du die neueste Beta-Version direkt von GitHub nutzen möchtest:
1. Lade das Repository als ZIP herunter.
2. Entpacke den Inhalt in deinen QGIS-Plugin-Ordner:
   `%AppData%\Roaming\QGIS\QGIS3\profiles\default\python\plugins` (Windows)
3. Starte QGIS neu und aktiviere das Plugin im Erweiterungen-Manager.

---

## ✨ Features

* **Profilauswertung:** Erstellt Längsschnitte basierend auf Liniengeometrien und zugehörigen Punkten.
* **Zweite Höhenlinie:** Unterstützung für eine zweite Referenzlinie (z.B. Gelände vs. Sohle).
* **Dynamische Höhen:** Die Höhe der zweiten Profillinie kann direkt im Dialog angepasst werden (neu in v0.8).
* **Interaktive Grafik:** Schnelle Visualisierung der vertikalen Geometrie.

---

## 🚀 Kurzanleitung

1. Wähle den **Linienlayer** (Achse) in QGIS aus.
2. Definiere die Quelllayer für die **Höhendaten** (z.B. Punktlayer mit Z-Werten).
3. Öffne das Longitudinal-Fenster, um die Grafik zu generieren.
4. Nutze die Einstellungen, um Skalierung und Beschriftung anzupassen.

---

## 🤝 Mitwirken & Support

Fehler gefunden oder Verbesserungsvorschläge?
* Erstelle ein **Issue** hier auf GitHub.
* Schau ins [Wiki](https://github.com/Amphibitus/longitudinal/wiki) für detaillierte Dokumentationen.

---
*Entwickelt von geoplaning GmbH – Präzise Profile direkt in QGIS.*# 📈 QGIS-Plugin: Longitudinal

![QGIS Version](https://img.shields.io/badge/QGIS-3.x-green.svg)
![Status](https://img.shields.io/badge/Status-Experimental-yellow.svg)
![Version](https://img.shields.io/badge/Version-0.8-blue.svg)

**Longitudinal** ist ein spezialisiertes QGIS-Werkzeug zur Erzeugung von Längsschnitten (Profilen) entlang von Linien- und Punktdaten. Es eignet sich hervorragend für die Visualisierung von Höhenverläufen, Trassierungen oder Leitungsverläufen direkt in QGIS.

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
