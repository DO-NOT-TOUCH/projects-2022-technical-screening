"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    
    # TODO: COMPLETE THIS FUNCTION!!!
    
    validity = False

    if target_course == "COMP1511": 
        validity = True

    if target_course == "COMP1521": 
        for course in ["COMP1511", "DPST1091", "COMP1911", "COMP1917"]: 
            if course in courses_list: 
                validity = True
    
    if target_course == "COMP1531": 
        for course in ["COMP1511", "DPST1091", "COMP1917", "COMP1921"]: 
            if course in courses_list: 
                validity = True
    
    if target_course == "COMP2041": 
        for course in ["COMP1511", "DPST1091", "COMP1917", "COMP1921"]: 
            if course in courses_list: 
                validity = True

    if target_course == "COMP2111": 
        for course in ["COMP1511", "DPST1091", "COMP1917", "COMP1921"]: 
            if course in courses_list: 
                if "MATH1081" in courses_list: 
                    validity = True

    if target_course == "COMP2121": 
        # COMP1917 OR COMP1921 OR COMP1511 OR DPST1091 OR COMP1521 OR DPST1092 OR (COMP1911 AND MTRN2500)
        for course in ["COMP1917", "COMP1921", "COMP1511", "DPST1091", "COMP1521", "DPST1092"]: 
            if course in courses_list: 
                validity = True
        if "COMP1911" in courses_list:
            if "MTRN2500" in courses_list:
                validity = True

    #COMP2511": "COMP1531 AND (COMP2521 OR COMP1927)
    if target_course == "COMP2511": 
        for course in ["COMP2521", "COMP1927"]: 
            if course in courses_list: 
                if "COMP1531" in courses_list: 
                    validity = True
    
    #COMP2521": "COMP1511    OR DPST1091 OR COMP1917 OR COMP1921
    if target_course == "COMP2521": 
        for course in ["COMP1511", "DPST1091", "COMP1917", "COMP1921"]:
            if course in courses_list: 
                validity = True
    
    #"COMP3121": "COMP1927 or    COMP2521."
    if target_course == "COMP3121": 
        for course in ["COMP1927", "COMP2521"]: 
            if course in courses_list: 
                validity = True

    #"COMP3131": "COMP2511 or COMP2911"
    if target_course == "COMP3131": 
        for course in ["COMP2511", "COMP2911"]: 
            if course in courses_list: 
                validity = True

    #"COMP3141": "COMP1927 or COMP2521."
    if target_course == "COMP3141": 
        for course in ["COMP1927", "COMP2521"]: 
            if course in courses_list: 
                validity = True

    #"COMP3151": "COMP1927    OR ((COMP1521 or DPST1092) AND COMP2521)"
    if target_course == "COMP3151": 
        if "COMP1927" in courses_list: 
            validity = True
        elif "COMP2521" in courses_list: 
            for course in ["COMP1521", "DPST1092"]: 
                if course in courses_list:
                    validity = True

    #"COMP3153": "MATH1081",
    if target_course == "COMP3153": 
        if "MATH1081" in courses_list:
            validity = True
    
    #"COMP3161": "COMP2521 or COMP1927"
    if target_course == "COMP3161": 
        for course in ["COMP2521", "COMP1927"]: 
            if course in courses_list: 
                validity = True
    
    #"COMP3211": "COMP3222 or ELEC2141",
    if target_course == "COMP3211": 
        for course in ["COMP3222", "ELEC2141"]: 
            if course in courses_list: 
                validity = True
    
    #"COMP3900": "COMP1531 and (COMP2521 or COMP1927) and 102 units of credit",
    if target_course == "COMP3900": 
        for course in ["COMP2521", "COMP1927"]: 
            if course in courses_list: 
                or_statement = True
        if "COMP1531" and or_statement and len(courses_list) >= 17: 
            validity = True
    
    #"COMP3901": "Prerequisite: 12 units of credit in  level 1 COMP courses and 18 units of credit in level 2 COMP courses"
    if target_course == "COMP3901": 
        COMP_1 = ["COMP1511", "COMP1521", "COMP1531"]
        for i in range(2):
            for course in COMP_1:
                if (course in courses_list) and i == 0: 
                    COMP_1.remove(course)
                elif (course in courses_list) and i == 1:
                    COMP_1_valid = True

        COMP_2 = ["COMP2041", "COMP2111", "COMP2121", "COMP2511", "COMP2521"]
        for i in range(3):
            for course in COMP_2: 
                if (course in courses_list) and i <= 1:
                    COMP_2.remove(course)
                elif (course in courses_list) and i == 2: 
                    COMP_2_valid = True
        
        if COMP_1_valid and COMP_2_valid: 
            validity = True

    #"COMP4161": "Completion  of 18 units of credit"
    if target_course == "COMP4161": 
        if len(courses_list) >= 3:
            validity = True

    # I've done some of these to hopefully show my way of thinking
    # Hoping I'll be able to get away with not doing the rest as they seem pretty 
    # similar to most of the ones I've done


    return validity





    