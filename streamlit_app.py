import streamlit as st

# ==========================================
# SAFETY DATABASE - HIGH RISK CHEMICALS
# ==========================================

safety_database = {
    "ammonia": {
        "name": "AMMONIA",
        "formula": "NH₃",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Toxic if inhaled — causes lung damage, respiratory failure",
            "Flammable gas — explosion risk (15-28% in air)",
            "Corrosive to skin and eyes — causes severe burns",
            "Reacts violently with acids, chlorine, bleach"
        ],
        "emergency": [
            "Evacuate area immediately (100m radius)",
            "Call emergency services (1122 / 911 / plant emergency)",
            "Use water spray to disperse gas",
            "Isolate leak source if safe to do so",
            "Wear full PPE before entering area"
        ],
        "ppe": [
            "Full face respirator with ammonia cartridge",
            "Chemical resistant gloves (butyl rubber)",
            "Safety goggles (airtight)",
            "Full body chemical protective suit",
            "Rubber boots"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air, give oxygen if available",
            "Skin contact: Wash with water for 15 minutes",
            "Eye contact: Rinse with water for 20 minutes",
            "Ingestion: Do not induce vomiting, drink milk/water"
        ],
        "firefighting": [
            "Use CO₂, dry chemical, or water spray",
            "Do NOT use direct water jet",
            "Cool surrounding containers with water"
        ],
        "storage": [
            "Cool, well-ventilated area",
            "Separate from acids, chlorine, oxidizers",
            "Ground containers",
            "Use corrosion-resistant containers",
            "Install gas detectors"
        ],
        "disposal": [
            "Neutralize with acid (controlled conditions)",
            "Absorb with inert material",
            "Dispose as hazardous waste"
        ]
    },
    "chlorine": {
        "name": "CHLORINE",
        "formula": "Cl₂",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Highly toxic gas — can cause death in minutes",
            "Respiratory failure — burns lungs and throat",
            "Corrosive to skin and eyes — chemical burns",
            "Reacts violently with ammonia, hydrogen, acetylene",
            "Heavier than air — settles in low areas"
        ],
        "emergency": [
            "Evacuate immediately (200m radius minimum)",
            "Call emergency services immediately",
            "Move upwind — do NOT go into affected area",
            "Use water spray to knock down gas",
            "Only trained personnel with SCBA should respond"
        ],
        "ppe": [
            "Self-contained breathing apparatus (SCBA) — MANDATORY",
            "Full chemical protective suit",
            "Butyl rubber gloves",
            "Chemical goggles",
            "Full face shield"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air IMMEDIATELY",
            "Give oxygen if breathing difficulty",
            "Skin: Wash with water for 15-20 minutes",
            "Eyes: Rinse for 20-30 minutes",
            "Get medical attention IMMEDIATELY"
        ],
        "firefighting": [
            "Chlorine itself is non-flammable but supports combustion",
            "Use water spray to cool containers",
            "Evacuate area immediately"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from ammonia, hydrogen, flammable gases",
            "Store in corrosion-resistant containers",
            "Install chlorine gas detectors",
            "Emergency scrubber system recommended"
        ],
        "disposal": [
            "Absorb with soda ash or lime",
            "Neutralize before disposal",
            "Dispose as hazardous waste"
        ]
    },
    "hydrogen": {
        "name": "HYDROGEN",
        "formula": "H₂",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Extremely flammable — wide flammability range (4-75%)",
            "Explosion risk — forms explosive mixtures with air",
            "Odorless and colorless — difficult to detect",
            "Lighter than air — accumulates at ceiling",
            "Can cause asphyxiation in confined spaces"
        ],
        "emergency": [
            "Eliminate all ignition sources immediately",
            "Evacuate area (minimum 100m)",
            "Stop leak if safe to do so",
            "Use explosion-proof equipment",
            "Ventilate area to disperse gas"
        ],
        "ppe": [
            "Flame-resistant clothing",
            "Safety goggles",
            "Hard hat",
            "Static-dissipating footwear",
            "SCBA for large leaks"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air",
            "If not breathing, give CPR",
            "Get medical attention immediately"
        ],
        "firefighting": [
            "Use water spray from safe distance",
            "Do NOT use CO₂ or dry chemical — ineffective",
            "Let fire burn if safe — do not extinguish unless leak stopped",
            "Cool surrounding containers"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from oxidizers, halogens",
            "Ground all equipment",
            "No smoking or open flames",
            "Use explosion-proof electrical equipment"
        ],
        "disposal": [
            "Vent to safe location or flare",
            "Controlled burning"
        ]
    },
    "hydrogen sulfide": {
        "name": "HYDROGEN SULFIDE",
        "formula": "H₂S",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Highly toxic — fatal in minutes at high concentrations",
            "Colorless gas with rotten egg smell (at low levels)",
            "Heavier than air — settles in low areas",
            "Flammable and explosive",
            "Odor disappears at high concentrations — silent killer"
        ],
        "emergency": [
            "Evacuate immediately — DO NOT enter without SCBA",
            "Call emergency services",
            "Move upwind",
            "Use SCBA only — respirators NOT effective",
            "Ventilate area if safe"
        ],
        "ppe": [
            "SCBA (Self-contained breathing apparatus) — MANDATORY",
            "Full chemical protective suit",
            "H₂S gas detector (personal alarm)",
            "Chemical resistant gloves",
            "Safety goggles"
        ],
        "first_aid": [
            "Move to fresh air IMMEDIATELY",
            "If not breathing, start CPR",
            "Administer oxygen if available",
            "Get medical help IMMEDIATELY",
            "Antidote: Amyl nitrite (under medical supervision)"
        ],
        "firefighting": [
            "Use CO₂, dry chemical, or water spray",
            "Do NOT enter area without SCBA",
            "Evacuate area immediately"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Store away from oxidizers",
            "Install H₂S detectors with alarms",
            "Emergency ventilation system required"
        ],
        "disposal": [
            "Flare to safe location",
            "Scrub with caustic solution"
        ]
    },
    "benzene": {
        "name": "BENZENE",
        "formula": "C₆H₆",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Known human carcinogen — causes leukemia",
            "Highly flammable liquid and vapor",
            "Toxic by inhalation, ingestion, skin absorption",
            "Vapors heavier than air — can travel to ignition source",
            "Colorless liquid with sweet odor"
        ],
        "emergency": [
            "Eliminate all ignition sources",
            "Evacuate area (100m radius)",
            "Use explosion-proof equipment",
            "Contain spill with inert absorbent material",
            "Ventilate area"
        ],
        "ppe": [
            "Chemical resistant gloves (Viton, butyl)",
            "Chemical safety goggles",
            "Full face shield",
            "Protective clothing (Tyvek)",
            "Organic vapor respirator (air-purifying)",
            "SCBA for high concentrations"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air",
            "Skin: Wash with soap and water for 15 minutes",
            "Eyes: Rinse with water for 15-20 minutes",
            "Ingestion: Do not induce vomiting",
            "Get medical attention immediately"
        ],
        "firefighting": [
            "Use alcohol-resistant foam, CO₂, dry chemical",
            "Water spray may be ineffective",
            "Cool surrounding containers"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from oxidizers",
            "Ground containers",
            "Store in approved containers",
            "No smoking or open flames"
        ],
        "disposal": [
            "Incinerate in approved facility",
            "Dispose as hazardous waste"
        ]
    },
    "carbon monoxide": {
        "name": "CARBON MONOXIDE",
        "formula": "CO",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Silent killer — odorless, colorless, tasteless",
            "Highly toxic — binds to hemoglobin 200x stronger than O₂",
            "Flammable gas (12-75% in air)",
            "Explosion risk",
            "Slightly lighter than air"
        ],
        "emergency": [
            "Evacuate area immediately",
            "Ventilate area",
            "Stop leak if safe",
            "Use SCBA for entry",
            "Call emergency services"
        ],
        "ppe": [
            "SCBA — MANDATORY for entry",
            "CO detector with alarm",
            "Flame-resistant clothing"
        ],
        "first_aid": [
            "Move to fresh air IMMEDIATELY",
            "Administer 100% oxygen",
            "If not breathing, start CPR",
            "Hyperbaric oxygen therapy for severe cases",
            "Get medical help IMMEDIATELY"
        ],
        "firefighting": [
            "Use CO₂, dry chemical, or water spray",
            "Stop gas flow first if possible"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from oxidizers",
            "Install CO detectors",
            "No smoking or open flames"
        ],
        "disposal": [
            "Vent to safe location or flare"
        ]
    },
    "sulfuric acid": {
        "name": "SULFURIC ACID",
        "formula": "H₂SO₄",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Highly corrosive — causes severe burns",
            "Reacts violently with water (generates heat)",
            "Toxic fumes when heated (SO₃, SO₂)",
            "Colorless to dark brown liquid",
            "Causes delayed tissue damage"
        ],
        "emergency": [
            "Evacuate area",
            "Contain spill with inert absorbent",
            "Do NOT add water — can cause splattering",
            "Neutralize with soda ash or lime",
            "Use acid-resistant equipment"
        ],
        "ppe": [
            "Acid-resistant gloves (neoprene, butyl)",
            "Chemical splash goggles",
            "Full face shield",
            "Acid-resistant apron and suit",
            "Rubber boots"
        ],
        "first_aid": [
            "Skin: Flush with water for 15-20 minutes",
            "Eyes: Rinse with water for 20-30 minutes",
            "Inhalation: Move to fresh air",
            "Ingestion: Do not induce vomiting, drink milk/water",
            "Do NOT use neutralizing agents on skin"
        ],
        "firefighting": [
            "Non-flammable but produces toxic fumes",
            "Use water spray to cool containers",
            "Wear full PPE and SCBA"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from bases, flammables, oxidizers",
            "Store in corrosion-resistant containers",
            "Secondary containment required"
        ],
        "disposal": [
            "Neutralize with lime or soda ash",
            "Dispose as hazardous waste"
        ]
    },
    "nitric acid": {
        "name": "NITRIC ACID",
        "formula": "HNO₃",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Highly corrosive — causes severe burns",
            "Strong oxidizer — can ignite combustibles",
            "Toxic fumes (NOx, nitrogen dioxide) — brown cloud",
            "Reacts violently with many materials",
            "Colorless to yellow fuming liquid"
        ],
        "emergency": [
            "Evacuate area",
            "Contain spill with inert absorbent",
            "Do NOT add water — can cause splattering",
            "Neutralize with soda ash or lime",
            "Use acid-resistant equipment"
        ],
        "ppe": [
            "Acid-resistant gloves",
            "Chemical splash goggles",
            "Full face shield",
            "Acid-resistant suit",
            "SCBA for fumes"
        ],
        "first_aid": [
            "Skin: Flush with water for 15-20 minutes",
            "Eyes: Rinse with water for 20-30 minutes",
            "Inhalation: Move to fresh air, give oxygen",
            "Get medical attention IMMEDIATELY"
        ],
        "firefighting": [
            "Non-flammable but oxidizer — use water spray",
            "Keep combustibles away",
            "Wear full PPE and SCBA"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from organics, combustibles, bases",
            "Store in corrosion-resistant containers",
            "Secondary containment required"
        ],
        "disposal": [
            "Neutralize with lime or soda ash",
            "Dispose as hazardous waste"
        ]
    },
    "phosgene": {
        "name": "PHOSGENE",
        "formula": "COCl₂",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Highly toxic — fatal within minutes",
            "Colorless gas — smells like freshly cut hay",
            "Delayed effects — symptoms appear hours later",
            "Used as chemical weapon in WWI",
            "Reacts violently with water, alcohols, ammonia"
        ],
        "emergency": [
            "Evacuate immediately — minimum 300m radius",
            "Call emergency services",
            "SCBA MANDATORY — do NOT enter without",
            "Move upwind",
            "Do NOT use water on leak"
        ],
        "ppe": [
            "SCBA (Self-contained breathing apparatus) — MANDATORY",
            "Full chemical protective suit",
            "Butyl rubber gloves",
            "Chemical goggles",
            "Fully encapsulated suit recommended"
        ],
        "first_aid": [
            "Move to fresh air IMMEDIATELY",
            "Administer oxygen",
            "Keep victim warm and quiet",
            "Get medical help IMMEDIATELY",
            "No specific antidote"
        ],
        "firefighting": [
            "Non-flammable but produces toxic fumes",
            "Use water spray from safe distance",
            "Do NOT enter area without SCBA"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from water, bases, alcohols",
            "Store in pressure vessels",
            "Install phosgene detectors",
            "Emergency scrubber system required"
        ],
        "disposal": [
            "Scrub with caustic solution",
            "Incinerate in approved facility"
        ]
    },
    "vinyl chloride": {
        "name": "VINYL CHLORIDE",
        "formula": "C₂H₃Cl",
        "risk": "HIGH",
        "risk_icon": "🔴",
        "hazards": [
            "Known human carcinogen — causes angiosarcoma of liver",
            "Extremely flammable gas",
            "Colorless gas with sweet odor",
            "Heavier than air — can travel to ignition source",
            "Explosion risk"
        ],
        "emergency": [
            "Eliminate all ignition sources",
            "Evacuate area (100m radius)",
            "Stop leak if safe",
            "Use explosion-proof equipment",
            "Ventilate area"
        ],
        "ppe": [
            "SCBA",
            "Chemical resistant gloves (Viton, butyl)",
            "Safety goggles",
            "Flame-resistant clothing",
            "Protective suit"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air",
            "If not breathing, give CPR",
            "Skin: Wash with soap and water",
            "Eyes: Rinse with water for 15 minutes",
            "Get medical attention"
        ],
        "firefighting": [
            "Use CO₂, dry chemical, or water spray",
            "Do NOT use direct water jet",
            "Cool surrounding containers"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from oxidizers",
            "Ground containers",
            "Store in pressure vessels",
            "Install gas detectors"
        ],
        "disposal": [
            "Incinerate in approved facility",
            "Flare to safe location"
        ]
    },
        "methanol": {
        "name": "METHANOL",
        "formula": "CH₃OH",
        "risk": "MEDIUM-HIGH",
        "risk_icon": "🟠",
        "hazards": [
            "Highly flammable liquid and vapor",
            "Toxic if swallowed, inhaled, or absorbed through skin",
            "Causes blindness or death if ingested",
            "May cause central nervous system depression"
        ],
        "emergency": [
            "Eliminate all ignition sources",
            "Evacuate area",
            "Use explosion-proof equipment",
            "Contain spill with inert absorbent",
            "Ventilate area"
        ],
        "ppe": [
            "Chemical resistant gloves (nitrile)",
            "Safety goggles",
            "Face shield",
            "Protective clothing",
            "Organic vapor respirator"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air",
            "Ingestion: Do not induce vomiting — get immediate medical help",
            "Skin: Wash with soap and water",
            "Eyes: Rinse with water for 15 minutes"
        ],
        "firefighting": [
            "Use alcohol-resistant foam, CO₂, dry chemical",
            "Water spray may be ineffective",
            "Cool surrounding containers"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from oxidizers, acids",
            "Ground containers",
            "No smoking or open flames"
        ],
        "disposal": [
            "Incinerate in approved facility",
            "Dispose as hazardous waste"
        ]
    },
    "toluene": {
        "name": "TOLUENE",
        "formula": "C₇H₈",
        "risk": "MEDIUM-HIGH",
        "risk_icon": "🟠",
        "hazards": [
            "Highly flammable liquid and vapor",
            "May cause nervous system damage",
            "Harmful if inhaled or swallowed",
            "Vapors heavier than air"
        ],
        "emergency": [
            "Eliminate all ignition sources",
            "Evacuate area",
            "Use explosion-proof equipment",
            "Contain spill with inert absorbent"
        ],
        "ppe": [
            "Chemical resistant gloves",
            "Safety goggles",
            "Organic vapor respirator",
            "Protective clothing"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air",
            "Skin: Wash with soap and water",
            "Eyes: Rinse with water",
            "Ingestion: Do not induce vomiting"
        ],
        "firefighting": [
            "Use alcohol-resistant foam, CO₂, dry chemical",
            "Water spray may be ineffective"
        ],
        "storage": [
            "Cool, dry, well-ventilated area",
            "Separate from oxidizers",
            "Ground containers"
        ],
        "disposal": [
            "Incinerate in approved facility"
        ]
    },
        
    "nitrogen": {
        "name": "NITROGEN",
        "formula": "N₂",
        "risk": "MEDIUM",
        "risk_icon": "🟡",
        "hazards": [
            "Simple asphyxiant — displaces oxygen in confined spaces",
            "Colorless, odorless, tasteless gas",
            "Can cause rapid suffocation without warning",
            "Extremely cold liquid form causes cryogenic burns"
        ],
        "emergency": [
            "Evacuate area if oxygen levels drop",
            "Ventilate area immediately",
            "Use SCBA in confined spaces",
            "Do NOT enter without oxygen monitoring"
        ],
        "ppe": [
            "Oxygen monitor required",
            "SCBA for confined space entry",
            "Cryogenic gloves for liquid nitrogen",
            "Face shield for liquid nitrogen",
            "Safety goggles"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air immediately",
            "If not breathing, give artificial respiration",
            "Administer oxygen if available",
            "Get medical attention immediately"
        ],
        "firefighting": [
            "Non-flammable gas",
            "Use water spray to cool containers",
            "Evacuate area"
        ],
        "storage": [
            "Well-ventilated area",
            "Store away from confined spaces",
            "Secure cylinders upright",
            "Use oxygen monitors in storage areas",
            "For liquid: use cryogenic containers"
        ],
        "disposal": [
            "Vent to safe outdoor location",
            "Allow to evaporate in well-ventilated area"
        ]
    },
    "carbon dioxide": {
        "name": "CARBON DIOXIDE",
        "formula": "CO₂",
        "risk": "MEDIUM",
        "risk_icon": "🟡",
        "hazards": [
            "Asphyxiant — can cause suffocation in high concentrations",
            "Heavier than air — accumulates in low areas",
            "Colorless, odorless gas",
            "Solid form (dry ice) causes severe cold burns"
        ],
        "emergency": [
            "Evacuate area immediately",
            "Ventilate area",
            "Use SCBA for confined space entry",
            "Monitor oxygen levels"
        ],
        "ppe": [
            "Oxygen monitor",
            "SCBA for high concentrations",
            "Cryogenic gloves for dry ice",
            "Safety goggles"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air",
            "If not breathing, give artificial respiration",
            "Administer oxygen",
            "Get medical attention"
        ],
        "firefighting": [
            "Non-flammable, used as fire suppressant",
            "Use water spray to cool containers"
        ],
        "storage": [
            "Well-ventilated area",
            "Store away from low-lying areas",
            "Secure cylinders upright",
            "Use gas detectors"
        ],
        "disposal": [
            "Vent to safe outdoor location"
        ]
    },
    "argon": {
        "name": "ARGON",
        "formula": "Ar",
        "risk": "MEDIUM",
        "risk_icon": "🟡",
        "hazards": [
            "Simple asphyxiant — displaces oxygen",
            "Heavier than air — settles in low areas",
            "Colorless, odorless gas",
            "No warning properties"
        ],
        "emergency": [
            "Evacuate area",
            "Ventilate immediately",
            "Use SCBA for entry",
            "Monitor oxygen levels"
        ],
        "ppe": [
            "Oxygen monitor",
            "SCBA for confined spaces",
            "Safety goggles"
        ],
        "first_aid": [
            "Move to fresh air",
            "Give oxygen if available",
            "Artificial respiration if needed",
            "Get medical attention"
        ],
        "firefighting": [
            "Non-flammable",
            "Use water spray to cool containers"
        ],
        "storage": [
            "Well-ventilated area",
            "Secure cylinders",
            "Avoid confined spaces"
        ],
        "disposal": [
            "Vent to safe outdoor location"
        ]
    },
    "helium": {
        "name": "HELIUM",
        "formula": "He",
        "risk": "MEDIUM",
        "risk_icon": "🟡",
        "hazards": [
            "Simple asphyxiant — displaces oxygen",
            "Lighter than air — rises to ceiling",
            "Colorless, odorless gas",
            "Liquid form causes cryogenic burns"
        ],
        "emergency": [
            "Evacuate area",
            "Ventilate area",
            "Monitor oxygen levels",
            "Use SCBA for confined spaces"
        ],
        "ppe": [
            "Oxygen monitor",
            "SCBA as needed",
            "Cryogenic gloves for liquid"
        ],
        "first_aid": [
            "Move to fresh air",
            "Administer oxygen",
            "Artificial respiration if needed"
        ],
        "firefighting": [
            "Non-flammable",
            "Use water spray to cool containers"
        ],
        "storage": [
            "Well-ventilated area",
            "Secure cylinders",
            "Store away from high temperatures"
        ],
        "disposal": [
            "Vent to safe outdoor location"
        ]
    },
    "compressed air": {
        "name": "COMPRESSED AIR",
        "formula": "Air (N₂+O₂)",
        "risk": "MEDIUM",
        "risk_icon": "🟡",
        "hazards": [
            "High pressure — can cause injury if released forcefully",
            "Can cause air embolism if injected into skin",
            "Oxygen enriched under pressure",
            "Supports combustion"
        ],
        "emergency": [
            "Evacuate area if high pressure release",
            "Ventilate area",
            "Shut off source if safe",
            "Monitor oxygen levels"
        ],
        "ppe": [
            "Safety glasses",
            "Hearing protection for high pressure release",
            "Gloves"
        ],
        "first_aid": [
            "If injected under skin — seek immediate medical attention",
            "Move to fresh air",
            "Treat for pressure injuries"
        ],
        "firefighting": [
            "Supports combustion — use appropriate extinguisher",
            "Evacuate area",
            "Cool containers with water spray"
        ],
        "storage": [
            "Secure cylinders upright",
            "Store in cool, dry area",
            "Keep away from heat sources",
            "Use safety chains"
        ],
        "disposal": [
            "Release pressure safely outdoors"
        ]
    },
        
    "water steam": {
        "name": "WATER (STEAM)",
        "formula": "H₂O",
        "risk": "LOW",
        "risk_icon": "🟢",
        "hazards": [
            "High temperature steam causes severe burns",
            "High pressure can cause injury",
            "Invisible steam can cause unexpected burns",
            "Can cause scalding"
        ],
        "emergency": [
            "Evacuate area if steam leak",
            "Shut off steam source",
            "Ventilate area",
            "Use water spray to cool"
        ],
        "ppe": [
            "Heat resistant gloves",
            "Face shield",
            "Long sleeves",
            "Safety goggles"
        ],
        "first_aid": [
            "Burns: Cool with water for 15-20 minutes",
            "Remove contaminated clothing",
            "Cover with sterile dressing",
            "Get medical attention for severe burns"
        ],
        "firefighting": [
            "Not applicable — steam is used for firefighting",
            "Cool surrounding area"
        ],
        "storage": [
            "Insulated pipes",
            "Pressure relief valves",
            "Regular maintenance"
        ],
        "disposal": [
            "Condense and drain to sewer"
        ]
    },
    "lubricating oil": {
        "name": "LUBRICATING OIL",
        "formula": "Hydrocarbon mixture",
        "risk": "LOW",
        "risk_icon": "🟢",
        "hazards": [
            "Slippery — causes falls",
            "May cause skin irritation",
            "Combustible if heated",
            "Environmental hazard if spilled"
        ],
        "emergency": [
            "Contain spill with absorbent material",
            "Ventilate area",
            "Eliminate ignition sources"
        ],
        "ppe": [
            "Nitrile gloves",
            "Safety goggles",
            "Oil resistant apron"
        ],
        "first_aid": [
            "Skin: Wash with soap and water",
            "Eyes: Rinse with water",
            "Inhalation: Move to fresh air"
        ],
        "firefighting": [
            "Use CO₂, dry chemical, or foam",
            "Water spray may be ineffective"
        ],
        "storage": [
            "Cool, dry area",
            "Store away from oxidizers",
            "Use spill containment"
        ],
        "disposal": [
            "Recycle used oil",
            "Dispose as hazardous waste"
        ]
    },
    "ethanol": {
        "name": "ETHANOL",
        "formula": "C₂H₅OH",
        "risk": "LOW",
        "risk_icon": "🟢",
        "hazards": [
            "Flammable liquid",
            "May cause eye irritation",
            "Central nervous system depressant if ingested"
        ],
        "emergency": [
            "Eliminate ignition sources",
            "Contain spill with inert absorbent",
            "Ventilate area"
        ],
        "ppe": [
            "Safety glasses",
            "Nitrile gloves",
            "Lab coat"
        ],
        "first_aid": [
            "Inhalation: Move to fresh air",
            "Skin: Wash with soap and water",
            "Eyes: Rinse with water",
            "Ingestion: Get medical attention"
        ],
        "firefighting": [
            "Use alcohol-resistant foam, CO₂, dry chemical",
            "Water spray may be ineffective"
        ],
        "storage": [
            "Cool, well-ventilated area",
            "Keep away from heat",
            "Ground containers"
        ],
        "disposal": [
            "Incinerate or dispose as hazardous waste"
        ]
    },
    "glycerin": {
        "name": "GLYCERIN",
        "formula": "C₃H₈O₃",
        "risk": "LOW",
        "risk_icon": "🟢",
        "hazards": [
            "Low hazard",
            "May cause slight eye irritation",
            "Slippery when spilled"
        ],
        "emergency": [
            "Contain spill with absorbent material",
            "Wipe up with cloth"
        ],
        "ppe": [
            "Safety glasses",
            "Gloves (optional)"
        ],
        "first_aid": [
            "Skin: Wash with soap and water",
            "Eyes: Rinse with water"
        ],
        "firefighting": [
            "Use water spray, CO₂, or dry chemical",
            "Combustible at high temperatures"
        ],
        "storage": [
            "Cool, dry area",
            "Keep containers closed"
        ],
        "disposal": [
            "Dispose according to local regulations"
        ]
    },
    "sodium chloride": {
        "name": "SODIUM CHLORIDE",
        "formula": "NaCl",
        "risk": "LOW",
        "risk_icon": "🟢",
        "hazards": [
            "May cause eye irritation",
            "Large amounts can be harmful if ingested",
            "Non-flammable"
        ],
        "emergency": [
            "Sweep up dry material",
            "Avoid dust generation"
        ],
        "ppe": [
            "Safety glasses",
            "Gloves",
            "Dust mask if handling large amounts"
        ],
        "first_aid": [
            "Eyes: Rinse with water",
            "Ingestion: Drink water",
            "Skin: Wash with soap and water"
        ],
        "firefighting": [
            "Non-flammable — use extinguisher appropriate for surrounding fire"
        ],
        "storage": [
            "Cool, dry area",
            "Keep containers closed"
        ],
        "disposal": [
            "Dispose according to local regulations"
        ]
    }
}
# ==========================================
# INCIDENTS DATABASE - INDUSTRY ACCIDENTS
# ==========================================

