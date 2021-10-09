# battery model
import numpy as np

class battery():
    """Class of a simple battery pack. The battery
    pack is treated as a single unit, individual cell
    properties is not considered. 
    
    This battery model assumes that the output voltage
    does not vary based on percent charge.
    
    This module is intended to be used in the following way:
    1. Initialize the class
    2. Set the static values initialized in the __init__ function
    When running the lap simulation:
    3. To determine the power supplied by the capacitor during a step run the 
       calculate_actual_battery_power function
    4. After the step has been executed run the calculate_energy_values function
       to calculate the energy values. This should be done before running the 
       calculate_actual_battery_power function for the next step, though it 
       could be done all after the simulation is run because in the model
       the power output of the battery does not depend on the energy state of the battery
       
    After the lap is done there are power, energy, and temperature arrays
    that are available to use for analysis."""

    def __init__(self, number_of_points, capacity, max_discharge_rate,
                 max_charge_rate, voltage, internal_resistance,
                 thermal_mass, thermal_resistance, thermal_rejection_temp,
                 maximum_temperature, initial_temp):
        """Initialize the battery model.
        
        Inputs:
            - number_of_points (int): number of points along track, closed!
            
        """
        self.capacity = capacity  # kWh, capacity of battery
        self.max_discharge_rate = max_discharge_rate  # Watts, max output of battery
        self.max_charge_rate = max_charge_rate  # Watts, SHOULD BE NEGATIVE max input into the battery

        self.voltage = voltage  # volts, nominal voltage of battery
        self.internal_resistance = internal_resistance  # ohms, internal resistance of the battery
        self.thermal_resistance = thermal_resistance  # deg C/Watt, battery to coolant
        self.thermal_mass = thermal_mass  # J/deg C
        self.thermal_rejection_temp = thermal_rejection_temp # deg C, temperature of cooling effect on battery
        self.maximum_temperature = maximum_temperature # maximum battery temperature, deg C

        self.temperature = np.zeros(number_of_points) # kelvin or celsius, current temperature
        self.current = np.zeros(number_of_points)  # amps, current output amperage
        self.power = np.zeros(number_of_points)  # output power in watts, negative for power into the battery
        self.energy_cumulative = np.zeros(number_of_points)  # net energy expended from battery in Joules
        self.heat_power = np.zeros(number_of_points)  # watts, heat power at each point on the track
        self.heat_energy_cumulative = np.zeros(number_of_points)  # joules, cumulative heat energy generated in battery

        self.temperature[0] = initial_temp
    
    def calculate_energy_values(self, i, time):
        """Calculate the energy and temperature values
        based on the previously calculated power conditions.
        
        
        Inputs:
            - i (int): index in array
            - time (float): time between previous step and current step
        
        Outputs:
            - None
        
        """

        energy = self.power[i - 1] * time
        heat_energy = self.heat_power[i - 1] * time

        self.energy_cumulative[i] = self.energy_cumulative[i - 1] + energy
        self.heat_energy_cumulative[i] = self.heat_energy_cumulative[i - 1] + heat_energy

        rejected_thermal_power = (self.temperature[i - 1] - self.thermal_rejection_temp) / self.thermal_resistance
        rejected_thermal_energy = rejected_thermal_power * time
        temperature_increase = (heat_energy - rejected_thermal_energy) / self.thermal_mass

        self.temperature[i] = self.temperature[i - 1] + temperature_increase

    def calculate_actual_battery_power(self, i, requested_power):
        """Calculates the power of the battery pack based on
        requested power and current state of the battery.
        It also calculates the other power characteristics to do with the battery.
        
        Inputs:
            - i (int): index in array
            - requested_power (float): requested output of the battery, negative for input
        
        Outputs:
            - actual_power (float): actual output power of the battery
        
        """

        # charging
        if requested_power < 0:
            self.power[i] = max(requested_power, self.max_charge_rate)
        # discharging
        else:
            self.power[i] = min(requested_power, self.max_discharge_rate)
        
        self.current[i] = self.power[i] / self.voltage


        self.heat_power[i] = self.current[i] ** 2 * self.internal_resistance

        actual_power = self.power[i]

        return actual_power



