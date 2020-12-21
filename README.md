# Json-Subset
Since the dataset we have contains a huge amount of duplicates (12M records with only 1.5M unique) and massive size of 29.6GB, we needed to write a code that generates a new dataset with only the unique applications and the features we need.  
This code takes the unique records from the first 1M records which will end up by 370K unique records.  \
\
You can use this code to generate a JSON file that contains all the unique records by removing the lines 52 and 54.  \
\
Link to the original dataset: https://drive.google.com/file/d/10xudbVaIIQT3mQiwvuljQJpnu7J1oOrr/
\
Here is how each record looks like in the original file:
\
{
\
  "Ratings": [
\
    "406,297"
\
  ],
\
  "Title": [
\
    "WWE SuperCard"
\
  ],
\
  "FourStarRatings": [
\
    "49,851"
\
  ],
\
  "DeveloperAddress": [
\
    "9 Hamilton Landing\nNovato, CA. 94949"
\
  ],
\
  "LastUpdated": [
\
    "March 14, 2017"
\
  ],
\
  "WhatsNew": [
\
    "· WrestleMania 33 Tier – WM 33 Tier explodes on the scene featuring the WWE SuperCard debut of Mickie James, Ken Shamrock and James Ellsworth!",
\
    "· Attitudes – Bring more attitude to PVP matches with the addition of Brock Lesnar, Bayley and more.",
\
    "· General optimizations and improvements."
\
  ],
\
  "Description": [
\
    "Get ready to dominate them all with Season 3 of WWE Supercard, the biggest, baddest update yet to the card battle game that has thrilled over 11 million \
players around the world! WWE Supercard delivers over 150 Superstars of the past, present and future as well as fast-paced, in-your-face action like you’ve never \
seen before!  Featuring the series’ first real time battle against live opponents, including a 15-on-15 Royal Rumble and ranked player-versus-player, Season 3 \
allows you to engage and compete with others from around the world for ranking and rewards! ",
\
    "WWE SuperCard Season 3 includes:",
\
    "•\tRANKED / PVP MODE – Battle in real time against live opponents from around the world for the top slot in a new monthly leaderboard for ranking and \
rewards.",
\
    "•\tROYAL RUMBLE – Pit 15 of your best cards against 15 of an opponent’s cards in a brand new, real-time gameplay mode in a battle to see the last card \
standing;",
\
    "•\tNEW CARD TIERS – Access three new card tiers and compete for more than 100 new cards;",
\
    "•\tWILD MODE – Use both Active and Legacy cards to compete against opponents and gain more Active cards for your deck; ",
\
    "•\tSEASON 1 LEGACY CARDS – Retain Season 1 cards through their transition to Legacy cards in Season 3, with the cards available for play in the game’s new \
Wild Mode feature; ",
\
    "•\tYOUR FAVORITE MODES  - Money in the Bank, Ring Domination, People’s Champion Challenge, King of the Ring, and Road to Glory are all carrying over to S3. \
And, yes, your S2 cards will be playable across all this in addition to Ranked, Wild, and Royal Rumble mode.",
\
    "**Update requires OS 4.0.3+ WILL NOT RUN ON ANY EARLIER OS**"
\
  ],
\
  "ReviewsAverage": [
\
    "4.3"
\
  ],
\
  "Price": [
\
    "0"
\
  ],
\
  "ThreeStarRatings": [
\
    "25,658"
\
  ],
\
  "PrivacyPolicyLink": [
\
    "https://www.google.com/url?q=http://www.take2games.com/privacy/&sa=D&usg=AFQjCNFEUsYmzZvkJfMbewZaesonA8RvxQ"
\
  ],
\
  "Genre": [
\
    "Sports"
\
  ],
\
  "FiveStarRatings": [
\
    "279,372"
\
  ],
\
  "OneStarRatings": [
\
    "37,368"
\
  ],
\
  "Url": "https://play.google.com/store/apps/details?id=com.catdaddy.cat22",
\
  "ContentRating": [
\
    "Teen"
\
  ],
\
  "CurrentVersion": [
\
    " 2.0.0.240052  "
\
  ],
\
  "DeveloperEmail": [
\
    "wwesupercardsupport@2k.com "
\
  ],
\
  "AndroidVersion": [
\
    "      4.0.3 and up    "
\
  ],
\
  "DeveloperWebsite": [
\
    "https://www.google.com/url?q=http://support.2k.com/&sa=D&usg=AFQjCNHK-xtbRuE_s7Rrhf5IW3m7hhL_Xw"
\
  ],
\
  "DeveloperName": [
\
    "2K, Inc."
\
  ],
\
  "FileSize": [],
\
  "TwoStarRatings": [
\
    "14,048"
\
  ],
\
  "Downloads": [
\
    "  5,000,000 - 10,000,000  "
\
  ]
\
\
}\
\
