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
    (2024, 'Central', 'Elec'),
    (2024, 'Oriental', 'Elec'),
    (2024, 'Occidental', 'Elec'),
    (2024, 'Noroeste', 'Elec'),
    (2024, 'Norte', 'Elec'),
    (2024, 'Noreste', 'Elec'),
    (2024, 'Baja_California', 'Elec'),
    (2024, 'Baja_California_Sur', 'Elec'),
    (2024, 'Peninsular', 'Elec'),
    (2024, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2029, 'Central', 'Elec'),
    (2029, 'Oriental', 'Elec'),
    (2029, 'Occidental', 'Elec'),
    (2029, 'Noroeste', 'Elec'),
    (2029, 'Norte', 'Elec'),
    (2029, 'Noreste', 'Elec'),
    (2029, 'Baja_California', 'Elec'),
    (2029, 'Baja_California_Sur', 'Elec'),
    (2029, 'Peninsular', 'Elec'),
    (2029, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2034, 'Central', 'Elec'),
    (2034, 'Oriental', 'Elec'),
    (2034, 'Occidental', 'Elec'),
    (2034, 'Noroeste', 'Elec'),
    (2034, 'Norte', 'Elec'),
    (2034, 'Noreste', 'Elec'),
    (2034, 'Baja_California', 'Elec'),
    (2034, 'Baja_California_Sur', 'Elec'),
    (2034, 'Peninsular', 'Elec'),
    (2034, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2019, 'Central', 'Gas'),
    (2019, 'Oriental', 'Gas'),
    (2019, 'Occidental', 'Gas'),
    (2019, 'Noroeste', 'Gas'),
    (2019, 'Norte', 'Gas'),
    (2019, 'Noreste', 'Gas'),
    (2019, 'Baja_California', 'Gas'),
    (2019, 'Baja_California_Sur', 'Gas'),
    (2019, 'Peninsular', 'Gas'),
    (2019, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Gas'),
    (2024, 'Central', 'Gas'),
    (2024, 'Oriental', 'Gas'),
    (2024, 'Occidental', 'Gas'),
    (2024, 'Noroeste', 'Gas'),
    (2024, 'Norte', 'Gas'),
    (2024, 'Noreste', 'Gas'),
    (2024, 'Baja_California', 'Gas'),
    (2024, 'Baja_California_Sur', 'Gas'),
    (2024, 'Peninsular', 'Gas'),
    (2024, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Gas'),
    (2029, 'Central', 'Gas'),
    (2029, 'Oriental', 'Gas'),
    (2029, 'Occidental', 'Gas'),
    (2029, 'Noroeste', 'Gas'),
    (2029, 'Norte', 'Gas'),
    (2029, 'Noreste', 'Gas'),
    (2029, 'Baja_California', 'Gas'),
    (2029, 'Baja_California_Sur', 'Gas'),
    (2029, 'Peninsular', 'Gas'),
    (2029, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Gas'),
    (2034, 'Central', 'Gas'),
    (2034, 'Oriental', 'Gas'),
    (2034, 'Occidental', 'Gas'),
    (2034, 'Noroeste', 'Gas'),
    (2034, 'Norte', 'Gas'),
    (2034, 'Noreste', 'Gas'),
    (2034, 'Baja_California', 'Gas'),
    (2034, 'Baja_California_Sur', 'Gas'),
    (2034, 'Peninsular', 'Gas'),
    (2034, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Gas'),      
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
    (2024, 'Central', 'Elec'),
    (2024, 'Oriental', 'Elec'),
    (2024, 'Occidental', 'Elec'),
    (2024, 'Noroeste', 'Elec'),
    (2024, 'Norte', 'Elec'),
    (2024, 'Noreste', 'Elec'),
    (2024, 'Baja_California', 'Elec'),
    (2024, 'Baja_California_Sur', 'Elec'),
    (2024, 'Peninsular', 'Elec'),
    (2024, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2029, 'Central', 'Elec'),
    (2029, 'Oriental', 'Elec'),
    (2029, 'Occidental', 'Elec'),
    (2029, 'Noroeste', 'Elec'),
    (2029, 'Norte', 'Elec'),
    (2029, 'Noreste', 'Elec'),
    (2029, 'Baja_California', 'Elec'),
    (2029, 'Baja_California_Sur', 'Elec'),
    (2029, 'Peninsular', 'Elec'),
    (2029, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2034, 'Central', 'Elec'),
    (2034, 'Oriental', 'Elec'),
    (2034, 'Occidental', 'Elec'),
    (2034, 'Noroeste', 'Elec'),
    (2034, 'Norte', 'Elec'),
    (2034, 'Noreste', 'Elec'),
    (2034, 'Baja_California', 'Elec'),
    (2034, 'Baja_California_Sur', 'Elec'),
    (2034, 'Peninsular', 'Elec'),
    (2034, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Elec'),
    (2019, 'Central', 'Gas'),
    (2019, 'Oriental', 'Gas'),
    (2019, 'Occidental', 'Gas'),
    (2019, 'Noroeste', 'Gas'),
    (2019, 'Norte', 'Gas'),
    (2019, 'Noreste', 'Gas'),
    (2019, 'Baja_California', 'Gas'),
    (2019, 'Baja_California_Sur', 'Gas'),
    (2019, 'Peninsular', 'Gas'),
    (2019, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Gas'),
    (2024, 'Central', 'Gas'),
    (2024, 'Oriental', 'Gas'),
    (2024, 'Occidental', 'Gas'),
    (2024, 'Noroeste', 'Gas'),
    (2024, 'Norte', 'Gas'),
    (2024, 'Noreste', 'Gas'),
    (2024, 'Baja_California', 'Gas'),
    (2024, 'Baja_California_Sur', 'Gas'),
    (2024, 'Peninsular', 'Gas'),
    (2024, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Gas'),
    (2029, 'Central', 'Gas'),
    (2029, 'Oriental', 'Gas'),
    (2029, 'Occidental', 'Gas'),
    (2029, 'Noroeste', 'Gas'),
    (2029, 'Norte', 'Gas'),
    (2029, 'Noreste', 'Gas'),
    (2029, 'Baja_California', 'Gas'),
    (2029, 'Baja_California_Sur', 'Gas'),
    (2029, 'Peninsular', 'Gas'),
    (2029, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Gas'),
    (2034, 'Central', 'Gas'),
    (2034, 'Oriental', 'Gas'),
    (2034, 'Occidental', 'Gas'),
    (2034, 'Noroeste', 'Gas'),
    (2034, 'Norte', 'Gas'),
    (2034, 'Noreste', 'Gas'),
    (2034, 'Baja_California', 'Gas'),
    (2034, 'Baja_California_Sur', 'Gas'),
    (2034, 'Peninsular', 'Gas'),
    (2034, ['Central', 'Oriental', 'Occidental', 'Noroeste', 'Norte', 'Noreste', 'Baja_California', 'Baja_California_Sur', 'Peninsular'], 'Gas'),      
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
