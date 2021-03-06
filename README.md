# Overview

A python script for Path Of Exile controlled by in game text input (it scans the Client.txt file). Licenced under AGPLv3.

# Features

* poe.trade online/offline toggle. Either manual or toggled off during maps (between mapstart/map end). If you have an automatic online toggler (like acquisition / procurement) it won't work since they'll put you back online.
* Whisper (and others channels if you want) notifier. Uses notify-send ; this is primarily done for Linux, but it works on windows using [notify-send](http://vaskovsky.net/notify-send/). However i highly recommend using [PoeWhisperNotifier](https://github.com/Kapps/PoEWhisperNotifier) who is far more complete and easier to install / use on windows.
* Map recorder. Simplifies recording map by avoiding you to alt-tab every time you want to write it down. It scans only local channel, and message by you. Can also sends to a server to centralise map data.
* Generic recorder. This can works with any finite numbers of value you want to record. An example (suited for MF run on dominus/voll for example) is used here ; simply changes the "generic_headers" in config.ini

# Installation

  You can grab the binary in the release section for windows use. If you want to run the python script, you will need python3(>=3.3), [pyperclip](https://pypi.python.org/pypi/pyperclip/) (used to access clipboard data for MapRecorder), [click](https://pypi.python.org/pypi/click) (used to get the path to user config folder) and [pyglet](https://pypi.python.org/pypi/pyglet) (to play the warning/error sound).
  
# Quick start

  After installation, you'll need to set up your config.ini file. Important values :
* [global]usernames. A list of all your characters usernames (only character in this list will be able to trigger the script)
* [global].log_path. The path to the logs/ folder (not the Client.txt file). 
* [map_recorder].send_data. Activated by default, sends data to my server for mass map data.
* [map_recorder].output_path. The name of the .csv file where the data is stored
* [map_recorder].additional_iiq. Set it to your zana level
* [map_recorder].map_input. Either "tier" or "level" ; how the drop will be input'd (see map recorder for more explanation). Note that this doesn't affect mapstart/mapedit commands, who will always use 
For others values, the name should either be clear enough, or should be explicited in the comment before.

# Server

  I've setup a simple server to record map data from anyone who is interested. You can find the code in server/server.py. You can send data to it either automatically using the mapRecorder, or using csv_sender.py on a csv file. If you want to send your own data, the csv needs to be formatted like that :
``` 
"timestamp,character,level,pack size,IIQ,boss,ambush,beyond,domination,magic,zana,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82"
```

You can add column after the 82, it won't be used.

  If the server can't be reached, data will be saved locally in another file (named "unsent_"+[map_recorder].output_path) and can be manually sent using "map:force_send".
  
  You can get a .csv with data from everyone who sent some [on my server](http://poe.glorf.fr/map_data.csv) (this is updated every hour).
  
# GUI Display

 You can use a GUI to display your log. Relevant options in config.ini :
 * [global].alpha : transparency of the windows
 * [global].active : display it at the start of the game
 * [global].always_on_top : put the windows always on top

  You can deactivate (it just hide the windows actually) by typing "display off", and reactivating it by "display on".
  
  
# Map recorder


## Ctrl-C reporting

I recommend using this method for regulars maps (ie no ambush/domination mods added with zana, no unID maps, no additionnal IIQ with sacrifice piece/rampage mod ...). It's better to use the manual reporting method for them.

* Hover over the map and hit ctrl+C
* type "ms:" (or whatever keyword you defined) in chat.
* The script will take information from the clipboard, adn start a map according to that. It will also add the "additional_iiq" value from the config file.
* If there is info you can't get on the ctrl+c (IIQ from unID map, IIQ different because of sacrifice piece, ambush/domination mod from zana...), you can use the "medit:" command (see Available commands)

## Manual reporting
```
ms:75,14,134,m #Map level 75, 14 pack size, 134 IIQ, with magic monsters.
ml:76 #Got a level 76 map
ml:78,75 #You can input multiple maps
mn:loot mjolner #You can add as much notes as you want
me:1 # You killed 1 boss on this maps
```

## Available commands

* map start : (keyword)map_level,map_packsize,map_iiq[,abdmz]. The last is optional, and you can use 1, 2 or 3 of them. "a" is for Ambush, "d" for Domination, "b" is for Beyond mod, "m" is for magic monsters, "z" for zana. Default keyword is **"ms:"**
* map loot : (keyword)map_level[,map_n_level...]. Pretty straightforward. Default keyword is **"ml:"**. If you have [map_recorder].map_input to "tier", it will expect tier (so number in the range 1-15). If it's set to "level", it will expect level (number in the range 68-82)
* map note : (keyword)note. The note can be any size, comma will be removed though (to avoid breaking the .csv) ; multiples notes will be separated by a "|". Default keyword is **"mn:"**
* map end : (keyword)[boss_killed]. You can omit boss_killed, in this case the default value in config.py will be used. Default keyword is **"me:"**
* map abort : (keyword). Remove the last active map (if you made a mistake or whatever). Default keyword is **"ma:"**
* map edit : (keyword)level[,psize,iiq,abdmz]. Edit the last active map, same syntax as map_start. If IIQ/packsize exists, the current IIQ/packsize will be replaced by it. Default keyword is **"medit:"**
* map name : (keyword)Name. Update the name for the last active map. Default keyword is **"mname:"**

## Using your recorded data with a map analyser

In this example i'll be using [tackle70's spreadsheet](https://docs.google.com/spreadsheets/d/1qoTlUlq630svWh4oy_OQVOA-vqwm0DUGDpVft59Gnmw/edit?pli=1#gid=1866770458). If you have any problem with the .ods export, you can use [this one](http://exiletools.com/tackle70/).

What we have to do is open the map_data.csv file with Libreoffice (or excel), and move around the columns (works with any spreadsheet analyser). Unfortunately, tackle's spreadsheet have relatively different column (map drops goes from 82 to 68 where poewatcher records them from 68 to 82 among other things), and it's a bit annoying. Fortunately, poewatcher is a great program who can do it for you. Just write
`map:export_tackle` in your chat, it will put the good csv in "tackle_"+[map_recorder].output_path

After that :
* Open this file with libreoffice (with excel, follow [this](https://support.office.com/en-za/article/Import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba) tutorial to open a .csv)
* Open tackle's spreadsheet
* Remove map data from tackle's spreadsheet
* Copy your data from the first file, paste it in tackle's spreadsheet starting in H4.
* Wait a little for the calculations and enjoy the results :)


# Advanced

## Changing the keywords for action
  You need to look at the actions variable in the corresponding section in config.ini ([map_recorder] for example). Change simply the second value in the tuple by whatever you want. For example, if you want to use "map start:" as a keyword for starting the map, the line will be :
  ```
  actions = ("start", "map start:", "add_map")
  ```
  
## Misc

If you have a config.ini located in your app_dir (provided by click, see [the doc](http://click.pocoo.org/5/api/#click.get_app_dir) for more informations), rather than in the script directory, so you can change your config.ini without messing the git repo.


# Credits

* Thanks to /u/SayyadinaAtreides, /u/aggixx and abhaysrinivas3012 for their help debugging PoE Watcher 
* [extras/warning.wav](http://freesound.org/people/base_trix/sounds/50344/) by [base_trix](http://freesound.org/people/base_trix/) under [CC BY NC 3.0](http://creativecommons.org/licenses/by-nc/3.0/) 
* [extras/error.wav](https://freesound.org/people/Autistic%20Lucario/sounds/142608/) by [Autistic Lucario](https://freesound.org/people/Autistic%20Lucario/) under [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) 
