from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import google.generativeai as genai

# ---------------------- CONFIG ---------------------- #
# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Upload folder path
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Flask app
app = Flask(__name__)
CORS(app, resources={
     r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})


# ---------------------- PROMPTS ---------------------- #
booking_prompt = """
You are a friendly and helpful chatbot assistant for the Calcutta Transport Corporation (CTC). 
You also act as a Kolkata tourist guide.


    name: "Victoria Memorial",
    location: "Maidan, Kolkata",
    description: "A large marble building dedicated to Queen Victoria, now a museum and tourist destination.",
    longDescription: "The Victoria Memorial is a majestic and iconic landmark of Kolkata, often regarded as the city's most splendid architectural marvel. Conceived by Lord Curzon, the then Viceroy of India, it was built between 1906 and 1921 as a tribute to Queen Victoria following her demise in 1901. The monument stands as a powerful symbol of the British Raj's grandeur and its historical imprint on the city. Constructed from pristine white Makrana marble, the same material used for the Taj Mahal, its architectural style is a sublime blend of British and Mughal elements, known as the Indo-Saracenic revivalist style. The design, crafted by architect William Emerson, features a grand central dome topped by the famous bronze statue, the 'Angel of Victory,' which rotates with the wind. The memorial is surrounded by 64 acres of lush, meticulously maintained gardens with serene water bodies, statues, and tree-lined pathways, making it a popular spot for locals and tourists to relax. Inside, the building serves as a museum housing an extensive collection of artifacts from the colonial era. It features 25 galleries, including the Royal Gallery, which showcases paintings of Queen Victoria and Prince Albert, and the Calcutta Gallery, which offers a vivid portrayal of the city's history and development. The collection includes rare books, manuscripts, sculptures, weapons, and paintings that provide a deep insight into India's past. The evening sound and light show, 'Son-et-Lumiere,' further enhances the visitor experience by narrating the story of Kolkata's heritage.",
    price: ["20 INR (Indians)", "200 INR (Foreigners)"],
    openingTime: "10:00 AM",
    closingTime: "5:00 PM",
    dayoff: "Monday",
    category: "Historical Place"

    name: "Science City",
    location: "EM Bypass, Kolkata",
    description: "India's largest science centre offering interactive exhibits, a space theatre, and science park.",
    longDescription: "Science City, Kolkata, is the largest science centre in the Indian subcontinent and a pioneering institution in the realm of science popularization. Inaugurated in 1997, it operates under the National Council of Science Museums (NCSM) and was designed to make science and technology engaging and accessible to people of all ages. Spread over a vast area, it is a major attraction for students, families, and science enthusiasts. The complex is divided into several distinct zones. The Dynamotion Hall is filled with interactive exhibits that allow visitors to experience the principles of physics and mechanics firsthand. The Space Odyssey section is a major highlight, featuring a state-of-the-art Space Theatre with a dome-shaped screen for immersive astronomical shows, a 3D vision theatre, and the Time Machine, a motion simulator that takes visitors on thrilling virtual journeys. Outside, the Science Park offers a unique learning environment with hands-on exhibits on life sciences, physics, and ecology set amidst lush greenery. Another popular attraction is the Evolution Park, which features a captivating walkthrough exhibition with large, robotic prehistoric animals that depict the story of evolution on Earth. The Maritime Centre provides insights into India's maritime history with displays of ship models and nautical artifacts. With its blend of education and entertainment, including a convention centre complex, Science City serves as a vital hub for scientific awareness, hosting seminars, workshops, and exhibitions throughout the year, truly living up to its motto of 'edutainment'.",
    price: ["60 INR (General)"],
    openingTime: "9:00 AM",
    closingTime: "8:00 PM",
    dayoff: "Open All Days",
    category: "Museum"
  
    name: "Eco Park",
    location: "New Town, Kolkata",
    description: "An urban park with themed gardens, boating, cycling, and recreational zones.",
    longDescription: "Eco Park, located in the planned satellite city of New Town, is a sprawling urban oasis that stands as a testament to modern landscape architecture and environmental conservation. Spanning over 480 acres and encircling a massive 112-acre water body, it is the largest park in India and a premier destination for recreation and relaxation in Kolkata. The park is thoughtfully divided into three main zones: the ecological zones, which include wetlands, grasslands, and an urban forest; the themed gardens and open spaces; and the urban recreational areas. One of its most famous attractions is the 'Seven Wonders of the World,' an area featuring impressive replicas of iconic global monuments like the Taj Mahal, Eiffel Tower, Christ the Redeemer, and the Great Wall of China, making it a favorite spot for photography. The themed gardens offer diverse experiences, from the tranquility of the Japanese Garden and the fragrance of the Rose Garden to the vibrant Butterfly Garden and the unique Mask Garden. For those seeking adventure and activity, Eco Park provides a plethora of options. Visitors can enjoy boating, kayaking, and water zorbing on the lake, or explore the vast grounds by cycling, duo-cycling, or taking a ride on the toy train. It also offers activities like archery, rifle shooting, and land zorbing. With numerous food courts, an artist's cottage, and spaces for cultural events, Eco Park successfully combines nature, art, and entertainment, providing a refreshing escape from the city's hustle and bustle for millions of visitors each year.",
    price: ["30 INR (Entry)"],
    openingTime: "2:30 PM",
    closingTime: "8:30 PM",
    dayoff: "Monday",
    category: "Park"
 
    name: "Nicco Park",
    location: "Salt Lake, Kolkata",
    description: "An amusement park known as the Disneyland of Bengal with rides and water park.",
    longDescription: "Nicco Park, affectionately known as the 'Disneyland of Bengal,' has been a cornerstone of entertainment and amusement in Kolkata for decades. Established in 1991, it was created not just for recreation but also with an educational purpose, aiming to provide 'edutainment' by incorporating scientific principles into its ride designs. This sprawling amusement park is located in the Salt Lake City area and offers a wide array of attractions for all age groups, making it a perfect destination for family outings and thrill-seekers alike. The park is home to over 35 different rides, ranging from gentle, family-friendly attractions like the Toy Train, Merry-Go-Round, and Paddle Boats to high-octane thrill rides such as the Cyclone roller coaster, the Water Chute, and the Flying Saucer. Each ride's operational mechanics are explained on accompanying plaques, subtly educating visitors about the underlying scientific concepts. A major extension of the park is 'Wet-O-Wild,' its dedicated water park, which features a variety of water slides, a wave pool, and splash zones, providing a much-needed respite during the hot summer months. Nicco Park also boasts other attractions like a 4D movie theatre, a bowling alley, and a haunted house called the 'River Cave Ride.' The park is beautifully landscaped with gardens and a large lake where visitors can enjoy boating. With its commitment to safety, regular introduction of new rides, and a vibrant atmosphere filled with fun and excitement, Nicco Park remains one of Eastern India's most beloved and enduring amusement destinations.",
    price:Entry Fee: ₹500 per person
    Includes entry plus access to 15 specified rides and attractions, such as Family Carousel, Vortex, Mirror Maze, Crazy Tea Party, Toy Train, MIG-21, Pirate Ship, Water Merry Go Round, Caterpillar, Flume Ride at Children's Corner, Moon Racker, Paddle Boat, Octopus, and Eiffel Tower. 
    Parks’ Package: ₹1,200 per person
    Grants access to all rides & attractions in both the Amusement Park and Water Park (Wet-O-Wild). Bull & Games are not included in this package. 
    openingTime: "10:30 AM",
    closingTime: "7:30 PM",
    dayoff: "Open All Days",
    category: "Park"

    name: "Birla Planetarium",
    location: "Maidan, Kolkata",
    description: "Asia’s largest planetarium offering astronomy shows in multiple languages.",
    longDescription: "The M. P. Birla Planetarium, located near the iconic Victoria Memorial in Kolkata, is a distinguished landmark for both astronomy enthusiasts and curious tourists. Inaugurated in 1963 by Prime Minister Jawaharlal Nehru, it is one of the oldest and largest planetariums in Asia. Its distinct single-storied, circular structure, designed in a traditional Indian architectural style reminiscent of the Sanchi stupa, makes it an easily recognizable building. The planetarium's primary mission is to foster scientific temper and disseminate knowledge about astronomy, astrophysics, and cosmology to the public in an engaging manner. The heart of the institution is its massive dome-shaped projection screen, where state-of-the-art projectors create a stunningly realistic simulation of the night sky. It regularly hosts captivating sky shows that explore a wide range of cosmic topics, from the mysteries of the solar system and constellations to the origins of the universe and the latest astronomical discoveries. These shows are meticulously produced and narrated, and are available in multiple languages including English, Bengali, and Hindi, catering to a diverse audience. The planetarium is also equipped with an electronics laboratory and an astronomy gallery that features a fascinating collection of paintings and astronomical models. Over the years, it has been continually upgraded with modern technology, including a hybrid projection system, to provide an even more immersive and educational experience. The Birla Planetarium remains a vital center for astronomical education in India, inspiring wonder and curiosity about the cosmos in generations of visitors.",
    price: ["120 INR (Adults)"],
    openingTime: "12:00 PM",
    closingTime: "7:00 PM",
    dayoff: "Open All Days",
    category: "Museum"
 
    name: "Howrah Bridge",
    location: "Howrah, Kolkata",
    description: "Iconic cantilever bridge over the Hooghly River, one of Kolkata’s landmarks.",
    longDescription: "The Howrah Bridge, officially named Rabindra Setu in 1965 in honor of the great poet Rabindranath Tagore, is arguably the most iconic symbol of Kolkata. This magnificent steel structure is a balanced cantilever bridge that spans the Hooghly River, connecting the twin cities of Kolkata and Howrah. Commissioned in 1943 during the height of World War II, it replaced an older pontoon bridge and was a phenomenal feat of engineering for its time. What makes the Howrah Bridge particularly remarkable is that it was constructed without the use of any nuts or bolts, utilizing a riveting system throughout its entire structure. It is one of the busiest cantilever bridges in the world, bearing the weight of over 100,000 vehicles and countless pedestrians every day. Its massive frame, built from high-tensile alloy steel, stands as a testament to industrial strength and architectural foresight. The bridge is not just a vital transportation artery but also a cultural landmark deeply embedded in the identity of the city. It has been featured in numerous films, photographs, and literary works, capturing the spirit and dynamism of Kolkata. The view from the bridge itself offers a panoramic spectacle of the bustling river life, with ferries crisscrossing the water and the historic ghats lining the banks. At night, the bridge is beautifully illuminated, transforming into a shimmering spectacle that dominates the city's skyline. For both residents and visitors, the Howrah Bridge is more than just a bridge; it is a living, breathing monument that represents the heart and soul of Kolkata.",
    price: ["Free Entry"],
    openingTime: "Open 24 Hours",
    closingTime: "Open 24 Hours",
    dayoff: "Open All Days",
    category: "Historical Place"
  
    name: "Indian Museum",
    location: "Chowringhee, Kolkata",
    description: "The largest and oldest museum in India, featuring art, archaeology, and natural history collections.",
    longDescription: "The Indian Museum in Kolkata, fondly known as 'Jadughar' (House of Magic), is a titan among cultural institutions in the Asia-Pacific region. Founded in 1814 by the Asiatic Society of Bengal, it is the ninth oldest museum in the world and the largest and oldest in India. Its majestic neoclassical building on Chowringhee Avenue is a landmark in itself, housing an extraordinary collection that spans six main sections: Art, Archaeology, Anthropology, Geology, Zoology, and Botany. The museum offers an encyclopedic journey through India's rich natural and cultural heritage. The Archaeology section is particularly renowned, featuring a priceless collection of artifacts, including the Bharhut Stupa railings, Gandhara sculptures depicting the life of Buddha, and ancient coins and inscriptions that trace millennia of Indian history. A major highlight is the Egyptian gallery, which contains a genuine 4,000-year-old mummy, a source of endless fascination for visitors. The Art section displays a vast array of textiles, miniature paintings, and decorative arts from across the country. In the Natural History galleries, visitors can marvel at massive skeletons of prehistoric animals, including dinosaurs and mammoths, alongside meticulously arranged exhibits of flora and fauna. The Anthropology gallery provides a deep dive into the diverse cultures and lifestyles of India's myriad communities. With over one hundred thousand exhibits, the Indian Museum serves as an invaluable repository of the subcontinent's history and biodiversity, offering an unparalleled educational experience and a profound glimpse into the soul of a nation.",
    price: ["50 INR (Indians)", "500 INR (Foreigners)"],
    openingTime: "10:00 AM",
    closingTime: "5:00 PM",
    dayoff: "Monday",
    category: "Museum"
  
    name: "Kolkata Library (National Library)",
    location: "Belvedere Estate, Alipore, Kolkata",
    description: "India’s largest library by volume, serving as a repository of books and periodicals.",
    longDescription: "The National Library of India, located on the beautiful Belvedere Estate in Alipore, Kolkata, is the largest library in the country by volume and a premier institution of national importance. Its primary objective is to acquire and conserve all printed material generated in India, as well as all foreign works published about the country. The library's history is rich and intertwined with the city's colonial past. The Belvedere House, which now serves as the main building, was once the official residence of the Lieutenant Governor of Bengal. After India's independence, the Imperial Library was merged with the Calcutta Public Library and renamed the National Library, and it was moved to its current prestigious location. The library's collection is staggering, boasting over 2.2 million books and countless periodicals, maps, manuscripts, and official documents, making it an invaluable resource for scholars, researchers, and students. It serves as a repository for nearly every book published in India, in all Indian languages, under the Delivery of Books and Newspapers (Public Libraries) Act, 1954. The sprawling 30-acre campus is serene and picturesque, with lush lawns and historic architecture that provide a tranquil atmosphere conducive to reading and research. In recent years, the library has embraced modernization through extensive digitization projects to preserve its rare and fragile collections and make them accessible to a global audience. It stands as a guardian of India's literary heritage and intellectual output, a testament to the nation's commitment to knowledge and learning.",
    price: ["Free Entry"],
    openingTime: "9:00 AM",
    closingTime: "8:00 PM",
    dayoff: "Sunday",
    category: "Museum"
  
    name: "St. Paul’s Cathedral",
    location: "Maidan, Kolkata",
    description: "A Gothic Revival Anglican cathedral and one of the city’s architectural landmarks.",
    longDescription: "St. Paul's Cathedral, situated at the southern end of the Maidan, is one of Kolkata's most significant and visually stunning architectural landmarks. As the first Episcopal Cathedral in the eastern world, it holds a prominent place in the city's colonial history. The cornerstone was laid in 1839, and the cathedral was consecrated in 1847. It was designed by Major William Nairn Forbes in a magnificent Gothic Revival style, characterized by its towering central spire, pointed arches, and large stained-glass windows. The original spire was destroyed by earthquakes in 1897 and 1934, after which it was rebuilt, modeled on the Bell Harry Tower of Canterbury Cathedral. The interior of the cathedral is equally impressive, exuding an atmosphere of peace and solemnity. The cavernous nave, polished wooden pews, and the ornate high altar create a space of spiritual reverence. The eastern wall is adorned with exquisite stained-glass windows designed by the famed pre-Raphaelite artist Sir Edward Burne-Jones. The cathedral also houses numerous memorials and plaques dedicated to notable British figures who lived and served in India. The well-maintained grounds surrounding the cathedral offer a quiet retreat from the bustling city. Its proximity to other major landmarks like the Victoria Memorial and the Birla Planetarium makes it part of a popular tourist circuit. St. Paul's Cathedral is not only an active place of worship for the Anglican community but also a historical monument that attracts visitors of all faiths, who come to admire its architectural splendor and soak in its serene ambiance.",
    price: ["Free Entry"],
    openingTime: "9:00 AM",
    closingTime: "6:00 PM",
    dayoff: "Open All Days",
    category: "Historical Place"
 
    name: "Alipore Zoo",
    location: "Alipore, Kolkata",
    description: "India’s oldest zoological park, home to tigers, elephants, and a variety of fauna.",
    longDescription: "The Alipore Zoological Gardens, commonly known as Alipore Zoo, holds the distinction of being India's oldest formally stated zoological park. Established in 1876, it has been a popular attraction in Kolkata for nearly 150 years. Located in the Alipore area of the city, the zoo is spread over 46.5 acres and provides a home to a wide array of fauna, including mammals, reptiles, and birds. It has played a significant role in wildlife conservation and public education about biodiversity over the decades. The zoo is particularly famous for its collection of megafauna. It houses majestic Royal Bengal tigers, African lions, elephants, one-horned rhinoceroses, and several species of deer and primates. The reptile house is another major draw, featuring venomous snakes like the king cobra and Russell's viper, as well as large crocodiles and gharials. The zoo's aviaries are filled with a colorful variety of native and exotic birds. The Alipore Zoo is also known for its historical significance, particularly for being the home of 'Adwaita,' an Aldabra giant tortoise that was reputedly over 250 years old when it died in 2006. The zoo has been undergoing significant modernization efforts to improve animal enclosures, moving towards more naturalistic habitats to enhance the well-being of its inhabitants. With its lush greenery, large water bodies, and diverse animal population, the Alipore Zoo remains a cherished destination for families, school children, and nature lovers, offering a valuable window into the animal kingdom right in the heart of the city.",
    price: ["30 INR (Adults)", "10 INR (Children)"],
    openingTime: "9:00 AM",
    closingTime: "5:00 PM",
    dayoff: "Thursday",
    category: "Park"
 
    
    name: "Birla Industrial and Technological Museum",
    location: "Gurusahai Dutta Rd, Kolkata",
    description: "Interactive science and technology museum, part of the National Council of Science Museums.",
    longDescription: "The Birla Industrial and Technological Museum (BITM), located on Gurusaday Road, is a pioneering institution that set the trend for interactive science museums in India. It was the country's first science museum, inaugurated in 1959. Housed in a beautiful colonial-era mansion that once belonged to the Tagore family and was later acquired by industrialist G.D. Birla, the museum is now part of the National Council of Science Museums (NCSM). BITM's core philosophy is to make learning science a fun, hands-on experience. It features numerous galleries dedicated to various scientific disciplines, including physics, biotechnology, electricity, and mathematics. Unlike traditional museums, most exhibits at BITM are interactive, encouraging visitors, especially children, to touch, play, and experiment to understand complex scientific principles. Popular attractions include the mock-up coal mine, which provides a realistic simulation of an underground mine, and the fascinating physics gallery with exhibits on sound, light, and mechanics. The museum also regularly hosts exciting science shows, such as the High Voltage Show and the 'Science Magic' demonstration, which are both educational and highly entertaining. The Taramandal, a small inflatable planetarium, offers introductory shows on astronomy for young children. BITM plays a crucial role in supplementing science education outside the classroom through its mobile science exhibition buses that travel to rural areas, its well-organized workshops, seminars, and science fairs. It continues to be a vital educational hub, sparking curiosity and nurturing a scientific temper among the youth of the nation.",
    price: ["50 INR (Adults)", "20 INR (Students)"],
    openingTime: "10:00 AM",
    closingTime: "6:00 PM",
    dayoff: "Monday",
    category: "Museum"
  
    name: "Nehru Children Museum",
    location: "Maidan, Kolkata",
    description: "A museum dedicated to children featuring dolls, toys, and epics like Ramayana & Mahabharata.",
    longDescription: "The Nehru Children's Museum, located on Chowringhee Road, is a magical place designed to delight and educate young minds. Established in 1972, this unique museum is a treasure trove of dolls, toys, and miniature models that capture the imagination of every child who walks through its doors. The museum is spread over four floors, each with a distinct and captivating theme. One of the most enchanting sections is the Dolls Gallery, which showcases a vast collection of dolls from over 88 countries, all dressed in their traditional attire. This gallery serves as a wonderful introduction to global cultures, diversity, and costumes. The museum is particularly famous for its two epic galleries: the Ramayana Gallery and the Mahabharata Gallery. Here, the great Indian epics are narrated through a series of stunningly detailed miniature clay models, bringing the ancient stories to life in a three-dimensional format that is both engaging and easy for children to understand. Each diorama is a work of art, meticulously crafted to depict key scenes and characters from the tales. Another section is dedicated to toys, featuring a charming collection of antique and modern toys from around the world. The museum also has a gallery dedicated to the life and work of Ganesha. The Nehru Children's Museum successfully creates a world of wonder, blending learning with entertainment. It offers a nostalgic journey for adults and an unforgettable experience for children, making it a cherished institution in Kolkata's cultural landscape.",
    price: ["20 INR (Children)", "50 INR (Adults)"],
    openingTime: "11:00 AM",
    closingTime: "7:00 PM",
    dayoff: "Monday",
    category: "Museum"
  
    name: "Rabindra Bharati Museum (Jorasanko Thakur Bari)",
    location: "Jorasanko, Kolkata",
    description: "The ancestral home of Rabindranath Tagore, now a museum on his life and works.",
    longDescription: "Jorasanko Thakur Bari, the ancestral home of the illustrious Tagore family, is one of Kolkata's most revered cultural and historical landmarks. Located in the Jorasanko area of North Kolkata, this sprawling 18th-century mansion is the birthplace of Rabindranath Tagore, the first non-European Nobel laureate, and the place where he spent most of his life and breathed his last. Today, the house has been converted into the Rabindra Bharati Museum, a part of the Rabindra Bharati University, which is dedicated to preserving and showcasing the life, works, and philosophies of Tagore and other prominent members of his highly influential family. A visit to the museum is a poignant journey back in time. Visitors can walk through the various rooms and verandas used by Tagore, which are preserved with his personal belongings, including his writing desk, chair, robes, and paintings. The museum houses an extensive collection of his manuscripts, letters, and rare photographs. The galleries are thoughtfully curated, with separate sections dedicated to his life in India and abroad, his interactions with global luminaries like Albert Einstein, and his artistic pursuits. The museum also sheds light on the broader cultural and social contributions of the Tagore family, who were at the forefront of the Bengal Renaissance. It features artworks by his nephews, Abanindranath Tagore and Gaganendranath Tagore, who were pioneers of the Bengal School of Art. Jorasanko Thakur Bari is more than just a museum; it is a pilgrimage site for lovers of literature and art, a place where the spirit of one of history's greatest polymaths still resonates.",
    price: ["30 INR (Indians)", "150 INR (Foreigners)"],
    openingTime: "10:30 AM",
    closingTime: "5:00 PM",
    dayoff: "Monday",
    category: "Museum"
  
    name: "Shibpur Botanical Garden (Acharya Jagadish Chandra Bose Botanical Garden)",
    location: "Shibpur, Howrah (Kolkata)",
    description: "One of India’s oldest botanical gardens, home to the famous Great Banyan Tree.",
    longDescription: "The Acharya Jagadish Chandra Bose Indian Botanic Garden, more commonly known as the Shibpur Botanical Garden, is a vast expanse of greenery and biodiversity located in Shibpur, Howrah, near Kolkata. Established in 1787 by Colonel Robert Kyd of the British East India Company, it is one of the oldest and largest botanical gardens in Asia. Spanning over 273 acres, the garden's original purpose was to cultivate commercially viable plants like teak and spices, but it soon evolved into a major center for horticultural and botanical research. Today, it is under the jurisdiction of the Botanical Survey of India and houses an incredible collection of over 12,000 plant specimens, including many rare and endangered species from across the globe. The garden's most famous and awe-inspiring attraction is The Great Banyan Tree. This single tree, with its massive canopy and thousands of aerial prop roots, covers an area of nearly 4.67 acres, making it the widest tree in the world. It looks more like a dense forest than an individual tree and is a breathtaking sight. Beyond the Great Banyan, the garden features numerous other collections, such as a palm house (palmetum), a cactus house, orchid houses, and serene lakes adorned with giant water lilies. The landscaped gardens and tree-lined avenues provide a tranquil escape from the urban environment, making it a popular spot for nature lovers, botanists, photographers, and families seeking a peaceful day out. It remains a vital institution for botanical conservation and research in India.",
    price: ["20 INR (Entry)"],
    openingTime: "10:00 AM",
    closingTime: "5:00 PM",
    dayoff: "Monday",
    category: "Park"
  
    name: "Marble Palace",
    location: "Machuabazar, Kolkata",
    description: "A 19th-century mansion with a collection of Western sculptures, paintings, and antiques.",
    longDescription: "The Marble Palace, located in a quiet lane in North Kolkata, is one of the city's most unusual and fascinating landmarks. This opulent 19th-century mansion was built in 1835 by Raja Rajendra Mullick, a wealthy Bengali merchant and an avid art collector. The palace is an architectural marvel, constructed in a neoclassical style with traditional Bengali influences, featuring open courtyards and tall, fluted Corinthian columns. Its name derives from the extensive use of over 126 different types of imported Italian marble for its walls, floors, and sculptures, creating an aura of extravagant splendor. The interior is a veritable treasure trove of Western art and antiques, reflecting the collector's passion. The halls are filled with priceless statues, including original works by renowned European artists like Reuben and Reynolds, intricate glassware, and antique furniture. The collection of paintings is particularly noteworthy, featuring works by both Western masters and Indian artists. The palace also houses a private zoo, the Marble Palace Zoo, which is considered the first zoo opened in India and is home to various birds and animals. Visiting the Marble Palace is a unique experience, as it remains a private residence of the Mullick family. Access is restricted, and visitors need to obtain a permit from the West Bengal Tourism Information Bureau beforehand. This exclusivity adds to its mystique, offering a rare and preserved glimpse into the lavish lifestyle and artistic tastes of the 19th-century Calcutta elite.",
    price: ["Free Entry (with permit)"],
    openingTime: "10:00 AM",
    closingTime: "4:00 PM",
    dayoff: "Monday & Thursday",
    category: "Historical Place"
 
    name: "Town Hall",
    location: "Esplanade, Kolkata",
    description: "A historical building used for cultural events, exhibitions, and gatherings.",
    longDescription: "Kolkata's Town Hall, standing gracefully in the B.B.D. Bagh area near the Esplanade, is a magnificent heritage building that embodies the city's rich architectural and political history. Built in 1813 in a Roman-Doric architectural style, it was constructed through a public lottery to provide a venue for social gatherings for the European community. The building's grand facade, with its majestic two-story portico and massive Doric columns, exudes an aura of classical elegance and authority. For much of the 19th and early 20th centuries, it was the epicenter of public life in Calcutta, hosting grand receptions, official meetings, and cultural performances. Over the years, the building fell into disrepair but was saved from demolition by public outcry and underwent extensive restoration by the Kolkata Municipal Corporation and the Archaeological Survey of India. It was reopened to the public in 2007 as a museum and cultural space. The ground floor now houses the 'Kolkata Museum,' which beautifully chronicles the story of the city from its inception to the present day through a collection of rare archival photographs, maps, models, and artifacts. The upper floor features a grand, high-ceilinged hall that is used for exhibitions, seminars, and cultural events, thus reviving its original purpose as a public gathering space. The Town Hall is not just a relic of the past; it is a vibrant institution that connects Kolkata's colonial legacy with its contemporary cultural identity, standing as a proud symbol of the city's heritage.",
    price: ["Free Entry"],
    openingTime: "10:00 AM",
    closingTime: "5:00 PM",
    dayoff: "Sunday",
    category: "Historical Place"

    name: "Metcalfe Hall",
    location: "Esplanade, Kolkata",
    description: "A neoclassical heritage building housing exhibitions by the ASI and cultural institutions.",
    longDescription: "Metcalfe Hall is a striking heritage building located at the junction of Strand Road and Hare Street in the heart of Kolkata's business district. Its distinctive neoclassical architecture, heavily influenced by the classical temples of ancient Greece, makes it a prominent landmark. The building is characterized by a colossal colonnade of thirty Corinthian columns that rise from a high plinth, supporting a massive entablature. Built between 1840 and 1844, it was named after Sir Charles T. Metcalfe, a former Governor-General of India, in honor of his efforts to promote a free press. Originally, the building was designed to house the Calcutta Public Library, which later formed the nucleus of the National Library of India's collection. After the library was relocated, Metcalfe Hall served various purposes, including housing the Imperial Library. Today, this magnificent structure is under the care of the Archaeological Survey of India (ASI). After a period of restoration, it has been repurposed into a vibrant exhibition space. The ground floor now features an exhibition titled 'Ami Kolkata' (I am Kolkata), which showcases the tangible and intangible heritage of the city through interactive displays and artifacts. The upper floors often host temporary exhibitions and cultural events organized by institutions like the Asiatic Society and the Victoria Memorial Hall. Metcalfe Hall stands as a beautiful example of adaptive reuse of a heritage structure, successfully bridging its historical past with a dynamic cultural present, and offering visitors a unique window into the soul of Kolkata.",
    price: ["Free Entry"],
    openingTime: "10:00 AM",
    closingTime: "5:00 PM",
    dayoff: "Sunday",
    category: "Historical Place"
  
    name: "Jorasanko Thakur Bari",
    location: "Jorasanko, Kolkata",
    description: "The ancestral home of Rabindranath Tagore, now a museum dedicated to his life and works.",
    longDescription: "Jorasanko Thakur Bari, the ancestral seat of the Tagore family, is a cultural sanctuary nestled in the bustling lanes of North Kolkata. This historic mansion is profoundly significant as it was the birthplace of Rabindranath Tagore, Asia's first Nobel laureate, and the home where he spent his formative years and eventually passed away in 1941. The name 'Thakur Bari' translates to 'House of the Tagores.' The sprawling red-brick building is a quintessential example of the architectural style favored by the Bengali aristocracy of the 18th and 19th centuries. Today, it functions as the Rabindra Bharati Museum, an integral part of Rabindra Bharati University, which is dedicated to celebrating the life and immense contributions of Tagore and his extraordinarily talented family, who were pivotal figures in the Bengal Renaissance. A tour of the museum is a deeply immersive experience. Visitors can explore the preserved living quarters of Tagore, viewing his personal artifacts, from his writing desk to the clothes he wore. The museum's galleries are thoughtfully arranged, chronologically tracing his journey as a poet, novelist, musician, painter, and philosopher. It showcases a rich collection of his paintings, original manuscripts, letters exchanged with global figures, and rare family photographs. Beyond Rabindranath, the museum also highlights the artistic contributions of other family members, including the pioneering artists Abanindranath Tagore and Gaganendranath Tagore. Jorasanko Thakur Bari is not merely a memorial; it is a hallowed ground that continues to inspire artists, writers, and thinkers, offering a profound insight into the mind of one of history's greatest creative geniuses.",
    price: ["30 INR (Indians)", "150 INR (Foreigners)"],
    openingTime: "10:30 AM",
    closingTime: "5:00 PM",
    dayoff: "Monday",
    category: "Museum"
  
    
    name: "Shaheed Minar",
    location: "Esplanade, Kolkata",
    description: "Also known as Ochterlony Monument, built in 1828, now a memorial to Indian independence martyrs.",
    longDescription: "The Shaheed Minar, or Martyrs' Monument, stands tall and proud in the northern part of the Maidan in Esplanade, Kolkata. This towering monument has a dual identity, reflecting the city's transition from a colonial capital to the heart of India's freedom struggle. Originally named the Ochterlony Monument, it was erected in 1828 by the British East India Company to commemorate the military victory of Sir David Ochterlony in the Anglo-Nepalese War (1814–1816). Its architectural style is a unique and eclectic blend of different influences: the base is built in an Egyptian style, the column itself is a classic Syrian pillar, and the dome on top is Turkish in design. This 48-meter (157-foot) high structure offers panoramic views of the cityscape to those who climb its 223-step spiral staircase, though public access is now often restricted. After India gained independence, the monument was rededicated in 1969 to the memory of the martyrs of the Indian independence movement, and its name was officially changed to 'Shaheed Minar.' Since then, the vast field at its base, known as the Shaheed Minar Maidan, has become a significant political landmark. It has served as the venue for countless political rallies, public meetings, and cultural fairs, becoming a powerful symbol of public expression and democratic assembly in West Bengal. The Shaheed Minar thus stands as a silent witness to history, its identity evolving from a symbol of colonial might to a revered tribute to national sacrifice and freedom.",
    price: ["Free Entry"],
    openingTime: "10:00 AM",
    closingTime: "6:00 PM",
    dayoff: "Sunday",
    category: "Historical Place"
  
    name: "Netaji Bhawan",
    location: "Elgin Road, Kolkata",
    description: "Residence of Netaji Subhash Chandra Bose, now preserved as a museum with his memorabilia.",
    longDescription: "Netaji Bhawan, located on Elgin Road in South Kolkata, is a place of immense historical and national importance. This was the ancestral residence of one of India's most revered freedom fighters, Netaji Subhas Chandra Bose. The house has been meticulously preserved and converted into a museum and research center, managed by the Netaji Research Bureau. It offers a deeply personal and moving glimpse into the life and work of this iconic leader. The building itself is a typical early 20th-century Bengali mansion. A visit to Netaji Bhawan is like stepping into history. The museum showcases Netaji's personal belongings, including his bedroom, furniture, clothes, and an extensive collection of photographs that chronicle his life from childhood to his leadership of the Indian National Army (INA). The most captivating exhibit for many visitors is the very room from which he planned and executed his 'Great Escape' in 1941, when he slipped past British surveillance and fled the country to continue his fight for India's freedom from abroad. The German Wanderer sedan car, in which he made his daring escape, is also preserved in a glass enclosure and is a key attraction. The museum houses a rich archive of his letters, writings, and important documents related to the INA. The library and archives serve as a vital resource for scholars and historians researching the Indian independence movement. Netaji Bhawan is more than a museum; it is a shrine of inspiration, preserving the legacy of a man whose courage and patriotism continue to resonate with millions.",
    price: ["20 INR (Indians)", "100 INR (Foreigners)"],
    openingTime: "11:00 AM",
    closingTime: "4:30 PM",
    dayoff: "Monday",
    category: "Museum"
  
    name: "Mother’s Wax Museum",
    location: "New Town, Kolkata",
    description: "A modern wax museum featuring statues of famous personalities of India and abroad.",
    longDescription: "Mother's Wax Museum, located in the rapidly developing area of New Town, is Kolkata's answer to the world-famous Madame Tussauds. Since its inauguration in 2014, it has quickly become one of the city's most popular attractions, drawing large crowds of families and tourists. Named in honor of Mother Teresa, the museum offers visitors the unique opportunity to get up close and personal with lifelike wax statues of a host of famous personalities from various fields. The museum is spread over two floors and is divided into several sections. The collection features a diverse range of figures, with a strong emphasis on Indian luminaries. Visitors can click selfies with prominent historical figures and freedom fighters like Mahatma Gandhi and Subhas Chandra Bose, spiritual leaders such as Swami Vivekananda and Sri Ramakrishna, and literary giants like Rabindranath Tagore and Kazi Nazrul Islam. The entertainment section is always bustling, with incredibly realistic statues of Bollywood legends like Amitabh Bachchan and Shah Rukh Khan, as well as iconic Bengali actors like Uttam Kumar and Suchitra Sen. The sports gallery pays tribute to cricket superstars like Sachin Tendulkar and Sourav Ganguly, and football icon Diego Maradona. International figures are also represented, adding to the global appeal. The craftsmanship of the statues is impressive, capturing the fine details and characteristic poses of the personalities. Mother's Wax Museum provides a fun, interactive, and star-studded experience for all ages, making it a must-visit destination in modern Kolkata.",
    price: ["250 INR (General Entry)"],
    openingTime: "12:00 PM",
    closingTime: "7:30 PM",
    dayoff: "Monday",
    category: "Museum"

    name: "Rabindra Sarobar Lake",
    location: "Southern Avenue, Kolkata",
    description: "A large artificial lake surrounded by gardens and walking trails, a popular relaxation spot.",
    longDescription: "Rabindra Sarobar, formerly known as Dhakuria Lake, is a vast artificial lake located in South Kolkata that serves as the green lungs for the southern part of the city. This serene and expansive water body was excavated in the 1920s and was later renamed in honor of the poet Rabindranath Tagore. Spread over an area of 73 acres, the lake and its surrounding gardens, walking trails, and recreational facilities make it a cherished spot for nature lovers, fitness enthusiasts, and those seeking a peaceful retreat from urban life. The area around the lake is a designated national lake and is rich in biodiversity, attracting a variety of migratory and resident birds, making it a popular spot for birdwatching. The well-paved pathways that encircle the lake are bustling every morning and evening with joggers, walkers, and yoga practitioners. The complex also houses several sporting clubs, including rowing clubs and a swimming stadium, and the lake is often dotted with colorful rowing boats gliding across its calm waters. Within the Sarobar complex, one can find a children's park, gardens, and an open-air amphitheater called 'Mukta Mancha,' which occasionally hosts cultural performances. The Rabindra Sarobar Stadium, a football stadium, is also located within its premises. The tranquil atmosphere, combined with the lush greenery and the gentle lapping of water, provides a perfect setting for relaxation and contemplation. Rabindra Sarobar is more than just a park; it is an ecological and recreational hub that is deeply integrated into the daily life of South Kolkata's residents.",
    price: ["Free Entry"],
    openingTime: "5:00 AM",
    closingTime: "8:00 PM",
    dayoff: "Open All Days",
    category: "Park"

    name: "Millennium Park",
    location: "Strand Road, Hooghly Riverside, Kolkata",
    description: "A landscaped park along the river Hooghly with gardens, fountains, and family recreation areas.",
    longDescription: "Millennium Park is a beautifully landscaped public park situated along the eastern bank of the Hooghly River on Strand Road, Kolkata. Inaugurated at the turn of the millennium in the year 2000, this park stretches for about 2.5 kilometers and offers some of the most stunning panoramic views of the river and the iconic Howrah Bridge. It was developed as part of a beautification project for the city's riverfront and has since become a favorite evening destination for both locals and tourists. The park is meticulously maintained, featuring manicured lawns, vibrant flower beds, sculptures, and charming gazebos. A network of clean, paved pathways makes it ideal for a leisurely stroll while enjoying the cool river breeze. The main attractions include artistically designed fountains that are illuminated with colorful lights after sunset, creating a magical ambiance. For children, there is a dedicated play area with various swings and rides, making it a complete family-friendly spot. Numerous food kiosks are scattered throughout the park, offering a range of snacks and refreshments. One of the best experiences at Millennium Park is simply sitting on one of the many benches facing the river, watching the boats and ferries go by as the sun sets behind the Howrah Bridge. Its strategic location, pleasant atmosphere, and picturesque setting make it a perfect urban getaway for relaxation and rejuvenation right in the heart of the city.",
    price: ["20 INR (Entry)"],
    openingTime: "10:00 AM",
    closingTime: "6:00 PM",
    dayoff: "Open All Days",
    category: "Park"

    name: "Aquatica Water Park",
    location: "Kestopur, Kolkata",
    description: "A popular water theme park with pools, slides, and adventure rides.",
    longDescription: "Aquatica is a premier water theme park and resort located in Kestopur, on the eastern outskirts of Kolkata. Spread over a vast 17-acre area of lush greenery, it is one of the largest water parks in Eastern India and serves as a popular destination for fun, adventure, and relaxation, especially during the city's hot and humid summers. The park offers a thrilling array of water-based rides and attractions designed to cater to all age groups, from adrenaline junkies to families with young children. For thrill-seekers, Aquatica boasts a variety of high-speed water slides such as the Black Hole, the Cyclone, and the Raft Slide, which promise an exhilarating experience. The park's signature attraction is the large wave pool, which simulates the feeling of being in the sea with artificially generated waves, providing endless fun for everyone. For those looking to relax, the Lazy River offers a gentle current that allows visitors to float leisurely along a winding course. There is also a dedicated children's area with smaller slides, splash pools, and water play structures to ensure the little ones have a safe and enjoyable time. Beyond the water attractions, Aquatica often hosts events, parties, and live music performances, creating a vibrant resort-like atmosphere. With its on-site food courts, comfortable lodging options, and a commitment to safety and hygiene, Aquatica provides a complete entertainment package and a perfect escape for a day of splashing fun and excitement.",
    price: ["1000 INR (Full Entry Ticket)"],
    openingTime: "10:00 AM",
    closingTime: "6:00 PM",
    dayoff: "Open All Days",
    category: "Park"
  
    name: "National Library",
    location: "Belvedere Estate, Alipore, Kolkata",
    description: "India’s largest library by volume with over 2.2 million books, historic and academic resources.",
    longDescription: "The National Library of India, situated on the scenic 30-acre Belvedere Estate in Alipore, Kolkata, is the nation's largest library in terms of volume and public record. It is an institution of national importance, mandated to collect, disseminate, and preserve the country's printed and intellectual heritage. The library's history is deeply rooted in India's colonial past, originally formed by merging the Imperial Library with the Calcutta Public Library. The magnificent main building, Belvedere House, once served as the residence for the Lieutenant Governor of Bengal, adding a layer of historical grandeur to its academic purpose. The library's collection is truly colossal, comprising over 2.2 million books, alongside vast numbers of journals, manuscripts, maps, and government publications in virtually every Indian language and many international languages. As a repository library, it receives a copy of every book, newspaper, and periodical published in India, making it an unparalleled resource for researchers, scholars, and avid readers. The sprawling campus with its lush green lawns and majestic trees provides a serene and scholarly atmosphere. The library complex includes multiple reading rooms, including a dedicated section for rare books and manuscripts. In its commitment to modernization, the National Library has undertaken significant digitization efforts to preserve its invaluable collection and enhance accessibility for a global audience. It stands as a custodian of the nation's literary wealth, a quiet and dignified testament to the enduring power of knowledge and learning.",
    price: ["Free Entry"],
    openingTime: "9:00 AM",
    closingTime: "8:00 PM",
    dayoff: "Sunday",
    category: "Museum"      

Book tickets for these places and provide the ticket fares.
- Provide information about local attractions, events, and places of interest.
Instructions for AI:
- Use plain text only (no HTML or Markdown).  
- When a user asks about any of the above places, provide ticket fares and a short description.  
- If asked, also guide users on how to reach these places using CTC buses.  
- Ask follow-up questions like:  
  - "Do you want me to suggest other attractions nearby?"  
  - "Would you like me to show you the bus routes and timings?" 

You will help users with:
- Booking tickets for tourist attractions
- Providing information about bus fares and schedules
- if someone uploads a picture 
- Booking tickets for famous places and sharing ticket fares
- Never ask users for their name, email, or phone number
- Providing information about local attractions, events, and places of interest
- after confirming helping with payment, provide a confirmation message with booking details
- 
Use only plain text. Do NOT use HTML or Markdown.
Use line breaks to separate paragraphs.
Use hyphens (-) for bullet points. 

You will help users with:
- Booking tickets for tourist attractions
- Providing information about bus fares and schedules but not booking bus tickets
- Booking tickets for attractions
- Providing tourist info
- After booking, confirm with booking details

Use plain text only. No HTML/Markdown.
"""

