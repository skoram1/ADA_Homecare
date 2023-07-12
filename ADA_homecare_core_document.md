# ADA_Homecare

**Warsaw SNH (Supply Network Hub) ADA (Automation Digitization Analytics) Homecare Category**

Dear Citizen Developer,

_Welcome on board and fasten your seatbelt._ 

This document will give you initial overview on _who we are_ and _how we work_ in ADA Homecare organization.

We as ADA Homecare are **data and customer** oriented team that understands the importance of data that supports our business.
We know who our customers are and where they _buy_ - to constalntly serve them with our products.

ADA Homecare mission is to provide on time, best qualtity and _fit-for-use_ data to all Homecare users. We are committed to developing solutions that enable informed decisions and optimize the balance between _human_ workload and automation. 

Our main goal is to create a user-friendly IT environment for the entire category. We want to make it easy for users to focus on analyzing data and solving business problems, rather than spending time searching for or verifying data. At ADA Homecare, we are here to ensure that your daily data is of high quality, trustworthy, and well-governed.

**Our model design was guided by the following essential principles:**

1/ Everyone, all the time, deserves equal access to the same data  
2/ We are here to deliver P&G quality  
3/ We want to be available on each shelf  

Those key elements led to creation of **ADA homecare core document** which started our digital transformation journey. You are becoming part of it now. Our model we engraved in IT _"stone"_ in Excel. To start it simple. One part of _core document_ is a _control panel_. It contains all critical information for the _multi-chain_ to work collecting and distributing our data using _ADA Solutions_ and Excel. This _file_ is owned by ADA Homecare B2 and is shared with limited number of people using adahomercare.im folder in ADA Homecare Sharepoint.  

All _ADA Solutions_ need to meet **iRisk** requirements. To make it simple we do it via EUPSC HOME PowerBI Workspace. Our _core document_ collects all TID's and AED's for connections we operate with. Any new model has to be designed with ADA Homecare team and stored in _core document_ with approved TID/AED in **_draw.io_**.  

**data storage location:** EUPSC HOME Workspace (Premium)  
**orchestration tool:** adahomecare.im for data governance and quality  

<span style="font-size: 5;">Dataflows:</span>

**official** - only queries based on P&G owned tables example: _ap_financial_shipment.open_orders_ from PS Data Hub

**external not allowed** - if your query is complex and cannot be fully moved to datamart you must provide complete technical documentation. It will be stored for it's governance on our _ADA Solutions_ **sharepoint list** owned by ADA Homecare B2.

**refresh frequency:** daily, monthly, weekly, liveb  
*_disclaimer: for external sources we will require timestamp of last refresh - continously_

**refresh triggers:** api, powerbi

**quality** - all our data requires evidence of quality against specified P&G official sources. We will keep continous check against those sourcse with our PowerAutomate quality schedule

**correct documentation** is understood as clearly described KNIME flow or any type of code. PowerAutomate flows need to be transferred to adahomrecare.im, KNIME files stored in _adahomecare.im_ folder on Sharepoint 

**query must be provided** mandatory. No dataflow will be created before previous check with ADA team. Your query is stored in P&G GitHub repository under the name: ADA_Homecare. This makes our queries easily accesible by all members of ADA Homecare.

_(consider using ChatGPT to provide you with entry description for each step - then YOU responsible to correct or provide details)_  
**DO NOT DISCLOSE ANY CONNECTION DETAILS AND REPLACE _SCHEMA_ NAME WITH SPECIFIC WORD TO EASILY REPLACE AFTERWARDS**

<span style="font-size: 5;">Datamarts:</span>

**contains official measures** - end user connected to datamart will be able to source all official measures that ADA Team delivers for Homecare category.We provide correct and quality data for any 'recognized' end-point when connected by combination of fpc/dc/time to our masterdata matrix tables.

**single point data source for PowerBI reports/dashboards** - direct connect to datamart = synchronized refresh. PowerBI reports/dashboards sourcing from same datamart are being refreshed simultaneously with datamart using minimum capacity. 


Shortly on _Core Document_:

**full skeleton** is provided. The Excel file allows you to orchestrate your flows, dataflows, datamart and synchronize them. This is a control panel. It contains all the references to GitHub where queries are stored. We use GitHub to feed our python codes with SQL code we use for further automation.

Welcome on board and enjoy the trip!
<br></br>
Your sincere
ADA Homecare team
<br></br>
_**Mateusz Skóra**_  
ADA Homecare B2
<br></br>
<span style="font-style: italic;">July 12, 2023</span>
