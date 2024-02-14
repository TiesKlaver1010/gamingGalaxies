# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Y = Character("You", color = "#ffffff")
define flash = Fade (0.1, 0.0, 0.4, color ="#fff")
define danger = Fade(0.1, 0.0, 0.3, color= "bb393b")
image mansion bg = "mansion_bg.png"
image entrance = "entrance_begin.png"
image shadow = "shadow.png"
image red bg = "red bg.png"



# The game starts here.

label start:
     play music "audio/background.mp3"
     scene entrance_begin
     show entrance_begin

     Y "In the heart of the desolate countryside stood the horror mansion, a decrepit monument to forgotten days."
     Y "Its crumbling facade loomed like a specter, casting long shadows over the overgrown grounds."

     scene mansion bg
     Y "You, drawn by tales of its haunted past, ventured forth alone one moonlit night, their heart thrumming with trepidation. "
     Y "The mansion's interior was a labyrinth of darkness, its halls echoing with the whispers of the dead. "
     Y "Their footsteps echoed through the empty corridors as you ventured deeper, their lantern casting feeble light upon the decaying walls."
     Y "In a forgotten chamber, they discovered a dusty journal filled with cryptic writings. "
     Y "As they traced their fingers over the weathered pages, a chill wind swept through the room, carrying with it the scent of decay and despair."
     show mansion bg with hpunch
     Y "Suddenly, a figure materialized before them a specter draped in tattered robes, its eyes burning with an otherworldly fire."
     Y "It spoke of a curse that had befallen the mansion, of souls trapped within its walls for eternity."
     
menu:
     "What should i do?"
     "Fight back":
          jump Fight_back
     "Watch the spirit":
          jump Watch_spirit
     
          
label Fight_back:
     show shadow
     Y "In their moment of terror, their survival instinct surged forth like a beacon of hope in the darkness. "
     Y "With a desperate gasp for air, they fought against the icy grip of the specter, summoning every ounce of strength within them."
     show mansion_bg with danger
     Y "Summoning their willpower, They seized the crucifix around their neck, channeling their faith and determination into a radiant burst of light. "
     show mansion_bg with flash
     Y "The specter recoiled, its form waning as their resolve grew stronger."
     show mansion_bg with vpunch
     hide shadow 
     Y "With a final, valiant effort, they broke free from the spirit's grasp, stumbling backward into the chamber's shadows. Gasping for air"
     Y "They clutched the journal to their chest, the pages fluttering in the rush of wind that swept through the room."
     Y "In that moment of reprieve, they knew they had to act swiftly. "
     Y "With trembling hands, they clambered to their feet, their lantern flickering defiantly against the encroaching darkness."
     Y "With one last look at the haunted chamber, they turned and fled, their heart pounding with a mixture of fear and relief."
     Y "Through the labyrinthine halls they raced, her footsteps echoing like thunder against the cold, stone floors."
     show entrance_begin with vpunch
     Y "As they burst through the mansion's heavy doors, a rush of cool night air greeted them, carrying with it the promise of freedom. "
     Y "The moon cast its silvery glow upon the overgrown grounds, illuminating the path to safety."
     Y "With each step, they felt the weight of the mansion's curse lift from their shoulders, replaced by a newfound sense of resolve. "
     Y "Though their encounter had been harrowing, they emerged stronger, more resilient than before. "
     Y "And as they disappeared into the night, the horror mansion loomed behind them, its secrets buried once more in the depths of the past. "
     Y "Their tale would be one of survival, a testament to the indomitable spirit that resides within us all."
     return 

label Watch_spirit:
     scene mansion bg
     show shadow with vpunch
     Y "Your heart raced as the specter drew closer, its touch like ice upon their skin. With trembling hands, they reached for her crucifix, but it was too late. "
     Y "The spirit's icy grip tightened around her throat, draining the life from her fragile form."
     show shadow at right
     with danger
     

     Y "In their final moments, You glimpsed the mansion's dark secrets a tapestry of betrayal and anguish that stretched back through the ages."
     scene red bg
     Y "As your vision faded and the darkness consumed them, they became one with the haunted mansion, forever bound to its spectral embrace."
     Y "And so, the horror mansion claimed another victim, its hunger for souls unsated."
     Y "Your name would be whispered in hushed tones "
     Y "A cautionary tale for those who dared to tread upon its cursed grounds. "
     Y "And as the moon cast its pale light upon the mansion's crumbling walls"
     show mansion_bg 
     Y "the spirits within danced in triumph, their legacy of terror living on for eternity."
     return

    
    
          




     






     


    
     