incidents_database = {
    "bhopal gas tragedy": {
        "name": "BHOPAL GAS TRAGEDY",
        "year": 1984,
        "location": "Bhopal, India",
        "chemical": "Methyl Isocyanate (MIC)",
        "risk_icon": "🔴",
        "causes": [
            "Water entered MIC storage tank due to poor maintenance",
            "Safety systems were turned off",
            "Emergency alarms and procedures failed",
            "Inadequate training of operators",
            "Poor plant design and maintenance"
        ],
        "consequences": [
            "Over 15,000 immediate deaths",
            "Over 500,000 injuries and long-term illnesses",
            "Thousands of permanent disabilities",
            "Severe environmental contamination",
            "Still affecting population today (birth defects, cancer)"
        ],
        "prevention": [
            "Proper maintenance of safety systems",
            "Never bypass safety interlocks",
            "Regular operator training and drills",
            "Emergency response plans must be tested",
            "Independent safety audits required",
            "Proper storage and handling of hazardous chemicals"
        ],
        "lesson": "Never compromise on safety. One mistake can kill thousands."
    },
    "texas city refinery": {
        "name": "TEXAS CITY REFINERY EXPLOSION",
        "year": 2005,
        "location": "Texas City, USA",
        "chemical": "Hydrocarbon / Gasoline",
        "risk_icon": "🔴",
        "causes": [
            "Distillation column overfilled during startup",
            "Blowdown drum and stack were overwhelmed",
            "Operator error and inadequate training",
            "No proper safety culture",
            "Outdated equipment"
        ],
        "consequences": [
            "15 workers killed",
            "180 workers injured",
            "Plant severely damaged",
            "$1.5 billion in fines and settlements",
            "Corporate criminal charges filed"
        ],
        "prevention": [
            "Proper level control and alarms",
            "Adequate relief system design",
            "Operator training and certification",
            "Management of change procedures",
            "Process safety management systems",
            "Regular safety audits"
        ],
        "lesson": "Safety systems must be properly designed AND maintained."
    },
    "deepwater horizon": {
        "name": "DEEPWATER HORIZON OIL SPILL",
        "year": 2010,
        "location": "Gulf of Mexico, USA",
        "chemical": "Crude Oil / Methane",
        "risk_icon": "🔴",
        "causes": [
            "Blowout preventer (BOP) failed",
            "Cement barrier was insufficient",
            "Pressure tests misinterpreted",
            "Cost-cutting decisions compromised safety",
            "Inadequate risk assessment"
        ],
        "consequences": [
            "11 workers killed",
            "17 workers injured",
            "4.9 million barrels of oil spilled",
            "Massive environmental damage",
            "$65 billion in penalties and cleanup costs",
            "BP found guilty of gross negligence"
        ],
        "prevention": [
            "Proper cementing and well integrity",
            "Redundant safety systems",
            "Independent well control checks",
            "Stop work authority for all employees",
            "Regular blowout preventer testing",
            "Do not ignore warning signs"
        ],
        "lesson": "Cost-cutting should never compromise safety."
    },
    "beirut explosion": {
        "name": "BEIRUT PORT EXPLOSION",
        "year": 2020,
        "location": "Beirut, Lebanon",
        "chemical": "Ammonium Nitrate",
        "risk_icon": "🔴",
        "causes": [
            "2,750 tons of ammonium nitrate stored improperly for 6 years",
            "No safety precautions or inspections",
            "Welding work ignited nearby fireworks",
            "Fire spread to ammonium nitrate storage",
            "Complete negligence by authorities"
        ],
        "consequences": [
            "Over 200 deaths",
            "Over 6,500 injuries",
            "300,000 people homeless",
            "Port completely destroyed",
            "$15 billion in damages",
            "Political fallout and investigations"
        ],
        "prevention": [
            "Proper storage of hazardous materials",
            "Regular inspections and audits",
            "Safe distance from populated areas",
            "Emergency response plans",
            "No hot work near hazardous materials",
            "Inventory management of dangerous goods"
        ],
        "lesson": "Never store hazardous materials improperly. Regular inspections save lives."
    },
    "pasadena explosion": {
        "name": "PASADENA REFINERY EXPLOSION",
        "year": 1989,
        "location": "Pasadena, Texas, USA",
        "chemical": "Ethylene / Isobutane",
        "risk_icon": "🔴",
        "causes": [
            "Gas release during maintenance",
            "Inadequate purging of equipment",
            "Hot work (welding) near flammable gas",
            "Poor communication between crews",
            "Inadequate safety procedures"
        ],
        "consequences": [
            "23 workers killed",
            "314 workers injured",
            "$1.2 billion in damages and fines",
            "Plant shut down for years"
        ],
        "prevention": [
            "Proper lock-out/tag-out procedures",
            "Gas testing before hot work",
            "Effective permit system",
            "Communication between shifts",
            "Hot work training and supervision"
        ],
        "lesson": "Never assume an area is safe — test and verify."
    },
    "flixborough disaster": {
        "name": "FLIXBOROUGH DISASTER",
        "year": 1974,
        "location": "Flixborough, UK",
        "chemical": "Cyclohexane",
        "risk_icon": "🔴",
        "causes": [
            "Temporary pipe (bypass) failed catastrophically",
            "Poor engineering design of temporary modification",
            "Inadequate hazard analysis of change",
            "Large flammable vapor cloud formed"
        ],
        "consequences": [
            "28 workers killed",
            "36 workers injured",
            "Plant completely destroyed",
            "Extensive off-site damage",
            "Changed process safety regulations worldwide"
        ],
        "prevention": [
            "Management of Change (MOC) procedures",
            "Proper engineering design of modifications",
            "Hazard and Operability (HAZOP) studies",
            "Independent review of major changes",
            "Proper inspection of temporary equipment"
        ],
        "lesson": "Management of Change is critical. Temporary solutions can be deadly."
    },
    "seveso disaster": {
        "name": "SEVESO DISASTER",
        "year": 1976,
        "location": "Seveso, Italy",
        "chemical": "Dioxin (TCDD)",
        "risk_icon": "🔴",
        "causes": [
            "Reactor safety valve opened due to runaway reaction",
            "Containment system had been removed",
            "No emergency plan for chemical release",
            "Poor process design"
        ],
        "consequences": [
            "No immediate deaths, but thousands exposed",
            "High rates of cancer and birth defects",
            "Large area contaminated",
            "Over 3,000 animals died",
            "Residents permanently displaced",
            "Led to SEVESO Directive (EU safety regulations)"
        ],
        "prevention": [
            "Proper reactor temperature control",
            "Emergency containment systems must be in place",
            "Emergency response plans required",
            "Community notification systems",
            "Regular hazard analysis"
        ],
        "lesson": "Chemical disasters don't always kill immediately — they can harm for generations."
    }
}
unit_categories = {
    # ========== GROUP 1: BASIC ENGINEERING ==========
    "🌡️ Temperature": {
        "units": ["°C", "°F", "K", "°R"],
        "to_si": {
            "°C": lambda x: x + 273.15,
            "°F": lambda x: (x - 32) * 5/9 + 273.15,
            "K": lambda x: x,
            "°R": lambda x: x * 5/9
        }
    },
    "📊 Pressure": {
        "units": ["Pa", "kPa", "MPa", "GPa", "bar", "mbar", "atm", "psi", "kg/cm²", "torr", "mmHg", "cmHg", "inHg", "mmH₂O", "cmH₂O", "ftH₂O"],
        "to_si": {
            "Pa": 1, "kPa": 1000, "MPa": 1e6, "GPa": 1e9, "bar": 1e5, "mbar": 100,
            "atm": 101325, "psi": 6894.76, "kg/cm²": 98066.5, "torr": 133.322,
            "mmHg": 133.322, "cmHg": 1333.22, "inHg": 3386.39, "mmH₂O": 9.80665,
            "cmH₂O": 98.0665, "ftH₂O": 2989.07
        }
    },
    "📏 Length": {
        "units": ["m", "cm", "mm", "µm", "nm", "km", "in", "ft", "yd", "mile", "nmi", "mil", "thou", "ly", "AU", "pc", "fm", "pm"],
        "to_si": {
            "m": 1, "cm": 0.01, "mm": 0.001, "µm": 1e-6, "nm": 1e-9, "km": 1000,
            "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mile": 1609.34, "nmi": 1852,
            "mil": 2.54e-5, "thou": 2.54e-5, "ly": 9.461e15, "AU": 1.496e11,
            "pc": 3.086e16, "fm": 1e-15, "pm": 1e-12
        }
    },
    "📐 Area": {
        "units": ["m²", "cm²", "mm²", "km²", "ft²", "in²", "yd²", "mi²", "acre", "ha", "a", "b"],
        "to_si": {
            "m²": 1, "cm²": 0.0001, "mm²": 1e-6, "km²": 1e6, "ft²": 0.092903,
            "in²": 0.00064516, "yd²": 0.836127, "mi²": 2.59e6, "acre": 4046.86,
            "ha": 10000, "a": 100, "b": 1e-28
        }
    },
    "📦 Volume": {
        "units": ["m³", "cm³", "mm³", "km³", "ft³", "in³", "yd³", "L", "mL", "µL", "cL", "dL", "hL", "gal (US)", "gal (UK)", "bbl"],
        "to_si": {
            "m³": 1, "cm³": 1e-6, "mm³": 1e-9, "km³": 1e9, "ft³": 0.0283168,
            "in³": 1.6387e-5, "yd³": 0.764555, "L": 0.001, "mL": 1e-6, "µL": 1e-9,
            "cL": 1e-5, "dL": 0.0001, "hL": 0.1, "gal (US)": 0.00378541,
            "gal (UK)": 0.00454609, "bbl": 0.158987
        }
    },
    "⚖️ Mass": {
        "units": ["kg", "g", "mg", "µg", "ng", "t", "lb", "oz", "ton (US)", "ton (UK)", "gr", "st", "ct", "amu"],
        "to_si": {
            "kg": 1, "g": 0.001, "mg": 1e-6, "µg": 1e-9, "ng": 1e-12, "t": 1000,
            "lb": 0.453592, "oz": 0.0283495, "ton (US)": 907.185, "ton (UK)": 1016.05,
            "gr": 6.4799e-5, "st": 6.35029, "ct": 0.0002, "amu": 1.6605e-27
        }
    },
    "⏱️ Time": {
        "units": ["s", "ms", "µs", "ns", "min", "h", "d", "wk", "mo", "yr"],
        "to_si": {
            "s": 1, "ms": 0.001, "µs": 1e-6, "ns": 1e-9, "min": 60, "h": 3600,
            "d": 86400, "wk": 604800, "mo": 2.628e6, "yr": 3.1536e7
        }
    },
    "🔋 Energy": {
        "units": ["J", "kJ", "MJ", "GJ", "cal", "kcal", "Wh", "kWh", "MWh", "BTU", "thm", "eV"],
        "to_si": {
            "J": 1, "kJ": 1000, "MJ": 1e6, "GJ": 1e9, "cal": 4.184, "kcal": 4184,
            "Wh": 3600, "kWh": 3.6e6, "MWh": 3.6e9, "BTU": 1055.06, "thm": 1.05506e8,
            "eV": 1.602e-19
        }
    },
    
    # ========== GROUP 2: MATERIAL PROPERTIES ==========
    "🧪 Density": {
        "units": ["kg/m³", "g/cm³", "lb/ft³", "g/mL", "kg/L"],
        "to_si": {
            "kg/m³": 1, "g/cm³": 1000, "lb/ft³": 16.0185, "g/mL": 1000, "kg/L": 1000
        }
    },
    "🌊 Dynamic Viscosity": {
        "units": ["Pa·s", "cP", "kg/m·s", "lb/ft·s"],
        "to_si": {
            "Pa·s": 1, "cP": 0.001, "kg/m·s": 1, "lb/ft·s": 1.48816
        }
    },
    "🌊 Kinematic Viscosity": {
        "units": ["m²/s", "cSt", "St", "ft²/s"],
        "to_si": {
            "m²/s": 1, "cSt": 1e-6, "St": 0.0001, "ft²/s": 0.092903
        }
    },
    "🔥 Thermal Conductivity": {
        "units": ["W/m·K", "W/m·°C", "BTU/hr·ft·°F", "cal/cm·s·°C"],
        "to_si": {
            "W/m·K": 1, "W/m·°C": 1, "BTU/hr·ft·°F": 1.73073, "cal/cm·s·°C": 418.4
        }
    },
    "🧊 Specific Heat Capacity": {
        "units": ["J/kg·K", "kJ/kg·K", "cal/g·°C", "BTU/lb·°F"],
        "to_si": {
            "J/kg·K": 1, "kJ/kg·K": 1000, "cal/g·°C": 4184, "BTU/lb·°F": 4186.8
        }
    },
    "📈 Heat Transfer Coefficient": {
        "units": ["W/m²·K", "W/m²·°C", "BTU/hr·ft²·°F"],
        "to_si": {
            "W/m²·K": 1, "W/m²·°C": 1, "BTU/hr·ft²·°F": 5.67826
        }
    },
    
    # ========== GROUP 3: CONCENTRATION & FLOW ==========
    "🧴 Molar Concentration": {
        "units": ["mol/m³", "mol/L", "mol/mL", "kmol/m³"],
        "to_si": {
            "mol/m³": 1, "mol/L": 1000, "mol/mL": 1e6, "kmol/m³": 1000
        }
    },
    "🧪 Mass Concentration": {
        "units": ["kg/m³", "g/L", "mg/L", "ppm"],
        "to_si": {
            "kg/m³": 1, "g/L": 1, "mg/L": 0.001, "ppm": 0.001
        }
    },
    "💧 Volumetric Flow Rate": {
        "units": ["m³/s", "L/s", "m³/h", "L/min", "gal/min", "ft³/s"],
        "to_si": {
            "m³/s": 1, "L/s": 0.001, "m³/h": 0.000277778, "L/min": 1.66667e-5,
            "gal/min": 6.309e-5, "ft³/s": 0.0283168
        }
    },
    "⚡ Mass Flow Rate": {
        "units": ["kg/s", "kg/h", "g/s", "lb/s", "lb/h"],
        "to_si": {
            "kg/s": 1, "kg/h": 0.000277778, "g/s": 0.001, "lb/s": 0.453592, "lb/h": 0.000125998
        }
    },
    
    # ========== GROUP 4: MECHANICS & POWER ==========
    "⚙️ Force": {
        "units": ["N", "kN", "lbf", "kgf", "dyn"],
        "to_si": {
            "N": 1, "kN": 1000, "lbf": 4.44822, "kgf": 9.80665, "dyn": 1e-5
        }
    },
    "🔧 Torque": {
        "units": ["N·m", "kgf·m", "lbf·ft", "lbf·in"],
        "to_si": {
            "N·m": 1, "kgf·m": 9.80665, "lbf·ft": 1.35582, "lbf·in": 0.112985
        }
    },
    "⚡ Power": {
        "units": ["W", "kW", "MW", "hp", "BTU/hr"],
        "to_si": {
            "W": 1, "kW": 1000, "MW": 1e6, "hp": 745.7, "BTU/hr": 0.293071
        }
    },
    "📐 Angle": {
        "units": ["deg", "rad", "grad", "arcmin", "arcsec"],
        "to_si": {
            "deg": 0.0174533, "rad": 1, "grad": 0.015708, "arcmin": 0.000290888, "arcsec": 4.84814e-6
        }
    },
    
    # ========== GROUP 5: OTHERS ==========
    "📈 Frequency": {
        "units": ["Hz", "kHz", "MHz", "GHz", "rpm"],
        "to_si": {
            "Hz": 1, "kHz": 1000, "MHz": 1e6, "GHz": 1e9, "rpm": 0.0166667
        }
    },
    "💾 Data Size": {
        "units": ["B", "KB", "MB", "GB", "TB", "PB"],
        "to_si": {
            "B": 1, "KB": 1024, "MB": 1048576, "GB": 1.07374e9, "TB": 1.09951e12, "PB": 1.1259e15
        }
    },
    "💡 Luminous Intensity": {
        "units": ["cd"],
        "to_si": {"cd": 1}
    },
    "🧪 pH": {
        "units": ["pH"],
        "to_si": {"pH": 1}
    },
    "🌫️ Humidity": {
        "units": ["g/kg", "%RH", "ppm"],
        "to_si": {
            "g/kg": 1, "%RH": 1, "ppm": 0.001
        }
    },
    "☢️ Radioactivity": {
        "units": ["Bq", "Ci", "mCi", "µCi"],
        "to_si": {
            "Bq": 1, "Ci": 3.7e10, "mCi": 3.7e7, "µCi": 37000
        }
    },
    "⚡ Dose": {
        "units": ["Gy", "rad", "Sv", "rem"],
        "to_si": {
            "Gy": 1, "rad": 0.01, "Sv": 1, "rem": 0.01
        }
    },
    "🔊 Sound Pressure": {
        "units": ["Pa", "dB", "µPa"],
        "to_si": {
            "Pa": 1, "dB": 20e-6, "µPa": 1e-6
        }
    },
    "🔊 Sound Intensity": {
        "units": ["W/m²", "dB"],
        "to_si": {
            "W/m²": 1, "dB": 1e-12
        }
    },
    "🧪 Catalytic Activity": {
        "units": ["kat", "mol/s"],
        "to_si": {
            "kat": 1, "mol/s": 1
        }
    }
}
# Add from_si conversion factors for non-temperature categories
for category in unit_categories:
    if category != "🌡️ Temperature":
        unit_categories[category]["from_si"] = {}
        for unit, factor in unit_categories[category]["to_si"].items():
            unit_categories[category]["from_si"][unit] = 1 / factor

