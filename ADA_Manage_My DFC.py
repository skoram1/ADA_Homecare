# Databricks notebook source
# MAGIC %python
# MAGIC %pip install black tokenize-rt
# MAGIC %pip install tqdm

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS userdb_skora_m_1.ADA_hc_sog;
# MAGIC CREATE TABLE userdb_skora_m_1.ADA_hc_sog USING CSV
# MAGIC SELECT
# MAGIC   distinct TRIM(
# MAGIC     leading '0'
# MAGIC     FROM
# MAGIC       material
# MAGIC   ) AS material_id,
# MAGIC   tdc_d.category,
# MAGIC   tdc_d.tdc_val,
# MAGIC   valclass_d.material_type_derived,
# MAGIC   inv.plant as site_id,
# MAGIC   inv.calday as `Date`,
# MAGIC   SUM(inv.buom_total_plant_stock) as buom_total_plant_stock,
# MAGIC   SUM(inv.buom_stock_in_transit) as buom_stock_in_transit,
# MAGIC   SUM(inv.buom_mrp_available_csp_agg) as buom_mrp_available_csp_agg,
# MAGIC   SUM(inv.buom_quality_inspection) as buom_quality_inspection,
# MAGIC   SUM(inv.buom_unrestricted) as buom_unrestricted,
# MAGIC   SUM(inv.buom_blocked) as buom_blocked,
# MAGIC   SUM(inv.buom_pg_owned_stock) as buom_pg_owned_stock,
# MAGIC   SUM(inv.buom_safety_stock) as buom_safety_stock,
# MAGIC   SUM(inv.buom_maximum_stock) as buom_maximum_stock,
# MAGIC   SUM(inv.buom_released_orders_fpc_only) as buom_released_orders_fpc_only,
# MAGIC   SUM(inv.c_pal_total_plant_stock) as c_pal_total_plant_stock,
# MAGIC   SUM(inv.buom_shipment_actuals) as buom_shipment_actuals,
# MAGIC   SUM(inv.su_shipment_actuals) as su_shipment_actuals,
# MAGIC   SUM(inv.msu_shipment_actuals) as msu_shipment_actuals,
# MAGIC   SUM(inv.buom_maximum_stock_ship_det_portion) as buom_maximum_stock_ship_det_portion,
# MAGIC   SUM(inv.buom_maximum_stock_original_apo_sap) as buom_maximum_stock_original_apo_sap,
# MAGIC   SUM(inv.buom_maximum_stock_otherwise_apo_sap) as buom_maximum_stock_otherwise_apo_sap,
# MAGIC   SUM(inv.su_total_plant_stock) as su_total_plant_stock,
# MAGIC   SUM(inv.su_stock_in_transit) as su_stock_in_transit,
# MAGIC   SUM(inv.su_mrp_available_csp_agg) as su_mrp_available_csp_agg,
# MAGIC   SUM(inv.su_quality_inspection) as su_quality_inspection,
# MAGIC   SUM(inv.su_unrestricted) as su_unrestricted,
# MAGIC   SUM(inv.su_blocked) as su_blocked,
# MAGIC   SUM(inv.su_pg_owned_stock) as su_pg_owned_stock,
# MAGIC   SUM(inv.su_safety_stock) as su_safety_stock,
# MAGIC   SUM(inv.su_maximum_stock) as su_maximum_stock,
# MAGIC   SUM(inv.su_released_orders_fpc_only) as su_released_orders_fpc_only,
# MAGIC   SUM(inv.msu_total_plant_stock) as msu_total_plant_stock,
# MAGIC   SUM(inv.msu_stock_in_transit) as msu_stock_in_transit,
# MAGIC   SUM(inv.msu_mrp_available_csp_agg) as msu_mrp_available_csp_agg,
# MAGIC   SUM(inv.msu_quality_inspection) as msu_quality_inspection,
# MAGIC   SUM(inv.msu_unrestricted) as msu_unrestricted,
# MAGIC   SUM(inv.msu_blocked) as msu_blocked,
# MAGIC   SUM(inv.msu_pg_owned_stock) as msu_pg_owned_stock,
# MAGIC   SUM(inv.msu_safety_stock) as msu_safety_stock,
# MAGIC   SUM(inv.msu_maximum_stock) as msu_maximum_stock,
# MAGIC   SUM(inv.msu_released_orders_fpc_only) as msu_released_orders_fpc_only,
# MAGIC   SUM(inv.raw_total_plant_stock) as raw_total_plant_stock,
# MAGIC   SUM(inv.raw_stock_in_transit) as raw_stock_in_transit,
# MAGIC   SUM(inv.raw_mrp_available_csp_agg) as raw_mrp_available_csp_agg,
# MAGIC   SUM(inv.raw_quality_inspection) as raw_quality_inspection,
# MAGIC   SUM(inv.raw_unrestricted) as raw_unrestricted,
# MAGIC   SUM(inv.raw_blocked) as raw_blocked,
# MAGIC   SUM(inv.raw_pg_owned_stock) as raw_pg_owned_stock,
# MAGIC   SUM(inv.raw_safety_stock) as raw_safety_stock,
# MAGIC   SUM(inv.raw_maximum_stock) as raw_maximum_stock,
# MAGIC   SUM(inv.raw_released_orders_fpc_only) as raw_released_orders_fpc_only,
# MAGIC   SUM(inv.usd_total_plant_stock) as usd_total_plant_stock,
# MAGIC   SUM(inv.usd_stock_in_transit) as usd_stock_in_transit,
# MAGIC   SUM(inv.usd_mrp_available_csp_agg) as usd_mrp_available_csp_agg,
# MAGIC   SUM(inv.usd_quality_inspection) as usd_quality_inspection,
# MAGIC   SUM(inv.usd_unrestricted) as usd_unrestricted,
# MAGIC   SUM(inv.usd_blocked) as usd_blocked,
# MAGIC   SUM(inv.usd_pg_owned_stock) as usd_pg_owned_stock,
# MAGIC   SUM(inv.usd_safety_stock) as usd_safety_stock,
# MAGIC   SUM(inv.usd_maximum_stock) as usd_maximum_stock,
# MAGIC   SUM(inv.usd_released_orders_fpc_only) as usd_released_orders_fpc_only,
# MAGIC   SUM(inv.stdpal_total_plant_stock) as stdpal_total_plant_stock,
# MAGIC   SUM(inv.stdpal_stock_in_transit) as stdpal_stock_in_transit,
# MAGIC   SUM(inv.stdpal_mrp_available_csp_agg) as stdpal_mrp_available_csp_agg,
# MAGIC   SUM(inv.stdpal_quality_inspection) as stdpal_quality_inspection,
# MAGIC   SUM(inv.stdpal_unrestricted) as stdpal_unrestricted,
# MAGIC   SUM(inv.stdpal_blocked) as stdpal_blocked,
# MAGIC   SUM(inv.stdpal_pg_owned_stock) as stdpal_pg_owned_stock,
# MAGIC   SUM(inv.stdpal_safety_stock) as stdpal_safety_stock,
# MAGIC   SUM(inv.stdpal_maximum_stock) as stdpal_maximum_stock,
# MAGIC   SUM(inv.stdpal_released_orders_fpc_only) as stdpal_released_orders_fpc_only,
# MAGIC   SUM(inv.buom_consignment_qi) as buom_consignment_qi,
# MAGIC   SUM(inv.su_consignment_qi) as su_consignment_qi,
# MAGIC   SUM(inv.msu_consignment_qi) as msu_consignment_qi,
# MAGIC   SUM(inv.raw_consignment_qi) as raw_consignment_qi,
# MAGIC   SUM(inv.usd_consignment_qi) as usd_consignment_qi,
# MAGIC   SUM(inv.stdpal_consignment_qi) as stdpal_consignment_qi,
# MAGIC   SUM(inv.buom_consignment_unrestricted) as buom_consignment_unrestricted,
# MAGIC   SUM(inv.su_consignment_unrestricted) as su_consignment_unrestricted,
# MAGIC   SUM(inv.msu_consignment_unrestricted) as msu_consignment_unrestricted,
# MAGIC   SUM(inv.raw_consignment_unrestricted) as raw_consignment_unrestricted,
# MAGIC   SUM(inv.usd_consignment_unrestricted) as usd_consignment_unrestricted,
# MAGIC   SUM(inv.stdpal_consignment_unrestricted) as stdpal_consignment_unrestricted,
# MAGIC   SUM(inv.buom_consignment_blocked) as buom_consignment_blocked,
# MAGIC   SUM(inv.su_consignment_blocked) as su_consignment_blocked,
# MAGIC   SUM(inv.msu_consignment_blocked) as msu_consignment_blocked,
# MAGIC   SUM(inv.raw_consignment_blocked) as raw_consignment_blocked,
# MAGIC   SUM(inv.usd_consignment_blocked) as usd_consignment_blocked,
# MAGIC   SUM(inv.stdpal_consignment_blocked) as stdpal_consignment_blocked,
# MAGIC   SUM(inv.buom_stock_transfer_plant_sloc) as buom_stock_transfer_plant_sloc,
# MAGIC   SUM(inv.su_stock_transfer_plant_sloc) as su_stock_transfer_plant_sloc,
# MAGIC   SUM(inv.msu_stock_transfer_plant_sloc) as msu_stock_transfer_plant_sloc,
# MAGIC   SUM(inv.raw_stock_transfer_plant_sloc) as raw_stock_transfer_plant_sloc,
# MAGIC   SUM(inv.usd_stock_transfer_plant_sloc) as usd_stock_transfer_plant_sloc,
# MAGIC   SUM(inv.stdpal_stock_transfer_plant_sloc) as stdpal_stock_transfer_plant_sloc,
# MAGIC   SUM(inv.site_demand_forecast_week1) as site_demand_forecast_week1,
# MAGIC   SUM(inv.site_demand_forecast_week2) as site_demand_forecast_week2,
# MAGIC   SUM(inv.site_demand_forecast_week3) as site_demand_forecast_week3,
# MAGIC   SUM(inv.site_demand_forecast_week4) as site_demand_forecast_week4,
# MAGIC   SUM(inv.site_demand_forecast_week5) as site_demand_forecast_week5,
# MAGIC   SUM(inv.site_demand_forecast_week6) as site_demand_forecast_week6,
# MAGIC   SUM(inv.site_demand_forecast_week7) as site_demand_forecast_week7,
# MAGIC   SUM(inv.site_demand_forecast_week8) as site_demand_forecast_week8,
# MAGIC   SUM(inv.site_demand_forecast_week26) as site_demand_forecast_week26,
# MAGIC   SUM(inv.network_demand_forecast_week1) as network_demand_forecast_week1,
# MAGIC   SUM(inv.network_demand_forecast_week2) as network_demand_forecast_week2,
# MAGIC   SUM(inv.network_demand_forecast_week3) as network_demand_forecast_week3,
# MAGIC   SUM(inv.network_demand_forecast_week4) as network_demand_forecast_week4,
# MAGIC   SUM(inv.network_demand_forecast_week5) as network_demand_forecast_week5,
# MAGIC   SUM(inv.network_demand_forecast_week6) as network_demand_forecast_week6,
# MAGIC   SUM(inv.network_demand_forecast_week7) as network_demand_forecast_week7,
# MAGIC   SUM(inv.network_demand_forecast_week8) as network_demand_forecast_week8,
# MAGIC   SUM(inv.network_demand_forecast_week26) as network_demand_forecast_week26,
# MAGIC   SUM(inv.mrp_inventory_for_dfc) as mrp_inventory_for_dfc,
# MAGIC   SUM(inv.total_inventory_for_dfc) as total_inventory_for_dfc
# MAGIC FROM
# MAGIC   dp_inventory.inv_fct_emea AS inv
# MAGIC   LEFT JOIN dp_inventory.plant_dim AS plant_d ON inv.plant = plant_d.plant
# MAGIC   JOIN dp_inventory.tdc_val_dim AS tdc_d ON inv.tdc_val = tdc_d.tdc_val
# MAGIC   JOIN dp_inventory.val_class_dim as valclass_d ON inv.valuation_class = valclass_d.valuation_class
# MAGIC WHERE
# MAGIC   inv.COMPLEX_DECOMPOSITION IN ("C", "S")
# MAGIC   AND IFNULL(plant_d.JOINT_VENTURE_FLAG, "") <> "JV"
# MAGIC   AND tdc_d.sector = "F&HC"
# MAGIC   AND tdc_d.subsector = "HOMECARE"
# MAGIC   AND to_date(CAST(inv.calday as string), "yyyyMMdd") = date_add(current_date(), -1) -- yday date
# MAGIC   AND inv.region IN ("EUR", "EUF", "EUE")
# MAGIC GROUP BY
# MAGIC   material_id,
# MAGIC   tdc_d.sector,
# MAGIC   tdc_d.category,
# MAGIC   tdc_d.tdc_val,
# MAGIC   valclass_d.material_type_derived,
# MAGIC   site_id,
# MAGIC   inv.calday

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ADA_hc_stockbalancing_rr 
# MAGIC DROP TABLE IF EXISTS userdb_skora_m_1.ADA_hc_stockbalancing_rr_temp;
# MAGIC CREATE TABLE userdb_skora_m_1.ADA_hc_stockbalancing_rr_temp USING CSV
# MAGIC SELECT
# MAGIC   Site as site_id,
# MAGIC   Part as material_id,
# MAGIC   EAN,
# MAGIC   UOM,
# MAGIC   CASE
# MAGIC     WHEN `Date` = 'Past' THEN date_add(current_date(), -1)
# MAGIC     ELSE `Date`
# MAGIC   END AS `Date`,
# MAGIC   DemandOrders as OO,
# MAGIC   Forecast as FF,
# MAGIC   DependentDemand as DD,
# MAGIC   DistributionDemand,
# MAGIC   ShipNotes,
# MAGIC   FirmProduction,
# MAGIC   FirmReceipts,
# MAGIC   QMLots,
# MAGIC   TotalPlannedSupply,
# MAGIC   Safety,
# MAGIC   DataExtractDate
# MAGIC FROM
# MAGIC   dp_rapidresponse.emea_sca_detail_duedate
# MAGIC where
# MAGIC   Part IN (
# MAGIC     SELECT
# MAGIC       distinct material_id
# MAGIC     FROM
# MAGIC       userdb_skora_m_1.ADA_hc_sog
# MAGIC   )
# MAGIC   and Site IN (
# MAGIC     '4108',
# MAGIC     '4106',
# MAGIC     '4830',
# MAGIC     '4853',
# MAGIC     '4856',
# MAGIC     '4104',
# MAGIC     '4863',
# MAGIC     '8486',
# MAGIC     '9120',
# MAGIC     'A752',
# MAGIC     'A732'
# MAGIC   ) 
# MAGIC   

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS userdb_skora_m_1.ADA_hc_stockbalancing_rr;
# MAGIC CREATE TABLE userdb_skora_m_1.ADA_hc_stockbalancing_rr USING CSV
# MAGIC SELECT * FROM userdb_skora_m_1.ADA_hc_stockbalancing_rr_temp
# MAGIC WHERE CAST(`Date` as Date) < date_add(current_date(),30)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- ADA_hc_stockbalancing_sog 
# MAGIC DROP TABLE IF EXISTS userdb_skora_m_1.ADA_hc_stockbalancing_sog;
# MAGIC CREATE TABLE userdb_skora_m_1.ADA_hc_stockbalancing_sog USING CSV
# MAGIC SELECT
# MAGIC   material_id as material_id,
# MAGIC   site_id as site_id,
# MAGIC   `Date`,
# MAGIC   buom_mrp_available_csp_agg
# MAGIC FROM
# MAGIC   userdb_skora_m_1.ADA_hc_sog
# MAGIC WHERE
# MAGIC   material_type_derived = 'FPC'
# MAGIC   and site_id IN (
# MAGIC     '4108',
# MAGIC     '4106',
# MAGIC     '4830',
# MAGIC     '4853',
# MAGIC     '4856',
# MAGIC     '4104',
# MAGIC     '4863',
# MAGIC     '8486',
# MAGIC     '9120',
# MAGIC     'A752',
# MAGIC     'A732'
# MAGIC   )

