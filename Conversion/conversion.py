def inches_feet(text):
    return float(text) / 12


def inches_cm(text):
    return float(text) * 2.54


def inches_yards(text):
    return float(text) / 36


def inches_meter(text):
    return float(text) / 39.37


def inches_mile(text):
    return float(text) / 63360


def inches_km(text):
    return float(text) / 39370.8


def inches_mm(text):
    return float(text) * 25.4


def cm_feet(text):
    return float(text) / 30.48


def cm_inches(text):
    return float(text) / 2.54


def cm_yard(text):
    return float(text) / 91.44


def cm_meter(text):
    return float(text) / 100


def cm_miles(text):
    return float(text) / 160934.4


def cm_km(text):
    return float(text) / 100000


def cm_mm(text):
    return float(text) * 10


def yards_feet(text):
    return float(text) * 3


def yards_inches(text):
    return float(text) * 36


def yards_cm(text):
    return float(text) * 91.44


def yards_meter(text):
    return float(text) / 1.09


def yards_miles(text):
    return float(text) / 1760


def yards_km(text):
    return float(text) / 1093.61


def yards_mm(text):
    return float(text) * 914.4


def meters_feet(text):
    return float(text) * 3.28


def meters_inches(text):
    return float(text) * 39.37


def meters_cm(text):
    return float(text) * 100


def meters_yards(text):
    return float(text) * 1.09


def meters_miles(text):
    return float(text) / 1609.34


def meters_km(text):
    return float(text) / 1000


def meters_mm(text):
    return float(text) * 1000


def miles_feet(text):
    return float(text) * 5280


def miles_inches(text):
    return float(text) * 63360


def miles_yard(text):
    return float(text) * 1760


def miles_meters(text):
    return float(text) * 1609.34


def miles_cm(text):
    return float(text) * 160934.4


def miles_km(text):
    return float(text) * 1.61


def miles_mm(text):
    return float(text) * 1609344


def km_feet(text):
    return float(text) * 3280.84


def km_inches(text):
    return float(text) * 39370.08


def km_cm(text):
    return float(text) * 100000


def km_yards(text):
    return float(text) * 1093.61


def km_meters(text):
    return float(text) * 1000


def km_miles(text):
    return float(text) * 0.62


def km_mm(text):
    return float(text) * 1000000


def feet_inches(text):
    return float(text) * 12


def feet_cm(text):
    return float(text) * 30.48


def feet_yards(text):
    return float(text) * 0.33


def feet_meters(text):
    return float(text) * 0.3


def feet_miles(text):
    return float(text) * 0.00019


def feet_km(text):
    return float(text) * 0.0003


def feet_mm(text):
    return float(text) * 304.8


def mm_inches(text):
    return float(text) * 0.039


def mm_cm(text):
    return float(text) * 0.1


def mm_yards(text):
    return float(text) * 0.0011


def mm_meters(text):
    return float(text) * 0.001


def mm_miles(text):
    return float(text) * 0.00000062


def mm_km(text):
    return float(text) * 0.000001


def mm_feet(text):
    return float(text) * 0.0033


print(
    "We can conver between inches,feet,centimeters,meters,yards,miles,kilometers, and millimeters"
)
question = input("What do you want to convert? (inches to centimeters)\n:")
new_question = question.split()
first = new_question[0].lower()
second = new_question[2].lower()
second_question = input(f"How many {first} do you want to convert to {second}?\n:")
value = second_question
if first == "inches" and second == "centimeters":
    incm = str(inches_cm(value))
    new_incm = incm[0:8]
    print("There are " + new_incm + " centimeters in " + value + " inches!")
if first == "inches" and second == "feet":
    inft = str(inches_feet(value))
    new_inft = inft[0:8]
    print("There are " + new_inft + " feet in " + value + " inches!")
if first == "inches" and second == "yards":
    inyd = str(inches_yards(value))
    new_inyd = inyd[0:8]
    print("There are " + new_inyd + " yards in " + value + " inches!")
if first == "inches" and second == "meters":
    inm = str(inches_meter(value))
    new_inm = inm[0:8]
    print("There are " + new_inm + " meters in " + value + " inches!")
if first == "inches" and second == "miles":
    inmi = str(inches_mile(value))
    new_inmi = inmi[0:8]
    print("There are " + new_inmi + " miles in " + value + " inches!")
if first == "inches" and second == "kilometers":
    inkm = str(inches_km(value))
    new_inkm = inkm[0:8]
    print("There are " + new_inkm + " kilometers in " + value + " inches!")
if first == "inches" and second == "millimeters":
    inmm = str(inches_mm(value))
    new_inmm = inmm[0:8]
    print("There are " + new_inmm + " millimeters in " + value + " inches!")
