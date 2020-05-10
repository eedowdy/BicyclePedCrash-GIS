import arcpy
from arcpy import env
w = arcpy.GetParameterAsText(4)
env.workspace = w
env.overwriteOutput = True


jurisdictional_limits = arcpy.GetParameterAsText(0)

signal_locations = arcpy.GetParameterAsText(1)

bicycle_crash_data = arcpy.GetParameterAsText(2)

pedestrian_crash_data = arcpy.GetParameterAsText(3)

j_signals = "j_signals.shp"
j_bicycle = "j_bicycle_crashes.shp"
j_pedestrians = "j_ped_crashes.shp"

arcpy.Clip_analysis(signal_locations, jurisdictional_limits, j_signals, "")
arcpy.Clip_analysis(bicycle_crash_data, jurisdictional_limits, j_bicycle, "")
arcpy.Clip_analysis(pedestrian_crash_data, jurisdictional_limits, j_pedestrians, "")

signals_buffer = "signals_buff.shp"

arcpy.Buffer_analysis(j_signals, signals_buffer, "400 Feet", "FULL", "ROUND", "NONE")

bicycle_count = "bicycle_count.shp"
arcpy.SpatialJoin_analysis(signals_buffer, j_bicycle, bicycle_count)

bicycle_and_ped = "count_bikes_ped_crashes.shp"
arcpy.SpatialJoin_analysis(bicycle_count, j_pedestrians, bicycle_and_ped)

arcpy.AddField_management(bicycle_and_ped, "Accidents", "SHORT", 5, "", "", "accidents", "NULLABLE")

arcpy.CalculateField_management(bicycle_and_ped, "Accidents", "[Join_Count] + [Join_Cou_1]")