# COMMAND ----------

results = spark.sql("SELECT * FROM userdb_skora_m_1.ADA_hc_stockbalancing_sog")

# Convert the Spark DataFrame to a Pandas DataFrame
ada_hc_sb_sog = results.toPandas()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM userdb_skora_m_1.ada_hc_sog

# COMMAND ----------

import pandas as pd

ada_hc_sb_sog['Date'] = pd.to_datetime(ada_hc_sb_sog['Date'], format='%Y%m%d')
ada_hc_sb_sog = ada_hc_sb_sog[['material_id','site_id','buom_mrp_available_csp_agg']]

# Add 'Date' column with today's date
ada_hc_sb_sog['Date'] = pd.Timestamp.now().date() - pd.Timedelta(days=1)

# Rename 'buom_mrp_available_csp_agg' to 'InitialSOG'
ada_hc_sb_sog.rename(columns={'buom_mrp_available_csp_agg': 'InitialSOG'}, inplace=True)

# COMMAND ----------

results = spark.sql("SELECT * FROM userdb_skora_m_1.ADA_hc_stockbalancing_rr")

# Convert the Spark DataFrame to a Pandas DataFrame
ada_hc_sb_rr = results.toPandas()

ada_hc_sb_rr['Date'] = pd.to_datetime(ada_hc_sb_rr['Date'], format='%Y-%m-%d')

