obisMap = {
    '0-0:1.0.0': 'datetime',
    '0-0:42.0.0': 'deviceName',
    '0-0:96.1.0': 'deviceSerialNumber',
    '0-0:96.14.0': 'currentlyActiveTariff',
    '0-0:96.50.68': 'circuitBreakerStatus',
    '0-0:17.0.0': 'circuitBreakerLimit',
    '1-0:1.8.0': 'ingressEnergy',
    '1-0:1.8.1': 'ingressEnergyT1',
    '1-0:1.8.2': 'ingressEnergyT2',
    '1-0:1.8.3': 'ingressEnergyT3',
    '1-0:1.8.4': 'ingressEnergyT4',
    '1-0:2.8.0': 'egressEnergy',
    '1-0:2.8.1': 'egressEnergyT1',
    '1-0:2.8.2': 'egressEnergyT2',
    '1-0:2.8.3': 'egressEnergyT3',
    '1-0:2.8.4': 'egressEnergyT4',
    '1-0:3.8.0': 'ingressTotalReactiveEnergy',
    '1-0:4.8.0': 'egressTotalReactiveEnergy',
    '1-0:5.8.0': 'ingressInductiveReactiveEnergyQ1',
    '1-0:6.8.0': 'ingressCapacitiveReactiveEnergyQ2',
    '1-0:7.8.0': 'egressInductiveReactiveEnergyQ3',
    '1-0:8.8.0': 'egressCapacitiveReactiveEnergyQ4',
    '1-0:15.8.0': 'absoluteActiveEnergy',
    '1-0:32.7.0': 'instantaneousVoltageL1',
    '1-0:52.7.0': 'instantaneousVoltageL2',
    '1-0:72.7.0': 'instantaneousVoltageL3',
    '1-0:31.7.0': 'instantaneousCurrentL1',
    '1-0:51.7.0': 'instantaneousCurrentL2',
    '1-0:71.7.0': 'instantaneousCurrentL3',
    '1-0:13.7.0': 'instantaneousPowerFactor',
    '1-0:33.7.0': 'instantaneousPowerFactorL1',
    '1-0:53.7.0': 'instantaneousPowerFactorL2',
    '1-0:73.7.0': 'instantaneousPowerFactorL3',
    '1-0:14.7.0': 'frequency',
    '1-0:1.7.0': 'ingressPositiveActiveInstantaneousPower',
    '1-0:2.7.0': 'egressPositiveActiveInstantaneousPower',
    '1-0:5.7.0': 'instantaneousReactivePowerQ1',
    '1-0:6.7.0': 'instantaneousReactivePowerQ2',
    '1-0:7.7.0': 'instantaneousReactivePowerQ3',
    '1-0:8.7.0': 'instantaneousReactivePowerQ4',
    # not used '0-0:98.1.0': 'priorMonthValuesSinceLastBilling',
    # not used '0-0:96.13.0': 'textMessageSMS'
}

#
# /AUX59940200979
# 
# 0-0:1.0.0(231219112120W)
# 0-0:42.0.0(AUX1030340200979)
# 0-0:96.1.0(9940200979)
# 0-0:96.14.0(0001)
# 0-0:96.50.68(ON)
# 0-0:17.0.0(90.000*kW)
# 1-0:1.8.0(018456.016*kWh)
# 1-0:1.8.1(009792.212*kWh)
# 1-0:1.8.2(008663.804*kWh)
# 1-0:1.8.3(000000.000*kWh)
# 1-0:1.8.4(000000.000*kWh)
# 1-0:2.8.0(035161.853*kWh)
# 1-0:2.8.1(024664.677*kWh)
# 1-0:2.8.2(010497.176*kWh)
# 1-0:2.8.3(000000.000*kWh)
# 1-0:2.8.4(000000.000*kWh)
# 1-0:3.8.0(004820.827*kvarh)
# 1-0:4.8.0(007780.958*kvarh)
# 1-0:5.8.0(003683.456*kvarh)
# 1-0:6.8.0(001137.371*kvarh)
# 1-0:7.8.0(001948.085*kvarh)
# 1-0:8.8.0(005832.873*kvarh)
# 1-0:15.8.0(053617.912*kWh)
# 1-0:32.7.0(242.8*V)
# 1-0:52.7.0(240.8*V)
# 1-0:72.7.0(241.7*V)
# 1-0:31.7.0(001*A)
# 1-0:51.7.0(001*A)
# 1-0:71.7.0(001*A)
# 1-0:13.7.0(0.974)
# 1-0:33.7.0(0.977)
# 1-0:53.7.0(0.928)
# 1-0:73.7.0(0.998)
# 1-0:14.7.0(49.99*Hz)
# 1-0:1.7.0(00.000*kW)
# 1-0:2.7.0(00.849*kW)
# 1-0:5.7.0(00.000*kvar)
# 1-0:6.7.0(00.000*kvar)
# 1-0:7.7.0(00.196*kvar)
# 1-0:8.7.0(00.000*kvar)
# 0-0:98.1.0(231201000000W)(018060.278*kWh)(009561.131*kWh)(008499.147*kWh)(035052.478*kWh)(024609.593*kWh)(010442.885*kWh)(004793.855*kvarh)(007666.942*kvarh)(003660.840*kvarh)(001133.015*kvarh)(001931.502*kvarh)(005735.440*kvarh)(053112.795*kWh)(14.316*kW)(13.988*kW)(14.316*kW)(08.208*kW)(08.208*kW)(07.768*kW)
# 0-0:96.13.0(яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя)
# !536D
