# ####              DICT            #######





# # int, str, bool, list, tuple
# # dict()  mutble

# my_dict={
#     "apple":"olma",
#     "ism":"Ali",
#     "yoshi":"14",
#     "user_name":"Ali",
#     1:"bir",
#     True:"true",
#     2.3:"ikki butun uchun",
#     (1,2,3,4):"tuple element",
#     #{"1":"bir"}:"dict da ishlamaydi."
#     #[1,2,3,4,5,6]:"listda ham ishlamaydi"
# }
# my_dict["apple"]="anor"
# my_dict["ism"]="vali"
# print(my_dict)



# print(my_dict["Ism"])
# print(my_dict.get('Ism', "Ism degan key yo'q"))
# my_dict ['apple' ] = 'anor'
# my_dict['ism'] = 'Vali'
# print(my_dict)
# my_dict1= dict(ism="Ali", yosh=17)
# # print(my_dict1)
# # print(list(my_dict.keys()))
# print(my_dict.pop("ism"))
# print(my_dict)
# my_dict.update(my_dict1)
# print(my_dict)
# print(my_dict.get("Ism", "smth went wrong, plz try again later!") )
# for key in my_dict:
# p
# print (value)


# my_dict={
#     "ism":"Suhrob",
#     "yoshi":20,
#     "ishi":"QarDTU da student.",
#     "bo'yi":"175 cm"
# }










# my_dict={


#       "degree": "Master, Computer Software Engineering",
#       "description": "I did my thesis in spatial anomaly detection and its applicability in the public transport market.",
#       "institution_name": "University of Amsterdam",
#       "institution_full_address": "Spui 21, Amsterdam; Amsterdam, 1012 WX, NL",
#       "institution_country_iso2": "NL",
#       "institution_country_iso3": "NLD",
#       "institution_regions": [
#         "Europe",
#         "Western Europe",
#         "EMEA",
#         "EU"
#       ],
#       "institution_city": "Amsterdam",
#       "date_to_year": 2024,
#       "order_in_profile": 1,
#       "institution_city": "Amsterdam",
#       "institution_state": "Noord-Holland",
#       "date_from_year": 2015,
#       "date_to_year": 2019,
#       "order_in_profile": 2

# }






















my_dict={

  "id": 390491994,
  "parent_id": 390491994,
  "created_at": "2017-07-24T08:36:51.000Z",
  "updated_at": "2025-12-01T05:24:46.222410Z",
  "checked_at": "2025-12-01T05:24:46.222410Z",
  "changed_at": "2025-12-01T05:24:46.222410Z",
  "is_deleted": 0,
  "is_parent": 1,
  "public_profile_id": 551832805,
  "linkedin_url": "https://www.linkedin.com/in/jessie-liauw-a-fong-831983134",
  "linkedin_shorthand_names": [
    "jcb-liauw-a-fong",
    "jessie-liauw-a-fong-831983134"
  ],
  "historical_ids": [
    390491994
  ],
  "full_name": "Jessie Liauw A Fong",
  "first_name": "Jessie",
  "first_name_initial": None,
  "middle_name": "Liauw A",
  "middle_name_initial": "L",
  "last_name": "Fong",
  "last_name_initial": "F",
  "headline": "Full stack developer",
  "picture_url": "https://media.licdn.com/dms/image/v2/D4E03AQF100dDA61SLw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1727001238451?e=2147483647&v=beta&t=0sTUvW1-9TYr3d_oJWfl9x95yuEw0xKZyhKI5xyQnz4",
  "location_country": "Netherlands",
  "location_country_iso2": "NL",
  "location_country_iso3": None,
  "location_full": "Amsterdam, North Holland, Netherlands",
  "location_regions": [
    "Europe",
    "Western Europe",
    "EMEA",
    "EU"
  ],
  "location_city": "Amsterdam",
  "location_state": "North Holland",
  "interests": [],
  "inferred_skills": [
    "software",
    "devops",
    "technology"
  ],
  "historical_skills": [
    "microsoft office",
    "javascript",
    "jquery",
    "scrum",
    "json",
    "es6",
    "kotlin",
    "mysql",
    "customer service",
    "html",
    "java",
    "nuxtjs",
    "vuejs",
    "python",
    "php",
    "cascading style sheets (css)",
    "git",
    "web development"
  ],
  "connections_count": 469,
  "professional_emails_collection": [],
  "is_working": 1,
  "active_experience_company_id": 8697858,
  "active_experience_title": "Software Engineer",
  "active_experience_department": "Engineering and Technical",
  "active_experience_management_level": "Specialist",
  "is_decision_maker": 0,
  "total_experience_duration_months": None,
    "experience_recently_started": [],
  "experience_recently_closed": []
}


new_dict={}
list=[]
for kalitlar in my_dict:
    if not my_dict[kalitlar]:
        len_list=len(list)
        list.append(kalitlar)

# print("Nonelar: >>> ",list)
# print("Nonelar soni: >>> ",len_list)

len_list=len(new_dict)
my_dict[len_list]=new_dict
print(my_dict)