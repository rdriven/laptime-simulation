This file outlines how the parameters in the vehicle parameters files and how to construct
and use the parameter files.

The files are constructed using toml syntax: https://toml.io/en/v1.0.0

The parameters in these files are a combination of parameters that were in the original .ini 
files and some additional parametesr that we have added in.

Notes about the parameters:

- The way most of the parameters is handled is how the parameter car_model_type
  - There are 2 possible values "static" or "dynamic"
  - If the value is "static" then the parameters in the file need to be different than if it is "dynamic"
  - The names "static" and "dynamic" refer to how the size of the motor, and car chassis are calculated
  - If the value is "static" then you specify the parameters of the chassis and motor directly
  - If the value is "dynamic" then chassis and motor parameters are calculated indirectly with other specified parameters such as 'motor_constant'.

- Any paramater can be either a single value or a range of values except a few params listed below
- If you want the paramater to be a range of values then it should take the form:
    [min_value, max_value, number_of_steps] 
    all values must be doubles (add a ".0" after any whole number) this is to work with the python toml library
    the number_of_steps must be a whole number > 1, ex: 3.0, 9.0
    examples: [12.34, 25.0, 6.0] or [0.0003, 0.0004, 55.0]
- exceptions, these parameters must not take this form:
    these I decided would be too complex to have a range of values for now and the 
    simulation doesn't support it
  - "car_model_type" must be a string
  - "powertrain_type" must be a string
  - "engine.topology" must be a string 
  - "gearbox.i_trans" must be a list and represents the gear ratios for the transmission, only one set of
        gear ratios are allowed in the config at a time
  - "gearbox.n_shift" must a list same lenght of "gearbosx.i_trans"
       same rational as "gearbox.i_trans"
  - "gearbox.e_i" same as "gearbox.i_trans" and "gearbox.n_shift"
!! Do keep in mind that every combination of paramaters through all ranges
will be executed so the number of iterations can quickly be very high!!

If the car_model_type is "dynamic" then these are the parameters: 
car property options -----------------------------------------
The values here are reperesentative of the car model defined in the following
references and are used in the race_car_model.py file:
https://docs.google.com/presentation/d/1Fe2ebMumncOxJ_XGSEA_o8PTu6qjORcLRfJFTbei6lo/edit#slide=id.p
https://docs.google.com/document/d/1X2Aovz6VcKqkIUcsu5Z-QPbyDjBc7IG8CdWpZJr58eI/edit#


vehicle parameters ----------------------------------------------------------------------------------------------------------------------

car_model_type                "static" or "dynamic"
powertrain_type:              electric, hybrid, combustion

lf:                           [m] x distance front axle to center of gravity
lr:                           [m] x distance rear axle to center of gravity
h_cog:                        [m] height of center of gravity
sf:                           [m] track width front
sr:                           [m] track width rear
m: NOT USED                           [kg] vehicle mass inlcuding driver excluding fuel (FE minimum 880kg)
f_roll:  NOT USED                     [-] rolling resistance coefficient
c_w_a:   NOT USED                     [m^2] c_w * A_car -> air resistance calculation
c_z_a_f:                      [m^2] c_z_f * A_frontwing
c_z_a_r:                      [m^2] c_z_r * A_rearwing
g:                            [m/s^2]
rho_air:                      [kg/m^3] air density
drs_factor:                   [-] part of reduction of air resistance by DRS
coefficient_of_drag           [-] coefficient of drag
vehicle_curb_mass             [kg] vehicle curb mass according to manufacturer
mass_reduction                [kg] mass removed to make it a racecar! 
chassis_motor_mass_factor     [kg/kg] mass added to chassis to support the motor mass
chassis_battery_mass_factor   [kg/kg] mass added to chassis to support the battery mass
car_density                   [kg/m^3] vehicle density, used to calculate frontal area
max_vehicle_weight_ratio      [-] maximum vehicle weight ratio allowed by rules 
rolling_resistance_mass_factor [1/kg] rolling resistance scaling with vehicle mass


battery_size:                 [kWh] battery size
battery_energy_density        [kWh/kg] energy storage per mass
battery_change_constant       [minutes] constant time penalty for replacing battery
battery_mass_pit_factor       [minutes/kg] time added to pit time per kg of battery mass
battery_power_output_factor   [W/kWh] maximum power output of battery per kWh of storage

