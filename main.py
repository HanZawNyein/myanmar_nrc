import csv

file_path = "/home/agga/Documents/odoo-dev/odoo_app_store_18/nrc/6NRC_Tanintharyi_Region.csv"


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
            <field name="state_id" ref="ica_mm_nrc.region_tanintharyi"/>
        </record>
""")