# COMMAND ----------

# Extract demand and supply columns
demand_cols = ['OO', 'FF', 'DD', 'DistributionDemand']
supply_cols = ['ShipNotes', 'FirmProduction', 'FirmReceipts', 'QMLots']

# COMMAND ----------

# Unpivoted ada_hc_sb_rr table
ada_hc_sb_rr_unpivoted = pd.melt(ada_hc_sb_rr, id_vars=['material_id', 'site_id', 'Date'],
                                 value_vars=demand_cols + supply_cols,
                                 var_name='KeyFigure', value_name='_values')

# Unpivoted ada_hc_sb_sog table
ada_hc_sb_sog_unpivoted = pd.melt(ada_hc_sb_sog, id_vars=['material_id', 'site_id', 'Date'],
                                 value_vars='InitialSOG',
                                 var_name='KeyFigure', value_name='_values')

# # Replace '0E-18' with 0
ada_hc_sb_rr_unpivoted['_values'] = ada_hc_sb_rr_unpivoted['_values'].replace('0E-18', 0)
ada_hc_sb_sog_unpivoted['_values'] = ada_hc_sb_sog_unpivoted['_values'].replace('0E-18', 0)

# Convert _values column to double data type
ada_hc_sb_rr_unpivoted['_values'] = ada_hc_sb_rr_unpivoted['_values'].astype(float)
ada_hc_sb_sog_unpivoted['_values'] = ada_hc_sb_sog_unpivoted['_values'].astype(float)

