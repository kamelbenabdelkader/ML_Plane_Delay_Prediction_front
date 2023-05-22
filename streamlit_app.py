import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import pickle
from PIL import Image




# Fonction qui charge le fichier css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

holidates = pd.read_pickle('holidates.pickle')


# Appel à l'API pour récupérer les informations de vol
url = "https://simplonmarketapi.azurewebsites.net/mois/mars"
response = requests.get(url)
flights = response.json()
url1 = "https://simplonmarketapi.azurewebsites.net/add"

airport_cities = { 11298 : 'Dallas/Fort Worth, TX', 12478 : 'New York, NY', 14747 : 'Seattle, WA', 13930 : 'Chicago, IL', 14831 : 'San Jose, CA', 11278 : 'Washington, DC', 15304 : 'Tampa, FL', 13303 : 'Miami, FL', 11292 : 'Denver, CO', 12892 : 'Los Angeles, CA',12758 : 'Kona, HI', 12266 : 'Houston, TX', 12889 : 'Las Vegas, NV', 13204 : 'Orlando, FL',14869 : 'Salt Lake City, UT', 10721 : 'Boston, MA', 15016 : 'St. Louis, MO',14771 : 'San Francisco, CA', 12173 : 'Honolulu, HI', 13830 : 'Kahului, HI',14100 : 'Philadelphia, PA', 12264 : 'Washington, DC', 12953 : 'New York, NY',11433 : 'Detroit, MI', 14492 : 'Raleigh/Durham, NC', 14057 : 'Portland, OR',11540 : 'El Paso, TX', 13198 : 'Kansas City, MO', 13891 : 'Ontario, CA',15376 : 'Tucson, AZ', 14679 : 'San Diego, CA', 14893 : 'Sacramento, CA',14107 : 'Phoenix, AZ', 12982 : 'Lihue, HI', 13931 : 'Norfolk, VA',10693 : 'Nashville, TN', 15370 : 'Tulsa, OK', 14635 : 'Fort Myers, FL',14683 : 'San Antonio, TX', 10821 : 'Baltimore, MD', 15024 : 'Charlotte Amalie, VI',12012 : 'Gunnison, CO', 11618 : 'Newark, NJ', 14908 : 'Santa Ana, CA',10397 : 'Atlanta, GA', 13487 : 'Minneapolis, MN', 14843 : 'San Juan, PR',11697 : 'Fort Lauderdale, FL', 11057 : 'Charlotte, NC', 13495 : 'New Orleans, LA',11109 : 'Colorado Springs, CO', 13342 : 'Milwaukee, WI', 13851 : 'Oklahoma City, OK',10423 : 'Austin, TX', 14570 : 'Reno, NV', 14122 : 'Pittsburgh, PA',14262 : 'Palm Springs, CA', 14027 : 'West Palm Beach/Palm Beach, FL',11267 : 'Dayton, OH', 11503 : 'Eagle, CO', 14524 : 'Richmond, VA',10140 : 'Albuquerque, NM', 14730 : 'Louisville, KY', 12451 : 'Jacksonville, FL',15027 : 'Christiansted, VI', 11423 : 'Des Moines, IA', 13871 : 'Omaha, NE',11638 : 'Fresno, CA',10529 : 'Hartford, CT', 11066 : 'Columbus, OH',12339 : 'Indianapolis, IN',12094 : 'Hayden, CO', 13502 : 'Montrose/Delta, CO',11042 : 'Cleveland, OH', 12441 : 'Jackson, WY', 13256 : 'Mission/McAllen/Edinburg, TX',13244 : 'Memphis, TN', 10713 : 'Boise, ID', 13796 : 'Oakland, CA',11884 : 'Spokane, WA', 10299 : 'Anchorage, AK', 10792 : 'Buffalo, NY', 10257 : 'Albany, NY', 14576 : 'Rochester, NY', 14307 : 'Providence, RI', 15096 : 'Syracuse, NY', 12323 : 'Wilmington, NC', 14321 : 'Portland, ME', 10666 : 'Bellingham, WA', 12954 : 'Long Beach, CA', 15070 : 'Newburgh/Poughkeepsie, NY', 12197 : 'White Plains, NY', 12191 : 'Houston, TX', 14254 : 'Ponce, PR', 10732 : 'Aguadilla, PR', 14986 : 'Sarasota/Bradenton, FL', 14685 : 'Savannah, GA', 10994 : 'Charleston, SC', 10785 : 'Burlington, VT', 13933 : 'Worcester, MA', 10800 : 'Burbank, CA', 11193 : 'Cincinnati, OH', 11637 : 'Fargo, ND', 13485 : 'Madison, WI',11986 : 'Grand Rapids, MI', 11612 : 'Evansville, IN', 10434 : 'Scranton/Wilkes-Barre, PA', 10620 : 'Billings, MT', 11252 : 'Daytona Beach, FL', 10208 : 'Augusta, GA', 11259 : 'Dallas, TX', 15323 : 'Bristol/Johnson City/Kingsport, TN', 13232 : 'Chicago, IL', 11973 : 'Gulfport/Biloxi, MS', 14098 : 'Newport News/Williamsburg, VA', 13360 : 'Melbourne, FL', 10849 : 'Bozeman, MT',10980 : 'Chattanooga, TN', 13486 : 'Missoula, MT', 10599 : 'Birmingham, AL', 10990 : 'Charlottesville, VA', 12945 : 'Lexington, KY', 11624 : 'Key West, FL', 12278 : 'Wichita, KS', 13230 : 'Harrisburg, PA', 11481 : 'Panama City, FL', 15624 : 'Valparaiso, FL', 11996 : 'Greer, SC', 10408 : 'Appleton, WI', 12951 : 'Lafayette, LA', 14783 : 'Springfield, MO', 10874 : 'Akron, OH', 11775 : 'Sioux Falls, SD', 11641 : 'Fayetteville, NC', 11995 : 'Greensboro/High Point, NC', 14193 : 'Pensacola, FL', 12402 : 'Hilo, HI', 13577 : 'Myrtle Beach, SC', 10158 : 'Atlantic City, NJ', 12898 : 'Latrobe, PA', 14222 : 'Pago Pago, TT', 12265 : 'Niagara Falls, NY', 10868 : 'Columbia, SC', 15412 : 'Knoxville, TN', 11982 : 'Killeen, TX', 13158 : 'Midland/Odessa, TX', 10781 : 'Baton Rouge, LA', 12511 : 'Joplin, MO', 12891 : 'Lawton/Fort Sill, OK', 15411 : 'Tyler, TX', 14952 : 'Springfield, IL', 10155 : 'Waco, TX', 10747 : 'Brownsville, TX', 12884 : 'Lansing, MI', 14689 : 'Santa Barbara, CA', 11413 : 'Durango, CO', 10372 : 'Aspen, CO', 15919 : 'Fayetteville, AR',
                  11823 : 'Fort Wayne, IN', 14814 : 'Shreveport, LA', 14905 : 'Santa Maria, CA', 14457 : 'Rapid City, SD', 14696 : 'South Bend, IN', 14252 : 'Pasco/Kennewick/Richland, WA', 11695 : 'Flagstaff, AZ', 16218 : 'Yuma, AZ', 12156 : 'Helena, MT', 10157 : 'Arcata/Eureka, CA', 13184 : 'Saginaw/Bay City/Midland, MI', 14025 : 'Plattsburgh, NY', 10561 : 'Bakersfield, CA', 12280 : 'Idaho Falls, ID', 11003 : 'Cedar Rapids/Iowa City, IA', 11921 : 'Grand Junction, CO', 14794 : 'St. George, UT', 11525 : 'Elko, NV', 12389 : 'Williston, ND', 12888 : 'Laramie, WY', 12003 : 'Great Falls, MT', 13476 : 'Monterey, CA', 11977 : 'Green Bay, WI', 13264 : 'Medford, OR', 11648 : 'Kalispell, MT', 10469 : 'Kalamazoo, MI', 11140 : 'Corpus Christi, TX', 13388 : 'Mammoth Lakes, CA', 14489 : 'Bend/Redmond, OR', 11898 : 'Grand Forks, ND', 13076 : 'La Crosse, WI', 10627 : 'Bismarck/Mandan, ND', 11603 : 'Eugene, OR', 15041 : 'Sun Valley/Hailey/Ketchum, ID', 13433 : 'Minot, ND', 11337 : 'Duluth, MN', 12992 : 'Little Rock, AR', 11076 : 'Hancock/Houghton, MI', 12519 : 'Jamestown, ND', 11447 : 'Devils Lake, ND', 10431 : 'Asheville, NC', 14006 : 'Paducah, KY', 14698 : 'San Luis Obispo, CA', 13344 : 'Muskegon, MI', 11865 : 'Gillette, WY', 12896 : 'Lubbock, TX', 13029 : 'Lincoln, NE', 10141 : 'Aberdeen, SD', 10333 : 'Alpena, MI', 12397 : 'Ithaca/Cortland, NY',11013 : 'Sault Ste. Marie, MI', 14520 : 'Rhinelander, WI', 12335 : 'Iron Mountain/Kingsfd, MI', 10577 : 'Binghamton, NY', 12343 : 'International Falls, MN', 14113 : 'Pocatello, ID', 15389 : 'Twin Falls, ID', 14150 : 'Pellston, MI', 12129 : 'Hibbing, MN', '11587': 'Escanaba, MI', 13459 : 'Marquette, MI', 13127 : 'Lewiston, ID', 10631 : 'Bemidji, MN', 11122 : 'Casper, WY', 10739 : 'Brainerd, MN', 10779 : 'Butte, MT', 10918 : 'Cedar City, UT', 11097 : 'Cody, WY', 14543 : 'Rock Springs, WY', 11471 : 'Eau Claire, WI', 12255 : 'Hays, KS', 14487 : 'Redding, CA', 14108 : 'Peoria, IL', 12016 : 'Guam, TT', 14574 : 'Roanoke, VA', 13296 : 'Manchester, NH', 12523 : 'Juneau, AK', 15249 : 'Tallahassee, FL', 12217 : 'Huntsville, AL', 11721 : 'Flint, MI', 12448 : 'Jackson/Vicksburg, MS', 10551 : 'Bethel, AK', 10170 : 'Kodiak, AK', 10754 : 'Barrow, AK', 14709 : 'Deadhorse, AK', 11630 : 'Fairbanks, AK', 12819 : 'Ketchikan, AK', 14828 : 'Sitka, AK', 14256 : 'Petersburg, AK', 15841 : 'Wrangell, AK', 13873 : 'Nome, AK', 13970 : 'Kotzebue, AK', 13241 : 'Meridian, MS', 14109 : 'Hattiesburg/Laurel, MS', 15401 : 'Texarkana, AR', 10728 : 'Beaumont/Port Arthur, TX', 13061 : 'Laredo, TX', 14674 : 'Santa Fe, NM', 11778 : 'Fort Smith, AR', 13377 : 'Monroe, LA', 10185 : 'Alexandria, LA', 12915 : 'Lake Charles, LA', 15380 : 'Traverse City, MI', 11577 : 'Erie, PA', 10279 : 'Amarillo, TX', 12206 : 'Harlingen/San Benito, TX', 11203 : 'Mosinee, WI', 13422 : 'Mobile, AL', 12177 : 'Hobbs, NM', 13367 : 'Moline, IL', 11146 : 'Charleston/Dunbar, WV', 11049 : 'College Station/Bryan, TX', 11953 : 'Gainesville, FL', 13277 : 'Montgomery, AL', 11537: 'Elmira/Corning, NY', 15607: 'Valdosta, GA', 12007: 'Columbus, MS', 11308: 'Dothan, AL', 10135: 'Allentown/Bethlehem/Easton, PA', 13795: 'Jacksonville/Camp Lejeune, NC', 10685: 'Bloomington/Normal, IL', 11150: 'Columbus, GA', 10146: 'Albany, GA', 10581: 'Bangor, ME', 14711: 'State College, PA', 11617: 'New Bern/Morehead/Beaufort, NC', 10731: 'Brunswick, GA', 15356: 'Trenton, NJ', 15497: 'St. Augustine, FL', 12391: 'Islip, NY', 10926: 'Cordova, AK', 15991: 'Yakutat, AK', 10165: 'Adak Island, AK', 14633: 'Rochester, MN', 13964: 'North Bend/Coos Bay, OR', 14588: 'Roswell, NM', 14842: 'San Angelo, TX', 11905: 'Longview, TX', 14960: 'Wichita Falls, TX',10154: 'Nantucket, MA', 13541: "Martha's Vineyard, MA", 12250: 'Hyannis, MA', 15897: 'West Yellowstone, MT', 11867: 'Garden City, KS', 13290: 'Manhattan/Ft. Riley, KS', 11997: 'Gustavus, AK', 11336: 'Dillingham, AK', 10245: 'King Salmon, AK', 10136: 'Abilene, TX', 11980: 'Grand Island, NE', 14955: 'Saipan, TT', 14082: 'Punta Gorda, FL'}