if first == "centimeters" and second == "inches":
    cmin = str(cm_inches(value))
    new_cmin = cmin[0:8]
    print("There are " + new_cmin + " inches in " + value + " centimeters!")
if first == "centimeters" and second == "feet":
    cmft = str(cm_feet(value))
    new_cmft = cmft[0:8]
    print("There are " + new_cmft + " feet in " + value + " centimeters!")
if first == "centimeters" and second == "yards":
    cmyd = str(cm_yard(value))
    new_cmyd = cmyd[0:8]
    print("There are " + new_cmyd + " yards in " + value + "centimeters!")
if first == "centimeters" and second == "meters":
    cmm = str(cm_meter(value))
    new_cmm = cmm[0:8]
    print("There are " + new_cmm + " meters in " + value + " centimeters!")
if first == "centimeters" and second == "miles":
    cmmi = str(cm_miles(value))
    new_cmmi = cmmi[0:8]
    print("There are " + new_cmmi + " miles in " + value + " centimeters!")
if first == "centimeters" and second == "kilometers":
    cmkm = str(cm_km(value))
    new_cmkm = cmkm[0:8]
    print("There are " + new_cmkm + " kilometers in " + value + "centimeters!")
if first == "centimeters" and second == "millimeters":
    cmmm = str(cm_mm(value))
    new_cmmm = cmmm[0:8]
    print("There are " + new_cmmm + " millimeters in " + value + " centimeters!")
if first == "yards" and second == "centimeters":
    ydcm = str(yards_cm(value))
    new_ydcm = ydcm[0:8]
    print("There are " + new_ydcm + " centimeters in " + value + " yards!")
if first == "yards" and second == "inches":
    ydin = str(yards_inches(value))
    new_ydin = ydin[0:8]
    print("There are " + new_ydin + " inches in " + value + " yards!")
if first == "yards" and second == "meters":
    ydm = str(yards_meter(value))
    new_ydm = ydm[0:8]
    print("There are " + new_ydm + " meters in " + value + " yards!")
if first == "yards" and second == "miles":
    ydmi = str(yards_miles(value))
    new_ydmi = ydmi[0:8]
    print("There are " + new_ydmi + " miles in " + value + " yards!")
if first == "yards" and second == "kilometers":
    ydkm = str(yards_km(value))
    new_ydkm = ydkm[0:8]
    print("There are " + new_ydkm + " kilometers in " + value + " yards!")
if first == "yards" and second == "millimeters":
    ydmm = str(yards_mm(value))
    new_ydmm = ydmm[0:8]
    print("There are " + new_ydmm + " millimeters in " + value + " yards!")
if first == "yards" and second == "feet":
    ydft = str(yards_feet(value))
    new_ydft = ydft[0:8]
    print("There are " + new_ydft + " feet in " + value + " yards!")
if first == "meters" and second == "centimeters":
    mcm = str(meters_cm(value))
    new_mcm = mcm[0:8]
    print("There are " + new_mcm + " centimeters in " + value + " meters!")
if first == "meters" and second == "inches":
    minch = str(meters_inches(value))
    new_min = minch[0:8]
    print("There are " + new_min + " inches in " + value + "meters!")
if first == "meters" and second == "feet":
    mft = str(meters_feet(value))
    new_mft = mft[0:8]
    print("There are " + new_mft + " feet in " + value + "meters!")
if first == "meters" and second == "yards":
    myd = str(meters_yards(value))
    new_myd = myd[0:8]
    print("There are " + new_myd + " yards in " + value + " meters!")
if first == "meters" and second == "miles":
    mmi = str(meters_miles(value))
    new_mmi = mmi[0:8]
    print("There are " + new_mmi + " miles in " + value + " metes!")
if first == "meters" and second == "millimeters":
    mmm = str(meters_mm(value))
    new_mmm = mmm[0:8]
    print("There are " + new_mmm + " millimeters in " + value + " meters!")
if first == "meters" and second == "kilometers":
    mkm = str(meters_km(value))
    new_mkm = mkm[0:8]
    print("There are " + new_mkm + " kilometers in " + value + " meters!")
if first == "feet" and second == "inches":
    ftin = str(feet_inches(value))
    new_ftin = ftin[0:8]
    print("There are " + new_ftin + " inches in " + value + " feet!")
if first == "feet" and second == "centimeters":
    ftcm = str(feet_cm(value))
    new_ftcm = ftcm[0:8]
    print("There are " + new_ftcm + " centimeters in " + value + " feet!")
if first == "feet" and second == "yards":
    ftyd = str(feet_yards(value))
    new_ftyd = ftyd[0:8]
    print("There are " + new_ftyd + " yards in " + value + " feet!")
if first == "feet" and second == "meters":
    ftm = str(feet_meters(value))
    new_ftm = ftm[0:8]
    print("There are " + new_ftm + " meters in " + value + " feet!")