# ada_hc_sb_rr_unpivoted['Date'] = ada_hc_sb_rr_unpivoted['Date'].str.lstrip()
# ada_hc_sb_sog_unpivoted['Date'] = ada_hc_sb_sog_unpivoted['Date'].str.lstrip()

# Convert Date column to date only data type
ada_hc_sb_rr_unpivoted['Date'] = pd.to_datetime(ada_hc_sb_rr_unpivoted['Date']).dt.date
ada_hc_sb_sog_unpivoted['Date'] = pd.to_datetime(ada_hc_sb_sog_unpivoted['Date']).dt.date

spark_ada_hc_sb_rr_unpivoted = spark.createDataFrame(ada_hc_sb_rr_unpivoted)
spark_ada_hc_sb_rr_unpivoted.write.mode("overwrite").saveAsTable("userdb_skora_m_1.ada_hc_sb_rr_unpivoted")

spark_ada_hc_sb_sog_unpivoted = spark.createDataFrame(ada_hc_sb_sog_unpivoted)
spark_ada_hc_sb_sog_unpivoted.write.mode("overwrite").saveAsTable("userdb_skora_m_1.ada_hc_sb_sog_unpivoted")

#ada_hc_sb_rr_unpivoted.to_csv(r'C:\Temp\ada_hc_sb_rr_unpivoted.csv', index=False)
#ada_hc_sb_sog_unpivoted.to_csv(r'C:\Temp\ada_hc_sb_sog_unpivoted.csv', index=False)

