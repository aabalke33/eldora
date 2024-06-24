from enum import Enum

class StatusCode(Enum):
    FAILED = -1
    INITIATED = 0
    COMPLETED = 1

valid_ein_prefixes = [
        "10", "12", "60", "67", "50", "53", "01", "02", "03", "04", "05", "06",
        "11", "13", "14", "16", "21", "22", "23", "25", "34", "51", "52", "54",
        "55", "56", "57", "58", "59", "65", "30", "32", "35", "36", "37", "38",
        "61", "15", "24", "40", "44", "94", "95", "80", "90", "33", "39", "41",
        "42", "43", "46", "48", "62", "63", "64", "66", "68", "71", "72", "73",
        "74", "75", "76", "77", "85", "86", "87", "88", "91", "92", "93", "98",
        "99", "20", "26", "27", "45", "46", "47", "81", "82", "83", "84", "85",
        "86", "87", "88", "92", "93", "99", "31"
        ]

state_abbreviations = [
        "AL", "AK", "AZ", "AR", "AS", "CA", "CO", "CT", "DE", "DC", "FL", "GA",
        "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA",
        "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
        "ND", "MP", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX",
        "TT", "UT", "VT", "VA", "VI", "WA", "WV", "WI", "WY"
        ]

form_data = {
    'wages': [
        "w-2", "w2", "wages", "wage", "employee", "employees", "employer", "employers",
        "tips", "other", "12a", "12b", "12c", "12d", "ein"
    ],
    'retirement': [
        "1099-r", "1099r", "retirement", "irr", "roth", "fatca", "distribution",
        "distributions", "ira", "sep", "simple", "recipient", "recipients",
        "payer", "payers", "gross"
    ],
    'interest': [
        "1099-int", "interest", "1099int", "int", "payer", "payers", "withdrawal",
        "recipient", "recipients", "savings", "treasury", "bond", "market"
    ]
}

key_data = {
        "wages": {
            "a": [ "a", "a.", "employees", "ssa", "number"],
            "b": [ "b", "b.", "employers", "fed", "id", "number"],
            "c": [ "c", "c.", "employers", "name", "address", "and", "zip", "code"],
            "d": [ "d", "d.", "control", "number"],
            "e/f": [ "e/f", "e", "f", "e.", "f.", "employees", "name", "address", "and", "zip", "code"],
            "1": [ "1", "1.", "wages", "tips", "other", "compensation", "comp"],
            "2": [ "2", "2.", "federal", "income", "tax", "withheld"],
            "3": [ "3", "3.", "social", "security", "wages"],
            "4": [ "4", "4.", "social", "security", "tax", "withheld"],
            "5": [ "5", "5.", "medicare", "wages", "and", "tips"],
            "6": [ "6", "6.", "medicare", "tax", "withheld"],
            "7": [ "7", "7.", "social", "security", "tips"],
            "8": [ "8", "8.", "allocated", "tips"],
            "9": [ "9", "9."],
            "10": [ "10", "10.", "dependent", "care", "benefits"],
            "11": [ "11", "11.", "nonqualified", "plans"],
            "12": [ "12", "12.", "12a", "12a.", "12b", "12b.", "12c", "12c.", "12d", "12d.", "see", "instructions", "for", "box"],
            "13": [ "13", "13.", "stat", "statutory", "emp", "employee", "retirement", "ret", "plan", "3rd", "third", "part", "sick", "pay"],
            "13a": ["stat", "statutory", "emp", "employee"],
            "13b": ["retirement", "ret", "plan"],
            "13c": ["3rd", "third", "part", "sick", "pay"],
            "14": [ "14", "14.", "other"],
            "15a": ["15", "state"],
            "15": [ "15", "15.", "state", "employers", "state", "id", "number", "no."],
            "16": [ "16", "16.", "state", "wages", "tips", "etc"],
            "17": [ "17", "17.", "state", "income", "tax"],
            "18": [ "18", "18.", "local", "wages", "tips", "etc"],
            "19": [ "19", "19.", "local", "income", "tax"],
            "20": [ "20", "20.", "locality", "name"],
            "dept": [ "dept", "dept."],
            "corp": [ "corp", "corp."],
            "employeruse": [ "employer", "use", "only"]
            }
        }
