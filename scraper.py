

def scrape(link):
    import pickle
    
    # TEMP!!!!!!!!
    # im just gonna use pre determinded content for now

    article_content = {
        "title": "A Black Hole in the Solar System?",
        "body": """
        If Earth was dense enough to collapse to a black hole, its horizon size would be the size of a marble. Fortunately, quantum mechanics prevents the Earth from such a collapse. According to the Heisenberg uncertainty principle, electrons compressed to a small volume must possess a large momentum or energy. Compression of Earth to the size of a marble would be accompanied by a soup of hot particles with energies similar to those achieved in the Large Hadron Collider at CERN, trillions of times above the core temperature of Earth.

Such a hot and dense soup of particles existed a trillionth of a second after the Big Bang. Therefore, a viable production channel for compact Earth-mass marbles is through a novel process in the early Universe that would make some regions sufficiently dense so that they would collapse to primordial black holes.

In principle, Earth-mass black holes could have made dark matter, the unknown constituent which dominates the cosmic mass budget by a factor of six relative to ordinary matter. However, observational data rule-out this possibility. In 1936 Albert Einstein calculated that a black hole which happens to pass across the line-of-sight to a distant star would focus the star’s light-rays and create a temporary brightening of the background star, known as a gravitational microlensing event. The human-size Hyper-Suprime-Cam camera of the 8.2 meter Subaru Telescope in Hawaii, monitored stars in our neighboring galaxy, Andromeda, and did not record any such brightening. This resulted in a tight upper limit of ten percent on the fraction of dark matter that can be made of Earth-mass black holes. Nevertheless, a smaller population of primordial black holes might exist.

Six years ago, the clustering of objects beyond Neptune hinted that a ninth planet with 5–10 Earth masses might reside in the Solar system at a distance of about 500 times the Earth-Sun separation. Searches for the reflected sunlight from Planet Nine came empty handed so far. But what if Planet Nine was actually a primordial black hole? A couple of years ago, I wrote a paper with my student, Amir Siraj, showing that if the conjectured Planet Nine is a primordial black hole, then it would inevitably collide with asteroids in the outer solar system, disrupt them by gravitational tide and accrete their matter. This process would result in a flare of light that would be detectable within a year of observations by the upcoming Legacy Survey of Space and Time (LSST) of the Vera C. Rubin observatory in Chile. Ed Witten suggested in another paper an alternative method to detect such a black hole, through its gravitational influence on a spacecraft passing near it.

If Planet Nine exists and it is a primordial black hole, it would be by far the nearest black hole known. Obviously, it would provide an excellent testbed for any theory that unifies quantum mechanics and gravity, like string theory. But let’s be more practical. Could humanity harness its tremendous potential for energy supply?

Currently, space agencies like NASA, Blue Origin of Jeff Bezos or SpaceX of Elon Musk, focus their attention on rocky destinations, such as the Moon or Mars. But what if we knew that a black hole like Planet Nine resided in the Solar system? Should governments and venture capitalists invest in getting there?

To assess the related engineering challenge, let us go through some numbers. A 10-Earth-mass black-hole fed by a kilometer-size asteroid every minute, would shine at the luminosity of the Sun. This happens to be the maximum luminosity of such a black hole, beyond which radiation pressure counteracts gravity and removes the fuel supply, according to a calculation presented a century ago by Sir Arthur Eddington. Feeding the black hole more vigorously than its Eddington limit would lead to a situation where the black hole vomits the extra matter in an outflow.

Having a black hole in our backyard would be particularly handy once the Sun will boil off all oceans on Earth in a billion years and eventually die about 7 billion years later. To keep itself warm and illuminated, humanity could light up the campfire of a primordial black hole in the outskirts of the solar system. With careful feeding, we could create an artificial Sun and establish a sustainable space station in orbit around it. Similar to a fireplace, we can tune the amount of heat and light that it produces through its fuel supply.

Life near a black hole could be far more comfortable than our current life on Earth. First, a black hole offers a much higher efficiency for converting rest mass to energy and hence requires less fuel than stars. Second, this heater has a stable engine that could last forever. Its output can be controlled and monitored to avoid the natural catastrophes associated with the evolution of stars like the Sun.

This is all to say that there might be a far more interesting destination for space travel in the Solar system than the familiar rocks of the Moon and Mars.

In case we choose to camp with a space station in orbit around the furnace of a primordial black hole, our future history books will not have nostalgia to the old days when humanity was bound to a fixed distance from a fusion reactor called the Sun, having no control over its heat supply and losing sleep over global climate change.

Other civilizations may have figured it out already. If we search carefully through our telescopes, we might realize that some of the stars in the sky are actually the campfires of primordial black holes, lit by extraterrestrials whose Sun had died and became a white dwarf by now. Most Sun-like stars formed ten billion years ago and consumed their nuclear fuel by now. It would be fun to discover that the bright companion of some white dwarfs is artificially lit by extraterrestrial civilizations. In ten trillion years — when all stars will be extinguished, these artificially-fueled campfires might be the only sources of light left in the darkness of the cosmos."""
    }

    with open("./content/og_article_content.dat", "wb") as f:
        pickle.dump(article_content, f)

    return article_content