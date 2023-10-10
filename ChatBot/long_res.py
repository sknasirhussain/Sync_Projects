""" Created this file to enter all the types of long responses to expect formt he bot """

import random

eat = 'I am a bot. only thing I "eat" or occupy is CPU and RAM! ;P '
facts = ['Honey Never Spoils: Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible. Honey\'s natural composition makes it resistant to bacteria and spoilage.',
         'The Eiffel Tower Can Be 15 cm Taller During the Summer: Due to the expansion of iron in the heat, the Eiffel Tower can grow about 15 centimeters (6 inches) in height during hot summer days.',
         'A Group of Flamingos Is Called a "Flamboyance": When flamingos gather together, they are referred to as a flamboyance. These social birds are known for their vibrant pink feathers and distinctive appearance.',
         'Octopuses Have Three Hearts: Octopuses have two branchial hearts that pump blood to the gills and one systemic heart that pumps oxygenated blood to the rest of the body. This unique circulatory system helps them survive in diverse underwater environments.',
         'Bananas Are Berries, But Strawberries Aren\'t: Botanically speaking, bananas are classified as berries because they have seeds on the inside. On the other hand, strawberries, despite their name, are not true berries because their seeds are on the outside.'][random.randrange(5)]

# afunction to handle unknown responses
def unknown():
    responses = ['Could you please re-phrase that?',
               'Sorry, that is something I cant help you with :(',
               'What does that mean?'][random.randrange(3)]
    
    return responses