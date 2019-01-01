# step2
# get certain unigram and bigram features
# send to longleaf
import pandas as pd
import numpy as np

review_by_business = pd.read_table('review_by_business.txt')

review_by_business['uni_good_notext'] = 0
review_by_business['uni_bad_notext'] = 0
review_by_business['bi_sani_good_notext'] = 0
review_by_business['bi_sani_bad_notext'] = 0
review_by_business['bi_loc_good_notext'] = 0
review_by_business['bi_loc_bad_notext'] = 0
review_by_business['bi_service_good_notext'] = 0
review_by_business['bi_service_bad_notext'] = 0
review_by_business['bi_taste_good_notext'] = 0
review_by_business['bi_taste_bad_notext'] = 0

ugw_count,ubw_count,sgnw_count,sbnw_count,lgnw_count,lbnw_count, \
sergnw_count,serbnw_count,tgnw_count,tbnw_count = 0,0,0,0,0,0,0,0,0,0

# (uni_good_notext_count,uni_bad_notext,bi_sani_good_notext,bi_sani_bad_notext, \
#  bi_sani_bad_notext,   =0
uni_good_notext_list = ['good','great','perfect', 'favorite','favourite','best', \
                        'love','nice','delicious','amazing','top','pretty', \
                        'excellent','perfect','underrated','superb','decent']
uni_bad_notext_list = ['nasty','noisy','disappoint','cockroach','fly','mosquito', \
                       'bug','worse','worst','disgusting','hell','sad','r.i.p']

sani_noun_notext_list = ['sanitation','environment','health','hygiene', \
                         'surrounding','floor','table']
sani_good_notext_list = ['clean','quiet']
sani_good_notext_list.extend(uni_good_notext_list)
sani_bad_notext_list = uni_bad_notext_list

loc_noun_notext_list = ['location','place','bar','bartenders','bartender', \
                        'atmosphere','parking','beach']
loc_good_notext_list = ['easy','pleasant','pleased','fun']
loc_good_notext_list.extend(uni_good_notext_list)
loc_bad_notext_list = ['hard','busy','annoy','underground']
loc_bad_notext_list.extend(uni_bad_notext_list)

service_noun_notext_list = ['service','quality','staff','waiter','waitress', \
                            'prepare','price']
service_good_notext_list = ['24hour','welcoming','fantastic','nice', \
                            'communicative','helpful','quick','fast','super']
service_good_notext_list.extend(uni_good_notext_list)
service_bad_notext_list = ['bad','worse','worst''confusing','improper','late', \
                           'disrespect','tragic']

taste_noun_notext_list = ['taste','food','drink','appetizer','dessert']
taste_good_notext_list = ['great','good','fantastic','pleasant','pleased','quick', \
                          'fast','decent','organic','inexpensive','cheap','fresh']
taste_bad_notext_list = uni_bad_notext_list

print("finished initializing file")
# iter
# first use a subset to test
for index,row in review_by_business.iterrows():
    for sentence in row['lemma_text']:
        # uni_good_notext
        for uni_good_word in uni_good_notext_list:
            if uni_good_word in sentence:
                # temp.uni_good_notext.iloc[index] += 1
                ugw_count += 1

        # uni_bad_notext
        for uni_bad_word in uni_bad_notext_list:
            if uni_bad_word in sentence:
                # temp.uni_bad_notext.iloc[index] += 1
                ubw_count += 1

        # bi_sani_good/bad_notext
        for sani_noun_notext_word in sani_noun_notext_list:
            if sani_noun_notext_word in sentence:
                for sani_good_notext_word in sani_good_notext_list:
                    if sani_good_notext_word in sentence:
                        # temp.bi_sani_good_notext.iloc[index] += 1
                        sgnw_count += 1
                for sani_bad_notext_word in sani_bad_notext_list:
                    if sani_bad_notext_word in sentence:
                        # temp.bi_sani_bad_notext.iloc[index] += 1
                        sbnw_count += 1

        # bi_loc_good/bad_notext
        for loc_noun_notext_word in loc_noun_notext_list:
            if loc_noun_notext_word in sentence:
                for loc_good_notext_word in loc_good_notext_list:
                    if loc_good_notext_word in sentence:
                        lgnw_count += 1
                for loc_bad_notext_word in loc_bad_notext_list:
                    if loc_bad_notext_word in sentence:
                        lbnw_count += 1

        # bi_service_good/bad_notext
        for service_noun_notext_word in service_noun_notext_list:
            if service_noun_notext_word in sentence:
                for service_good_notext_word in service_good_notext_list:
                    if service_good_notext_word in sentence:
                        sergnw_count += 1
                for service_bad_notext_word in service_bad_notext_list:
                    if service_bad_notext_word in sentence:
                        serbnw_count += 1

        # bi_taste_good/bad_notext
        for taste_noun_notext_word in taste_noun_notext_list:
            if taste_noun_notext_word in sentence:
                for taste_good_notext_word in taste_good_notext_list:
                    if taste_good_notext_word in sentence:
                        tgnw_count += 1
                for taste_bad_notext_word in taste_bad_notext_list:
                    if taste_bad_notext_word in sentence:
                        tbnw_count += 1

    # give value back to corresponding cols
    print(ugw_count)
    review_by_business.uni_good_notext.iloc[index] = ugw_count
    review_by_business.uni_bad_notext.iloc[index] = ubw_count
    review_by_business.bi_sani_good_notext.iloc[index] = sgnw_count
    review_by_business.bi_sani_bad_notext.iloc[index] = sbnw_count
    review_by_business.bi_loc_good_notext.iloc[index]=lgnw_count
    review_by_business.bi_loc_bad_notext.iloc[index]=lbnw_count
    review_by_business.bi_service_good_notext.iloc[index]=sergnw_count
    review_by_business.bi_service_bad_notext.iloc[index]=serbnw_count
    review_by_business.bi_taste_good_notext.iloc[index]=tgnw_count
    review_by_business.bi_taste_bad_notext.iloc[index]=tbnw_count

    ugw_count,ubw_count,sgnw_count,sbnw_count,lgnw_count,lbnw_count, \
    sergnw_count,serbnw_count,tgnw_count,tbnw_count = 0,0,0,0,0,0,0,0,0,0
    if index % 1 == 0:
        print(index)
print("finished feature generation!")
review_by_business.to_csv('review_by_business_done.txt',sep='\t', encoding='utf-8', index=False)
print("saved!")

