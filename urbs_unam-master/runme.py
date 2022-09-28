import os
import shutil
import urbs
from itertools import chain


input_files = 'Input'
result_name = 'MEXICO_model'
result_dir = urbs.prepare_result_directory(result_name)  # name + time stamp

# copy input file to result directory
try:
    shutil.copytree(input_files, os.path.join(result_dir, 'Input'))
except NotADirectoryError:
    shutil.copyfile(input_files, os.path.join(result_dir, input_files))
# copy runme.py to result directory
shutil.copy(__file__, result_dir)

# objective function
objective = 'cost' # set either 'cost' or 'CO2' as objective

# Choose Solver (cplex, glpk, gurobi, ...)
solver = 'gurobi'

# simulation timesteps
(offset, length) = (3480, 168)  # time step selection
timesteps = range(offset, offset+length+1)
dt = 1  # length of each time step (unit: hours)


# detailed reporting commodity/sites
report_tuples = [
    (2019, 'Central', 'Elec'),
    (2019, 'Oriental', 'Elec'),
    (2019, 'Occidental', 'Elec'),
    (2019, 'Noroeste', 'Elec'),
    (2019, 'Norte', 'Elec'),
    (2019, 'Noreste', 'Elec'),
    (2019, 'Baja_California', 'Elec'),
    (2019, 'Baja_California_Sur', 'Elec'),
    (2019, 'Peninsular', 'Elec'),
    (2019, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2030, 'Central', 'Elec'),
    (2030, 'Oriental', 'Elec'),
    (2030, 'Occidental', 'Elec'),
    (2030, 'Noroeste', 'Elec'),
    (2030, 'Norte', 'Elec'),
    (2030, 'Noreste', 'Elec'),
    (2030, 'Baja_California', 'Elec'),
    (2030, 'Baja_California_Sur', 'Elec'),
    (2030, 'Peninsular', 'Elec'),
    (2030, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2040, 'Central', 'Elec'),
    (2040, 'Oriental', 'Elec'),
    (2040, 'Occidental', 'Elec'),
    (2040, 'Noroeste', 'Elec'),
    (2040, 'Norte', 'Elec'),
    (2040, 'Noreste', 'Elec'),
    (2040, 'Baja_California', 'Elec'),
    (2040, 'Baja_California_Sur', 'Elec'),
    (2040, 'Peninsular', 'Elec'),
    (2040, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2050, 'Central', 'Elec'),
    (2050, 'Oriental', 'Elec'),
    (2050, 'Occidental', 'Elec'),
    (2050, 'Noroeste', 'Elec'),
    (2050, 'Norte', 'Elec'),
    (2050, 'Noreste', 'Elec'),
    (2050, 'Baja_California', 'Elec'),
    (2050, 'Baja_California_Sur', 'Elec'),
    (2050, 'Peninsular', 'Elec'),
    (2050, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),      
    ]

# optional: define names for sites in report_tuples
report_sites_name = {('Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'): 'All'}

# plotting commodities/sites
plot_tuples = [
    (2019, 'Central', 'Elec'),
    (2019, 'Oriental', 'Elec'),
    (2019, 'Occidental', 'Elec'),
    (2019, 'Noroeste', 'Elec'),
    (2019, 'Norte', 'Elec'),
    (2019, 'Noreste', 'Elec'),
    (2019, 'Baja_California', 'Elec'),
    (2019, 'Baja_California_Sur', 'Elec'),
    (2019, 'Peninsular', 'Elec'),
    (2019, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2030, 'Central', 'Elec'),
    (2030, 'Oriental', 'Elec'),
    (2030, 'Occidental', 'Elec'),
    (2030, 'Noroeste', 'Elec'),
    (2030, 'Norte', 'Elec'),
    (2030, 'Noreste', 'Elec'),
    (2030, 'Baja_California', 'Elec'),
    (2030, 'Baja_California_Sur', 'Elec'),
    (2030, 'Peninsular', 'Elec'),
    (2030, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2040, 'Central', 'Elec'),
    (2040, 'Oriental', 'Elec'),
    (2040, 'Occidental', 'Elec'),
    (2040, 'Noroeste', 'Elec'),
    (2040, 'Norte', 'Elec'),
    (2040, 'Noreste', 'Elec'),
    (2040, 'Baja_California', 'Elec'),
    (2040, 'Baja_California_Sur', 'Elec'),
    (2040, 'Peninsular', 'Elec'),
    (2040, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2050, 'Central', 'Elec'),
    (2050, 'Oriental', 'Elec'),
    (2050, 'Occidental', 'Elec'),
    (2050, 'Noroeste', 'Elec'),
    (2050, 'Norte', 'Elec'),
    (2050, 'Noreste', 'Elec'),
    (2050, 'Baja_California', 'Elec'),
    (2050, 'Baja_California_Sur', 'Elec'),
    (2050, 'Peninsular', 'Elec'),
    (2050, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),      
    ]

# optional: define names for sites in plot_tuples
plot_sites_name = {('Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'): 'All'}

plot_data=[]
for x in timesteps:
    plot_data.append(x)
    
# plotting timesteps
plot_periods = {
    'all': timesteps[1:72],
    'all_2': timesteps[-72:-1]

}

# add or change plot colors
my_colors = {
    'Central': (230, 200, 200),
    'Oriental': (200, 230, 200),
    'Occidental': (200, 230, 230),
    'Noroeste': (100, 130, 100),
    'Norte': (100, 130, 100),
    'Noreste': (100, 100, 130),
    'Baja_California': (180, 150, 150),
    'Baja_California_Sur': (150, 180, 150),
    'Peninsular': (150, 150, 180)}
for country, color in my_colors.items():
    urbs.COLORS[country] = color

# select scenarios to be run
scenarios = [
             urbs.scenario_base,
             #urbs.scenario_stock_prices,
             #urbs.scenario_co2_limit,
             #urbs.scenario_co2_tax_mid,
             #urbs.scenario_no_dsm,
             #urbs.scenario_north_process_caps,
             #urbs.scenario_all_together
            ]

for scenario in scenarios:
    prob = urbs.run_scenario(input_files, solver, timesteps, scenario, 
                        result_dir, dt, objective, 
                        plot_tuples=plot_tuples,
                        plot_sites_name=plot_sites_name,
                        plot_periods=plot_periods,
                        report_tuples=report_tuples,
                        report_sites_name=report_sites_name)
