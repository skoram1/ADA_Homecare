# ADA_Homecare

**Warsaw SNH (Supply Network Hub) ADA (Automation Digitization Analytics) Homecare Category**

Dear Citizen Developer,

_Welcome on board and fasten your seatbelt._ 

This document will give you initial overview on _who we are_ and _how we work_ in _ADA Homecare_ organization.

We as _ADA Homecare_ are **data and customer** oriented team which understands the importance of data that supports our business.
We know who our customers are and where they _"buy"_ to constalntly serve them with our products.

**Our mission:** provide on time, best qualtity and _fit-for-use_ data to all Homecare users. We are committed to developing solutions that enable informed decisions and optimize the balance between _human_ workload and automation. 

We want to achieve this by creating user-friendly IT environment for the entire category. Making it easy for users to focus on analyzing data and solving business problems, rather than spending time searching for or verifying data. At _ADA Homecare_, we are here to ensure that your daily data is of high quality, trustworthy, and well-governed.

**Our model design was guided by the following essential principles:**

1/ Everyone, all the time, deserves equal access to the same data  
2/ We are here to deliver P&G quality  
3/ We want to be available on each shelf  

Those key elements led to the creation of the **ADA Homecare Core Document**, marking the beginning of our digital transformation journey. You are now becoming an integral part of it. We have embedded our model in IT "engraved stone" which is Excel. We wanted to keep it simple. This _file_ serves as a control panel where we centralize all information, ensuring the **sustainability** of our products. It ensures the continuous and synchronized operation of our _multi-chain_, which collects and distributes our data using ADA Solutions and Excel. The **ADA Homecare Core Document** is owned by _ADA Homecare_ B2 and is shared with a limited number of people via the adahomercare.im folder in the _ADA Homecare_ Sharepoint. 

_ADA Solutions_ must meet **iRisk** requirements. To make it simple we do it via EUPSC HOME PowerBI Workspace. Our _core document_ collects all TID's and AED's for connections we operate with. Any new model has to be designed with _ADA Homecare_ team and stored in _core document_ with approved TID/AED provided in **_draw.io_**.  

**data storage location:** EUPSC HOME Workspace (Premium)  
**orchestration tool:** adahomecare.im for data governance and quality  

<span style="font-size: 5;">Dataflows:</span>

**official** - only queries based on P&G owned tables example: _ap_financial_shipment.open_orders_ from PS Data Hub

**external not allowed** - if your query is complex and cannot be fully moved to datamart you must provide complete technical documentation. It will be stored for it's governance on our _ADA Solutions_ **sharepoint list** owned by _ADA Homecare_ B2.

**refresh frequency:** daily, monthly, weekly, liveb  
*_disclaimer: for external sources we will require timestamp of last refresh - continously_

**refresh triggers:** api, powerbi

**quality** - all our data requires evidence of quality against specified P&G official sources. We will keep continous check against those sourcse with our PowerAutomate quality schedule

**correct documentation** is understood as clearly described KNIME flow or any type of code. PowerAutomate flows need to be transferred to adahomrecare.im, KNIME files stored in _adahomecare.im_ folder on Sharepoint 

**query must be provided** mandatory. No dataflow will be created before previous check with ADA team. Your query is stored in P&G GitHub repository under the name: ADA_Homecare. This makes our queries easily accesible by all members of _ADA Homecare_.

_(consider using ChatGPT to provide you with entry description for each step - then YOU responsible to correct or provide details)_  
**DO NOT DISCLOSE ANY CONNECTION DETAILS AND REPLACE _SCHEMA_ NAME WITH SPECIFIC WORD TO EASILY REPLACE AFTERWARDS**

<span style="font-size: 5;">Datamarts:</span>

**contains official measures** - end user connected to datamart will be able to source all official measures that ADA Team delivers for Homecare category.We provide correct and quality data for any 'recognized' end-point when connected by combination of fpc/dc/time to our masterdata matrix tables.

**single point data source for PowerBI reports/dashboards** - direct connect to datamart = synchronized refresh. PowerBI reports/dashboards sourcing from same datamart are being refreshed simultaneously with datamart using minimum capacity. 


Shortly on _Core Document_:

**full skeleton** is provided. The Excel file allows you to orchestrate your flows, dataflows, datamart and synchronize them. This is a control panel. It contains all the references to GitHub where queries are stored. We use GitHub to feed our python codes with SQL code to use it in for further automations.

Welcome on board and enjoy the trip!
<br></br>
Your sincere
ADA Homecare team
<br></br>
_**Mateusz Skóra**_  
ADA Homecare B2
<br></br>
<span style="font-style: italic;">July 12, 2023</span>
