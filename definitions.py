# Constants to use for data tags in the simulation



# Inputs
BATTERY_SIZE_TAG = "Battery Size (kWh)"
BATTERY_CHANGE_CONSTANT_TAG = "Battery Change Constant (minutes)"
MOTOR_MAX_TORQUE_TAG = "Maximum Motor Torque (Nm)"
GROSS_VEHICLE_WEIGHT_TAG = "Gross Vehicle Weight (kg)"
WEIGHT_REDUCTION_TAG = "Weight Reduction (kg)"
COEFFICIENT_OF_DRAG_TAG = "Coefficient of Drag (unitless)"

GWC_TIMES_TAG = "gwc times (minutes)"
WINNING_GAS_CAR_LAPS = "Winning Gas Car Laps"
PIT_DRIVE_THROUGH_PENALTY_TIME = "Time to drive through pits (minutes)"


# This should include everything above
INPUT_VARIABLES = [
    BATTERY_SIZE_TAG, MOTOR_MAX_TORQUE_TAG,
    GROSS_VEHICLE_WEIGHT_TAG, WEIGHT_REDUCTION_TAG,
    COEFFICIENT_OF_DRAG_TAG, BATTERY_CHANGE_CONSTANT_TAG
]

# Relationships
BATTERY_ENERGY_DENSITY_TAG = "Battery Energy Density (kWh/kg)"
BATTERY_MASS_PIT_FACTOR_TAG = "Battery Mass Pit Factor (minutes/kg)"
BATTERY_POWER_OUTPUT_FACT0R_TAG = "Battery Output Factor (W/kWh)"
MOTOR_CONSTANT_TAG = "Motor Constant (Nm/sqrt(W))"
MOTOR_TORQUE_DENSITY_TAG = "Motor Torque Density (Nm/kg)"
MAX_VEHICLE_WEIGHT_RATIO_TAG = "Max Vehicle Weight Ratio (unitless)"
CAR_DENSITY_TAG = "Car Density (kg/m^3)"
CHASSIS_BATTERY_MASS_FACTOR_TAG = "Chassis Battery Mass Factor (kg/kg)"
CHASSIS_MOTOR_MASS_FACTOR_TAG = "Chassis Motor Mass Factor (kg/kg)"
ROLLING_RESISTANCE_MASS_FACTOR_TAG = "Rolling Resistance Mass Factor (1/kg)"

RELATIONSHIP_VARIABLES = [
    BATTERY_ENERGY_DENSITY_TAG, BATTERY_MASS_PIT_FACTOR_TAG,
    BATTERY_POWER_OUTPUT_FACT0R_TAG,
    MOTOR_CONSTANT_TAG, MOTOR_TORQUE_DENSITY_TAG,
    MAX_VEHICLE_WEIGHT_RATIO_TAG, CAR_DENSITY_TAG,
    CHASSIS_BATTERY_MASS_FACTOR_TAG,
    CHASSIS_MOTOR_MASS_FACTOR_TAG,
    ROLLING_RESISTANCE_MASS_FACTOR_TAG
]


# Results/outputs
ITER_TAG = "Iteration"
VEHICLE_TAG = "Vehicle Name"
TOTAL_LAPS_TAG = "Total Laps Completed"
LAPTIME_TAG = "Laptime (s)"
LAP_ENERGY_TAG = "Engery Per Lap (kJ)"
BATTERY_MASS_TAG = "Battery Mass (kg)"
PIT_TIME_TAG = "Pit Time (minutes)"
TOTAL_PITS_TAG = "total Number of Pits"
MOTOR_MASS_TAG = "Motor Mass (kg)"
MOTOR_MAX_POWER_TAG = "Motor Maximum Power (W)"
NET_CHASSIS_MASS_TAG = "Net Chassis Mass (kg)"
TOTAL_VEHICLE_MASS_TAG = "Total Vehicle Mass (kg)"
MAXIMUM_ALLOWABLE_VEHICLE_MASS_TAG = "Maximum Allowable Vehicle Mass (kg)"
FRONTAL_AREA_TAG = "Frontal Area (m^2)"
C_W_A_TAG = "c_w_a (m^2)"
ROLLING_RESISTANCE_TAG = "Rolling Resistance Coefficient (unitless)"

ENERGY_REMAINING_TAG = "Energy Remaining (sum of %)"

WINNING_ELECTRIC_CAR_TAG = "Does this electric car win? (bool)"

HEADER_ROW = [
    ITER_TAG, VEHICLE_TAG, TOTAL_LAPS_TAG, LAPTIME_TAG,
    LAP_ENERGY_TAG, BATTERY_MASS_TAG, PIT_TIME_TAG,
    TOTAL_PITS_TAG, ENERGY_REMAINING_TAG,
    MOTOR_MASS_TAG, MOTOR_MAX_POWER_TAG, NET_CHASSIS_MASS_TAG,
    TOTAL_VEHICLE_MASS_TAG, MAXIMUM_ALLOWABLE_VEHICLE_MASS_TAG,
    FRONTAL_AREA_TAG, BATTERY_SIZE_TAG, MOTOR_MAX_TORQUE_TAG,
    GROSS_VEHICLE_WEIGHT_TAG, WEIGHT_REDUCTION_TAG,
    COEFFICIENT_OF_DRAG_TAG, BATTERY_ENERGY_DENSITY_TAG,
    BATTERY_MASS_PIT_FACTOR_TAG, MOTOR_CONSTANT_TAG,
    MOTOR_TORQUE_DENSITY_TAG,
    MAX_VEHICLE_WEIGHT_RATIO_TAG, CAR_DENSITY_TAG,
    CHASSIS_BATTERY_MASS_FACTOR_TAG, CHASSIS_MOTOR_MASS_FACTOR_TAG,
    ROLLING_RESISTANCE_MASS_FACTOR_TAG, C_W_A_TAG,
    ROLLING_RESISTANCE_TAG, GWC_TIMES_TAG, BATTERY_POWER_OUTPUT_FACT0R_TAG,
    WINNING_ELECTRIC_CAR_TAG, PIT_DRIVE_THROUGH_PENALTY_TIME, BATTERY_CHANGE_CONSTANT_TAG,
    WINNING_GAS_CAR_LAPS
]

# All tags except the outputs/results
REQUIRED_INPUTS = [
    BATTERY_SIZE_TAG, MOTOR_MAX_TORQUE_TAG,
    GROSS_VEHICLE_WEIGHT_TAG, WEIGHT_REDUCTION_TAG,
    COEFFICIENT_OF_DRAG_TAG, BATTERY_ENERGY_DENSITY_TAG,
    BATTERY_MASS_PIT_FACTOR_TAG, MOTOR_CONSTANT_TAG,
    MOTOR_TORQUE_DENSITY_TAG,
    MAX_VEHICLE_WEIGHT_RATIO_TAG, CAR_DENSITY_TAG,
    CHASSIS_BATTERY_MASS_FACTOR_TAG, CHASSIS_MOTOR_MASS_FACTOR_TAG,
    ROLLING_RESISTANCE_MASS_FACTOR_TAG, BATTERY_POWER_OUTPUT_FACT0R_TAG,
    BATTERY_CHANGE_CONSTANT_TAG
]