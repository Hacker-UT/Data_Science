# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
#Code starts here
census=np.concatenate((data,new_record),axis=0)
age=np.array(census[:,0])
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)
race=np.array(census[:,2])
race_0=race[race==0]
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==3]
len_0=race_0.size
len_1=race_1.size
len_2=race_2.size
len_3=race_3.size
len_4=race_4.size
len_all=[len_0,len_1,len_2,len_3,len_4]
min_race=min(len_all)
minority_race=len_all.index(min_race)
senior_citizens=census[census[:,0]>60]
working_hours=np.array(senior_citizens[:,6])
working_hours_sum=working_hours.sum()
senior_citizens_len=working_hours.size
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
inc_h=np.array(high[:,7])
inc_l=np.array(low[:,7])
avg_pay_high=inc_h.mean()
avg_pay_low=inc_l.mean()



