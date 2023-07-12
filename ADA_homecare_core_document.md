# ADA_Homecare

**Warsaw SNH (Supply Network Hub) ADA (Automation Digitization Analytics) Homecare Category**

Below document provides general overview on Management of ADA Homecare organization.

We as ADA Homecare are **data and customer** oriented team and we understand the importance of data that supports our business.
We know who and where our customers are to constalntly serve them with our products.

ADA Homecare goal is to provide on time, best qualtity and _fit-for-use_ data to all Homecare users. At any point in time. 
Our core model was designed to create user friendly IT enviroment for total category. Allowing user to focus on analysis or business problem not looking for data or checking if data is correct.
We as ADA Homecare are here to ensure quality, integrity and governance of your daily data.

**Below are key elements we took while designing the model:**

1/ Everyone, all the time, deserves equal access to the same data  
2/ We are here to deliver P&G quality  
3/ We want to be available on each shelf  

Those key elements led to creation of **ADA_homecare_core_document** from which we started our data oriented journey.  
We engraved our model in IT _"stone"_ - Excel - so you can start it simple.  

**ADA_homecare_core_document** - serves as _control panel_ for the data we collect and distribute using _ADA Solutions_ (Powerbi, Python, Powerautomate, KNIME) and in our stone as well - Excel.  

**iRisk** - ADA Homecare has all the entry data points iRisked via EUPSC HOME PowerBI Workspace - to make it simple.  
Our _core document_ collects all TID's and AED's for connections we operate with.  
Any new model has to be designed with ADA Homecare team and stored in _core document_ with approved TID/AED.  

**data storage location:** EUPSC HOME Workspace (Premium)  
**orchestration tool:** PowerAutomate flows for data governance and quality  

On Dataflows:

**official** - only queries based on P&G owned tables example: _ap_financial_shipment.open_orders_ from PS Data Hub  
**external not allowed** - if your query is complex and cannot be fully moved to datamart you must provide complete technical documentation. It will be stored for it's governance on our _ADA Solutions_ **sharepoint list** owned by ADA Homecare B2.  
**refresh frequency:** daily, monthly, weekly, live *_disclaimer_: for external sources we will require timestamp of last refresh - continously  
**refresh triggers:** api, powerbi  
**quality** - all our data requires evidence of quality against specified P&G official sources. We will keep continous check against those sourcse with our PowerAutomate quality schedule.  
**correct documentation** is understood as clearly described KNIME flow and .knaf, .knar files, Databricks Notebook, PowerAutomate is shared with adahomrecare.im etc.  
**query must be provided** mandatory. No dataflow will be created before previous check with ADA team. You query is stored in GitHub space in P&G repository under the name: ADA_Homecare. This makes our queries easily accesible by all members of ADA Homecare. 

_(consider using ChatGPT to provide you with entry description for each step - then YOU correct or provide details - easy peasy)_  
**DO NOT DISCLOSE ANY CONNECTION DETAILS AND REPLACE _SCHEMA_ NAME WITH SPECIFIC WORD TO EASILY REPLACE AFTERWARDS**  

On Datamarts:  

**contains official measures** - end user connected to datamart will be able to source all official measures that ADA Team delivers for Homecare category.We provide correct and quality data for any 'recognized' end-point when connected by combination of fpc/dc/time to our masterdata matrix tables.  
**single point data source for PowerBI reports/dashboards** - direct connect to datamart = synchronized refresh. PowerBI reports/dashboards sourcing from same datamart are being refreshed simultaneously with datamart using minimum capacity.  