if first == "feet" and second == "miles":
    ftmi = str(feet_miles(value))
    new_ftmi = ftmi[0:8]
    print("There are " + new_ftmi + " miles in " + value + " feet!")
if first == "feet" and second == "kilometers":
    ftkm = str(feet_km(value))
    new_ftkm = ftkm[0:8]
    print("There are " + new_ftkm + " kilometers in " + value + " feet!")
if first == "feet" and second == "millimeters":
    ftmm = str(feet_mm(value))
    new_ftmm = ftmm[0:8]
    print("There are " + new_ftmm + " millimeters in " + value + " feet!")
if first == "millimeters" and second == "inches":
    mmin = str(mm_inches(value))
    new_mmin = mmin[0:8]
    print("There are " + new_mmin + " inches in " + value + " millimeters!")
if first == "millimeters" and second == "centimeters":
    mmcm = str(mm_cm(value))
    new_mmcm = mmcm[0:8]
    print("There are " + new_mmcm + " centimeters in " + value + " millimeters!")
if first == "millimeters" and second == "yards":
    mmyd = str(mm_yards(value))
    new_mmyd = mmyd[0:8]
    print("There are " + new_mmyd + " yards in " + value + " millimeters!")
if first == "millimeters" and second == "meters":
    m_mm = str(mm_meters(value))
    new_m_mm = m_mm[0:8]
    print("There are " + new_m_mm + " meters in " + value + " millimeters!")
if first == "millimeters" and second == "miles":
    mmmi = str(mm_miles(value))
    new_mmmi = mmmi[0:8]
    print("There are " + new_mmmi + " miles in " + value + " millimeters!")
if first == "millimeters" and second == "kilometers":
    mmkm = str(mm_km(value))
    new_mmkm = mmkm[0:8]
    print("There are " + new_mmkm + " kilometers in " + value + " millimeters!")
if first == "millimeters" and second == "feet":
    mmft = str(mm_feet(value))
    new_mmft = mmft[0:8]
    print("There are " + new_mmft + " feet in " + value + " millimeters!")
if first == "miles" and second == "inches":
    miin = str(miles_inches(value))
    new_miin = miin[0:8]
    print("There are " + new_miin + " inches in " + value + " miles!")
if first == "miles" and second == "centimeters":
    micm = str(miles_cm(value))
    new_micm = micm[0:20]
    print("There are " + new_micm + " centimeters in " + value + " miles!")
if first == "miles" and second == "feet":
    mift = str(miles_feet(value))
    new_mift = mift[0:20]
    print("There are " + new_mift + " feet in " + value + " miles!")
if first == "miles" and second == "yards":
    miyd = str(miles_yard(value))
    new_miyd = miyd[0:8]
    print("There are " + new_miyd + " yards in " + value + " miles!")
if first == "miles" and second == "meters":
    mim = str(miles_meters(value))
    new_mim = mim[0:8]
    print("There are " + new_mim + " meters in " + value + " miles!")
if first == "miles" and second == "kilometers":
    mikm = str(miles_km(value))
    new_mikm = mikm[0:8]
    print("There are " + new_mikm + " kilometers in " + value + " miles!")
if first == "miles" and second == "millimeters":
    mimm = str(miles_mm(value))
    new_mimm = mimm[0:30]
    print("There are " + new_mimm + " millimeters in " + value + " miles!")
if first == "kilometers" and second == "inches":
    kmin = str(km_inches(value))
    new_kmin = kmin[0:15]
    print("There are " + new_kmin + " inches in " + value + " kilometers!")
if first == "kilometers" and second == "centimeters":
    kmcm = str(km_cm(value))
    new_kmcm = kmcm[0:15]
    print("There are " + new_kmcm + " centimeters in " + value + " kilometers!")
if first == "kilometers" and second == "feet":
    kmft = str(km_feet(value))
    new_kmft = kmft[0:8]
    print("There are " + new_kmft + " feet in " + value + " kilometers!")
if first == "kilometers" and second == "yards":
    kmyd = str(km_yards(value))
    new_kmyd = kmyd[0:8]
    print("There are " + new_kmyd + " yards in " + value + " kilometers!")
if first == "kilometers" and second == "meters":
    kmm = str(km_meters(value))
    new_kmm = kmm[0:8]
    print("There are " + new_kmm + " meters in " + value + " kilometers!")
if first == "kilometers" and second == "millimeters":
    kmmm = str(km_mm(value))
    new_kmmm = kmmm[0:20]
    print("There are " + new_kmmm + " millimeters in " + value + " kilometers!")
if first == "kilometers" and second == "miles":
    kmmi = str(km_miles(value))
    new_kmmi = kmmi[0:8]
    print("There are " + new_kmmi + " miles in " + value + " kilometers!")