def mark_vacation_dates(date):
    date_without_year = date.strftime("%m-%d")
    vacation_dates = holidates['FL_DATE'].dt.strftime("%m-%d")

    if date_without_year in vacation_dates.values:
        return 1
    else:
        return 0

# Fonction pour insérer les données dans la base de données
def insert_data(date):
    vacation = mark_vacation_dates(date)
    return vacation


def transform_hour(hour_str):
    hour_int = int(hour_str.replace(":", ""))
    return hour_int


def transform_hour_back(hour_int):
    hour_str = str(hour_int).zfill(6)
    hour_back = f"{hour_str[2:4]}:{hour_str[4:]}"
    return hour_back

# Fonction pour la page "Ajouter"
def add_page():

    # Formulaire pour ajouter un vol à l'API
    st.title("Ajouter un vol")

    date = st.date_input("Date du vol")
    # Création d' un dictionnaire qui associe les noms de ville aux IDs d'aéroport
    city_airports_departure = {v: k for k, v in airport_cities.items()}
    # Afficher une liste déroulante avec les noms de ville
    departure_city = st.selectbox("Ville de départ", options=list(city_airports_departure.keys()))
    # Obtenir l'ID de l'aéroport à partir du nom de ville
    departure_airport_id = city_airports_departure.get(departure_city )
    # Afficher l'ID de l'aéroport
    st.write(f"ID de l'aéroport de départ: {departure_airport_id}")
    city_airports_arrival = {v: k for k, v in airport_cities.items()}
    origin_city = st.selectbox("Ville d'arrivée", options=list(city_airports_arrival.keys()))
    # Obtenir l'ID de l'aéroport à partir du nom de ville
    arrival_airport_id = city_airports_arrival.get(origin_city)
    st.write(f"ID de l'aéroport de d'arrivée: {arrival_airport_id}")
    # dest_airport_id = st.number_input("ID de l'aéroport d'arrivée", min_value=0)
    dep_time = st.time_input("Heure de départ")
    arr_time = st.time_input("Heure d'arrivé")
    origin_airport_id = departure_airport_id
    vacation =  insert_data(date)
    # Ajout bouton pour envoyer les données
    if st.button("Ajouter"):
        date_time = datetime.strptime(str(date), "%Y-%m-%d")
        quarter = (date_time.month - 1) // 3 + 1
        month = date.month
        day_of_month = date.day
        day_of_week = date.isoweekday()
        flight_data = {
            "QUARTER": quarter,
            "MONTH":   month,
            "DAY_OF_MONTH": day_of_month,
            "DAY_OF_WEEK": day_of_week,
            "ORIGIN_AIRPORT_ID": origin_airport_id,
            "DEST_AIRPORT_ID":  arrival_airport_id ,
            "DEP_TIME": transform_hour(dep_time.strftime("%H:%M")),
            "ARR_TIME": transform_hour(arr_time.strftime("%H:%M")),
            "VACATION":  vacation
        }

        # Envoyer les données à l'API
        response = requests.post(url1, json=flight_data)
        # Vérifier si la requête a réussi
        if response.ok:
            st.success("Les informations de votre vol ont été ajouté avec succès !")
        else:
            st.error("Erreur lors de l'ajout des informations de votre vol.")

