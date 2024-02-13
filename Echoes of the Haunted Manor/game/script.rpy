# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Y = Character("You", color = "#ffffff")
define flash = Fade (0.1, 0.0, 0.4, color ="#fff")
define danger = Fade(0.1, 0.0, 0.3, color= "bb393b")
image mansion bg = "mansion_bg.png"
image entrance = "entrance_begin.png"



# The game starts here.

label start:
     play music "audio/music.mp3"
     scene entrance_begin
     show entrance_begin

     Y "In the heart of the desolate countryside stood the horror mansion, a decrepit monument to forgotten days."
     Y "Its crumbling facade loomed like a specter, casting long shadows over the overgrown grounds."

     scene mansion bg
     Y "You, drawn by tales of its haunted past, ventured forth alone one moonlit night, their heart thrumming with trepidation. "
     Y "The mansion's interior was a labyrinth of darkness, its halls echoing with the whispers of the dead. "
     Y "Your footsteps echoed through the empty corridors as you ventured deeper, their lantern casting feeble light upon the decaying walls."
     Y "In a forgotten chamber, she discovered a dusty journal filled with cryptic writings. "
     Y "As they traced their fingers over the weathered pages, a chill wind swept through the room, carrying with it the scent of decay and despair."
     Y "Suddenly, a figure materialized before her—a specter draped in tattered robes, its eyes burning with an otherworldly fire."
     Y "It spoke of a curse that had befallen the mansion, of souls trapped within its walls for eternity."
     
            
     scene mansion
     show joe shock with vpunch
     Y "Your heart raced as the specter drew closer, its touch like ice upon their skin. With trembling hands, they reached for her crucifix, but it was too late. "
     Y "The spirit's icy grip tightened around her throat, draining the life from her fragile form."
     show joe shock at right
     with moveinright

     Y "In their final moments, You glimpsed the mansion's dark secrets—a tapestry of betrayal and anguish that stretched back through the ages."
     scene BG red
     show shadow with dissolve
     Y "As your vision faded and the darkness consumed them, they became one with the haunted mansion, forever bound to its spectral embrace."
     Y "And so, the horror mansion claimed another victim, its hunger for souls unsated."
     Y "Your name would be whispered in hushed tones "
     Y "A cautionary tale for those who dared to tread upon its cursed grounds. "
     Y "And as the moon cast its pale light upon the mansion's crumbling walls"
     hide shadow
     show sue miley with danger
     Y "the spirits within danced in triumph, their legacy of terror living on for eternity."
     hide sue miley
     scene BG commonroom
     show yui oc with dissolve
    
          




     






     


    
     






