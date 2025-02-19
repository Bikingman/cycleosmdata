
from cycleosmdata.bikeosm import BikeOSM

output_path = r'/Users/danielpatterson/Documents/GitHub/ExtractOSM/src/output'
# state_osm_urls = {'District of Columbia': 'http://download.geofabrik.de/north-america/us/district-of-columbia-latest.osm.pbf'}
# cambridge = {'Cambridgeshire': 'https://download.geofabrik.de/europe/united-kingdom/england/cambridgeshire-latest.osm.pbf'}


state_osm_urls = {
    "Alabama": "http://download.geofabrik.de/north-america/us/alabama-latest.osm.pbf",
    "Alaska": "http://download.geofabrik.de/north-america/us/alaska-latest.osm.pbf",
    "Arizona": "http://download.geofabrik.de/north-america/us/arizona-latest.osm.pbf",
    "Arkansas": "http://download.geofabrik.de/north-america/us/arkansas-latest.osm.pbf",
    "California": "http://download.geofabrik.de/north-america/us/california-latest.osm.pbf",
    "Colorado": "http://download.geofabrik.de/north-america/us/colorado-latest.osm.pbf",
    "Connecticut": "http://download.geofabrik.de/north-america/us/connecticut-latest.osm.pbf",
    "Delaware": "http://download.geofabrik.de/north-america/us/delaware-latest.osm.pbf",
    "District of Columbia": "http://download.geofabrik.de/north-america/us/district-of-columbia-latest.osm.pbf",
    "Florida": "http://download.geofabrik.de/north-america/us/florida-latest.osm.pbf",
    "Georgia": "http://download.geofabrik.de/north-america/us/georgia-latest.osm.pbf",
    "Hawaii": "http://download.geofabrik.de/north-america/us/hawaii-latest.osm.pbf",
    "Idaho": "http://download.geofabrik.de/north-america/us/idaho-latest.osm.pbf",
    "Illinois": "http://download.geofabrik.de/north-america/us/illinois-latest.osm.pbf",
    "Indiana": "http://download.geofabrik.de/north-america/us/indiana-latest.osm.pbf",
    "Iowa": "http://download.geofabrik.de/north-america/us/iowa-latest.osm.pbf",
    "Kansas": "http://download.geofabrik.de/north-america/us/kansas-latest.osm.pbf",
    "Kentucky": "http://download.geofabrik.de/north-america/us/kentucky-latest.osm.pbf",
    "Louisiana": "http://download.geofabrik.de/north-america/us/louisiana-latest.osm.pbf",
    "Maine": "http://download.geofabrik.de/north-america/us/maine-latest.osm.pbf",
    "Maryland": "http://download.geofabrik.de/north-america/us/maryland-latest.osm.pbf",
    "Massachusetts": "http://download.geofabrik.de/north-america/us/massachusetts-latest.osm.pbf",
    "Michigan": "http://download.geofabrik.de/north-america/us/michigan-latest.osm.pbf",
    "Minnesota": "http://download.geofabrik.de/north-america/us/minnesota-latest.osm.pbf",
    "Mississippi": "http://download.geofabrik.de/north-america/us/mississippi-latest.osm.pbf",
    "Missouri": "http://download.geofabrik.de/north-america/us/missouri-latest.osm.pbf",
    "Montana": "http://download.geofabrik.de/north-america/us/montana-latest.osm.pbf",
    "Nebraska": "http://download.geofabrik.de/north-america/us/nebraska-latest.osm.pbf",
    "Nevada": "http://download.geofabrik.de/north-america/us/nevada-latest.osm.pbf",
    "New Hampshire": "http://download.geofabrik.de/north-america/us/new-hampshire-latest.osm.pbf",
    "New Jersey": "http://download.geofabrik.de/north-america/us/new-jersey-latest.osm.pbf",
    "New Mexico": "http://download.geofabrik.de/north-america/us/new-mexico-latest.osm.pbf",
    "New York": "http://download.geofabrik.de/north-america/us/new-york-latest.osm.pbf",
    "North Carolina": "http://download.geofabrik.de/north-america/us/north-carolina-latest.osm.pbf",
    "North Dakota": "http://download.geofabrik.de/north-america/us/north-dakota-latest.osm.pbf",
    "Ohio": "http://download.geofabrik.de/north-america/us/ohio-latest.osm.pbf",
    "Oklahoma": "http://download.geofabrik.de/north-america/us/oklahoma-latest.osm.pbf",
    "Oregon": "http://download.geofabrik.de/north-america/us/oregon-latest.osm.pbf",
    "Pennsylvania": "http://download.geofabrik.de/north-america/us/pennsylvania-latest.osm.pbf",
    "Puerto Rico": "http://download.geofabrik.de/north-america/us/puerto-rico-latest.osm.pbf",
    "Rhode Island": "http://download.geofabrik.de/north-america/us/rhode-island-latest.osm.pbf",
    "South Carolina": "http://download.geofabrik.de/north-america/us/south-carolina-latest.osm.pbf",
    "South Dakota": "http://download.geofabrik.de/north-america/us/south-dakota-latest.osm.pbf",
    "Tennessee": "http://download.geofabrik.de/north-america/us/tennessee-latest.osm.pbf",
    "Texas": "http://download.geofabrik.de/north-america/us/texas-latest.osm.pbf",
    "United States Virgin Islands": "http://download.geofabrik.de/north-america/us/us-virgin-islands-latest.osm.pbf",
    "Utah": "http://download.geofabrik.de/north-america/us/utah-latest.osm.pbf",
    "Vermont": "http://download.geofabrik.de/north-america/us/vermont-latest.osm.pbf",
    "Virginia": "http://download.geofabrik.de/north-america/us/virginia-latest.osm.pbf",
    "Washington": "http://download.geofabrik.de/north-america/us/washington-latest.osm.pbf",
    "West Virginia": "http://download.geofabrik.de/north-america/us/west-virginia-latest.osm.pbf",
    "Wisconsin": "http://download.geofabrik.de/north-america/us/wisconsin-latest.osm.pbf",
    "Wyoming": "http://download.geofabrik.de/north-america/us/wyoming-latest.osm.pbf"
}

BikeOSM(state_osm_urls, output_path).handle_pbfs()