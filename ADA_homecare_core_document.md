# ADA_Homecare

**Warsaw SNH (Supply Network Hub) ADA (Automation Digitization Analytics) Homecare Category**

Below document provides general overview on Management of ADA Homecare organization.

We as ADA Homecare are data oriented team and we understand importance and quality of data that supports our business.
Being customer oriented _Digital_ team we know who and where our users are and how to serve them our products.

ADA Homecare goal is to provide on time,best qualtity and _fit-for-use_ data to all Homecare users. At any point in time. 
Our core model was designed to create user friendly and managable IT enviroment for total category. Ensuring the quality is there.

**Below are key elements we took while designing the model:**

1/ Everyone, all the time, deserves equal access to the same data
2/ We are here to deliver P&G quality
3/ We want to be available on each shelf

Those key elements led to creation of **ADA_homecare_core_document** from which we started our data oriented journey.
We engraved our model in IT _"stone"_ - Excel - so you can start it simple.

**ADA_homecare_core_document** serves as starting point for all the data used in any ADA Solution (Powerbi, Python, Powerautomate, KNIME) and in our stone as well - Excel.

**iRisk** we have tried to make it simple. Our _core document_ collects all TID and AED for connections we use - making it simple to pass iRisk with any new application. 
Any new model is developed in co-operation between project dev team of project and ADA Homecare team and stored in _core document_ with approved TID/AED.

**Data storage location:** EUPSC HOME Workspace (Premium)

**Orchestration tool:** PowerAutomate flows for data governance and quality

On Dataflows:

**official** only queries based on P&G owned tables example: _ap_financial_shipment.open_orders_ from PS Data Hub

**external not allowed** if your query is complex or you use KNIME to build your data
documentation must be provided and attached on ADA governance **sharepoint list**. 

**Sharepoint list** mentioned above is all time ADA Homecare B2 owned list _(2023: ADA Solutions)_
Correct documentation is understood as correctly described KNIME flow and files, Databricks Notebook, etc.

_(consider using ChatGPT to provide you entry description for each step - then YOU provide details)_
**DO NOT DISCLOSE ANY CONNECTION DETAILS. REPLACE MAIN SCHEMA NAME WITH SPECIFIC NAME THAT YOU CAN EASILY REPLACE AFTERWARDS**


**query must be provided** mandatory. No dataflow will be created before previous check with ADA team

**refresh frequency:** daily, monthly, weekly, live 
Disclaimer: for external sources we will require timestamp of last refresh continously

**refresh triggers:** api, powerbi

**quality** provide evidence of quality check against any official P&G source. We will check against this source with our powerautomate schedule flow basis

On Datamart:

**contains official measures** end user connected to datamart will be able to source all official measures that ADA Team delivers for Homecare category. 
We provide correct and works in any end point when connected to our masterdata combination of fpc/dc/time matrix

**endpoint data source for PowerBI reports/dashboards** direct connect to datamart synchronizes it's refresh - multiple reports/dashboards sourcing from same datamart are refreshed simo any premium capacity.

