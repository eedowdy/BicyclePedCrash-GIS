import arcpy
from arcpy import env
w = arcpy.GetParameterAsText(4)
env.workspace = w
env.overwriteOutput = True


jurisdictional_limits = arcpy.GetParameterAsText(0)
if jurisdictional_limits == '#' or not jurisdictional_limits:
    jurisdictional_limits = "chapel-hill-jurisdictional-limits" 

signal_locations = arcpy.GetParameterAsText(1)
if signal_locations == '#' or not signal_locations:
    signal_locations = "traffic-signal-location-list" 

bicycle_crash_data = arcpy.GetParameterAsText(2)
if bicycle_crash_data == '#' or not bicycle_crash_data:
    bicycle_crash_data = "bicycle-crash-data-chapel-hill-region" 

pedestrian_crash_data = arcpy.GetParameterAsText(3)
if pedestrian_crash_data == '#' or not pedestrian_crash_data:
    pedestrian_crash_data = "pedestrian-crashes-chapel-hill-region"


j_signals = "j_signals"
j_bicycle = "j_bicycle_crashes"
j_pedestrians = "j_ped_crashes"

arcpy.Intersect_analysis(jurisdictional_limits, signal_locations, j_signals)
arcpy.Intersect_analysis(jurisdictional_limits, bicycle_crash_data, j_bicycle)
arcpy.Intersect_analysis(jurisdictional_limits, pedestrian_crash_data, j_pedestrians)

signals_buffer = "signals_buff"

arcpy.Buffer_analysis(j_signals, signals_buffer, "400 Feet", "FULL", "ROUND", "NONE")

bicycle_count = "bicycle_count"
arcpy.SpatialJoin_analysis(signals_buffer, j_bicycle, bicycle_count)
bicycle_and_ped = "count_bikes_ped_crashes"
arcpy.SpatialJoin_analysis(bicycle_count, j_pedestrian, bicycle_and_ped)