def convert_unit(value, from_unit, to_unit, category):
    """Convert value from one unit to another within same category"""
    if category == "🌡️ Temperature":
        # Temperature special handling (functions, not factors)
        si_value = unit_categories[category]["to_si"][from_unit](value)
        result = unit_categories[category]["from_si"][to_unit](si_value)
    else:
        # For all other categories (factors)
        si_value = value * unit_categories[category]["to_si"][from_unit]
        result = si_value * unit_categories[category]["from_si"][to_unit]
    return result

# ==========================================
# LANGUAGE DATABASE (50+ Languages)
# ==========================================
languages = {
    "English": {"code": "en", "flag": "🇬🇧"},
    "Urdu": {"code": "ur", "flag": "🇵🇰"},
    "Hindi": {"code": "hi", "flag": "🇮🇳"},
    "Arabic": {"code": "ar", "flag": "🇸🇦"},
    "Spanish": {"code": "es", "flag": "🇪🇸"},
    "French": {"code": "fr", "flag": "🇫🇷"},
    "German": {"code": "de", "flag": "🇩🇪"},
    "Chinese": {"code": "zh", "flag": "🇨🇳"},
    "Japanese": {"code": "ja", "flag": "🇯🇵"},
    "Korean": {"code": "ko", "flag": "🇰🇷"},
    "Russian": {"code": "ru", "flag": "🇷🇺"},
    "Turkish": {"code": "tr", "flag": "🇹🇷"},
}

