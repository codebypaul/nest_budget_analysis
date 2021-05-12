import psycopg2
import os
DB_HOST = 'localhost'
DB_NAME = 'nest_homes'
DB_USER = 'paul'
DB_PASS = '236Raceway'

conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)

# cur = conn.cursor()
class Database:
    def __init__(self,db):
        self.conn = conn
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS nest_budgets (id INTEGER PRIMARY KEY, prop_code text, plan text, date date, lot_cost integer, permits float, tap_fees float,surveying float,engineering float,soil_compaction_testing float, utilities float, dumpster float,portable_toilet float, street_clean float, rough_grade_clearing float, temp_drive float,erosion_sediment_control float, termite_pretreat float,sewer_water_connections float,gravel_fill float,septic float, 	footing float,foundation float,	overages float,interior_slabs float, water_proofing float, brick_stone float,framing_material float,framing_labor float,framing_additional float, stairs float, temp_stairs_total float, windows float, doors float, plumbing_rough float,plumbing_fixtures float, hvac float, electrical float,electrical_fixtures float,av_security float, fireplace float, roofing_shingle float, roofing_metal float,energy_efficiency_testing float, insulation float,drywall_material float, drywall_labor float, siding float,shutters float, decks_porches float,exterior_paint float,garage_door float,interior_trim_material float,	interior_trim_labor float,cabinets float,bench_seat float,countertops float,fireplace_mantel float,appliances float,interior_paint float,door_hardware float, shelving float,shower_doors float, bath_accessories float, mirrors float,tile float, carpet float, hardwood_turnkey float,gutters_downspouts float,mailbox float,lead_walk float,public_walk float,driveway float,landscaping float, docks float, seawalls float, construction_clean float,	pressure_wash float,punchwork float)")
        
        with open('../../../Documents/Nest_Docs/DataBasing/Nest_Budgets.csv','r') as f:
            next(f)
            self.cur.copy_from(f,'nest_budgets',sep=', ')

        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def fetch_one(self,):
        self.cur.execute("SELECT * FROM nest_budgets WHERE prop_code = ?")
        rows = self.cur.fetchall()
        return rows

    # def insert(self,part,customer,retailer,price):
    #     self.cur.execute("INSERT INTO parts VALUE (NULL, ?,?,?,?)",(part,customer,retailer,price))
    #     self.conn.commit()

    # def remove(self,id):
    #     self.cur.execute("DELETE FROM parts WHERE id=?",(id,))
    #     self.conn.commit()

    # def update(self,id,part,customer,retailer,price):
    #     self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer =  ?, price = ?WHERE id = ?", (part,customer,retailer,price,id))
    #     self.conn.commit()

    # def __del__(self):
    #     self.conn.close()

class ActDatabase:
    def __init__(self,db):
        self.conn = conn
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS nest_actuals (id INTEGER PRIMARY KEY, prop_code text, plan text, date date, lot_cost integer, permits float, tap_fees float,surveying float,engineering float,soil_compaction_testing float, utilities float, dumpster float,portable_toilet float, street_clean float, rough_grade_clearing float, temp_drive float,erosion_sediment_control float, termite_pretreat float,sewer_water_connections float,gravel_fill float,septic float, 	footing float,foundation float,	overages float,interior_slabs float, water_proofing float, brick_stone float,framing_material float,framing_labor float,framing_additional float, stairs float, temp_stairs_total float, windows float, doors float, plumbing_rough float,plumbing_fixtures float, hvac float, electrical float,electrical_fixtures float,av_security float, fireplace float, roofing_shingle float, roofing_metal float,energy_efficiency_testing float, insulation float,drywall_material float, drywall_labor float, siding float,shutters float, decks_porches float,exterior_paint float,garage_door float,interior_trim_material float,	interior_trim_labor float,cabinets float,bench_seat float,countertops float,fireplace_mantel float,appliances float,interior_paint float,door_hardware float, shelving float,shower_doors float, bath_accessories float, mirrors float,tile float, carpet float, hardwood_turnkey float,gutters_downspouts float,mailbox float,lead_walk float,public_walk float,driveway float,landscaping float, docks float, seawalls float, construction_clean float,	pressure_wash float,punchwork float)")
        
        self.conn.commit()

db=Database('budget.db')
db=ActDatabase('act.db')
# permits, tap_fees ,surveying,engineering,soil_compaction_testing, utilities,dumpster,portable_toilet,street_clean,rough_grade_clearing,temp_drive,erosion_sediment_control,termite_pretreat,sewer_water_connections,gravel_fill,septic, 	footing,foundation,	overages,interior_slabs,water_proofing,brick_stone,framing_material,framing_labor,framing_additional,	stairs,temp_stairs_total,windows,doors,plumbing_rough,plumbing_fixtures,hvac,electrical,electrical_fixtures,av_security, fireplace,roofing_shingle,roofing_metal,energy_efficiency_testing,	insulation,drywall_material,drywall_labor,siding,shutters,decks_porches,exterior_paint,garage_door,interior_trim_material,	interior_trim_labor,cabinets,bench_seat,countertops,fireplace_mantel,appliances,interior_paint,door_hardware,	shelving,shower_doors,bath_accessories,mirrors,tile,carpet,  	hardwood_turnkey,gutters_downspouts,mailbox,lead_walk,public_walk,driveway,landscaping,docks,seawalls, construction_clean,	pressure_wash,punchwork