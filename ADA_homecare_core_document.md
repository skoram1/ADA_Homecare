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

Those key elements led to creation of **ADA homecare core document** which started our digital transformation journey. You are reading it now. Our model we engraved in IT _"stone"_ in Excel. To start it simple. One part of _core document_ is a _control panel_. It contains all critical information for the _multi-chain_ to work collecting and distributing our data using _ADA Solutions_ and Excel. This _file_ is owned by ADA Homecare B2 and is shared with limited number of people using adahomercare.im folder in ADA Homecare Sharepoint.  

All _ADA Solutions_ need to meet **iRisk** requirements. To make it simple we do it via EUPSC HOME PowerBI Workspace. Our _core document_ collects all TID's and AED's for connections we operate with. Any new model has to be designed with ADA Homecare team and stored in _core document_ with approved TID/AED in **_draw.io_**.  

**data storage location:** EUPSC HOME Workspace (Premium)  
**orchestration tool:** adahomecare.im for data governance and quality  

Dataflows:

**official** - only queries based on P&G owned tables example: _ap_financial_shipment.open_orders_ from PS Data Hub

**external not allowed** - if your query is complex and cannot be fully moved to datamart you must provide complete technical documentation. It will be stored for it's governance on our _ADA Solutions_ **sharepoint list** owned by ADA Homecare B2.

**refresh frequency:** daily, monthly, weekly, liveb  
*_disclaimer: for external sources we will require timestamp of last refresh - continously_

**refresh triggers:** api, powerbi

**quality** - all our data requires evidence of quality against specified P&G official sources. We will keep continous check against those sourcse with our PowerAutomate quality schedule

**correct documentation** is understood as clearly described KNIME flow and .knaf, .knar files, Databricks Notebook, PowerAutomate is shared with adahomrecare.im etc.

**query must be provided** mandatory. No dataflow will be created before previous check with ADA team. You query is stored in GitHub space in P&G repository under the name: ADA_Homecare. This makes our queries easily accesible by all members of ADA Homecare.

_(consider using ChatGPT to provide you with entry description for each step - then YOU responsible to correct or provide details)_  
**DO NOT DISCLOSE ANY CONNECTION DETAILS AND REPLACE _SCHEMA_ NAME WITH SPECIFIC WORD TO EASILY REPLACE AFTERWARDS**

Datamarts:

**contains official measures** - end user connected to datamart will be able to source all official measures that ADA Team delivers for Homecare category.We provide correct and quality data for any 'recognized' end-point when connected by combination of fpc/dc/time to our masterdata matrix tables.

**single point data source for PowerBI reports/dashboards** - direct connect to datamart = synchronized refresh. PowerBI reports/dashboards sourcing from same datamart are being refreshed simultaneously with datamart using minimum capacity. 


Shortly on _Core Document_:

**full skeleton** is provided. The Excel file allows you to orchestrate your flows, dataflows, datamart and synchronize them. This is a control panel. It contains all the references to GitHub where queries are stored. We use GitHub to feed our python codes with SQL code we use for further automation.

Welcome on board and enjoy the trip!

<br>
<br>

Your sincere
ADA Homecare team
<br></br>
Powered by _**Mister**_