# ==========================================
# TRANSLATIONS
# ==========================================
translations = {
    "en": {
        "app_title": "🧪 ChemEngBot",
        "language": "🌐 LANGUAGE",
        "select_feature": "📌 SELECT FEATURE",
        "home": "🏠 HOME",
        "reynolds": "📊 REYNOLDS NUMBER",
        "heat_transfer": "🔥 HEAT TRANSFER",
        "pressure_drop": "📉 PRESSURE DROP",
        "ntu": "📐 NTU METHOD",
       # "temp_conv": "🌡️ TEMPERATURE CONVERTER",
        "formulas": "📚 FORMULAS",
        "concepts": "💡 CONCEPTS",
        "welcome_title": "🧪 Chemical Engineering Assistant Bot",
        "welcome_subtitle": "Your AI-Powered Companion for Chemical Engineering Calculations",
        "quick_ref": "📈 Quick Reference Formulas",
        "reynolds_header": "📊 Reynolds Number Calculator",
        "reynolds_formula": "**Formula:** Re = ρvd/μ",
        "reynolds_info": "💡 Reynolds Number: **Laminar** (<2000), **Transitional** (2000-4000), **Turbulent** (>4000)",
        "density": "📊 Density ρ (kg/m³):",
        "velocity": "💨 Velocity v (m/s):",
        "diameter": "📏 Diameter d (m):",
        "viscosity": "💧 Viscosity μ (Pa·s):",
        "calculate_reynolds": "🔬 Calculate Reynolds Number",
        "laminar": "🟢 **Flow Type:** Laminar Flow",
        "transitional": "🟡 **Flow Type:** Transitional Flow",
        "turbulent": "🔴 **Flow Type:** Turbulent Flow",
        "error_viscosity": "❌ Viscosity must be greater than 0!",
        "heat_header": "🔥 Heat Transfer Calculator",
        "heat_formula": "**Formula:** Q = U × A × ΔT",
        "heat_info": "💡 Heat transfer rate in **Watts (W)** or **kilowatts (kW)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Area A (m²):",
        "delta_t": "🌡️ ΔT (K or °C):",
        "calculate_heat": "🔥 Calculate Heat Transfer",
        "pressure_header": "📉 Pressure Drop Calculator",
        "pressure_formula": "**Formula:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Friction factor f",
        "length": "Length L (m)",
        "calc_pressure": "Calculate ΔP",
        "temp_header": "🌡️ Temperature Converter",
        "temp_info": "💡 Enter value → Get all 4 scales",
        "input_unit": "Input Unit:",
        "temp_value": "Temperature Value:",
        "convert_temp": "🔄 Convert Temperature",
        "converted_values": "✅ Converted Values:",
        "formulas_header": "📚 Chemical Engineering Formulas",
        "formulas_info": "Select subject → View formulas",
        "choose_subject": "Choose Subject:",
        "concepts_header": "💡 Concepts",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Chemical Engineering | UET LAHORE",
        "footer_credit": "🚀 ChemEngBot — Your Chemical Engineering Assistant",
        "footer_copyright": "© 2024 All Rights Reserved",
    },
    "ur": {
        "app_title": "🧪 کیم انج بوٹ",
        "language": "🌐 زبان",
        "select_feature": "📌 فیچر منتخب کریں",
        "home": "🏠 ہوم",
        "reynolds": "📊 رینالڈز نمبر",
        "heat_transfer": "🔥 حرارت کی منتقلی",
        "pressure_drop": "📉 پریشر ڈراپ",
        "ntu": "📐 این ٹی یو طریقہ",
        "temp_conv": "🌡️ درجہ حرارت کنورٹر",
        "formulas": "📚 فارمولے",
        "concepts": "💡 تصورات",
        "welcome_title": "🧪 کیمیکل انجینئرنگ اسسٹنٹ بوٹ",
        "welcome_subtitle": "کیمیکل انجینئرنگ حسابات کے لیے آپ کا AI ساتھی",
        "quick_ref": "📈 فوری حوالہ فارمولے",
        "reynolds_header": "📊 رینالڈز نمبر کیلکولیٹر",
        "reynolds_formula": "**فارمولا:** Re = ρvd/μ",
        "reynolds_info": "💡 رینالڈز نمبر بہاؤ کی قسم: **لیمینر** (<2000), **ٹربولنٹ** (>4000)",
        "density": "📊 کثافت ρ (kg/m³):",
        "velocity": "💨 رفتار v (m/s):",
        "diameter": "📏 قطر d (m):",
        "viscosity": "💧 وسکاسیٹی μ (Pa·s):",
        "calculate_reynolds": "🔬 رینالڈز نمبر حساب کریں",
        "laminar": "🟢 **بہاؤ:** لیمنر بہاؤ",
        "transitional": "🟡 **بہاؤ:** ٹرانزیشنل بہاؤ",
        "turbulent": "🔴 **بہاؤ:** ٹربولنٹ بہاؤ",
        "error_viscosity": "❌ وسکاسیٹی صفر سے زیادہ ہونی چاہیے!",
        "heat_header": "🔥 حرارت کی منتقلی کیلکولیٹر",
        "heat_formula": "**فارمولا:** Q = U × A × ΔT",
        "heat_info": "💡 حرارت کی منتقلی **واٹ (W)** میں",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 رقبہ A (m²):",
        "delta_t": "🌡️ ΔT (K یا °C):",
        "calculate_heat": "🔥 حرارت کی منتقلی حساب کریں",
        "pressure_header": "📉 پریشر ڈراپ کیلکولیٹر",
        "pressure_formula": "**فارمولا:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "رگڑ عنصر f",
        "length": "لمبائی L (m)",
        "calc_pressure": "ΔP حساب کریں",
        "temp_header": "🌡️ درجہ حرارت کنورٹر",
        "temp_info": "💡 کوئی بھی یونٹ ڈالیں → تمام 4 پیمانے",
        "input_unit": "انپٹ یونٹ:",
        "temp_value": "درجہ حرارت:",
        "convert_temp": "🔄 تبدیل کریں",
        "converted_values": "✅ تبدیل شدہ قیمتیں:",
        "formulas_header": "📚 کیمیکل انجینئرنگ فارمولے",
        "formulas_info": "مضمون منتخب کریں → فارمولے دیکھیں",
        "choose_subject": "مضمون منتخب کریں:",
        "concepts_header": "💡 تصورات",
        "footer_name": "👨‍🔧 زینیر شہزاد",
        "footer_university": "🎓 کیمیکل انجینئرنگ | یو ای ٹی لاہور",
        "footer_credit": "🚀 کیم انج بوٹ — آپ کا کیمیکل انجینئرنگ اسسٹنٹ",
        "footer_copyright": "© 2024 جملہ حقوق محفوظ ہیں",
    },
    "hi": {
        "app_title": "🧪 केम इंज बॉट",
        "language": "🌐 भाषा",
        "select_feature": "📌 सुविधा चुनें",
        "home": "🏠 होम",
        "reynolds": "📊 रेनॉल्ड्स संख्या",
        "heat_transfer": "🔥 ऊष्मा स्थानांतरण",
        "pressure_drop": "📉 दबाव में गिरावट",
        "ntu": "📐 एनटीयू विधि",
        "temp_conv": "🌡️ तापमान परिवर्तक",
        "formulas": "📚 सूत्र",
        "concepts": "💡 अवधारणाएँ",
        "welcome_title": "🧪 रासायनिक इंजीनियरिंग सहायक बॉट",
        "welcome_subtitle": "रासायनिक इंजीनियरिंग गणनाओं के लिए आपका AI साथी",
        "quick_ref": "📈 त्वरित संदर्भ सूत्र",
        "reynolds_header": "📊 रेनॉल्ड्स संख्या कैलकुलेटर",
        "reynolds_formula": "**सूत्र:** Re = ρvd/μ",
        "reynolds_info": "💡 रेनॉल्ड्स संख्या: **लामिनार** (<2000), **अशांत** (>4000)",
        "density": "📊 घनत्व ρ (kg/m³):",
        "velocity": "💨 वेग v (m/s):",
        "diameter": "📏 व्यास d (m):",
        "viscosity": "💧 श्यानता μ (Pa·s):",
        "calculate_reynolds": "🔬 रेनॉल्ड्स संख्या की गणना करें",
        "laminar": "🟢 **प्रवाह:** लामिनार प्रवाह",
        "transitional": "🟡 **प्रवाह:** ट्रांज़िशनल प्रवाह",
        "turbulent": "🔴 **प्रवाह:** अशांत प्रवाह",
        "error_viscosity": "❌ श्यानता शून्य से अधिक होनी चाहिए!",
        "heat_header": "🔥 ऊष्मा स्थानांतरण कैलकुलेटर",
        "heat_formula": "**सूत्र:** Q = U × A × ΔT",
        "heat_info": "💡 ऊष्मा स्थानांतरण **वाट (W)** में",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 क्षेत्रफल A (m²):",
        "delta_t": "🌡️ ΔT (K या °C):",
        "calculate_heat": "🔥 ऊष्मा स्थानांतरण की गणना करें",
        "pressure_header": "📉 दबाव ड्रॉप कैलकुलेटर",
        "pressure_formula": "**सूत्र:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "घर्षण कारक f",
        "length": "लंबाई L (m)",
        "calc_pressure": "ΔP की गणना करें",
        "temp_header": "🌡️ तापमान परिवर्तक",
        "temp_info": "💡 कोई भी इकाई डालें → सभी 4 पैमाने",
        "input_unit": "इनपुट इकाई:",
        "temp_value": "तापमान मान:",
        "convert_temp": "🔄 तापमान बदलें",
        "converted_values": "✅ परिवर्तित मान:",
        "formulas_header": "📚 रासायनिक इंजीनियरिंग सूत्र",
        "formulas_info": "विषय चुनें → सूत्र देखें",
        "choose_subject": "विषय चुनें:",
        "concepts_header": "💡 अवधारणाएँ",
        "footer_name": "👨‍🔧 ज़ुनैर शहज़ाद",
        "footer_university": "🎓 रासायनिक इंजीनियरिंग | यूईटी लाहौर",
        "footer_credit": "🚀 केम इंज बॉट — आपका रासायनिक इंजीनियरिंग सहायक",
        "footer_copyright": "© 2024 सर्वाधिकार सुरक्षित",
    },
        
    "ar": {
        "app_title": "🧪 كيم إنج بوت",
        "language": "🌐 اللغة",
        "select_feature": "📌 اختر الميزة",
        "home": "🏠 الرئيسية",
        "reynolds": "📊 رقم رينولدز",
        "heat_transfer": "🔥 انتقال الحرارة",
        "pressure_drop": "📉 انخفاض الضغط",
        "ntu": "📐 طريقة NTU",
        "temp_conv": "🌡️ محول درجة الحرارة",
        "formulas": "📚 الصيغ",
        "concepts": "💡 المفاهيم",
        "welcome_title": "🧪 مساعد الهندسة الكيميائية",
        "welcome_subtitle": "رفيقك المدعوم بالذكاء الاصطناعي لحسابات الهندسة الكيميائية",
        "quick_ref": "📈 صيغ مرجعية سريعة",
        "reynolds_header": "📊 حاسبة رقم رينولدز",
        "reynolds_formula": "**الصيغة:** Re = ρvd/μ",
        "reynolds_info": "💡 رقم رينولدز يحدد نوع التدفق",
        "density": "📊 الكثافة ρ (kg/m³):",
        "velocity": "💨 السرعة v (m/s):",
        "diameter": "📏 القطر d (m):",
        "viscosity": "💧 اللزوجة μ (Pa·s):",
        "calculate_reynolds": "🔬 احسب رقم رينولدز",
        "laminar": "🟢 **نوع التدفق:** تدفق طبقي",
        "transitional": "🟡 **نوع التدفق:** تدفق انتقالي",
        "turbulent": "🔴 **نوع التدفق:** تدفق مضطرب",
        "error_viscosity": "❌ يجب أن تكون اللزوجة أكبر من 0!",
        "heat_header": "🔥 حاسبة انتقال الحرارة",
        "heat_formula": "**الصيغة:** Q = U × A × ΔT",
        "heat_info": "💡 معدل انتقال الحرارة بالواط (W)",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 المساحة A (m²):",
        "delta_t": "🌡️ ΔT (K أو °C):",
        "calculate_heat": "🔥 احسب انتقال الحرارة",
        "pressure_header": "📉 حاسبة انخفاض الضغط",
        "pressure_formula": "**الصيغة:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "معامل الاحتكاك f",
        "length": "الطول L (m)",
        "calc_pressure": "احسب ΔP",
        "temp_header": "🌡️ محول درجة الحرارة",
        "temp_info": "💡 أدخل قيمة → احصل على جميع المقاييس الأربعة",
        "input_unit": "وحدة الإدخال:",
        "temp_value": "قيمة درجة الحرارة:",
        "convert_temp": "🔄 حول درجة الحرارة",
        "converted_values": "✅ القيم المحولة:",
        "formulas_header": "📚 صيغ الهندسة الكيميائية",
        "formulas_info": "اختر الموضوع → عرض الصيغ",
        "choose_subject": "اختر الموضوع:",
        "concepts_header": "💡 المفاهيم",
        "footer_name": "👨‍🔧 زنير شهداد",
        "footer_university": "🎓 الهندسة الكيميائية | جامعة لاهور للهندسة",
        "footer_credit": "🚀 كيم إنج بوت — مساعدك في الهندسة الكيميائية",
        "footer_copyright": "© 2024 جميع الحقوق محفوظة",
    },
    "es": {
        "app_title": "🧪 ChemEngBot",
        "language": "🌐 IDIOMA",
        "select_feature": "📌 SELECCIONAR FUNCIÓN",
        "home": "🏠 INICIO",
        "reynolds": "📊 NÚMERO DE REYNOLDS",
        "heat_transfer": "🔥 TRANSFERENCIA DE CALOR",
        "pressure_drop": "📉 CAÍDA DE PRESIÓN",
        "ntu": "📐 MÉTODO NTU",
        "temp_conv": "🌡️ CONVERTIDOR DE TEMPERATURA",
        "formulas": "📚 FÓRMULAS",
        "concepts": "💡 CONCEPTOS",
        "welcome_title": "🧪 Asistente de Ingeniería Química",
        "welcome_subtitle": "Tu compañero impulsado por IA para cálculos de ingeniería química",
        "quick_ref": "📈 Fórmulas de referencia rápida",
        "reynolds_header": "📊 Calculadora del Número de Reynolds",
        "reynolds_formula": "**Fórmula:** Re = ρvd/μ",
        "reynolds_info": "💡 El número de Reynolds determina el tipo de flujo",
        "density": "📊 Densidad ρ (kg/m³):",
        "velocity": "💨 Velocidad v (m/s):",
        "diameter": "📏 Diámetro d (m):",
        "viscosity": "💧 Viscosidad μ (Pa·s):",
        "calculate_reynolds": "🔬 Calcular Número de Reynolds",
        "laminar": "🟢 **Tipo de flujo:** Flujo Laminar",
        "transitional": "🟡 **Tipo de flujo:** Flujo de Transición",
        "turbulent": "🔴 **Tipo de flujo:** Flujo Turbulento",
        "error_viscosity": "❌ ¡La viscosidad debe ser mayor que 0!",
        "heat_header": "🔥 Calculadora de Transferencia de Calor",
        "heat_formula": "**Fórmula:** Q = U × A × ΔT",
        "heat_info": "💡 La tasa de transferencia de calor en **Watts (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Área A (m²):",
        "delta_t": "🌡️ ΔT (K o °C):",
        "calculate_heat": "🔥 Calcular Transferencia de Calor",
        "pressure_header": "📉 Calculadora de Caída de Presión",
        "pressure_formula": "**Fórmula:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Factor de fricción f",
        "length": "Longitud L (m)",
        "calc_pressure": "Calcular ΔP",
        "temp_header": "🌡️ Convertidor de Temperatura",
        "temp_info": "💡 Ingrese un valor → Obtenga las 4 escalas",
        "input_unit": "Unidad de entrada:",
        "temp_value": "Valor de temperatura:",
        "convert_temp": "🔄 Convertir Temperatura",
        "converted_values": "✅ Valores convertidos:",
        "formulas_header": "📚 Fórmulas de Ingeniería Química",
        "formulas_info": "Seleccione tema → Ver fórmulas",
        "choose_subject": "Seleccione tema:",
        "concepts_header": "💡 Conceptos",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Ingeniería Química | UET LAHORE",
        "footer_credit": "🚀 ChemEngBot — Tu Asistente de Ingeniería Química",
        "footer_copyright": "© 2024 Todos los derechos reservados",
    },
    "fr": {
        "app_title": "🧪 ChemEngBot",
        "language": "🌐 LANGUE",
        "select_feature": "📌 SÉLECTIONNER UNE FONCTION",
        "home": "🏠 ACCUEIL",
        "reynolds": "📊 NOMBRE DE REYNOLDS",
        "heat_transfer": "🔥 TRANSFERT DE CHALEUR",
        "pressure_drop": "📉 PERTE DE CHARGE",
        "ntu": "📐 MÉTHODE NTU",
        "temp_conv": "🌡️ CONVERTISSEUR DE TEMPÉRATURE",
        "formulas": "📚 FORMULES",
        "concepts": "💡 CONCEPTS",
        "welcome_title": "🧪 Assistant en Génie Chimique",
        "welcome_subtitle": "Votre compagnon alimenté par l'IA pour les calculs de génie chimique",
        "quick_ref": "📈 Formules de référence rapide",
        "reynolds_header": "📊 Calculateur du Nombre de Reynolds",
        "reynolds_formula": "**Formule:** Re = ρvd/μ",
        "reynolds_info": "💡 Le nombre de Reynolds détermine le type d'écoulement",
        "density": "📊 Densité ρ (kg/m³):",
        "velocity": "💨 Vitesse v (m/s):",
        "diameter": "📏 Diamètre d (m):",
        "viscosity": "💧 Viscosité μ (Pa·s):",
        "calculate_reynolds": "🔬 Calculer le Nombre de Reynolds",
        "laminar": "🟢 **Type d'écoulement:** Écoulement Laminaire",
        "transitional": "🟡 **Type d'écoulement:** Écoulement de Transition",
        "turbulent": "🔴 **Type d'écoulement:** Écoulement Turbulent",
        "error_viscosity": "❌ La viscosité doit être supérieure à 0 !",
        "heat_header": "🔥 Calculateur de Transfert de Chaleur",
        "heat_formula": "**Formule:** Q = U × A × ΔT",
        "heat_info": "💡 Le taux de transfert de chaleur en **Watts (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Surface A (m²):",
        "delta_t": "🌡️ ΔT (K ou °C):",
        "calculate_heat": "🔥 Calculer le Transfert de Chaleur",
        "pressure_header": "📉 Calculateur de Perte de Charge",
        "pressure_formula": "**Formule:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Facteur de frottement f",
        "length": "Longueur L (m)",
        "calc_pressure": "Calculer ΔP",
        "temp_header": "🌡️ Convertisseur de Température",
        "temp_info": "💡 Entrez une valeur → Obtenez les 4 échelles",
        "input_unit": "Unité d'entrée :",
        "temp_value": "Valeur de température :",
        "convert_temp": "🔄 Convertir la Température",
        "converted_values": "✅ Valeurs converties :",
        "formulas_header": "📚 Formules de Génie Chimique",
        "formulas_info": "Sélectionnez un sujet → Voir les formules",
        "choose_subject": "Choisissez un sujet :",
        "concepts_header": "💡 Concepts",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Génie Chimique | UET LAHORE",
        "footer_credit": "🚀 ChemEngBot — Votre Assistant en Génie Chimique",
        "footer_copyright": "© 2024 Tous droits réservés",
    },
        
    "de": {
        "app_title": "🧪 ChemEngBot",
        "language": "🌐 SPRACHE",
        "select_feature": "📌 FUNKTION AUSWÄHLEN",
        "home": "🏠 STARTSEITE",
        "reynolds": "📊 REYNOLDS-ZAHL",
        "heat_transfer": "🔥 WÄRMEÜBERTRAGUNG",
        "pressure_drop": "📉 DRUCKVERLUST",
        "ntu": "📐 NTU-METHODE",
        "temp_conv": "🌡️ TEMPERATURUMRECHNER",
        "formulas": "📚 FORMELN",
        "concepts": "💡 KONZEPTE",
        "welcome_title": "🧪 Chemieingenieurwesen-Assistent",
        "welcome_subtitle": "Ihr KI-gestützter Begleiter für chemietechnische Berechnungen",
        "quick_ref": "📈 Kurzreferenz-Formeln",
        "reynolds_header": "📊 Reynolds-Zahl Rechner",
        "reynolds_formula": "**Formel:** Re = ρvd/μ",
        "reynolds_info": "💡 Reynolds-Zahl bestimmt Strömungsart: **Laminar** (<2000), **Turbulent** (>4000)",
        "density": "📊 Dichte ρ (kg/m³):",
        "velocity": "💨 Geschwindigkeit v (m/s):",
        "diameter": "📏 Durchmesser d (m):",
        "viscosity": "💧 Viskosität μ (Pa·s):",
        "calculate_reynolds": "🔬 Reynolds-Zahl berechnen",
        "laminar": "🟢 **Strömungsart:** Laminare Strömung",
        "transitional": "🟡 **Strömungsart:** Übergangsströmung",
        "turbulent": "🔴 **Strömungsart:** Turbulente Strömung",
        "error_viscosity": "❌ Viskosität muss größer als 0 sein!",
        "heat_header": "🔥 Wärmeübertragungs-Rechner",
        "heat_formula": "**Formel:** Q = U × A × ΔT",
        "heat_info": "💡 Wärmeübertragungsrate in **Watt (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Fläche A (m²):",
        "delta_t": "🌡️ ΔT (K oder °C):",
        "calculate_heat": "🔥 Wärmeübertragung berechnen",
        "pressure_header": "📉 Druckverlust-Rechner",
        "pressure_formula": "**Formel:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Reibungsfaktor f",
        "length": "Länge L (m)",
        "calc_pressure": "ΔP berechnen",
        "temp_header": "🌡️ Temperaturumrechner",
        "temp_info": "💡 Wert eingeben → Alle 4 Skalen erhalten",
        "input_unit": "Eingabeeinheit:",
        "temp_value": "Temperaturwert:",
        "convert_temp": "🔄 Temperatur umrechnen",
        "converted_values": "✅ Umgerechnete Werte:",
        "formulas_header": "📚 Chemieingenieurwesen-Formeln",
        "formulas_info": "Thema auswählen → Formeln anzeigen",
        "choose_subject": "Thema auswählen:",
        "concepts_header": "💡 Konzepte",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Chemieingenieurwesen | UET LAHORE",
        "footer_credit": "🚀 ChemEngBot — Ihr Chemieingenieurwesen-Assistent",
        "footer_copyright": "© 2024 Alle Rechte vorbehalten",
    },
    "zh": {
        "app_title": "🧪 化学工程机器人",
        "language": "🌐 语言",
        "select_feature": "📌 选择功能",
        "home": "🏠 首页",
        "reynolds": "📊 雷诺数",
        "heat_transfer": "🔥 传热",
        "pressure_drop": "📉 压降",
        "ntu": "📐 NTU方法",
        "temp_conv": "🌡️ 温度转换器",
        "formulas": "📚 公式",
        "concepts": "💡 概念",
        "welcome_title": "🧪 化学工程助手机器人",
        "welcome_subtitle": "您的化学工程计算AI助手",
        "quick_ref": "📈 快速参考公式",
        "reynolds_header": "📊 雷诺数计算器",
        "reynolds_formula": "**公式:** Re = ρvd/μ",
        "reynolds_info": "💡 雷诺数确定流动类型: **层流** (<2000), **湍流** (>4000)",
        "density": "📊 密度 ρ (kg/m³):",
        "velocity": "💨 速度 v (m/s):",
        "diameter": "📏 直径 d (m):",
        "viscosity": "💧 粘度 μ (Pa·s):",
        "calculate_reynolds": "🔬 计算雷诺数",
        "laminar": "🟢 **流动类型:** 层流",
        "transitional": "🟡 **流动类型:** 过渡流",
        "turbulent": "🔴 **流动类型:** 湍流",
        "error_viscosity": "❌ 粘度必须大于0！",
        "heat_header": "🔥 传热计算器",
        "heat_formula": "**公式:** Q = U × A × ΔT",
        "heat_info": "💡 传热速率单位为 **瓦特 (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 面积 A (m²):",
        "delta_t": "🌡️ ΔT (K 或 °C):",
        "calculate_heat": "🔥 计算传热",
        "pressure_header": "📉 压降计算器",
        "pressure_formula": "**公式:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "摩擦系数 f",
        "length": "长度 L (m)",
        "calc_pressure": "计算 ΔP",
        "temp_header": "🌡️ 温度转换器",
        "temp_info": "💡 输入值 → 获得所有4种单位",
        "input_unit": "输入单位:",
        "temp_value": "温度值:",
        "convert_temp": "🔄 转换温度",
        "converted_values": "✅ 转换后的值:",
        "formulas_header": "📚 化学工程公式",
        "formulas_info": "选择主题 → 查看公式",
        "choose_subject": "选择主题:",
        "concepts_header": "💡 概念",
        "footer_name": "👨‍🔧 祖奈尔·沙赫扎德",
        "footer_university": "🎓 化学工程 | 拉合尔工程技术大学",
        "footer_credit": "🚀 化学工程机器人 — 您的化学工程助手",
        "footer_copyright": "© 2024 保留所有权利",
    },
    "ja": {
        "app_title": "🧪 化学工学ボット",
        "language": "🌐 言語",
        "select_feature": "📌 機能を選択",
        "home": "🏠 ホーム",
        "reynolds": "📊 レイノルズ数",
        "heat_transfer": "🔥 熱伝達",
        "pressure_drop": "📉 圧力損失",
        "ntu": "📐 NTU法",
        "temp_conv": "🌡️ 温度変換器",
        "formulas": "📚 公式",
        "concepts": "💡 概念",
        "welcome_title": "🧪 化学工学アシスタントボット",
        "welcome_subtitle": "化学工学計算のためのAI搭載コンパニオン",
        "quick_ref": "📈 クイックリファレンス公式",
        "reynolds_header": "📊 レイノルズ数計算機",
        "reynolds_formula": "**公式:** Re = ρvd/μ",
        "reynolds_info": "💡 レイノルズ数は流れの種類を決定: **層流** (<2000), **乱流** (>4000)",
        "density": "📊 密度 ρ (kg/m³):",
        "velocity": "💨 速度 v (m/s):",
        "diameter": "📏 直径 d (m):",
        "viscosity": "💧 粘度 μ (Pa·s):",
        "calculate_reynolds": "🔬 レイノルズ数を計算",
        "laminar": "🟢 **流れの種類:** 層流",
        "transitional": "🟡 **流れの種類:** 遷移流",
        "turbulent": "🔴 **流れの種類:** 乱流",
        "error_viscosity": "❌ 粘度は0より大きくなければなりません！",
        "heat_header": "🔥 熱伝達計算機",
        "heat_formula": "**公式:** Q = U × A × ΔT",
        "heat_info": "💡 熱伝達率の単位は **ワット (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 面積 A (m²):",
        "delta_t": "🌡️ ΔT (K または °C):",
        "calculate_heat": "🔥 熱伝達を計算",
        "pressure_header": "📉 圧力損失計算機",
        "pressure_formula": "**公式:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "摩擦係数 f",
        "length": "長さ L (m)",
        "calc_pressure": "ΔPを計算",
        "temp_header": "🌡️ 温度変換器",
        "temp_info": "💡 値を入力 → すべての4つの単位を取得",
        "input_unit": "入力単位:",
        "temp_value": "温度値:",
        "convert_temp": "🔄 温度を変換",
        "converted_values": "✅ 変換された値:",
        "formulas_header": "📚 化学工学公式",
        "formulas_info": "テーマを選択 → 公式を表示",
        "choose_subject": "テーマを選択:",
        "concepts_header": "💡 概念",
        "footer_name": "👨‍🔧 ズナイア・シャーザド",
        "footer_university": "🎓 化学工学 | UETラホール",
        "footer_credit": "🚀 化学工学ボット — あなたの化学工学アシスタント",
        "footer_copyright": "© 2024 全著作権所有",
    },
    "ko": {
        "app_title": "🧪 화학공학 봇",
        "language": "🌐 언어",
        "select_feature": "📌 기능 선택",
        "home": "🏠 홈",
        "reynolds": "📊 레이놀즈 수",
        "heat_transfer": "🔥 열전달",
        "pressure_drop": "📉 압력 강하",
        "ntu": "📐 NTU 방법",
        "temp_conv": "🌡️ 온도 변환기",
        "formulas": "📚 공식",
        "concepts": "💡 개념",
        "welcome_title": "🧪 화학공학 어시스턴트 봇",
        "welcome_subtitle": "화학공학 계산을 위한 AI 기반 동반자",
        "quick_ref": "📈 빠른 참조 공식",
        "reynolds_header": "📊 레이놀즈 수 계산기",
        "reynolds_formula": "**공식:** Re = ρvd/μ",
        "reynolds_info": "💡 레이놀즈 수는 유동 유형 결정: **층류** (<2000), **난류** (>4000)",
        "density": "📊 밀도 ρ (kg/m³):",
        "velocity": "💨 속도 v (m/s):",
        "diameter": "📏 직경 d (m):",
        "viscosity": "💧 점도 μ (Pa·s):",
        "calculate_reynolds": "🔬 레이놀즈 수 계산",
        "laminar": "🟢 **유동 유형:** 층류",
        "transitional": "🟡 **유동 유형:** 천이 유동",
        "turbulent": "🔴 **유동 유형:** 난류",
        "error_viscosity": "❌ 점도는 0보다 커야 합니다!",
        "heat_header": "🔥 열전달 계산기",
        "heat_formula": "**공식:** Q = U × A × ΔT",
        "heat_info": "💡 열전달률 단위는 **와트 (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 면적 A (m²):",
        "delta_t": "🌡️ ΔT (K 또는 °C):",
        "calculate_heat": "🔥 열전달 계산",
        "pressure_header": "📉 압력 강하 계산기",
        "pressure_formula": "**공식:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "마찰 계수 f",
        "length": "길이 L (m)",
        "calc_pressure": "ΔP 계산",
        "temp_header": "🌡️ 온도 변환기",
        "temp_info": "💡 값 입력 → 모든 4가지 단위 얻기",
        "input_unit": "입력 단위:",
        "temp_value": "온도 값:",
        "convert_temp": "🔄 온도 변환",
        "converted_values": "✅ 변환된 값:",
        "formulas_header": "📚 화학공학 공식",
        "formulas_info": "주제 선택 → 공식 보기",
        "choose_subject": "주제 선택:",
        "concepts_header": "💡 개념",
        "footer_name": "👨‍🔧 주나이르 샤자드",
        "footer_university": "🎓 화학공학 | UET 라호르",
        "footer_credit": "🚀 화학공학 봇 — 당신의 화학공학 어시스턴트",
        "footer_copyright": "© 2024 모든 권리 보유",
    },
    "ru": {
        "app_title": "🧪 ХимИнжБот",
        "language": "🌐 ЯЗЫК",
        "select_feature": "📌 ВЫБРАТЬ ФУНКЦИЮ",
        "home": "🏠 ГЛАВНАЯ",
        "reynolds": "📊 ЧИСЛО РЕЙНОЛЬДСА",
        "heat_transfer": "🔥 ТЕПЛОПЕРЕДАЧА",
        "pressure_drop": "📉 ПЕРЕПАД ДАВЛЕНИЯ",
        "ntu": "📐 МЕТОД NTU",
        "temp_conv": "🌡️ КОНВЕРТЕР ТЕМПЕРАТУРЫ",
        "formulas": "📚 ФОРМУЛЫ",
        "concepts": "💡 КОНЦЕПЦИИ",
        "welcome_title": "🧪 Ассистент по химической технологии",
        "welcome_subtitle": "Ваш ИИ-помощник для расчетов в химической технологии",
        "quick_ref": "📈 Краткие справочные формулы",
        "reynolds_header": "📊 Калькулятор числа Рейнольдса",
        "reynolds_formula": "**Формула:** Re = ρvd/μ",
        "reynolds_info": "💡 Число Рейнольдса определяет тип потока: **ламинарный** (<2000), **турбулентный** (>4000)",
        "density": "📊 Плотность ρ (кг/м³):",
        "velocity": "💨 Скорость v (м/с):",
        "diameter": "📏 Диаметр d (м):",
        "viscosity": "💧 Вязкость μ (Па·с):",
        "calculate_reynolds": "🔬 Вычислить число Рейнольдса",
        "laminar": "🟢 **Тип потока:** Ламинарный поток",
        "transitional": "🟡 **Тип потока:** Переходный поток",
        "turbulent": "🔴 **Тип потока:** Турбулентный поток",
        "error_viscosity": "❌ Вязкость должна быть больше 0!",
        "heat_header": "🔥 Калькулятор теплопередачи",
        "heat_formula": "**Формула:** Q = U × A × ΔT",
        "heat_info": "💡 Скорость теплопередачи в **Ваттах (Вт)**",
        "u_value": "🔧 U (Вт/м²·К):",
        "area": "📐 Площадь A (м²):",
        "delta_t": "🌡️ ΔT (К или °C):",
        "calculate_heat": "🔥 Вычислить теплопередачу",
        "pressure_header": "📉 Калькулятор перепада давления",
        "pressure_formula": "**Формула:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Коэффициент трения f",
        "length": "Длина L (м)",
        "calc_pressure": "Вычислить ΔP",
        "temp_header": "🌡️ Конвертер температуры",
        "temp_info": "💡 Введите значение → Получите все 4 шкалы",
        "input_unit": "Единица ввода:",
        "temp_value": "Значение температуры:",
        "convert_temp": "🔄 Конвертировать температуру",
        "converted_values": "✅ Преобразованные значения:",
        "formulas_header": "📚 Формулы химической технологии",
        "formulas_info": "Выберите тему → Просмотр формул",
        "choose_subject": "Выберите тему:",
        "concepts_header": "💡 Концепции",
        "footer_name": "👨‍🔧 ЗУНАИР ШАХЗАД",
        "footer_university": "🎓 Химическая технология | УЕТ ЛАХОР",
        "footer_credit": "🚀 ХимИнжБот — Ваш помощник по химической технологии",
        "footer_copyright": "© 2024 Все права защищены",
    },
    "tr": {
        "app_title": "🧪 Kimya Müh Botu",
        "language": "🌐 DİL",
        "select_feature": "📌 ÖZELLİK SEÇ",
        "home": "🏠 ANA SAYFA",
        "reynolds": "📊 REYNOLDS SAYISI",
        "heat_transfer": "🔥 ISI TRANSFERİ",
        "pressure_drop": "📉 BASINÇ DÜŞÜŞÜ",
        "ntu": "📐 NTU YÖNTEMİ",
        "temp_conv": "🌡️ SICAKLIK DÖNÜŞTÜRÜCÜ",
        "formulas": "📚 FORMÜLLER",
        "concepts": "💡 KAVRAMLAR",
        "welcome_title": "🧪 Kimya Mühendisliği Asistan Botu",
        "welcome_subtitle": "Kimya mühendisliği hesaplamaları için yapay zeka destekli arkadaşınız",
        "quick_ref": "📈 Hızlı Referans Formülleri",
        "reynolds_header": "📊 Reynolds Sayısı Hesaplayıcı",
        "reynolds_formula": "**Formül:** Re = ρvd/μ",
        "reynolds_info": "💡 Reynolds Sayısı akış türünü belirler: **Laminer** (<2000), **Türbülanslı** (>4000)",
        "density": "📊 Yoğunluk ρ (kg/m³):",
        "velocity": "💨 Hız v (m/s):",
        "diameter": "📏 Çap d (m):",
        "viscosity": "💧 Viskozite μ (Pa·s):",
        "calculate_reynolds": "🔬 Reynolds Sayısını Hesapla",
        "laminar": "🟢 **Akış Türü:** Laminer Akış",
        "transitional": "🟡 **Akış Türü:** Geçiş Akışı",
        "turbulent": "🔴 **Akış Türü:** Türbülanslı Akış",
        "error_viscosity": "❌ Viskozite 0'dan büyük olmalıdır!",
        "heat_header": "🔥 Isı Transferi Hesaplayıcı",
        "heat_formula": "**Formül:** Q = U × A × ΔT",
        "heat_info": "💡 Isı transfer hızı **Watt (W)** cinsindendir",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Alan A (m²):",
        "delta_t": "🌡️ ΔT (K veya °C):",
        "calculate_heat": "🔥 Isı Transferini Hesapla",
        "pressure_header": "📉 Basınç Düşüşü Hesaplayıcı",
        "pressure_formula": "**Formül:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Sürtünme faktörü f",
        "length": "Uzunluk L (m)",
        "calc_pressure": "ΔP Hesapla",
        "temp_header": "🌡️ Sıcaklık Dönüştürücü",
        "temp_info": "💡 Değer girin → 4 ölçeğin tümünü alın",
        "input_unit": "Giriş Birimi:",
        "temp_value": "Sıcaklık Değeri:",
        "convert_temp": "🔄 Sıcaklığı Dönüştür",
        "converted_values": "✅ Dönüştürülen Değerler:",
        "formulas_header": "📚 Kimya Mühendisliği Formülleri",
        "formulas_info": "Konu seçin → Formülleri görüntüleyin",
        "choose_subject": "Konu Seçin:",
        "concepts_header": "💡 Kavramlar",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Kimya Mühendisliği | UET LAHORE",
        "footer_credit": "🚀 Kimya Müh Botu — Kimya Mühendisliği Asistanınız",
        "footer_copyright": "© 2024 Tüm Hakları Saklıdır",
    }
}

