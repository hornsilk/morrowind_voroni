# Morrowind_Voroni, a Almsivi/Divine Intervention Map Generator

![My Map](./display_maps/OpenMW_Almsivi_Intervention_Map.png)

Developed as an aid to [Tamriel Rebuilt](https://www.tamriel-rebuilt.org/) playthroughs, this tool generates maps for where you teleport to when casting Almsivi Intervention and Divine Intervention. Though these types of maps exist for the base, I couldn't find any that took into account the many new Temples and Shrines added by Tamriel Rebuilt. From there, I realized I should make a generator that could support any configuration of mods, including OpenMW.

![Old Map](https://images.uesp.net/4/4a/MW-map-Almsivi_Intervention.jpg)

![New Map](./display_maps/Almsivi_Intervention_Map-Basic.png)

## How to Use

Scroll up, click on the `generated_maps` folder, and download the images you want as reference for your TR playthrough. The filenames are long, but they describe the exact combo of mods used on that map (this is also printed on the top left of the map in case you rename it). I personally like to have [Improved Temple Experience](https://www.nexusmods.com/morrowind/mods/49373) installed, which just adds Almsivi Intervention to Ghostgate, Suran, Maar Gan and Molag Mar (and Vos, but TR also adds it to Vos).

## Disclaimer

THESE MAPS ARE NOT YET 100% PERFECT. Why?

The short answer is this is exceedingly tedious to verify in-game, as you would need to cast Intervention from every cell, with every combination of mods.

The long answer is that the base game calculates Interventions on a per-cell basis, and calculates distance based on the number of cells needed to traverse from the start point to the end point. This leads to a bunch of ties, and I haven't quite figured out what priority scheme it uses to resolve those ties. This accounts for small differences between my maps and the canonical ones on Vvardenfell (specifically, Divine Intervention from cell [9,2] taking you to Pelagiad in the base game). I'm working on it.

The shortest answer is that you should use OpenMW. I'm much more confident in the OpenMW maps because OpenMW uses continuous pythagorean distances to calculate the closest node. It also supports the Mournhold nodes, I think.

## How to Generate Your Own Maps

Clone the repository, then in `main.py` change `mod_list = [....]` to your set of mods, picking from the supported `mod_options` list. Run the program to generate the two maps for your configuration in the `generated_maps` folder.

Running this looks like typing `python main.py` into the command line. You will need to install a few python packages (it will ask for them why you try to run it) by typing `python -m pip install opencv-python` (with `opencv-python` replaced by whatever other packages you are missing).

To add in new Intervention points, look at `coord.json` and edit it by hand. `notes.txt` has a bit of guidance on using the Creation Set to list all of them for you with the exact cells.

If you want to change the area highlighted for current TR releases, you can run `release_clicker.py`. Controls are `left click` to add a cell to the release area, `right click` to remove it, `middle button` to every displayed cell, and `esc` to move to the next map. This updates the (raw) list of cells in `release_lookup_list.json`, so you could also just edit this by hand.

Maps are spliced together using current and future versions of the TR map, using `hack_maps.py`. Kudos to @Taniquetil for incredibly consistent map style that I could just use opencv to splice them as rectangles and not have to muck around in photoshop.