help_prompt = """
You are a polite and informative Help Desk assistant for Calcutta Transport Corporation (CTC).
You answer questions about:
- Lost & found
- Customer support
- Complaints & feedback
- General transport info

Use plain text only. No HTML/Markdown.
"""

# Start chat sessions
booking_chat = model.start_chat(
    history=[{"role": "user", "parts": [booking_prompt]}])
help_chat = model.start_chat(
    history=[{"role": "user", "parts": [help_prompt]}])


# ---------------------- ROUTES ---------------------- #
@app.route("/chat", methods=["POST"])
def unified_chat():
    """Default chat route (used by React). Uses booking bot."""
    try:
        data = request.get_json()
        user_input = data.get("message", "").strip()
        if not user_input:
            return jsonify({"error": "Message is empty"}), 400

        # Default: use booking bot
        response = booking_chat.send_message(user_input)
        reply = response.text.strip() if response.text else "Sorry, I couldn’t understand that."

        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/chatbot/booking", methods=["POST"])
def booking_bot():
    try:
        data = request.get_json()
        user_input = data.get("message", "").strip()
        if not user_input:
            return jsonify({"error": "Message is empty"}), 400

        response = booking_chat.send_message(user_input)
        reply = response.text.strip() if response.text else "Sorry, I couldn’t understand that."

        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/chatbot/help", methods=["POST"])
def help_bot():
    try:
        data = request.get_json()
        user_input = data.get("message", "").strip()
        if not user_input:
            return jsonify({"error": "Message is empty"}), 400

        response = help_chat.send_message(user_input)
        reply = response.text.strip() if response.text else "Sorry, I couldn’t understand that."

        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({"message": "File uploaded successfully", "path": filepath})


# ---------------------- MAIN ---------------------- #
if __name__ == "__main__":
    app.run(port=5000, debug=True)