# Concatenate the two tables vertically
merged_table = pd.concat([ada_hc_sb_sog_unpivoted, ada_hc_sb_rr_unpivoted], ignore_index=True)
merged_table['KeyFigure'] = merged_table['KeyFigure'].astype(str)
merged_table['KeyFigure'] = merged_table['KeyFigure'].str.strip()

# Get today's date
today = pd.Timestamp.now().date()
yday = pd.Timestamp.now().date() - pd.Timedelta(days=1)

# Create a list of dates for calculations
dates_to_calculate = pd.date_range(start=min(merged_table['Date']), end=(today + pd.Timedelta(days=14)), freq='D')
dates_to_calculate = dates_to_calculate.strftime('%Y-%m-%d')

merged_table['Date'] = merged_table['Date'].astype(str)
today = today.strftime('%Y-%m-%d')  # Convert 'today' to string for iteration filtering - otherwise fails
yday = yday.strftime('%Y-%m-%d')  # Convert 'today' to string for iteration filtering - otherwise fails

# COMMAND ----------

initial_sog_values = {}
for _, row in merged_table.loc[(merged_table['KeyFigure'] == 'InitialSOG') & (merged_table['Date'] == yday)].iterrows():
    material_id = row['material_id']
    site_id = row['site_id']
    Date = row['Date']
    initial_sog_values[(material_id, site_id, Date)] = row['_values']


