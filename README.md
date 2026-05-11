# 📈 QGIS Plugin: Longitudinal

![QGIS Version](https://img.shields.io/badge/QGIS-3.x-green.svg)
![Version](https://img.shields.io/badge/Version-1.0-blue.svg)
![License](https://img.shields.io/badge/License-GPL--3.0-orange.svg)

**Longitudinal** is a specialized QGIS tool designed to generate longitudinal profiles (cross-sections) along line and point data. It significantly simplifies the visualization of elevation profiles for planners, engineers, and surveyors.

---

## 📖 Overview

This plugin generates precise elevation profiles directly from your GIS data. A key highlight is the integrated export interface, which enables a seamless transition from GIS to CAD environments.

* **Category:** Civil Engineering / Water Management / Surveying
* **CAD Integration:** High-quality **DXF Export**
* **Developer:** [Amphibitus](https://github.com/Amphibitus) / geoplaning GmbH

---

## ✨ Key Features

* **Profile Analysis:** Creates longitudinal sections based on line geometries (axes) and point layers (elevation data).
* **💾 DXF Export:** Export your finished profile directly as a **DXF file** for further processing in AutoCAD, BricsCAD, or Civil 3D.
* **Second Elevation Line:** Supports an additional reference line (e.g., comparing ground level vs. pipe/trench invert).
* **Dynamic Elevations:** Interactively adjust the height of the second profile line directly within the dialog window.
* **Flexible Scaling:** Full control over horizontal scales and vertical exaggeration for optimal visualization.

---

## 🛠 Installation

### Via QGIS (Recommended)
1. Open the **QGIS Plugin Manager** (*Plugins > Manage and Install Plugins...*).
2. Search for **"Longitudinal"** in the "All" tab.
3. Click **Install Plugin**.
   > **Note:** If the plugin does not appear, go to the manager's settings and enable the option *"Show also experimental plugins"*.

### Manual Installation
1. Download this repository as a ZIP file.
2. Extract the content into your QGIS plugin folder:
   * **Windows:** `%AppData%\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
   * **Linux/macOS:** `~/.local/share/QGIS/QGIS3/profiles/default\python\plugins`
3. Restart QGIS and enable the plugin in the Plugin Manager.

---

## 🚀 Quick Start

1. **Select Axis:** Select the line layer that defines the horizontal path of your profile.
2. **Set Elevation Source:** Choose the layers providing the Z-values (elevations).
3. **Generate Profile:** Create the graphical preview with a single click.
4. **CAD Export:** Use the export button to save a scaled DXF file for your CAD project.

---

## 🤝 Support & Feedback

Found a bug or have an idea for a new feature?
* Feel free to create an [Issue on GitHub](https://github.com/Amphibitus/longitudinal/issues).
* Check out the [Wiki](https://github.com/Amphibitus/longitudinal/wiki) for detailed instructions.

---
*Developed for efficient engineering directly within QGIS.*
