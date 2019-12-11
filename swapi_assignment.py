import json, requests

ENDPOINT = 'https://swapi.co/api'
PEOPLE_KEYS = ("url", "name", "height", "mass", "hair_color", "skin_color", "eye_color",
                "birth_year", "gender", "homeworld", "species")
PLANET_KEYS = ("url", "name", "rotation_period", "orbital_period", "diameter", "climate",
                "gravity", "terrain", "surface_water", "population")
STARSHIP_KEYS = ("url", "starship_class", "name", "model", "manufacturer", "length", "width",
                "max_atmosphering_speed", "hyperdrive_rating", "MGLT", "crew", "passengers",
                "cargo_capacity", "consumables", "armament")
SPECIES_KEYS = ("url", "name", "classification", "designation", "average_height", "skin_colors",
                "hair_colors", "eye_colors", "average_lifespan", "language")
VEHICLE_KEYS = ("url", "vehicle_class", "name", "model", "manufacturer", "length",
                "max_atmosphering_speed", "crew", "passengers", "cargo_capacity", "consumables", "armament")
HOTH_KEYS = ("url", "name", "system_position", "natural_satellites", "rotation_period", "orbital_period",
            "diameter", "climate", "gravity", "terrain", "surface_water", "population", "indigenous_life_forms")


def assign_crew(starship, crew):
    """Assign crew members to a starship

    Parameters:
    starship (dict): a dictionary needed to be added some key-value pairs
    crew (dict): key-value pairs containing crew info.

    Returns:
    dict: an updated starship with one or more new crew member key-value pairs
    """
    for key in crew:
        starship[key] = crew[key]
    return starship



def clean_data(entity):
    """converts dictionary string values to more appropriate types 
    such as float, int, list, or, in certain cases, None.

    Parameters:
    entity (dict): a dictionary with all string type of values

    Returns:
    dict: a dictionary with proper value types.
    """

    cleaned_dict = {}
    float_props = ("gravity", "length", "width", "hyperdrive_rating")
    int_props = ("rotation_period", "orbital_period", "diameter", "surface_water", "population",
                "height", "mass", "average_height", "average_lifespan", "max_atmosphering_speed",
                "MGLT", "crew", "passengers", "cargo_capacity")
    list_props = ("hair_color", "skin_color", "hair_colors", "skin_colors", "eye_colors", "climate", "terrain")
    dict_props = ("homeworld", "species")
    # print(entity)
    for key in entity:
        if is_unknown(entity[key]):
            cleaned_dict[key] = None
        elif key in float_props:
            cleaned_dict[key] = convert_string_to_float(entity[key])
        elif key in int_props:
            cleaned_dict[key] = convert_string_to_int(entity[key])
        elif key in list_props:
            cleaned_dict[key] = convert_string_to_list(entity[key], delimiter=", ")
        elif key in dict_props:
            if key == "homeworld":
                result = get_swapi_resource(entity[key])
                filtered_dict = filter_data(result, PLANET_KEYS)
                cleaned_dict[key] = clean_data(filtered_dict)
            else:
                result = get_swapi_resource(entity[key][0])
                filtered_dict = filter_data(result, SPECIES_KEYS)
                cleaned_dict[key] = [clean_data(filtered_dict)]
        else:
            cleaned_dict[key] = entity[key]

    return cleaned_dict


def combine_data(default_data, override_data):
    """Combine the key-valuepairs of both the default dictionary and the override dictionary,
    with override values replacing default values on matching keys.
    
    Parameters:
    default_data (dict): the dictionary needed to be updated
    override_data (dict): the dictionary contains new infos for either being added to the old dict 
                        or replacing the old key-value pairs.

    Returns:
    dict: a updated dict contains all the newest info in both data.
    """

    default_data.update(override_data)
    return default_data


def convert_string_to_float(value):
    """Attempts to convert a string to a floating point value.

    Parameters:
    value (str): a string that is possible to be convert to a float

    Returns:
    float or str or bool: if converting is successful, return a floating number;
                        if converting is failed, return the value unchanged.
    """

    try:
        value = value.split()[0]
        return float(value)
    except:
        return value


def convert_string_to_int(value):
    """Attempts to convert a string to a integer value.

    Parameters:
    value (str): a string that is possible to be convert to an int

    Returns:
    int or str or bool: if converting is successful, return an integer number;
                        if converting is failed, return the value unchanged.
    """

    try:
        return int(value)
    except ValueError:
        return value


def convert_string_to_list(value, delimiter=','):
    """split the passed in string using the provided delimiter
    and return the resulting list

    Parameters:
    value (str): a string needed to be convert.
    delimiter (str): (optional) the character that used to split the str as a delimiter.

    Returns:
    list: a list of strings
    """

    new_list = value.split(delimiter)
    return new_list


def filter_data(data, filter_keys):
    """Filter the key-value pairs in a dictionary in the order of the given key name filter.

    Parameters:
    data (dict): a dictionary needed to be filtered
    filter_keys (tuple): a tuple contains all the keys for filtering

    Returns:
    dict: a dictionary only contains the key-value pairs based on key filter.
    """

    filtered_dict = {}
    for key in filter_keys:
        if key in data.keys():
            filtered_dict[key] = data[key]
    return filtered_dict