# Calculate Current demand and supply values
curr_demand_values = {}
curr_supply_values = {}
for date in dates_to_calculate:
    # Filter rows in merged_table for the current date and demand_cols + supply_cols
    filtered_rows = merged_table.loc[(merged_table['Date'] == date) & (merged_table['KeyFigure'].isin(demand_cols + supply_cols))]

    # Iterate over filtered_rows and update previous_demand_values and previous_supply_values dictionaries
    for _, row in filtered_rows.iterrows():
        material_id = row['material_id']
        site_id = row['site_id']
        Date = row['Date']
        if row['KeyFigure'] in demand_cols:
            # Initialize the dictionary with default value of 0 if the key is not present
            curr_demand_values.setdefault((material_id, site_id, Date), 0)
            # Sum the demand values for the same material_id, site_id, and Date
            curr_demand_values[(material_id, site_id, Date)] += row['_values']
        elif row['KeyFigure'] in supply_cols:
            # Initialize the dictionary with default value of 0 if the key is not present
            curr_supply_values.setdefault((material_id, site_id, Date), 0)
            # Sum the supply values for the same material_id, site_id, and Date
            curr_supply_values[(material_id, site_id, Date)] += row['_values']

# Copy the dictionaries to preserve original data
initial_sog_values_copy = initial_sog_values.copy()
curr_demand_values_copy = curr_demand_values.copy()
curr_supply_values_copy = curr_supply_values.copy()

# COMMAND ----------

from tqdm import tqdm

# COMMAND ----------

ada_hc_sb_rr_unpivoted = ada_hc_sb_rr_unpivoted.sort_values(by=['material_id', 'site_id'], ascending=[True, True])

# Extract unique material_id and site_id values from ada_hc_sb_rr_unpivoted DataFrame
material_ids = ada_hc_sb_rr_unpivoted['material_id'].unique().tolist()
site_ids = ada_hc_sb_rr_unpivoted['site_id'].unique().tolist()

# Calculate total number of iterations
total_iterations = len(material_ids) * len(site_ids) * (len(dates_to_calculate) - 1)

# Initialize progress bar
progress_bar = tqdm(total=total_iterations, desc='Calculating Initial SOG', unit='iteration')