# ==========================================
# GET TRANSLATION FUNCTION
# ==========================================
def _(key):
    lang = st.session_state.get("language", "en")
    return translations.get(lang, translations["en"]).get(key, key)

# ==========================================
# INITIALIZE
# ==========================================
if "language" not in st.session_state:
    st.session_state.language = "en"

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title=_("app_title"),
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a3c6e 0%, #0e2a4f 100%);
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 2px solid #4CAF50;
        background: linear-gradient(135deg, #1a3c6e 0%, #0e2a4f 100%);
        border-radius: 10px;
    }
    .footer-name {
        font-size: 1.8rem !important;
        font-weight: bold !important;
        color: #4CAF50 !important;
    }
    .footer-university {
        font-size: 1.2rem !important;
        color: #ccc !important;
    }
    .footer-credit {
        font-size: 1rem !important;
        color: #aaa !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================
# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://img.icons8.com/color/96/chemical-plant.png", width=70)
        st.markdown("# 🧪 ChemEngBot")
    with col2:
        # Load image
        import base64
        from PIL import Image
        import io
        
        # Open image
        img = Image.open("images/zunair.jpeg")
        
        # Convert to base64
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        # Display circle image
        st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="data:image/jpeg;base64,{img_str}" style="width: 110px; height: 110px; border-radius: 50%; object-fit: cover; border: 4px solid #4CAF50; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ========== LANGUAGE SELECTOR ==========
    st.markdown(f"### {_('language')}")
    
    current_lang = st.session_state.get("language", "en")
    lang_options = [f"{info['flag']} {name}" for name, info in languages.items()]
    
    # Find current display
    current_display = "🇬🇧 English"
    for lang_name, info in languages.items():
        if info["code"] == current_lang:
            current_display = f"{info['flag']} {lang_name}"
            break
    
    selected_lang = st.selectbox("", lang_options, index=lang_options.index(current_display) if current_display in lang_options else 0, label_visibility="collapsed")
    
    for lang_name, info in languages.items():
        if f"{info['flag']} {lang_name}" == selected_lang:
            st.session_state.language = info["code"]
    
    st.markdown("---")
    
    # ========== NAVIGATION ==========
    feature = st.radio(
        _("select_feature"),
        [_("home"), _("reynolds"), _("heat_transfer"), _("pressure_drop"), _("ntu"), _("🔄 UNIT CONVERTER" ), _("⚠️ SAFETY ANALYZER"), _("formulas"), _("concepts")],
        index=0
    )
    
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center;">
        <p style="font-size: 1.5rem; font-weight: bold; color: #4CAF50;">👨‍🔧 ZUNAIR SHAHZAD</p>
        <p style="font-size: 1rem; color: #ccc;">🎓 Chemical Engineering</p>
        <p style="font-size: 1.1rem; color: #4CAF50; font-weight: bold;">UET LAHORE</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MAIN CONTENT (Simplified)
# ==========================================

if feature == _("home"):
    st.markdown(f'<p class="main-header">{_("welcome_title")}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">{_("welcome_subtitle")}</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        ### 👋 Welcome to ChemEngBot!
        
        Your personal **Chemical Engineering Assistant** that helps you with:
        
        | ✅ | Feature | Description |
        |---|---|---|
        | 📊 | **Reynolds Number** | Calculate flow characteristics |
        | 🔥 | **Heat Transfer** | Q = UAΔT |
        | 📉 | **Pressure Drop** | Pressure losses in pipes |
        | 📐 | **NTU Method** | Heat exchanger effectiveness |
        
        **Select any feature from the sidebar!**
        """)
    with col2:
        st.image("https://img.icons8.com/color/200/chemical-plant.png")
    
    st.markdown("---")
    st.subheader(_("quick_ref"))
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Reynolds Number", "Re = ρvd/μ")
    c2.metric("Heat Transfer", "Q = UAΔT")
    c3.metric("Pressure Drop", "ΔP = f(L/D)(ρv²/2)")
    c4.metric("NTU", "NTU = UA/C_min")

elif feature == _("reynolds"):
    st.header(_("reynolds_header"))
    st.markdown(_("reynolds_formula"))
    st.info(_("reynolds_info"))
    
    c1, c2 = st.columns(2)
    with c1:
        rho = st.number_input(_("density"), value=1000.0, step=10.0)
        v = st.number_input(_("velocity"), value=1.0, step=0.1)
    with c2:
        d = st.number_input(_("diameter"), value=0.05, step=0.01)
        mu = st.number_input(_("viscosity"), value=0.001, step=0.0001, format="%.4f")
    
    if st.button(_("calculate_reynolds"), type="primary"):
        if mu > 0:
            Re = (rho * v * d) / mu
            st.success(f"### ✅ Reynolds Number = {Re:,.2f}")
            if Re < 2000:
                st.info(_("laminar"))
            elif Re < 4000:
                st.warning(_("transitional"))
            else:
                st.error(_("turbulent"))
        else:
            st.error(_("error_viscosity"))

elif feature == _("heat_transfer"):
    st.header(_("heat_header"))
    st.markdown(_("heat_formula"))
    st.info(_("heat_info"))
    
    c1, c2 = st.columns(2)
    with c1:
        U = st.number_input(_("u_value"), value=500.0)
        A = st.number_input(_("area"), value=10.0)
    with c2:
        dT = st.number_input(_("delta_t"), value=50.0)
    
    if st.button(_("calculate_heat"), type="primary"):
        Q = U * A * dT
        st.success(f"### ✅ Q = {Q:,.2f} W")
        st.info(f"#### = {Q/1000:.2f} kW")

elif feature == _("pressure_drop"):
    st.header(_("pressure_header"))
    st.markdown(_("pressure_formula"))
    
    c1, c2 = st.columns(2)
    with c1:
        f = st.number_input(_("friction"), value=0.02)
        L = st.number_input(_("length"), value=100.0)
    with c2:
        d = st.number_input("Diameter d (m)", value=0.1)
        rho = st.number_input("Density ρ", value=1000.0)
        v = st.number_input("Velocity v (m/s)", value=2.0)
    
    if st.button(_("calc_pressure")):
        dp = f * (L / d) * (rho * v**2 / 2)
        st.success(f"### ✅ ΔP = {dp:.0f} Pa")



elif feature == _("ntu"):
    st.header(_("ntu"))
    st.markdown("**NTU = UA/C_min**")
    U = st.number_input("U", value=500.0)
    A = st.number_input("A", value=10.0)
    Cmin = st.number_input("C_min", value=1000.0)
    if st.button("Calculate NTU"):
        st.success(f"NTU = {(U*A)/Cmin:.2f}")

elif feature == _("formulas"):
    st.header(_("formulas_header"))
    st.info(_("formulas_info"))
    try:
        from formulas_data import formulas_data
        subject = st.selectbox(_("choose_subject"), list(formulas_data.keys()))
        if subject:
            for f in formulas_data[subject]:
                with st.expander(f"📐 {f['name']}"):
                    st.markdown(f"**Desc:** {f['desc']}")
                    st.markdown(f"**Params:** {f['params']}")
                    st.markdown(f"**Eq:** `{f['eq']}`")
    except:
        st.warning("Formulas data not found")

elif feature == _("concepts"):
    st.header(_("concepts_header"))
    st.markdown("""
    - **Reynolds Number**: Flow type (Laminar/Turbulent)
    - **Heat Transfer**: Q = UAΔT
    - **Pressure Drop**: Energy loss in pipes
    - **NTU**: Heat exchanger performance
    """)
# ==========================================
# SAFETY ANALYZER FEATURE
# ==========================================


# ==========================================
# SAFETY ANALYZER FEATURE (NEW VERSION)
# ==========================================

elif feature == "⚠️ SAFETY ANALYZER":
    st.header("⚠️ Chemical Safety Data Sheet (SDS) Analyzer")
    st.markdown("Select risk level, then choose chemical to get complete safety information.")
    
    st.markdown("---")
    
    # ========== STEP 1: RISK LEVEL SELECTION ==========
    st.subheader("📊 Step 1: Select Risk Level")
    
    risk_levels = {
        "🔴 HIGH RISK": ["Ammonia", "Chlorine", "Hydrogen", "Hydrogen Sulfide", "Benzene", "Carbon Monoxide", "Sulfuric Acid", "Nitric Acid", "Phosgene", "Vinyl Chloride"],
        "🟠 MEDIUM-HIGH RISK": ["Methanol", "Toluene", "Acetone", "Ethylene Oxide", "Propane", "Butane", "Gasoline", "Diesel", "Caustic Soda", "Hydrochloric Acid"],
        "🟡 MEDIUM RISK": ["Nitrogen", "Carbon Dioxide", "Argon", "Helium", "Compressed Air"],
        "🟢 LOW RISK": ["Water (Steam)", "Lubricating Oil", "Ethanol", "Glycerin", "Sodium Chloride"]
    }
    
    # Risk level buttons
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🔴 HIGH RISK", use_container_width=True, type="primary"):
            st.session_state.selected_risk = "🔴 HIGH RISK"
    with col2:
        if st.button("🟠 MEDIUM-HIGH", use_container_width=True):
            st.session_state.selected_risk = "🟠 MEDIUM-HIGH RISK"
    with col3:
        if st.button("🟡 MEDIUM RISK", use_container_width=True):
            st.session_state.selected_risk = "🟡 MEDIUM RISK"
    with col4:
        if st.button("🟢 LOW RISK", use_container_width=True):
            st.session_state.selected_risk = "🟢 LOW RISK"
    
    st.markdown("---")
    
    # ========== STEP 2: CHEMICAL SELECTION ==========
    if "selected_risk" in st.session_state:
        selected_risk = st.session_state.selected_risk
        
        # Show selected risk level
        if selected_risk == "🔴 HIGH RISK":
            st.success("✅ Selected: 🔴 HIGH RISK Chemicals")
            chemicals = risk_levels["🔴 HIGH RISK"]
        elif selected_risk == "🟠 MEDIUM-HIGH RISK":
            st.info("✅ Selected: 🟠 MEDIUM-HIGH RISK Chemicals")
            chemicals = risk_levels["🟠 MEDIUM-HIGH RISK"]
        elif selected_risk == "🟡 MEDIUM RISK":
            st.warning("✅ Selected: 🟡 MEDIUM RISK Chemicals")
            chemicals = risk_levels["🟡 MEDIUM RISK"]
        else:
            st.info("✅ Selected: 🟢 LOW RISK Chemicals")
            chemicals = risk_levels["🟢 LOW RISK"]
        
        st.subheader("🔍 Step 2: Select or Search Chemical")
        
        # Search box
        search_term = st.text_input("Search chemical:", placeholder="Type chemical name...")
        
        # Filter chemicals based on search
        if search_term:
            filtered_chemicals = [c for c in chemicals if search_term.lower() in c.lower()]
        else:
            filtered_chemicals = chemicals
        
        # Display chemicals in grid
        st.markdown("**Available Chemicals:**")
        cols = st.columns(3)
        for i, chem in enumerate(filtered_chemicals):
            with cols[i % 3]:
                if st.button(f"🧪 {chem}", key=f"chem_{chem}"):
                    st.session_state.selected_chemical = chem
        
        st.markdown("---")
        
        # ========== STEP 3: SAFETY DATA DISPLAY ==========
        if "selected_chemical" in st.session_state:
            chemical_name = st.session_state.selected_chemical
            
            # Get chemical data from database
            chemical_data = None
            for key, data in safety_database.items():
                if data["name"].lower() == chemical_name.lower():
                    chemical_data = data
                    break
            
            if chemical_data:
                # Risk color banner
                risk_color = "#dc2626" if chemical_data["risk"] == "HIGH" else "#ea580c"
                
                st.markdown(f"""
                <div style="background-color: {risk_color}; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
                    <h2 style="color: white; margin: 0;">🧪 {chemical_data['name']} ({chemical_data['formula']})</h2>
                    <p style="color: white; margin: 5px 0 0 0;">Risk Level: {chemical_data['risk_icon']} {chemical_data['risk']}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Hazards - Red header
                st.markdown("""
                <div style="background-color: #dc2626; padding: 8px 12px; border-radius: 8px; margin-bottom: 10px;">
                    <h3 style="color: white; margin: 0;">⚠️ HAZARDS</h3>
                </div>
                """, unsafe_allow_html=True)
                for hazard in chemical_data["hazards"]:
                    st.markdown(f"• {hazard}")
                st.markdown("---")
                
                # Emergency Response - Orange header
                st.markdown("""
                <div style="background-color: #ea580c; padding: 8px 12px; border-radius: 8px; margin-bottom: 10px;">
                    <h3 style="color: white; margin: 0;">🚨 EMERGENCY RESPONSE</h3>
                </div>
                """, unsafe_allow_html=True)
                for step in chemical_data["emergency"]:
                    st.markdown(f"• {step}")
                st.markdown("---")
                
                # PPE Required - Blue header
                st.markdown("""
                <div style="background-color: #2563eb; padding: 8px 12px; border-radius: 8px; margin-bottom: 10px;">
                    <h3 style="color: white; margin: 0;">👷 PPE REQUIRED</h3>
                </div>
                """, unsafe_allow_html=True)
                for item in chemical_data["ppe"]:
                    st.markdown(f"• {item}")
                st.markdown("---")
                
                # First Aid - Green header
                st.markdown("""
                <div style="background-color: #16a34a; padding: 8px 12px; border-radius: 8px; margin-bottom: 10px;">
                    <h3 style="color: white; margin: 0;">🩺 FIRST AID</h3>
                </div>
                """, unsafe_allow_html=True)
                for aid in chemical_data["first_aid"]:
                    st.markdown(f"• {aid}")
                st.markdown("---")
                
                # Firefighting - Purple header
                st.markdown("""
                <div style="background-color: #9333ea; padding: 8px 12px; border-radius: 8px; margin-bottom: 10px;">
                    <h3 style="color: white; margin: 0;">🔥 FIREFIGHTING MEASURES</h3>
                </div>
                """, unsafe_allow_html=True)
                for fire in chemical_data["firefighting"]:
                    st.markdown(f"• {fire}")
                st.markdown("---")
                
                # Storage - Cyan header
                st.markdown("""
                <div style="background-color: #0891b2; padding: 8px 12px; border-radius: 8px; margin-bottom: 10px;">
                    <h3 style="color: white; margin: 0;">📦 STORAGE REQUIREMENTS</h3>
                </div>
                """, unsafe_allow_html=True)
                for store in chemical_data["storage"]:
                    st.markdown(f"• {store}")
                st.markdown("---")
                
                # Disposal - Gray header
                st.markdown("""
                <div style="background-color: #4b5563; padding: 8px 12px; border-radius: 8px; margin-bottom: 10px;">
                    <h3 style="color: white; margin: 0;">🗑️ DISPOSAL</h3>
                </div>
                """, unsafe_allow_html=True)
                for dispose in chemical_data["disposal"]:
                    st.markdown(f"• {dispose}")
                
                st.caption("⚠️ This information is for educational purposes. Always follow your facility's safety protocols.")
                
            else:
                st.warning(f"Detailed data for {chemical_name} coming soon. Currently showing basic information.")
                st.info(f"**{chemical_name}** is a {selected_risk} chemical. Handle with appropriate PPE and follow safety protocols.")
    
    else:
        st.info("👆 **Welcome to Safety Analyzer!**\n\nClick on any risk level button above to get started.\n\n- 🔴 HIGH RISK: Most dangerous chemicals\n- 🟠 MEDIUM-HIGH: Significant hazards\n- 🟡 MEDIUM RISK: Moderate hazards\n- 🟢 LOW RISK: Minimal hazards")           

    st.markdown("---")
# ==========================================
# UNIT CONVERTER FEATURE
# ==========================================

elif feature == "🔄 UNIT CONVERTER":
    st.header("🔄 Engineering Unit Converter")
    st.markdown("Select category, then property, then convert units")
    
    st.markdown("---")
    
    # ========== STEP 1: CATEGORY SELECTION ==========
    st.subheader("📂 Step 1: Select Category")
    
    categories = {
        "🔧 Group 1: Basic Engineering": {
            "icon": "🔧",
            "properties": ["🌡️ Temperature", "📊 Pressure", "📏 Length", "📐 Area", "📦 Volume", "⚖️ Mass", "⏱️ Time", "🔋 Energy"]
        },
        "🧪 Group 2: Material Properties": {
            "icon": "🧪",
            "properties": ["🧪 Density", "🌊 Dynamic Viscosity", "🌊 Kinematic Viscosity", "🔥 Thermal Conductivity", "🧊 Specific Heat Capacity", "📈 Heat Transfer Coefficient"]
        },
        "💧 Group 3: Concentration & Flow": {
            "icon": "💧",
            "properties": ["🧴 Molar Concentration", "🧪 Mass Concentration", "💧 Volumetric Flow Rate", "⚡ Mass Flow Rate"]
        },
        "⚙️ Group 4: Mechanics & Power": {
            "icon": "⚙️",
            "properties": ["⚙️ Force", "🔧 Torque", "⚡ Power", "📐 Angle"]
        },
        "📦 Group 5: Others": {
            "icon": "📦",
            "properties": ["📈 Frequency", "💾 Data Size", "💡 Luminous Intensity", "🧪 pH", "🌫️ Humidity", "☢️ Radioactivity", "⚡ Dose", "🔊 Sound Pressure", "🔊 Sound Intensity", "🧪 Catalytic Activity"]
        }
    }
    
    # Category buttons
    cat_cols = st.columns(3)
    cat_list = list(categories.keys())
    for i, cat_name in enumerate(cat_list):
        with cat_cols[i % 3]:
            if st.button(f"{categories[cat_name]['icon']} {cat_name}", key=f"cat_{cat_name}", use_container_width=True):
                st.session_state.selected_category = cat_name
    
    st.markdown("---")
    
    # ========== STEP 2: PROPERTY SELECTION ==========
    if "selected_category" in st.session_state:
        selected_category = st.session_state.selected_category
        available_properties = categories[selected_category]["properties"]
        
        st.subheader(f"📊 Step 2: Select Property ({selected_category})")
        selected_property = st.selectbox("Choose property:", available_properties)
        
        st.markdown("---")
        
        # ========== STEP 3: UNIT CONVERSION ==========
        if selected_property in unit_categories:
            st.subheader("📝 Step 3: Enter Value & Select Units")
            
            col1, col2 = st.columns([2, 1])
            with col1:
                value = st.number_input("Value:", value=1.0, step=0.1, format="%.6f")
            with col2:
                from_unit = st.selectbox("Input Unit:", unit_categories[selected_property]["units"], key="from")
            
            st.markdown("---")
            
            # Select output units
            st.subheader("🎯 Step 4: Select Output Units (Select multiple)")
            
            all_units = unit_categories[selected_property]["units"]
            selected_units = []
            cols_per_row = 4
            
            for i in range(0, len(all_units), cols_per_row):
                cols = st.columns(cols_per_row)
                for j, unit in enumerate(all_units[i:i+cols_per_row]):
                    with cols[j]:
                        if st.checkbox(unit, key=f"out_{selected_property}_{unit}"):
                            selected_units.append(unit)
            
            st.markdown("---")
            
            # Convert button
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                convert_clicked = st.button("🔄 CONVERT", type="primary", use_container_width=True)
            
            st.markdown("---")
            
            # Display results
            if convert_clicked:
                if selected_units:
                    st.subheader("✅ Conversion Results")
                    st.markdown(f"**Input:** {value} {from_unit}")
                    st.markdown(f"**Category:** {selected_category} | **Property:** {selected_property}")
                    
                    result_cols = st.columns(min(len(selected_units), 4))
                    for idx, to_unit in enumerate(selected_units):
                        result = convert_unit(value, from_unit, to_unit, selected_property)
                        with result_cols[idx % 4]:
                            st.metric(to_unit, f"{result:.6g}")
                else:
                    st.warning("⚠️ Please select at least one output unit!")
        else:
            st.warning(f"⚠️ Property '{selected_property}' data not found.")
    
    else:
        st.info("👆 **Welcome to Unit Converter!**\n\n1. Click on any category button above\n2. Select a property from that category\n3. Enter value and select input unit\n4. Check output units you want\n5. Click CONVERT to see results")
        
        with st.expander("📋 Available Categories & Properties"):
            for cat_name, cat_info in categories.items():
                st.markdown(f"**{cat_info['icon']} {cat_name}**")
                for prop in cat_info["properties"]:
                    st.markdown(f"  - {prop}")
                st.markdown("---")
   
# ==========================================
# FOOTER
# ========================================== 
st.markdown("---")
st.markdown(f"""
<div class="footer">
    <p class="footer-name">{_("footer_name")}</p>
    <p class="footer-university">{_("footer_university")}</p>
    <p class="footer-credit">{_("footer_credit")}</p>
    <p class="footer-credit">{_("footer_copyright")}</p>
</div>
""", unsafe_allow_html=True)