def get_swapi_resource(url, params=None):
    """Accept a URL and
    an optional query string of key:value pairs as search terms
    and issue an HTTP GET request
    to return a dictionary representation of the decoded JSON.
    Extract the value in the results key.

    Parameters:
    url (str): the endpoint used for API query
    params (dict): (optional) a dictionary containing query parameters as search terms.

    Returns:
    dict:  a dictionary representation of the decoded JSON
    """

    if "/people" or "/planets" or "/films" or "/species" or "/vehicles" or "/starships" in url:
        result = requests.get(url, params=params).json()
    else:
        result = requests.get(ENDPOINT).json()
    return result


def is_unknown(value):
    """Check the case-insensitive string value if equals to unknown or n/a

    Parameters:
    value (str): the string needed to be tested

    Returns:
    bool: return True if the value is "unknown" or "n/a", otherwise, return False.
    """

    try:
        value_lowercase = value.lower()
        if "unknown" in value_lowercase or "n/a" in value_lowercase:
            return True
        else:
            return False
    except:
        value_lowercase = value
        return False



def read_json(filepath):
    """
    Read a JSON file and return a dictionary representation of the decoded JSON.

    Parameters:
        filepath (str): the path to the file.

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    with open(filepath, "r", encoding="utf-8") as file_obj:
        result = json.load(file_obj)
        return result


def write_json(filepath, data):
    """
    Write a dictionary to a JSON file.

    Parameters:
        filepath (str): the path to the file.
        data (dict): the data to be encoded as JSON and written to the file.

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    """Entry point to program.
    Interact with local file assets and the Star Wars API to create two data files.
    One is a JSON file comprising a list of likely uninhabited planets where a new rebel base
    could be situated if Imperial forces discover the location of Echo Base on the ice planet Hoth.
    The other is a JSON file of Echo Base information including an evacuation plan of base personnel
    along with passenger assignments

    Parameters:
        None

    Returns:
        None
    """

    list_of_planets = read_json("swapi_planets-v1p0.json")
    uninhabited_planets = []
    for planet in list_of_planets:
        if is_unknown(planet["population"]):
            #filter planet data
            filtered_planet = filter_data(planet, PLANET_KEYS)
            #clean planet data
            cleaned_planet = clean_data(filtered_planet)
            uninhabited_planets.append(cleaned_planet)
    write_json("swapi_planets_uninhabited-v1p1.json", uninhabited_planets)

    #enrich echo base data
    echo_base = read_json("swapi_echo_base-v1p0.json") #default dict
    url = ENDPOINT + "/planets/"
    param = {"search" : "hoth"}
    swapi_hoth = get_swapi_resource(url, params=param)["results"][0] #override data
    echo_base_hoth = echo_base["location"]["planet"] #default data
    #combine default data and override data
    hoth = combine_data(echo_base_hoth, swapi_hoth)
    #filter hoth data
    hoth = filter_data(hoth, HOTH_KEYS)
    #clean hoth data
    hoth = clean_data(hoth)
    echo_base["location"]["planet"] = hoth

    #clean Garrison commander data
    echo_base_commander = echo_base["garrison"]["commander"]
    echo_base_commander = clean_data(echo_base_commander)
    echo_base['garrison']['commander'] = echo_base_commander

    #clean Dash Rendar data
    dash_rendar = echo_base["visiting_starships"]["freighters"][1]["pilot"]
    dash_rendar = clean_data(dash_rendar)
    echo_base["visiting_starships"]["freighters"][1]["pilot"] = dash_rendar

    #clean snowspeeder data
    echo_base_snowspeeder = echo_base['vehicle_assets']['snowspeeders'][0]['type'] #default data
    swapi_vehicles_url = f"{ENDPOINT}/vehicles/"
    swapi_snowspeeder = get_swapi_resource(swapi_vehicles_url, {'search': 'snowspeeder'})['results'][0] #override data
    snowspeeder = combine_data(echo_base_snowspeeder, swapi_snowspeeder)
    snowspeeder = filter_data(snowspeeder, VEHICLE_KEYS)
    snowspeeder = clean_data(snowspeeder)
    echo_base['vehicle_assets']['snowspeeders'][0]['type'] = snowspeeder

    #clean T-65 X-wing data
    echo_base_xwing = echo_base['starship_assets']['starfighters'][0]['type'] # default data
    swapi_starships_url = f"{ENDPOINT}/starships/"
    swapi_xwing = get_swapi_resource(swapi_starships_url, {'search': 'T-65'})['results'][0]  # override data
    xwing = combine_data(echo_base_xwing, swapi_xwing)
    xwing = filter_data(xwing, STARSHIP_KEYS)
    xwing = clean_data(xwing)
    echo_base['starship_assets']['starfighters'][0]['type'] = xwing

    #clean GR-75 medium transport data
    echo_base_gr = echo_base['starship_assets']['transports'][0]['type'] #default data
    swapi_gr = get_swapi_resource(swapi_starships_url, {'search': 'GR-75'})['results'][0]  # override data
    gr = combine_data(echo_base_gr, swapi_gr)
    gr = filter_data(gr, STARSHIP_KEYS)
    gr = clean_data(gr)
    echo_base['starship_assets']['transports'][0]['type'] = gr

    #clean Millennium Falcon data
    echo_base_mf = echo_base['visiting_starships']['freighters'][0]
    swapi_mf = get_swapi_resource(swapi_starships_url, {'search': 'millennium'})['results'][0]  # override data
    mf = combine_data(echo_base_mf, swapi_mf)
    mf = filter_data(mf, STARSHIP_KEYS)
    mf = clean_data(mf)
    echo_base['visiting_starships']['freighters'][0] = mf

    #clean crew Han Solo
    swapi_people_url = f"{ENDPOINT}/people/"
    han = get_swapi_resource(swapi_people_url, {'search': 'han solo'})['results'][0]
    han = filter_data(han, PEOPLE_KEYS)
    han = clean_data(han)

    #clean crew Chewbacca
    swapi_people_url = f"{ENDPOINT}/people/"
    chewbacca = get_swapi_resource(swapi_people_url, {'search': 'Chewbacca'})['results'][0]
    chewbacca = filter_data(chewbacca, PEOPLE_KEYS)
    chewbacca = clean_data(chewbacca)

    #assign two crews to Millennium Falcon
    mf = assign_crew(mf, {'pilot': han, 'copilot': chewbacca})
    echo_base['visiting_starships']['freighters'][0] = mf

    #update evacuation plan
    evac_plan = echo_base["evacuation_plan"]

    #calculate the total of personnel
    max_base_personnel = 0
    for value in echo_base["garrison"]["personnel"].values():
        max_base_personnel = value + max_base_personnel

    #calculate the total of personnel that could be evacuated in a single lift
    max_available_transports = echo_base["starship_assets"]["transports"][0]["num_available"]
    num_of_passengers = echo_base["starship_assets"]["transports"][0]["type"]["passengers"]
    passenger_overload_multiplier = 3
    max_passenger_overload_capacity = max_available_transports * num_of_passengers * passenger_overload_multiplier

    evac_plan["max_base_personnel"] = max_base_personnel
    evac_plan["max_available_transports"] = max_available_transports
    evac_plan["max_passenger_overload_capacity"] = max_passenger_overload_capacity

    # update transport assignments
    evac_transport = echo_base["starship_assets"]["transports"][0]["type"].copy() #shallow copy
    evac_transport["name"] = "Bright Hope"

    #assign passengers
    evac_transport["passenger_manifest"] = []
    #manifest princess leia
    leia = get_swapi_resource(swapi_people_url, {'search': 'leia'})['results'][0]
    leia = filter_data(leia, PEOPLE_KEYS)
    leia = clean_data(leia)
    #manifest c-3po
    c_3po = get_swapi_resource(swapi_people_url, {'search': 'c-3po'})['results'][0]
    c_3po = filter_data(c_3po, PEOPLE_KEYS)
    c_3po = clean_data(c_3po)
    evac_transport["passenger_manifest"] = [leia, c_3po]

    #assign escorts
    evac_transport["escorts"] = []
    luke_x_wing = echo_base["starship_assets"]["starfighters"][0]["type"].copy()
    wedge_x_wing = echo_base["starship_assets"]["starfighters"][0]["type"].copy()
    
    #escort luke and r2-d2
    luke = get_swapi_resource(swapi_people_url, {'search': 'luke skywalker'})['results'][0]
    luke = filter_data(luke, PEOPLE_KEYS)
    luke = clean_data(luke)

    r2_d2 = get_swapi_resource(swapi_people_url, {'search': "r2-d2"})['results'][0]
    r2_d2 = filter_data(r2_d2, PEOPLE_KEYS)
    r2_d2 = clean_data(r2_d2)

    luke_x_wing = assign_crew(luke_x_wing, {'pilot': luke, 'astromech_droid': r2_d2})
    evac_transport['escorts'].append(luke_x_wing)

    #escort wedge and r5-d4
    wedge = get_swapi_resource(swapi_people_url, {'search': 'wedge antilles'})['results'][0]
    wedge = filter_data(wedge, PEOPLE_KEYS)
    wedge = clean_data(wedge)

    r5_d4 = get_swapi_resource(swapi_people_url, {'search': "r5-d4"})['results'][0]
    r5_d4 = filter_data(r5_d4, PEOPLE_KEYS)
    r5_d4 = clean_data(r5_d4)

    wedge_x_wing = assign_crew(wedge_x_wing, {"pilot": wedge, "astromech_droid": r5_d4})
    evac_transport["escorts"].append(wedge_x_wing)

    #update evacuation plan and write to json file
    evac_plan["transport_assignments"].append(evac_transport)
    echo_base["evacuation_plan"] = evac_plan

    write_json("swapi_echo_base-v1p1.json", echo_base)


if __name__ == '__main__':
    main()