# Calculate remaining InitialSOG values
for material_id in material_ids:
    for site_id in site_ids:
        for i, date in enumerate(dates_to_calculate):
            if i == 0:
                # Skip calculation for the first date since InitialSOG value is already available
                continue

            # Convert date value to ncvdatetime object
            date = pd.to_datetime(date)

            # Get the InitialSOG value from the previous date
            prev_date = date - pd.Timedelta(days=1)

            # Convert date value to string strftime
            date = date.strftime('%Y-%m-%d')

            # Convert prev_date back to string using strftime
            prev_date = prev_date.strftime('%Y-%m-%d')

            prev_initial_sog = initial_sog_values.get((material_id, site_id, prev_date), 0)

            # Get the current demand and supply values for the previous date
            prev_demand = curr_demand_values.get((material_id, site_id, prev_date), 0)
            prev_supply = curr_supply_values.get((material_id, site_id, prev_date), 0)

            # Calculate the remaining InitialSOG value
            remaining_initial_sog = prev_initial_sog - prev_demand + prev_supply

            # Update the initial_sog_values dictionary with the remaining InitialSOG value for the current date
            initial_sog_values[(material_id, site_id, date)] = remaining_initial_sog

            # Update progress bar
            progress_bar.update(1)
            # print("initial_sog_values after iteration {}: {}".format(i, initial_sog_values))


# Close progress bar
progress_bar.close()


# COMMAND ----------

# Create DataFrames from dictionaries
print('Creating Dataframe from InitialSOG dictionary...')
df_initial_sog = pd.DataFrame(list(initial_sog_values.values()), index=initial_sog_values.keys(), columns=['_Values']).reset_index()
print('Creating Dataframe from Demand dictionary...')
df_curr_demand = pd.DataFrame(list(curr_demand_values.values()), index=curr_demand_values.keys(), columns=['_Values']).reset_index()
print('Creating Dataframe from Supply dictionary...')
df_curr_supply = pd.DataFrame(list(curr_supply_values.values()), index=curr_supply_values.keys(), columns=['_Values']).reset_index()

# Rename columns in df_initial_sog
df_initial_sog = df_initial_sog.rename(columns={'level_0': 'material_id', 'level_1': 'site_id', 'level_2': 'Date'})
df_curr_demand = df_curr_demand.rename(columns={'level_0': 'material_id', 'level_1': 'site_id', 'level_2': 'Date'})
df_curr_supply = df_curr_supply.rename(columns={'level_0': 'material_id', 'level_1': 'site_id', 'level_2': 'Date'})

# Add KeyFigure column to each DataFrame with different values
df_initial_sog['KeyFigure'] = 'InitialSOG'
df_curr_demand['KeyFigure'] = 'TotalDemand'
df_curr_supply['KeyFigure'] = 'TotalSupply'


print('Saving separate InitialSOG from Dataframe to Excel...')
spark_df_initial_sog = spark.createDataFrame(df_initial_sog)
spark_df_initial_sog.write.mode("overwrite").saveAsTable("userdb_skora_m_1.SOG")
#df_initial_sog.to_csv(r'C:\Temp\sog.xlsx', index=False)
print('Saving separate Demand from Dataframe to Excel...')
spark_df_curr_demand = spark.createDataFrame(df_curr_demand)
spark_df_curr_demand.write.mode("overwrite").saveAsTable("userdb_skora_m_1.curr_demand")
#df_curr_demand.to_csv(r'C:\Temp\demand.xlsx', index=False)
print('Saving separate Supply from Dataframe to Excel...')
spark_df_curr_supply = spark.createDataFrame(df_curr_supply)
spark_df_curr_supply.write.mode("overwrite").saveAsTable("userdb_skora_m_1.curr_supply")
#df_curr_supply.to_csv(r'C:\Temp\supply.xlsx', index=False)

# Reset index on each dataframe
df_initial_sog = df_initial_sog.reset_index(drop=True)
df_curr_demand = df_curr_demand.reset_index(drop=True)
df_curr_supply = df_curr_supply.reset_index(drop=True)

# Concatenate all DataFrames into a single merged DataFrame
print('Merging Dataframes...')
df_merged = pd.concat([df_initial_sog, df_curr_demand, df_curr_supply], ignore_index=False)

# Convert 'Date' columns to date only data type and format
df_merged['Date'] = pd.to_datetime(df_merged['Date']).dt.strftime('%Y-%m-%d')