topology:                     [-] RWD or AWD or FWD
pow_e_motor:  NOT USED                [W] total electric motor power (after efficiency losses)
eta_e_motor:                  [-] efficiency electric motor (drive)
eta_e_motor_re:               [-] efficiency electric motor (recuperation)
torque_e_motor_max:   VARIABLE RENAMED        [Nm] maximum torque of electric motor (after efficiency losses)
motor_max_torque              [Nm] maximum torque delivered at output shaft of motor
motor_constant                [Nm/sqrt(W)] motor constant
motor_torque_density          [Nm/kg] Amount of torque supplied per kg of motor mass

keep attention on the direction of the values, i.e. i_trans is from tire to engine!
i_trans:                      [-] gear ratio
n_shift:                      [1/min] shift rpm
e_i:                          [-] torsional mass factor
eta_g:                        [-] efficiency of gearbox/transmission

tire data should be normalized to mu = 1.0 (coefficient of friction of the track / tire test bench)
circ_ref:                     [m] loaded reference circumreference
fz_0:                         [N] nominal tire load
mux:                          [-] corresponds to the coefficient of friction at nominal tire load (fz == fz_0)
muy:                          [-] corresponds to the coefficient of friction at nominal tire load (fz == fz_0)
dmux_dfz:                     [-] reduction of force potential with rising tire load (fz > fz_0) -> negative value!
dmuy_dfz:                     [-] reduction of force potential with rising tire load (fz > fz_0) -> negative value!
tire_model_exp:               [-] exponent used in the tire model to adjust shape of friction "circle" -> [1.0, 2.0]


If the car_model_type is "static" then these are the parameters:

car_model_type: "static"
powertrain_type:              electric, always must be electric

lf:                           [m] x distance front axle to center of gravity
lr:                           [m] x distance rear axle to center of gravity
h_cog:                        [m] height of center of gravity
sf:                           [m] track width front
sr:                           [m] track width rear
m: NOT USED                           [kg] vehicle mass inlcuding driver excluding fuel (FE minimum 880kg)
f_roll:                       [-] rolling resistance coefficient
c_w_a:   NOT USED                     [m^2] c_w * A_car -> air resistance calculation
c_z_a_f:                      [m^2] c_z_f * A_frontwing
c_z_a_r:                      [m^2] c_z_r * A_rearwing
g:                            [m/s^2]
rho_air:                      [kg/m^3] air density
drs_factor:                   [-] part of reduction of air resistance by DRS
coefficient_of_drag           [-] coefficient of drag
frontal_area:                 [m^2] frontal area of the car
vehicle_curb_mass             [kg] vehicle curb mass according to manufacturer
mass_reduction                [kg] mass removed to make it a racecar! 
max_vehicle_weight_ratio      [-] maximum vehicle weight ratio allowed by rules 

battery_size:                 [kWh] battery size
battery_energy_density        [kWh/kg] energy storage per mass
battery_change_constant       [minutes] constant time penalty for replacing battery
battery_mass_pit_factor       [minutes/kg] time added to pit time per kg of battery mass
battery_power_output_factor   [W/kWh] maximum power output of battery per kWh of storage

topology:                     [-] RWD or AWD or FWD
pow_e_motor:                  [W] total electric motor power (after efficiency losses)
eta_e_motor:                  [-] efficiency electric motor (drive)
eta_e_motor_re:               [-] efficiency electric motor (recuperation)
torque_e_motor_max:   VARIABLE RENAMED        [Nm] maximum torque of electric motor (after efficiency losses)
motor_max_torque              [Nm] maximum torque delivered at output shaft of motor

keep attention on the direction of the values, i.e. i_trans is from tire to engine!
i_trans:                      [-] gear ratio
n_shift:                      [1/min] shift rpm
e_i:                          [-] torsional mass factor
eta_g:                        [-] efficiency of gearbox/transmission

tire data should be normalized to mu = 1.0 (coefficient of friction of the track / tire test bench)
circ_ref:                     [m] loaded reference circumreference
fz_0:                         [N] nominal tire load
mux:                          [-] corresponds to the coefficient of friction at nominal tire load (fz == fz_0)
muy:                          [-] corresponds to the coefficient of friction at nominal tire load (fz == fz_0)
dmux_dfz:                     [-] reduction of force potential with rising tire load (fz > fz_0) -> negative value!
dmuy_dfz:                     [-] reduction of force potential with rising tire load (fz > fz_0) -> negative value!
tire_model_exp:               [-] exponent used in the tire model to adjust shape of friction "circle" -> [1.0, 2.0]