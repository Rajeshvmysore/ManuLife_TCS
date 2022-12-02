import os
import pandas as pd
import glob

input_path=os.getcwd()
des_path=(input_path+'\\'+'Extracted_files')



files=glob.glob(os.path.join(des_path,"*.csv"))

print(files)

if not os.path.exists("Output-CSV"):
    os.makedirs("Output-CSV")

data1={
"Source IP":[],
"Environment":[],
}

data={
"Source IP":[],
"Environment":[],
}

for f in files:
    baseFileName = os.path.basename(f)
    base,exe=os.path.splitext(baseFileName)
    if base.startswith("NA"):
        df12 = pd.read_csv(f)
        cource_ids1 = df12["Source IP"].unique()
        #print(cource_ids1)
        for ij in cource_ids1:
            # print(ij)
            data["Source IP"].append(ij)
            data["Environment"]="NA Prod"
    if baseFileName.startswith("Asia"):
        df = pd.read_csv(f)
        cource_ids = df["Source IP"].unique()
        for ik in cource_ids:
            data1["Source IP"].append(ik)
            data1["Environment"] = "Asia Prod"
df23=pd.DataFrame(data)
df34=pd.DataFrame(data1)
merged_df = pd.concat([df23, df34])
merged_df.to_csv("Output-CSV\\Combined.csv",index=None)