# Fonction pour la page "Métriques"
def metrics_page():
    st.title("Métriques")
    # st.write(flights)
    # Affichage des métriques récupérées depuis l'API
    # Affichage des informations de vol sous forme de KPI
    for flight in flights:
        st.subheader(flight['FL_DATE'])
        st.metric("Airlines", flight['AIRLINE_ID'])
        st.metric("Origin Airport", flight['ORIGIN_AIRPORT_ID'])
        st.metric("Destination Airport", flight['DEST_AIRPORT_ID'])
        st.metric("Departure Time",  transform_hour_back(flight['DEP_TIME']))


# Fonction pour la page "Graphiques"
def charts_page():

    st.title("Graphiques")
    wch_colour_box = (0,204,102)
    wch_colour_font = (0,0,0)
    fontsize = 18
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = "Observations"
    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    i = 123

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]},
                                              {wch_colour_box[1]},
                                              {wch_colour_box[2]}, 0.75);
                        color: rgb({wch_colour_font[0]},
                                   {wch_colour_font[1]},
                                   {wch_colour_font[2]}, 0.75);
                        font-size: {fontsize}px;
                        border-radius: 7px;
                        padding-left: 12px;
                        padding-top: 18px;
                        padding-bottom: 18px;
                        line-height:25px;'>
                        <i class='{iconname} fa-xs'></i> {i}
                        </style><BR><span style='font-size: 14px;
                        margin-top: 0;'>{sline}</style></span></p>"""

    st.markdown(lnk + htmlstr, unsafe_allow_html=True)


#---------------------  Sidebar  ----------------------#
# Menu déroulant pour sélectionner la page à afficher
menu = ["Ajouter", "Métriques", "Graphiques"]
choice = st.sidebar.selectbox("Sélectionnez une page", menu)
image = Image.open('img.PNG')
im = image.resize((150, 300))
st.sidebar.image(im, caption='Sunrise by the mountains')


# Affichage de la page correspondant à la sélection du menu
if choice == "Ajouter":
    add_page()
elif choice == "Métriques":
    metrics_page()
else:
    charts_page()
