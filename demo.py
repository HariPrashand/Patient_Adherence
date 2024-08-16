import pandas as pd

df1 = pd.read_excel("streamlitapp/updated_file.xlsx")
df1["Adherence"] = ""
s = {}
for index, row in df1.iterrows():
    s = {}
    s = {
        'Age': row['Age'],
        'InsuranceType': row['InsuranceType'],
        'MedianIncome': row['MedianIncome'],
        'HospitalizationPriorYear': row['HospitalizationPriorYear'],
        'MSRelatedHospitalization': row['MSRelatedHospitalization'],
        'RelapsePriorYear': row['RelapsePriorYear'],
        'Disease': row['Disease'],
        'TherapeuticArea': row['TherapeuticArea'],
        'SpecialtyPharma': row['SpecialtyPharma'],
        'TrialLengthWeeks': row['TrialLengthWeeks'],
        'MicroReimbursements': row['MicroReimbursements'],
        'DoseLengthSeconds': row['DoseLengthSeconds'],
        'DoseDelayHours': row['DoseDelayHours'],
    }
    df1.loc[0,'Adherence'] = True
    df1.loc[1,'Adherence'] = False
    print(df1)