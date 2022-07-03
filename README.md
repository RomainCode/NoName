# Source code ![slime blurping](https://i.ibb.co/NZjr8DS/Slime.gif)

<!--- 
br : basic ligne return
* are <ul>
the syntax for images is ![Random Name](direct link)
for italic it's  ___example___
for bold it's __example__
for separation ligne it's multiple - 
for link same syntax but you put the ! at the end [Random Name](link)!
---> 
* main: Main folder.
  * __main.py__ : Contain main_code.
  
  * __config.py__ : Contain config of various elements and variables such as pygame color.
<br>  
<br>


  
* animations: A folder with classes that help to create animation into the game.


  * __animation.py__: Contain the classe used to import animation into pygame.
  
  * __animationManager.py__ : Contain the class used to manage the __animation__ class.
<br>  
<br> 

      
* assets: a folder that has all the medias of the project  
 
  * fonts: Contain all text font as .tff file
  
  * images : Contain all pictures/animations of the projects organise as sub files
  
  * flavicon.ico : it's the icon of the window
<br>  
<br> 

* entities: a folder containing all entities classes
  * __Character.py__: Contain the __Character__ class who is the player
  * __coin.py__: Contain the __coin__ class, i's s the currency that the player can gather
  * __entity.py__: Not defined
  * __staticEnemi.py__: Not Defined
  
  
<br>  
<br>

* game: a folder containing all scenes and class for the game
  * __game.py__: Contain the __Game__ class used in the  main loop to launch the game
  * __scene.py__: Contain the __Scene__ class that is all the different menu and scene available

  
  
<br>  
<br>

* gameLogic: a folder containing all calc around gain and upgrades
  * __gain.py__: Contain the __extractGain__ function used to manage all possibles gain in the game
  * __upgrade.py__: Contain the __Upgrade__, __UpgradableItem__ class and __GeneratorItem(UpgradableItem)__ subclass , check the file for more details

  
  
<br>  
<br>
<h2 align="center">Usages</h2>

Console commands
```py
Py main.py
```
<h1>à supprimer : si t'as le temps tu peux le continuer ducoup, t'as la syntaxe dans le code, je rajouterais des emojis sympa !<h1>
