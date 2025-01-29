course_id=input("Hicheeliin code: ")
course_name=input("Hicheeliin ner: ")
credit=input("Hicheeliin credit: ")

madlib="Ene hicheeliin code ni {}".format(course_id).upper()+\
", hicheeliin ner ni {}".format(course_name).title()+ \
" buguud ug hicheel ni {}".format(credit)+ " creditiin hicheel ym."
print(madlib)
