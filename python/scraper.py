

def scrape(link):
    import pickle
    import os

    # load env vars
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    BACKGROUND_RETRO_CLIP_LOC = os.getenv('BACKGROUND_RETRO_CLIP_LOC')
    BACKGROUND_MUSIC_LOC = os.getenv('BACKGROUND_MUSIC_LOC')
    SILENCE_AUDIO_LOC = os.getenv('SILENCE_AUDIO_LOC')
    CAPTION_DATA_LOC = os.getenv('CAPTION_DATA_LOC')
    TITLE_AUDIO_LOC = os.getenv('TITLE_AUDIO_LOC')
    BODY_AUDIO_LOC = os.getenv('BODY_AUDIO_LOC')
    OG_ARTICLE_LOC = os.getenv('OG_ARTICLE_LOC')
    NO_CAPS_AUDIO = os.getenv('NO_CAPS_AUDIO')
    NO_CAPS_VIDEO = os.getenv('NO_CAPS_VIDEO')
    FINAL_VIDEO = os.getenv('FINAL_VIDEO')
    CAPTION_DATA = os.getenv('CAPTION_DATA')
    
    # TEMP! ! ! ! ! ! ! ! 
    # im just gonna use pre determinded content for now

    article_content = {
        "title": "A dinosaur with a helmet-like head could fight like modern kangaroos. What kind of species is this?",
        "body": """
        Pachycephalosaurs had an unusually thick skull that looked like a gladiator’s helmet. Until now, it was thought that such a structure enabled these dinosaurs to strike from a fast run. Recent studies have shown that the animals fought in a similar way to how kangaroos fight.


[Photo: James St. John, CC BY 2.0, via Wikimedia Commons]
Pachycephalosaurus is a genus of thick-headed dinosaur that inhabited the territory of present-day North America during the Late Cretaceous period (from about 72 to 66 million years ago). It was herbivorous or omnivorous.

Paleontological studies have shown that the largest representative of pachycephalosaurs reached 4.5 meters in length and could weigh up to 450 kg. It moved on two hind limbs. The front limbs, on the other hand, were much shorter, so with its body structure it resembled larger theropods.

Paleontologists have created a 3D model of pachycephalosaurus
In ancient Greek, Pachycephalosaurus means “thick-headed lizard.” The name refers to the massive skull of this dinosaur. Paleontologists have thought for years that pachycephalosaurs used their heads in battles within the species. They fought each other mainly for dominance, territory, food and partners. However, with each successive discovery, this theory was increasingly called into question.

In the latest study, paleontologists at the Frost Museum of Science in Miami decided to take another look at the pachycephalosaur skeleton to learn more about its anatomy and fighting strategy. Based on the best-preserved fossil, the scientists created a 3D model to recreate its anatomy.

Did Pachycephalosaurus fight with its head, or with its head?
Previous research has mainly focused on the skulls of this type of dinosaur. This time, scientists decided to accurately reconstruct the animal’s body structure on the basis of, among other things, spinal bones. It turned out that the posture of the pachycephalosaur resembled that of a modern kangaroo. Moreover, the researchers claim that the animal would have moved in a similar manner.

“In our opinion, pachycephalosaurs used their tail in the same way that kangaroos do. When fighting, they use it as a support that they can lean on and keep their balance to launch a kick,” says Cary Woodruff, curator and paleontologist at the Frost Museum of Science. The researchers suggest that the tail of the pachycephalosaur could act as an “extra leg.”


Pachycephalosaur vertebrae were similar to those of a modern kangaroo
A specimen of Pachycephalosaurus wyomingensis found in the American Hell Creek Formation was analyzed. During laser scanning, paleontologists noticed that the dinosaur’s cervical vertebrae were undulated in a peculiar way. Prof. Woodruff’s team juxtaposed them with vertebrae of other animals that hit other individuals with their heads. These include Canadian sheep, Arctic muskoxen and deer.

It turned out that none of these mammals had such undulating vertebrae. Instead, kangaroo cervical vertebrae showed similar features. Moreover, both kangaroos and P. wyomingensis had very similar pelvic and tail bones. Prof. Woodruff points out that pachycephalosaurs could therefore have been pretty good kickboxers. However, this is still only a hypothesis for now.


[Photo: GFDL, CC BY 2.0, via Wikimedia Commons]
The authors of the discovery say they don’t rule out that these dinosaurs could have rammed each other with their heads, but they certainly didn’t do it at high speed. A 3D anatomical model of the animal showed that such an impact with momentum could have risked breaking some vertebrae.

“This would be more akin to a sumo fight than to knights on horseback charging at each other with their kicks”, the scientist concludes.

The research has not yet been published and reviewed in a scientific journal. The discovery was announced on November 2 at the Society of Vertebrate Paleontology’s annual conference, held in Toronto.
       """
    }

    with open(OG_ARTICLE_LOC, "wb") as f:
        pickle.dump(article_content, f)

    return article_content