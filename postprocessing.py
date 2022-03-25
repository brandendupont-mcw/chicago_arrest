import pandas as pd
import numpy as np
import time



## Global Vars
#set arrest data path to have an impossibly large data limit
ARREST_DATA_PATH = 'https://data.cityofchicago.org/resource/dpt3-jri9.csv?$limit=100000000'
# arrest crosswalk
ARREST_CROSSWALK_PATH = "data/arrest_statute_crosswalk.csv"



def get_arrest_data(PATH):
    
    #set up time
    start_time = time.time()
    
    try:
        arrest = pd.read_csv(ARREST_DATA_PATH)
        
    except Exception as e:
        print("ERROR : "+str(e))
    
    #get size of dataset
    mb_size = arrest.memory_usage()[0]
    
    print(f'Arrest data sucessfully downloaded.\
    The data has {len(arrest)} rows and the total file size is {mb_size} mb.\
    Downloading arrest data took {round(((time.time() - start_time) /60),2)} minutes.')
    
    return arrest

def main():
    
    # get arrest data from chicago open data portal
    ar = get_arrest_data(PATH)
    
    #get arrest statute lookup table
    sl = pd.read_csv(ARREST_CROSSWALK_PATH)
    
    #merge dataset
    arl = pd.merge(ar, sl, how="left", left_on='charge_1_statute', right_on='Statute')
    
    #cast report race column to titlecase
    arl['race'] =arl['race'].str.title()
    
    # print crosswalk match rate
    print(f"Crosswalk match rate is {100*round(1 - arl['Statute'].isnull().sum() / arl.shape[0],4)}%")
    
    # save data
    arl.to_csv("chicago_arrests.csv", index=False)




if __name__ == "__main__":
    
    main()

    df = pd.DataFrame(np.random.randint(
    0, 100, size=(10, 4)), columns=list('ABCD'))

    df.to_csv("df_output.csv")
