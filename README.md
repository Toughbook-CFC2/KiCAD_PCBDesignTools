# KiCAD PCB design plugins

The plugins in this project seek to add a variety of
usefull functions to the pcbnew tool of KiCAD. The need 
for these functions came up durign the conception phase for a 
highly symmetrical pcb with multiple instances of the same IC
footprint. Plugins for the following tasks were conceptionalized:

- Two Click Net Assign (TCNA)
- Multi Select (MSel)
- Set Net Multi
- Reflection Line
- Reflection Point

# Two Click Net Assign

This plugin allows to pick up the net that any pin or trace or via carries and
to transfer it to any other pin, trace or via or group thereof.
It becomes necessary after copying any element on the pcb because the copy 
doesn't inherit the net from the original (which makes sense) but a convenient
way to quickly assign nets to copied traces, vias or even pins of a footprint was needed.

Usage/Installation for the current Version is relatively easy:
Copy the TCNA.py script and the icon into your KiCAD plugin folder. In my case under Arch it is
at ~/.local/share/kicad/6.0/scripting/plugins/ 
You can start the plugin in pcbnew by clicking on the icon in the tool bar on the top right.
Then select a trace, via or pin you want to pick the net up from with a left click and press 'c'.
Select one or multiple traces, vias or pins and assign the net you picked up before by pressing 'v'. 

# Multi Select

This one is pretty simple. A tool to select all traces/vias that physically overlap with 
a root element. When a tricky trache between a few components has been successfully routed
and needs to be redone in the same way for multiple times still, this tool allows for 
the easy selection of all trace/via elements, that form that route to copy them.

Installation is the same as for TCNA.py

# Set Net Multi

A tool which allows the user to set the net for multiple elements at once.
Intended to work in conjuntion with multi select. Currently all elements of a 
routed trace have to be indiviually be set to a net in pcbnew.

Installation is the same as for TCNA.py

# Reflection Line

This tool opens a window with a selection box where mirroring along the y-axis(default) or
x-axis(when checked) can be selected and a text field where the coordinate (y or x) for the 
mirror line is asked. When pressing 'ok' all elements selected are mirrored along this
line. So if a via @x=10 is mirrored with a mirror line at 30, then a second via will apear
at x=50. This is also possible for Footprints. 
This makes the tool a bit dangerous, because most chips need their legs to be bent to still
connect to such a mirrored pad, and BGAs don't work at all anymore. Maybe a 
warning when the set of selected elements contains a footprint about these aspects is necessary.

Installation is the same as for TCNA.py

# Reflection Point

Same as reflection line, but x and y coordinates of elements are mirrored in a point.
(Not strictly required for my current project so low priority.)
