import pandas as pd
df=pd.DataFrame({
    'age': [39,50,38,53,28],
    'workclass': ['State-gov','Self-emp-not-inc','Private','Private','Private'],
    'fnlwgt':[77516,83311,215646,234721,338409],
    'education': ['Bachelors','Bachelors','HS-grad','11th','Bachelors'],
    'education-num': [13,13,9,7,13],
    'marital-status': ['Never-married','Married-civ-spouse','Divorced','Married-civ-spouse','Married-civ-spouse'],
    'occupation': ['Adm-clerical','Exe-managerial','Handlers-cleaners','Handlers-cleaners','Prof-speciality'],
    'relationship': ['Not-in-family','Husband','Not-in-family','Husband','Wife'],
    'race': ['White','White','White','Black','Black'],
    'sex': ['Male','Male','Male','Male','Female'],
    'capital-gain': [2174,0,0,0,0],
    'capital-loss': [0,0,0,0,0],
    'hours-per-week': [40,13,40,40,40],
    'native-country': ['United-States','United-States','United-States','United-States','Cuba'],
    'salary': ['<=50k','<=50','<=50','<=50','<=50']
})
df

df.index=[
    '1','2','3','4','5'
]


1. pd.Series(df['race'].value_counts())
2. df.drop('5')['age'].mean()
3. total_rows=df.shape[0]
   df1=df[df['education']=='Bachelors']
   df1
   total_bachelor=df1.shape[0]
   percentage=(total_bachelor/total_rows)*100
   print("Percentage of people who have Bachelor's degree =",percentage,'%')
4. df1['Income>50k']=0
   def salary(income):
       if income=='>=50k':
           return 1
       else:
           return 0
   df1['Income>50k']=df1['Income>50k'].apply(salary)
   df1
   df1['Income>50k'].sum()
   print("Percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K     is:",df1['Income>50k'].sum(),'%')
5. df2=df[df['education']!='Bachelors']
   df2['Income>50k']=0
   def salary(income):
       if income=='>=50k':
           return 1
       else:
           return 0
   df2['Income>50k']=df2['Income>50k'].apply(salary)
   df2
   print("Percentage of people without advanced education make more than 50K is:",df2['Income>50k'].sum(),'%')
6. df['hours-per-week'].min()
7. df[df['hours-per-week']>=13]
   df['Income>50k']=0
   def salary(income):
       if income=='>=50k':
           return 1
       else:
           return 0
   df['Income>50k']=df['Income>50k'].apply(salary)
   print("Percentage of the people who work the minimum number of hours per week have a salary of more than 50K  is:",df['Income>50k'].sum(),'%')
8. print(df['Income>50k'].sum()/5,'%')
   print('No country has the highest percentage of people that earn >50K' ,'and its percentage is',df['Income>50k'].sum()/5,'%')
9. df[df['native-country']=="India"]
   
   