class superCapacitor():
    """Class of a simple super capacitor. This capacitor
    model assumes that the output voltage of the capacitor
    does not vary based on percent charge.
    
    This model treats the capacitor like a constant voltage source
    with a consistent internal resistance.
    
    maximum charge/discharge rates do not vary based on percent capacity.
    
    This module is intended to be used in the following way:
    1. Initialize the class
    2. Set the static values initialized in the __init__ function
    When running the lap simulation:
    3. To determine the power supplied by the capacitor during a step run the 
       calculate_actual_capacitor_power function
    4. After the step has been executed run the calculate_energy_values function
       to calculate the energy values. This should be done before running the 
       calculate_actual_capacitor_power function for the next step. This is because
       the power output of the capacitor is in part dependent on the state of charge
       of the capacitor. If the capacitor is empty or full you cannot discharge or charge further!
       
    After the lap is done there are power, energy, and temperature arrays
    that are available to use for analysis."""

    def __init__(self, number_of_points, capacity, max_charge_rate,
                 max_discharge_rate, voltage, internal_resistance,
                 current, thermal_mass, thermal_resistance, 
                 thermal_rejection_temp, maximum_temperature,
                 initial_temp):
        self.capacity = capacity  # Joules, capacity of capacitor
        self.max_discharge_rate = max_discharge_rate  # Watts, max output of capacitor
        self.max_charge_rate = max_charge_rate  # Watts, max input into the capacitor

        self.voltage = voltage  # volts, nominal voltage of battery
        self.internal_resistance = internal_resistance  # ohms, internal resistance of the battery
        self.thermal_resistance = thermal_resistance  # deg C/Watt, battery to coolant
        self.thermal_mass = thermal_mass  # J/deg C
        self.thermal_rejection_temp = thermal_rejection_temp # deg C, temperature of cooling effect on battery
        self.maximum_temperature = maximum_temperature # maximum battery temperature, deg C

        self.temperature = np.zeros(number_of_points) # kelvin or celsius, current temperature
        self.current = np.zeros(number_of_points)  # amps, current output amperage
        self.power = np.zeros(number_of_points)  # output power in watts, negative for power into the battery
        self.energy_cumulative = np.zeros(number_of_points)  # net energy expended from battery in Joules
        self.heat_power = np.zeros(number_of_points)  # watts, heat power at each point on the track
        self.heat_energy_cumulative = np.zeros(number_of_points)  # joules, cumulative heat energy generated in battery

        self.temperature[0] = initial_temp
    
    def calculate_energy_values(self, i, time):
        """Calculate the energy and temperature values
        based on the previously calculated power conditions.
        
        
        Inputs:
            - i (int): index in array
            - time (float): time between previous step and current step
        
        Outputs:
            - None
        
        """

        energy = self.power[i - 1] * time
        heat_energy = self.heat_power[i - 1] * time

        self.energy_cumulative[i] = self.energy_cumulative[i - 1] + energy
        self.heat_energy_cumulative[i] = self.heat_energy_cumulative[i - 1] + heat_energy

        rejected_thermal_power = (self.temperature[i - 1] - self.thermal_rejection_temp) / self.thermal_resistance
        rejected_thermal_energy = rejected_thermal_power * time
        temperature_increase = (heat_energy - rejected_thermal_energy) / self.thermal_mass

        self.temperature[i] = self.temperature[i - 1] + temperature_increase

    def calculate_actual_capacitor_power(self, i, requested_power, prev_time):
        """Calculates the power of the battery pack based on
        requested power and current state of the battery.
        It also calculates the other power characteristics to do with the battery.
        
        Inputs:
            - i (int): index in array
            - requested_power (float): requested output of the battery, negative for input
            - prev_time (float): the time to complete the previous segment/increment. used to estimate if the capacitor
                will fill up or completely drain on this segment/increment
        
        Outputs:
            - actual_power (float): actual output power of the battery
        
        """
        
        # need to check if the capacitor will fill up or completely drain by charging/discharging the requsted power
        # estimate if that will happen by using the previous time, there is an assumption here
        # that there might be some over charge or under charge but if that happens then the first statement in 
        # this function will catch it and the next power output will be zero.

        # charging
        if requested_power < 0:
            if self.energy_cumulative[i - 1] >= self.capacity:
                # capacitor is full!
                self.power[i] = 0
            elif self.energy_cumulative[i - 1] + abs(self.power[i] * prev_time) > self.capacity:
                # capacitor is almost full, need to limit power into it.
                self.power[i] = (self.capacity - self.energy_cumulative[i - 1]) * prev_time
            else:
                # capacitor is not full, charge away!
                self.power[i] = max(requested_power, self.max_charge_rate)
        # discharging
        else:
            if self.energy_cumulative[i - 1] < 0:
                # capacitor is empty!
                self.power[i] = 0
            elif self.energy_cumulative[i - 1] - abs(self.power[i] * prev_time) > 0:
                # capacitor is almost empty, drain it all the way
                self.power[i] = (self.energy_cumulative[i - 1]) * prev_time
            else:
                # not discharged, charge away!
                self.power[i] = min(requested_power, self.max_discharge_rate)

        # power loss calculations
        self.current[i] = self.power[i] / self.voltage

        self.heat_power[i] = self.current[i] ** 2 * self.internal_resistance

        actual_power = self.power[i]

        return actual_power