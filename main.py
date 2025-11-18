import csv

org_path = "/home/agga/Documents/odoo-dev/odoo_app_store_18/myanmar_nrc/nrc/"

Region7Bago=f"{org_path}7NRC_Bago_Region.csv"
Region8Magway = f"{org_path}/8NRC_Magway_Region.csv"
Region9NRC_Naypyidaw_Union_Territory = f"{org_path}/9NRC_Naypyidaw_Union_Territory.csv"
Region1Mandalay = f"{org_path}/10NRC_Mandalay_Region.csv"
State10Mon = f"{org_path}/10NRC_Mon_State.csv"
State11Rakhine = f"{org_path}/11NRC_Rakhine_State.csv"
Region12Yangon= f"{org_path}/12NRC_Yangon_Region.csv"

State13Shan_State_South= f"{org_path}/13NRC_Shan_State_South.csv"
State13Shan_State_North= f"{org_path}/13NRC_Shan_State_North.csv"
State13Shan_State_East= f"{org_path}/13NRC_Shan_State_East.csv"

Region14Ayeyarwady= f"{org_path}/14NRC_Ayeyarwady_Region.csv"

file_path = Region14Ayeyarwady


with open(file_path, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        township_name = row[3]
        township_lower = row[3].lower()
        code = row[6]
        # print(township_lower, township_name, code)
        # print(row)
        print(f"""
<record id="township_{township_lower}" model="res.country.state.township">
            <field name="name">{township_name}</field>
            <field name="code">{code}</field>
            <field name="state_id" ref="ica_mm_nrc.region_ayeyarwady"/>
        </record>
""")
