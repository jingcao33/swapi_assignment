# SI 506 SWAPI Echo Base Assignment

### Release Date: Tuesday, 26 November 2019, 4:00 PM

### Due Date: Monday, 16 December, 11:59 PM (no late submissions accepted) 

## 1.0 The mission
Rebel Alliance Intelligence has detected the presence of Imperial probe 
[droids](https://starwars.fandom.com/wiki/Probe_droid/Legends) in the Hoth system. The Rebel
Alliance base named Echo Base is located on the ice planet Hoth. If the Imperial probes
discover the location of the base an Imperial assault is likely to be initiated. Your job is to
write a Python program capable of producing two JSON documents that contain enriched data sourced 
from local files (provided) and the [Star Wars API](https://swapi.co/).

The Python program you write will be capable of producing two JSON files:
 
1. a document comprising a list of uninhabited planets on which a new based could be located
2. an updated and enriched Echo Base document that includes an evacuation plan for base personnel 

Each document will be produced to a specified format.  You will submit your Python program 
to a site (codename: Gradescope) for evaluation on or before the appointed due date.
 
Good luck and may the Force be with you.

## 2.0 General assignment outline
You will perform the following steps:

- Analyze this document, two JSON files that serve as default documents, and two JSON solution
files. The program you write _must_ be capable of producing JSON files that match the solution JSON 
files.

- Read local JSON files (provided), returning dictionaries that represent default collections
of key-value pairs. 

- Enrich default data whenever possible by combining it with data sourced from SWAPI.

- Refine the data by creating new dictionaries featuring an ordered subset of key-value
pairs by filtering on named keys.

- Clean values by converting strings to more appropriate data types such as `float`, `int`, `list`, 
or `None`.

- write enriched, refined, and cleaned data to JSON files.

- submit the program file to Rebel Alliance Intelligence.

## 3.0 Constraints
Consider this an open book, open notes, open network take home final. You may submit partial
or completed solutions to Gradescope as many times as is necessary prior to the deadline.

That said, certain constraints exist regarding this assignment to which you _must_ comply:

- All submitted work _must_ be your own original work. Write this program on your own without any 
assistance from others including fellow classmates, other individuals, study groups, forums, or 
tutors. Abide by the rules regarding plagiarism as defined in the syllabus.

- If you have questions regarding the SWAPI Echo Base assignment post them on Piazza.

- Submit your Python program to Gradescope for auto grading on or before Monday,
16 December, 2019, at 11:59 PM Eastern. Late submissions will _not_ be accepted. Extensions
for late assignments will _not_ be granted unless exceptional circumstances arise that prevent
you from completing the assignment on time.

- Do not install the Python SWAPI module to communicate with the SWAPI Star Wars API. Your 
script must do all the work itself.

## 3.0 Template file
The teaching team will provide you with a stubbed out Python file (the template) that provides a 
skeletal implementation of the program that you are to write. The template will include no 
documentation. Look instead to this document for instructions and guidance.

## 4.0 Scoring (2500 points)
The SWAPI Echo Base assignment is worth 2500 points. Points are assigned to each function that 
must be implemented. Points allocated to the main() function cover both the code to be
written within the function block and the two JSON files that are to be written to disk. You
submit to Gradescope the Python program _only_. No JSON files are required to be provided as
part of the submission.

## 5.0 Functions
The program the you will write _must_ include the following functions. Each function must be 
provisioned with a Docstring (see Appendix A) and the statements required for it
to perform it's assigned task. You are free to write other functions to help accomplish the assignment objectives but you __must__ implement all the functions described below to earn 
points. The functions are listed in the order in which they are evaluated by the auto grader.

:bulb: A number of the functions described below have appeared in lecture exercises and problem 
sets. Feel free to utilize that code to jump-start your work.

### 5.1 def read_json(filepath): - 100 points
This function reads a JSON document and returns a dictionary if provided with a valid filepath. 
The function defines a single parameter `filepath` (str).

When calling the built-in `open()` function set the optional `encoding` parameter to `utf-8`.

### 5.2 def get_swapi_resource(url, params=None): - 150 points
This function initiates an HTTP GET request to the SWAPI service in order to return a 
representation of a resource. The function defines two parameters, the resource `url` (str) and an 
optional `params` (dict) query string of key:value pairs may be provided as search terms (e.g., 
`{'search': 'yoda'}`). If no category (e.g., people) is provided, the root resource will be 
returned. If a match is obtained the JSON object that is returned will include a list property 
named 'results' that contains the resource(s) matched by the search query term(s).

SWAPI data is serialized as JSON.  The `get_swapi_resource()` function must decode the response 
using the `.json()` method so that the data is returned as a dictionary. 

### 5.3 def combine_data(default_data, override_data): - 150 points
This function creates a shallow copy of the default dictionary and then updates the copy with 
key-value pairs from the 'override' dictionary. The function defines two parameters, `default_data` 
(dict) and `override_data (dict). The function returns a dictionary that combines the 
key-value pairs of both the default dictionary and the override dictionary, with override values 
replacing default values on matching keys.

### 5.4 def filter_data(data, filter_keys): - 150 points
This function applies a key name filter to a dictionary in order to return an ordered subset of 
key-values. The function defines two parameters, `data` (dict) and `filter_keys` (tuple). The 
insertion order of the filtered key-value pairs is determined by the `filter_key` sequence. The
function returns a filtered collection of key-value pairs to the caller.

### 5.5 def is_number(value): - 150 points
This function applies a _case-insensitive_ truth value test for string values that equal 
`unknown` or `n/a`. The function defines a single parameter `value` (str).  Returns `True` if a 
match is obtained.

### 5.6 def convert_string_to_float(value): - 150 points
This function attempts to convert a string to a floating point value. The function defines a single 
parameter `value` (str). If unsuccessful the function returns the value unchanged. Use `try` / `except` 
blocks to accomplish the task.

:bulb: implement `try` / `except` blocks that catch the expected exception to accomplish the task.

```
try:
    return float(value)
except ValueError:
    return value
```

:warning: this function will return `True` for boolean values, faux string boolean values 
(e.g., "true"), "NaN", exponential notation, etc. That said, you will encounter none of these 
values in this assignment.

### 5.7 def convert_string_to_int(value): - 150 points
This function attempts to convert a string to an int. The function defines a single parameter
`value` (str). If unsuccessful the function _must_ return the value unchanged.

:bulb: implement `try` / `except` blocks that catch the expected exception to accomplish the task.

```
try:
    return int(value)
except ValueError:
    return value
```

:warning: this function will return `True` for boolean values, faux string boolean values 
(e.g., "true"), "NaN", exponential notation, etc. That said, you will encounter none of these 
values in this assignment.

### 5.8 def convert_string_to_list(value, delimiter=','): - 150 points
This function converts a string of delimited text values to a list. The function defines two 
parameters, `value` (str) and an optional `delimiter` (str). The function will split the passed
in string using the provided delimiter and return the resulting list to the caller.

### 5.9 def clean_data(entity): - 350 points
This function converts dictionary string values to more appropriate types such as `float`, `int`, 
`list`, or, in certain cases, `None`. The function defines a single parameter 'entity' (dict). 
The function evaluates each key-value pair encountered with `if-elif-else` conditional statements, 
membership operators, and calls to other functions that perform the actual type conversions to 
accomplish this task. After checking all values and performing type conversions on strings 
capable of conversion the function will return a dictionary with 'cleaned' values to the caller.

:bulb: consider managing value checks with tuples of ordered named keys (e.g., `int_props = 
(<key_name_01>, <key_name_02>, . . .)` that serve as filters.

The function _must_ perform the following checks and conversions:

#### General
- Convert 'unknown' or 'n/a' values to `None`. Performs truth value test with `is_number(value)`.
- Convert a decimal value masquerading as a string to `float`. Calls `convert_string_to_float(value)`.
- Convert an integer value masquerading as a string to `int`. Calls `convert_string_to_int(value)`.
- Converts comma delimited string values to type list. Calls `convert_string_to_list(value)`.

#### Person
- Convert `height` and `mass` strings to type `int`.
- Convert `hair_color` values to type list (e.g., Obi-Wan Kenobi has two listed hair colors).
- Convert `skin_color` values to a list (e.g., R2-D2 has two listed skin colors).
- Convert `homeworld` to type dict. Calls the following functions to retrieve the resource, then 
  filter, and clean the key-value pairs:
   - `get_swapi_resource(value)`
   - `filter_data(entity, PLANET_KEYS)`
   - `clean_data(entity)`
- Convert `species[0]` element to type `dict`. Calls the following functions to retrieve the resource, then 
  filter, and clean the key-value pairs:
   - `get_swapi_resource(value)`
   - `filter_data(entity, SPECIES_KEYS)`
   - `clean_data(entity)`

#### Planet
- Convert `gravity` to float. Remove extraneous text characters and whitespace.
- Convert `rotation_period`, `orbital_period`, `diameter`, `surface_water`, and `population` to int.
- Convert `climate` and `terrain` strings to type `list`. Beware trailing whitespace after the delimiter.

#### Species
- Convert `average_height` and `average_lifespan` to type `int`.
- Convert `skin_colors`, `hair_colors`, and `eye_colors` to type `list`. Beware trailing whitespace 
  after delimiter.

#### Starship
- Convert `length`, `width`, and `hyperdrive_rating` to type `float`.
- Convert `max_atmosphering_speed`, `MGLT`, `crew`, `passengers`, and `cargo_capacity` to 
  type `int`.

#### Vehicle
- Convert `length` and `width` to type `float`.
- Convert `max_atmosphering_speed`, `crew`, `passengers`, and `cargo_capacity` to type `int`.

### 5.10 def assign_crew(starship, crew): - 150 points
This function assigns crew members to a starship. The function defines two parameters, `starship` (dict)
and `crew` (dict). Each `crew` key defines a role (e.g., `pilot`, `copilot`, 
`astromech_droid`) that _must_ be used as the new `starship` key (e.g., `starship['pilot']`).
The `crew` value (dict) represents the crew member (e.g., Han Solo, Chewbacca). The function
returns an updated `starship` with one or more new crew member key-value pairs added to
the caller.

### 5.11 def write_json(filepath, data): - 100 points
Write a general-purpose function named `write_json()` capable of writing SWAPI data to a 
target JSON document file. The function defines two parameters, `filepath` (str) and the `data` 
to be written to the file. The function must be capable of processing any arbitrary combination of 
SWAPI data and filepath provided to it as arguments.

Call this function and pass it the appropriate arguments whenever you need to generate a
JSON document file required to complete the assignment.

When calling the built-in `open()` function set the optional `encoding` parameter to `utf-8`.  When
calling `json.dump()` set the optional `ensure_ascii` parameter value to False and the optional 
`indent` parameter value to 2.

### 5.12 def main(): - 750 points
The program _must_ include a `main()` function that serves as the program's entry point. Design 
the program to interact with local file assets and the Star Wars API to create two data files 
required by Rebel Alliance Intelligence. Delegate sub-tasks to other functions. Call these 
ancillary functions from `main()` or, when appropriate, from other functions as needed. 

Code you write in main() will orchestrate the creation of the following two files:

- __250 points__: `swapi_planets_uninhabited-v1p1.json`, a JSON file comprising a list of 
  likely uninhabited planets where a new rebel base could be situated if Imperial forces discover the location of Echo Base on the ice planet Hoth. 

- __500 points__: `swapi_echo_base-v1p1.json1`, a JSON file of Echo Base information including an evacuation plan of base personnel
  along with passenger assignments for Princess Leia, the communications droid C-3PO aboard
  the transport Bright Hope escorted by two X-wing starfighters piloted by Luke Skywalker
  (with astromech droid R2-D2) and Wedge Antilles (with astromech droid R5-D4). - 500 points

## 6.0 Implementation steps
I recommend adopting an iterative approach when writing your code. First, focus on generating the 
`swapi_planets_uninhabited-v1p1.json` file. The functions you must write can be implemented in 
groups as described below. Follow the steps below before attempting to produce the more complex 
`swapi_echo_base-v1p1.json` file. 

### 6.1 Global constants
First, create a set of global constants located at the top of your program file immediately below
the `import` statements.

1. Assign the URL string 'https://swapi.co/api' to a global constant named `ENDPOINT`.
2. Create an additional set of tuple constants that comprise _ordered_ collection of key names based
   on the key names described in the Entity tables listed below:
   - `PEOPLE_KEYS`
   - `PLANET_KEYS`
   - `STARSHIP_KEYS`
   - `SPECIES_KEYS`
   - `VEHICLE_KEYS`  

You will use these constants as named key filters throughout your program.

### 6.2 Filter planet data
You will work with local file resources initially, not SWAPI. Review the following files: 

- input: `swapi_planets-v1p0.json`
- output: `swapi_planets_uninhabited-v1p1.json` (see provided test solution file)
 
then implement the following functions (described above):

- `read_json()`
- `filter_data()`
- `is_unknown()`
- `write_json()`

You will call these functions from `main()` in order to perform the following operations:

1. Read `swapi_planets-v1p0.json` and return a list of planet dictionaries.
2. Create an empty list in `main()` to hold uninhabited planet data.
3. Iterate over the list of planet dictionaries. 
   1. Call `is_unknown()` and perform a _case-insensitive_ truth value test on each planet's population value.
   2. If the value is considered an unknown (e.g., unknown or n/a) call 
      `filter_data(planet, PLANET_KEYS)` and return a new dictionary with a filtered set of 
      key-value pairs. 
   3. Append the new dictionary to a (growing) list of uninhabited planets.
4. Once all the uninhabited planets have been appended to the list of uninhabited planets,
   write the list of dictionaries to a file named `swapi_planets_uninhabited-v1p1.json`.

Demonstrate to yourself that you can execute the steps above and generate uninhabited planet
data. Once your read, filter and write operations are working correctly, start the next
iteration.

### 6.3 Clean planet values
This iteration step involves "cleaning" uninhabited planet values, converting strings capable of 
conversion to new types: `float`, `int`, `list` or `None` (for unknown, n/a values).

Implement the following functions (described above):

- `convert_string_to_float()`
- `convert_string_to_int()`
- `convert_string_to_list()`
- `clean_data()`

The focus of this phase of the development process is on the conversion of string values to more 
appropriate data types. The function `clean_data()` manages the value conversion logic, 
calling `is_number()` to check for unknown values and converting those values to `None.` 

`clean_data()` will also call various `convert_string_to_*()` functions that will perform the 
type conversion operations. In `clean_data()` create a set of property name tuples based on the 
Appendix B tables "converted to" types (see below)

```
float_props = (<key_01>, <key_02>, ...)
int_props = (<key_01>, <key_02>, ...) 
list_props = (<key_01, key_02, ...>)
dict_props = (<key_01, key_02, ...>)
```

Example:

```
int_props = ('rotation_period', 'orbital_period', 'diameter', 'surface_water', 'population',
             'height', 'mass', 'average_height', 'average_lifespan', 'max_atmosphering_speed',
             'MGLT', 'crew', 'passengers', 'cargo_capacity')
```

Use the tuples to perform membership tests on properties and their values in `clean_data()`:

```
cleaned = {}
. . .
if key in int_props:
    cleaned[key] = convert_string_to_int(value)
. . .
```

Once `clean_data()` and the `convert_string_to_*()` are written perform the perform the following 
operations:

1. Read `swapi_planets-v1p0.json` and return a list of planet dictionaries.
2. Create an empty list in `main()` to hold uninhabited planet data.
3. Iterate over the list of planet dictionaries. 
   1. Call `is_unknown()` and perform a _case-insensitive_ truth value test on each planet's 
   population value.
   2. If the value is considered an unknown (e.g., unknown or n/a) call 
      `filter_data(planet, PLANET_KEYS)` and return a new dictionary with a filtered set of 
      key-value pairs.
   3. __NEW__: while still in the loop call `clean_data(planet)` to convert the new dictionary's string values to an appropriate type such as `float`, `int`, `list` or `None`. If no match is 
   made return the original string unchanged. 
   4. Append the new dictionary to a (growing) list of uninhabited planets.
4. Once all the uninhabited planets have been appended to the list of uninhabited planets,
   write the list of dictionaries to a file named `swapi_planets_uninhabited-v1p1.json`.

Once the clean operation is integrated successfully start the next iteration.

:bulb: compare the file you are generating with the test solution file regularly in order
to gauge your process. This is called "diffing" your files. For VS Code users see Gérald Barré's 
blog post 
["Comparing files using Visual Studio Code"](https://www.meziantou.net/comparing-files-using-visual-studio-code.htm)
(Mar 2018) on how to compare two files using the VS Code user interface

### 6.4 Enrich Echo Base data
Starting with this phase you will work with local files _and_ the Star Wars API. Review the 
following files: 

- input: `swapi_echo_base-v1p0.json`
- output: `swapi_echo_base-v1p1.json` (see provided test solution file)

Implement the following functions (described above):

- `get_swapi_resource()`
- `combine_data()`
- `assign_crew()`

The task here is to implement `get_swapi_resource()` so that you can communicate with SWAPI in
order to request resources and `combine_data()` in order to blend or enrich the default dictionary 
representation of a person, planet, starship, or vehicle with data sourced from SWAPI.

#### 6.4.1 Ice planet Hoth
Now enrich the Echo Base ice planet Hoth nested dictionary. Call the new functions you have 
implemented from `main()` along with other functions implemented previously in order to perform 
the following operations:
  
 1. Read `swapi_echo_base-v1p0.json` and return a dictionary named `echo_base`. This comprises the
    default dictionary which you will enrich.
 2. Call `get_swapi_resource()` and retrieve a SWAPI representation of the ice planet Hoth. 
    Assign it to a variable named `swapi_hoth`.
 3. Assign the `eco_base` representation of the ice planet Hoth to a variable named 
    `echo_base_hoth`.
 4. Call `combine_data(echo_base_hoth, swapi_hoth)` and return a dictionary named `hoth` that 
    combines key-value pairs of two dictionaries passed to `combine_data()`.  
 5. Call `filter_data(hoth, PLANET_KEYS)` and return a new dictionary with a filtered set of 
    key-value pairs.
 6. Call `clean_data(hoth)` to convert the new dictionary's string values to an appropriate type 
    such as `float`, `int`, `list` or `None`. If no match is made return the original string unchanged.
 7. Replace the default `echo_base` Hoth value with the combined, filtered, and 
    cleaned `hoth` dictionary.
 8. Run your code and check the output file. Debug as necessary.
    
Your code should resemble the following snippet:
 
```
echo_base_hoth = echo_base['location']['planet']
hoth = combine_data(echo_base_hoth, swapi_hoth)
hoth = filter_data(hoth, PLANET_KEYS)
hoth = clean_data(hoth)
echo_base['location']['planet'] = hoth
```   

#### 6.4.2 Garrison commander
Next, enrich the Echo Base garrison commander's record. Since there is no SWAPI representation
of General Carlist_Rieekan you can skip calling `combine_data()` and `filter_data()`.

```
echo_base_commander = echo_base['garrison']['commander']
echo_base_commander = clean_data(echo_base_commander)
echo_base['garrison']['commander'] = echo_base_commander
```

If you have implemented `clean_data()` correctly, the updated `echo_base` Rieekan nested dictionary 
should itself now include nested dictionaries (cleaned of course) of Rieekan's `homeworld` and 
`species` values.

#### 6.4.3 Corellian Smuggler Dash Rendar
Perform the same set of operations to enrich the Corellian smuggler Dash Rendar's `echo_base` 
nested dictionary. He too has no SWAPI representation so no need to call `combine_data()` and 
`filter_data()` for him either.

#### 6.4.4 Snowspeeder
Next, enrich the `echo_base` snowspeeder nested dictionary. 

1. Assign the `echo_base` dictionary representation of the snowspeeder to a variable named 
   `echo_base_snowspeeder`.
2. Call `get_swapi_resource()` to retrieve a SWAPI representation of the snowspeeder (search on 
   'snowspeeder') and assign to a variable named `swapi_snowspeeder`.
3. Call `combine_data()`, `filter_data()`, and `clean_data()` in succession in order to create a
   new enriched dictionary representation of the snowspeeder.
4. Run your code and check the output file. Debug as necessary.

Your code should resemble the following snippet:

```
swapi_vehicles_url = f"{ENDPOINT}/vehicles/"
swapi_snowspeeder = get_swapi_resource(swapi_vehicles_url, {'search': 'snowspeeder'})['results'][0]

echo_base_snowspeeder = echo_base['vehicle_assets']['snowspeeders'][0]['type']

snowspeeder = combine_data(echo_base_snowspeeder, swapi_snowspeeder)
snowspeeder = filter_data(snowspeeder, VEHICLE_KEYS)
snowspeeder = clean_data(snowspeeder)
echo_base['vehicle_assets']['snowspeeders'][0]['type'] = snowspeeder
```

The enriched nested JSON representation of the snowspeeder should resemble the following:

```json
{
  "url": "https://swapi.co/api/vehicles/14/",
  "vehicle_class": "airspeeder",
  "name": "Snowspeeder",
  "model": "t-47 airspeeder",
  "manufacturer": "Incom corporation",
  "length": 4.5,
  "max_atmosphering_speed": 650,
  "crew": 2,
  "passengers": 0,
  "cargo_capacity": 10,
  "consumables": "none",
  "armament": [
    "CEC AP/11 double laser cannons[ (2x)",
    "Rear-facing Ubrikkian Mo/Dk energy harpoon[1] and tow cable (1x)",
    "Rear-facing light repeating blaster cannon (1x)"
  ]
}
```  
    
:bulb: The site [jsoncompare.com](https://jsoncompare.com/#!/simple/) provides a browser-based
GUI for inspecting and reformatting JSON documents {} and lists [].

#### 6.4.5 T-65 X-wing, GR-75 medium transport, and Millennium Falcon
Enriching the nested T-65 X-wing (search SWAPI for 't-65 x-wing'), GR-75 medium transport, and 
Millennium Falcon dictionaries involves implementing the same steps used to enrich the
`echo_base` snowspeeder nested dictionary. Note the implementation pattern (get, combine, 
filter, clean). You will follow it for the remainder of the assignment.

#### 6.4.6 Assign crew to the Millennium Falcon   
Update the enriched `echo_base` Millennium Falcon nested dictionary with crew assignments.
First, call SWAPI and retrieve a dictionary representation of Han Solo. Since Han is not
described in `echo_base` there is no default dictionary to combine with the SWAPI sourced
dictionary. Simply filter and clean his dictionary.

```
swapi_people_url = f"{ENDPOINT}/people/"
han = get_swapi_resource(swapi_people_url, {'search': 'han solo'})['results'][0]
han = filter_data(han, PERSON_KEYS)
han = clean_data(han)
```

Retrieve Chewbacca in the same manner. Then call `assign_crew()` passing in a dictionary
of the two crew members with key name providing the new property name to be added to
`m_falcon`:

```
m_falcon = assign_crew(m_falcon, {'pilot': han, 'copilot': chewie})
echo_base['visiting_starships']['freighters'][0] = m_falcon
```

Run your code and compare the output against the test solution file.

### 6.5 Update evacuation plan
Rebel Intelligence requires that the `echo_base['evacuation_plan']` nested dictionary be 
updated in case an Imperial probe discovers the location of the base. The following data
is required:

- total base personnel
- available transports
- total number of personnel that can be evacuated in a single lift (base personnel * 
  available transports * passenger overload multiplier)
- a single transport assignment to be added to the transport assignments list for Princess
  Leia Organa and the communications droid C-3PO
- two X-wing starfighter escorts piloted by Luke Skywalker (with `astromech_droid` R2-D2) and
  and Wedge Antilles (with `astromech_droid` R5-D4)

Assign the skeletal `echo_base` evacuation plan to a variable named `evac_plan`:

```
evac_plan = echo_base['evacuation_plan']
```

#### 6.5.1 Evacuation arithmetic
Loop over the `echo_base` nested `personnel` dictionary to get a total count of base personnel. Get
the total number of `echo_base` available transports and the evacuation plan 
`passenger_overload_multiplier` value. Then compute the total number of base personnel that can
be evacuated in a single lift prior to an Imperial assault on the base. Update the
`echo_base['evacuation_plan']` properties with these values.

#### 6.5.2 Bright Hope transport assignment
Next, make a _shallow_ copy of the `echo_base` transport dictionary (e.g., `transport.copy()`) and
assign it to a variable named `evac_transport`. Set the name of the transport to 'Bright Hope'.

#### 6.5.2 Assign passengers
Create a new list property:

```
evac_transport['passenger_manifest'] = []
```

Populate the `evac_transport['passenger_manifest']` with two passengers: Princess Leia Organa and
the communications droid C-3PO. Retrieve person data from SWAPI and filter and clean the data in the same manner as you did earlier for Han Solo.

#### 6.5.3 Assign starfighter escorts
The transport _Bright Hope_ is to be escorted by two X-wing starfighters. Create a new list 
property: 

```
evac_transport['escorts'] = []
```

Then create two _shallow_ copies of the `echo_base` nested X-wing starfighter dictionary. Assign
one copy to a variable named `luke_x_wing` and the second copy to a variable named `wedge_x_wing`.

Call `get_swapi_resource()` twice in order to retrieve SWAPI representations of Commander
Luke Skywalker and the astromech droid R2-D2.  Filter and clean these person dictionaries and then
call `assign_crew()`:

```
luke_x_wing = assign_crew(luke_x_wing, {'pilot': luke, 'astromech_droid': r2_d2})
evac_transport['escorts'].append(luke_x_wing)
```

Assign pilot Wedge Antilles and the astro mech droid R5-D4 to the second X-wing `wedge_x_wing` and 
then append the second escort starfighter to the `evac_transport['escorts']` list. Follow the same steps as 
above to complete the task.

#### 6.5.4 Complete the evacuation plan and write to file
Next, append the `evac_transport` dictionary to `evac_plan['transport_assignments']`. Then assign 
the updated `evac_plan` dictionary to `echo_base['evacuation_plan']` replacing the default 
skeletal plan.

Finally, write the enriched `echo_base` dictionary data to a file named `swapi_echo_base-v1p1.json`.
Perform a diff on the file against the test solution file. If differences exist debug as necessary.
If the files match, submit your `swapi_assignment.py` file to Rebel Alliance Intelligence 
(code name: Gradescope) for evaluation. You may resubmit your Python program file as many times as
is necessary to earn maximum points prior to the deadline. 

## Appendix A. Docstrings
Each function _must_ include a "Docstring" that describes the function, parameters (including 
optional parameter default values), and return value, if any. Utilize the following `Docstring` 
format to document your functions:

* Function description (~1-3 sentences).
* Parameters:
    - arg_1 (type): argument 1 description.
    - arg_2 (type): argument 2 description.
* Returns:
    - type: return value description

When describing parameters and return value (if any) use the following data type abbreviations:

| Data type | Abbreviation |
|:--------- | :----------- |
| Boolean | bool |
| Complex number | complex |
| Dictionary | dict |
| Float | float |
| Integer | int |
| List | list |
| String | str |
| Tuple | tuple |

### A.1 Docstring examples
```python
import json

def read_json(filepath):
    """Given a valid filepath reads a JSON document and returns a dictionary.

    Parameters:
        filepath (str): path to file.

    Returns:
        dict: dictionary representations of the decoded JSON document.
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        data = json.load(file_obj)

    return data
```

:bulb: If a function does not define any parameters and/or does not specify an explicit 
`return` statement (i.e., returns `None` implicitly) use the word "None" in place of any
parameter or return statement descriptions.

```python
def main():
    """Entry point. This program will interact with local file assets and the Star Wars
    API to create two data files required by Rebel Alliance Intelligence.

    - A JSON file comprising a list of likely uninhabited planets where a new rebel base could be
      situated if Imperial forces discover the location of Echo Base.

    - A JSON file of Echo Base information including an evacuation plan of base personnel
      along with passenger assignments for Princess Leia, the communications droid C-3PO aboard
      the transport Bright Hope escorted by two X-wing starfighters piloted by Luke Skywalker
      (with astromech droid R2-D2) and Wedge Antilles (with astromech droid R5-D4).

    Parameters:
        None

    Returns:
        None
    """

    # Orchestrate workflow starting here.
```

## Appendix B. Entities
Your program will interact with the following entities sourced from local files and from SWAPI.
You can use these tables as well as the test solution files to construct global constants of
named key values that you will employ as filters when excluding/including key-value pairs 
during filtering operations (e.g., `PEOPLE_KEYS`).  

Also, use these tables when writing the `clean_data()` function to create a set of filtering 
tuples of named properties linked to values that can be converted to a particular type as in 
the following example:

```
dict_props = ('homeworld', 'species')
```

### Person 
__sources: `swapi-echo_base-v1p0.json`, SWAPI__

The Echo Base `swapi-echo_base-v1p0.json` file contains default data on two individuals
not described in the SWAPI people data set: base commander General 
[Carlist Rieekan](https://starwars.fandom.com/wiki/Carlist_Rieekan/Legends)
and the Corellian smuggler [Dash Rendar](https://starwars.fandom.com/wiki/Dash_Rendar/Legends). Their records can be enriched with `homeworld` and `species` data 
obtained by issuing a GET request to SWAPI.

Data on other leading Rebel Alliance members including 
Princess [Leia Organa](https://starwars.fandom.com/wiki/Leia_Organa_Solo), 
Commander [Luke Skywalker](https://starwars.fandom.com/wiki/Luke_Skywalker/Legends), 
Pilot [Wedge Antilles](https://starwars.fandom.com/wiki/Wedge_Antilles/Legends), 
the smugglers [Han Solo](https://starwars.fandom.com/wiki/Han_Solo/Legends) and 
[Chewbacca](https://starwars.fandom.com/wiki/Chewbacca/Legends), and the droids 
[C-3PO](https://starwars.fandom.com/wiki/C-3PO/Legends), 
[R2-D2](https://starwars.fandom.com/wiki/R2-D2/Legends), and
[R5-D4](https://starwars.fandom.com/wiki/R5-D4/Legends) can be sourced from SWAPI.

| insert order | key | value type | convert to | notes |
| ------------: | :--- | :-------: | :--------: | :---- |
| 1 | url | str |  | |
| 2 | name | str | | SWAPI search field. |
| 3 | mass | str | int | |
| 4 | hair_color | str | list | |
| 5 | skin_color | str | list | |
| 6 | eye_color | str | | |
| 7 | birth_year | str | | |
| 8 | gender | str | | |
| 9 | homeworld | str | dict | Retrieve `homeworld` (planet) data from SWAPI. |
| 10 | species | str | dict | Retrieve `species` data from SWAPI. |

### Planet 
__sources: `swapi-planets-v1p0.json`, SWAPI__

Filtered SWAPI planet data is provided in `swapi-planets-v1p0.json`. A person's `homeworld` data
can be derived from this file or retrieved by issuing a GET request to SWAPI.

| insert order | key | value type | convert to | notes |
| ------------: | :--- | :-------: | :--------: | :---- |
| 1 | url | str |  | |
| 2 | name | str | | SWAPI search field. |
| 3 | rotation_period | str | int | |
| 4 | orbital_period | str | int | |
| 5 | diameter | str | int | |
| 6 | climate | str | list | |
| 7 | gravity | str | float | Conversion to a float requires first removing the trailing substring 'standard' and all whitespace, if included in the original string. |
| 8 | terrain | str | list | |
| 9 | surface_water | int | | |
| 10 | population | str | int | |

### Planet Hoth 
__sources: `swapi-echo_base-v1p0.json1`, SWAPI__

The Echo Base `swapi-echo_base-v1p0.json` file entry for the ice planet Hoth is enriched with 
additional key-value pairs that must be combined with Hoth data obtained from either the
`swapi-planets-v1p0.json` or from SWAPI.

| insert order | key | value type | convert to | notes |
| ------------: | :--- | :-------: | :--------: | :---- |
| 1 | url | str |  | |
| 2 | name | str | | SWAPI search field |
| 3 | system_position | int | | Non-SWAPI property sourced from [Wookieepedia](https://starwars.fandom.com/wiki/Hoth/Legends) Hoth legends entry. |
| 4 | natural_satellites | int | | |
| 5 | rotation_period | str | int | |
| 6 | orbital_period | str | int | |
| 7 | diameter | str | int | |
| 8 | climate | str | list | |
| 9 | gravity | str | float | Requires removal of trailing word 'standard' and all whitespace if exists. |
| 10 | terrain | str | list | |
| 11 | surface_water | int | | |
| 12 | population | str | int | |
| 13 | indigenous_life_forms | list | | |

### Species (SWAPI)
__source: SWAPI__

Obtaining species data requires issuing a GET request to SWAPI.

| insert order | key | value type | convert to | notes |
| ------------: | :--- | :-------: | :--------: | :---- |
| 1 | url | str |  | |
| 2 | name | str | | SWAPI search field. |
| 3 | classification | str |  | |
| 4 | designation | str |  | |
| 5 | average_height | str | int | |
| 6 | skin_colors | str | list | |
| 7 | hair_colors | str | list | |
| 8 | eye_colors | str | list | |
| 9 | average_lifespan | str | int |  |
| 10 | language | str |  |  |

### Starship 
__sources: `swapi-echo_base-v1p0.json`, SWAPI__

The Echo Base `swapi-echo_base-v1p0.json` file contains default data on the 
[T-65 X-wing starfighter](https://starwars.fandom.com/wiki/T-65B_X-wing_starfighter/Legends), 
[GR-75 medium transport](https://starwars.fandom.com/wiki/GR-75_medium_transport/Legends), 
and the light freighters [Millennium Falcon](https://starwars.fandom.com/wiki/Millennium_Falcon/Legends) 
and [Outrider](https://starwars.fandom.com/wiki/Outrider/Legends). Utilize SWAPI resources
to enrich the starship data as well as retrieve individual crew data.

| insert order | key | value type | convert to | notes |
| ------------: | :--- | :-------: | :--------: | :---- |
| 1 | url | str |  | |
| 2 | starship_class | str | | |
| 3 | name | str |  | SWAPI search field. |
| 4 | model | str |  | SWAPI search field. |
| 5 | manufacturer | str | | |
| 6 | length | str | float | |
| 7 | width | float | | Non-SWAPI property sourced from [Wookieepedia](https://starwars.fandom.com/wiki/Main_Page).  |
| 8 | max_atmosphering_speed | str | int | |
| 9 | hyperdrive_rating | str | float | |
| 10 | crew | str | int | |
| 11 | passengers | str | int |  |
| 12 | cargo_capacity | str | int |  |
| 13 | consumables | str |  |  |
| 14 | armament | list |  | Non-SWAPI property sourced from [Wookieepedia](https://starwars.fandom.com/wiki/Main_Page). |

### Vehicle 
__sources: `swapi-echo_base-v1p0.json`, SWAPI__

The Echo Base `swapi-echo_base-v1p0.json` file contains default data on the 
t-47 airspeeder, adapted for use on the ice planet Hoth and renamed the 
[snowspeeder](https://starwars.fandom.com/wiki/Snowspeeder). 
Enriching this data requires issuing a GET request to SWAPI.

| insert order | key | value type | convert to | notes |
| ------------: | :--- | :-------: | :--------: | :---- |
| 1 | url | str |  | |
| 2 | vehicle_class | str | | |
| 3 | name | str |  | SWAPI search field. |
| 4 | model | str |  | SWAPI search field. |
| 5 | manufacturer | str | | |
| 6 | length | str | float | |
| 7 | max_atmosphering_speed | str | int | |
| 8 | crew | str | int | |
| 9 | passengers | str | int |  |
| 10 | cargo_capacity | str | int |  |
| 11 | consumables | str |  |  |
| 12 | armament | list |  | Non-SWAPI property sourced from [Wookieepedia](https://starwars.fandom.com/wiki/Main_Page). |
