from parser import Parser

def execute():
    url_ = r"https://data.cms.gov/data-api/v1/dataset"

    field_list = ['CROSS_REF_PROVIDER_NUMBER','FAC_NAME','ST_ADR','CITY_NAME','ZIP_CD','FIPS_STATE_CD','STATE_CD',
    'CRTFD_BED_CNT','RSDNT_PGM_ALPTHC_SW','RSDNT_PGM_DNTL_SW','RSDNT_PGM_OSTPTHC_SW','RSDNT_PGM_OTHR_SW','RSDNT_PGM_PDTRC_SW',
    'RSDNT_PHYSN_CNT','ORGNZ_RSDNT_GRP_SW']

    quarter_dict = {
        'Q4_2021':'3cc6ad89-5cc0-4071-91e1-2a91aff79975',
        'Q3_2021':'4cc3f12e-128a-45ed-b308-1629f5973ffe',
        'Q2_2021':'7744bb2f-5377-4bfe-9a6c-2ffd05f53038',
        'Q1_2021':'50edc478-87ab-4741-ac65-b8f8720afa04',
        'Q4_2020':'8a22778e-880b-484a-89fa-d24e1f2ab95e',
        'Q3_2020':'a68c674f-1edf-48e4-8aa0-94804b2766c2',
        'Q2_2020':'2b838529-336f-4204-99d0-49372db0b6b3',
        'Q1_2020':'8f6da2b1-f719-40c2-8f73-2b7ecb7fb42a',
        'Q4_2019':'03cca0cc-13a0-4b8d-82c4-57185b6bbfbd',
        'Q3_2019':'4dac6d25-b481-4227-9c20-5fea5844d56e',
        'Q2_2019':'ed516084-cabf-4acf-98c0-8cac98c606c0',
        'Q1_2019':'41fe7455-62c9-4af6-b97d-9641b42be80b',
        'Q4_2018':'4ff7fcfb-2a40-4f76-875d-a4ac2aec268e',
        'Q4_2017':'d338dc0d-641c-486a-b586-88a662f36963',
        'Q4_2016':'96ba2257-2080-49c1-9e5b-7726f9f83cad',
        'Q4_2015':'8ccf4b97-58df-4a17-ba8b-4cc558eda6ef',
        'Q4_2014':'a091d8eb-ebed-4cfc-acad-bcd58a46a28a',
        'Q4_2013':'2bb03207-515d-48c3-96f9-edc377b21c76',
        'Q4_2012':'38b5dd08-4077-4adf-ba10-7af7c4eaab7c',
        'Q4_2011':'6a1c6074-4ecf-4a6d-bef7-2314b07573ab',
        'Q4_2010':'0f3c9721-0a0c-410d-8a4f-0a3b8abafcb9'
    }
    
    req = Parser(url_, field_list, quarter_dict)
    print("Making request")
    req.request()
    print("Checking fields")
    req.checkFields()
    print("Filtering JSON")
    req.filterDicts()
    print("Writing data to output files")
    req.outputData(r"path\goes\here")
    print("All done!")

if __name__ == "__main__":
    execute()