spark_df_merged = spark.createDataFrame(df_merged)
spark_df_merged.write.mode("overwrite").saveAsTable("userdb_skora_m_1.merged_data")
#df_merged.to_csv(r"C:\Users\sureshkumar.s\OneDrive - Procter and Gamble\Desktop\merged_data.csv", index=False)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from userdb_skora_m_1.merged_data

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists userdb_skora_m_1.data_pivoting_test

# COMMAND ----------

merged_data_result=spark.sql('SELECT * FROM userdb_skora_m_1.merged_data')
merged_data=merged_data_result.toPandas()

is_initial_sog = merged_data['KeyFigure'] == 'InitialSOG'
is_total_demand = merged_data['KeyFigure'] == 'TotalDemand'
merged_data_initialsog = merged_data[is_initial_sog][['material_id', 'site_id', 'Date', '_Values']].copy()
merged_data_initialsog.rename(columns={'_Values': 'InitialSOG'}, inplace=True)


demand_pivot = merged_data[is_total_demand].pivot(index=['material_id', 'site_id'], columns='Date', values='_Values').reset_index()
demand_pivot.rename_axis(None, axis=1, inplace=True)

new_merged_df = pd.merge(merged_data_initialsog, demand_pivot, on=['material_id', 'site_id'], how='left')

#new_merged_df['Date'] = pd.to_datetime(new_merged_df['Date'])
date_cols = new_merged_df.columns[4:]
# Update values based on date comparison
for col in date_cols:
    new_merged_df[col] = new_merged_df[col].where(new_merged_df['Date'] <= col, 0)

spark_pivoting = spark.createDataFrame(new_merged_df)
spark_pivoting.write.mode("overwrite").saveAsTable("userdb_skora_m_1.data_pivoting_test")

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists userdb_skora_m_1.DFC_test

# COMMAND ----------

import pandas as pd
import time

start_time = time.time()

merged_data = spark.table("userdb_skora_m_1.data_pivoting_test").toPandas()
#merged_data = pd.read_csv(r"C:\Users\sureshkumar.s\OneDrive - Procter and Gamble\Desktop\data_pivoting.csv")

# Get the date columns
date_cols = merged_data.columns[4:]

# Calculate DFC and DFCc columns
dfc_values = []
excess_values = []
new_values = []
new_dfc_values = []

for index, row in merged_data.iterrows():
    cumulative_sum = 0
    dfc = 0
    excess = 0
    new = 0
    new_dfc = 0
    found_matching_date = False

    for date_col in date_cols:
        if found_matching_date or date_col == row['Date']:
            found_matching_date = True
            value = row[date_col]
            cumulative_sum += value

            if cumulative_sum >= row['InitialSOG']:
                if value != 0:
                    excess = cumulative_sum - row['InitialSOG']
                    new = (value - excess)/value
                    cumulative_sum = row['InitialSOG']
                break

            dfc += 1
            if row['InitialSOG'] == 0: dfc = 0
    new_dfc = dfc + new

    dfc_values.append(dfc)
    excess_values.append(excess)
    new_values.append(new)
    new_dfc_values.append(new_dfc)

# Add DFC and Excess columns to the DataFrame
merged_data['DFC'] = dfc_values
#merged_data['Excess'] = excess_values
#merged_data['Value'] = new_values
merged_data['NewDFC'] = new_dfc_values

# Finish timing and display the result
end_time = time.time()
total_time = end_time - start_time
print("Execution time:", total_time, "seconds.")

spark_DFC= spark.createDataFrame(merged_data)
spark_DFC.write.mode("overwrite").saveAsTable("userdb_skora_m_1.DFC_test")



# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from userdb_skora_m_1.DFC_TEST

# COMMAND ----------

desired_columns = ["material_id", "site_id", "Date", "InitialSOG", "NewDFC"]
merged_data_selected = merged_data[desired_columns]

spark_DFC_without_dates= spark.createDataFrame(merged_data_selected)
spark_DFC_without_dates.write.mode("overwrite").saveAsTable("userdb_skora_m_1.DFC_without_dates")

merged_data_selected

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * from userdb_skora_m_1.DFC_without_dates

# COMMAND ----------


