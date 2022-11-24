# Morrowind_Voroni, a Almsivi/Divine Intervention Map Generator

![My Map](./show_maps/OpenMW_Almsivi_Intervention_Map.png)

Developed as an aid to [Tamriel Rebuilt](https://www.tamriel-rebuilt.org/) playthroughs, this tool generates maps for where you teleport to when casting Almsivi Intervention and Divine Intervention. Though these types of maps exist for the base, I couldn't find any that took into account the many new Temples and Shrines added by Tamriel Rebuilt. From there, I realized I should make a generator that could support any configuration of mods, including OpenMW.

![Old Map](https://images.uesp.net/4/4a/MW-map-Almsivi_Intervention.jpg)

![New Map](./show_maps/Almsivi_Intervention_Map-Basic.png)

## Disclaimer

THESE MAPS ARE NOT YET 100% PERFECT. Why?

The short answer is this is exceedingly tedious to verify in-game, as you would need to cast Intervention from every cell, with every combination of mods.

The long answer is that the base game calculates Interventions on a per-cell basis, and calculates distance based on the number of cells needed to traverse from the start point to the end point. This leads to a bunch of ties, and I haven't quite figured out what priority scheme it uses to resolve those ties. This accounts for small differences between my maps and the canonical ones on Vvardenfell (specifically, Divine Intervention from cell [9,2] taking you to Pelagiad in the base game). I'm working on it.

The shortest answer is that you should use OpenMW. I'm much more confident in the OpenMW maps because OpenMW uses continuous pythagorean distances to calculate the closest node. It also supports the Mournhold nodes, I think.

## How to Use

Clone the repository, then in `main.py` change `mod_list = [....]` to your set of mods, picking from the supported `mod_options` list. Run the program to generate the two maps for your configuration in the `generated_maps` folder.
