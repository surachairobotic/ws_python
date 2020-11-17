#!/usr/bin/env python3

import ctypes

def main():
    sp_ice = ctypes.CDLL("C:\\Program Files\\RAYLASE\\SP-ICE\\bin\\SP-ICE.dll")
    print("Hello world !!!")
    print("Get_Active_Card : " + str(sp_ice.Get_Active_Card()))
    print("Get_Counts : " + str(sp_ice.Get_Counts()))
    print("Get_CPU_Type : " + str(sp_ice.Get_CPU_Type()))
    print("Get_DLL_Version : " + str(sp_ice.Get_DLL_Version()))
    
    print("Get_Ident_Ex : " + str(sp_ice.Get_Ident_Ex()))
    print("Get_Jump_Speed : " + str(sp_ice.Get_Jump_Speed()))
    print("Get_Mark_Speed : " + str(sp_ice.Get_Mark_Speed()))
    #print("Get_Mode_Mask : " + str(sp_ice.Get_Mode_Mask()))
    print("Get_SPC1_Version : " + str(sp_ice.Get_SPC1_Version()))
    print("Get_System_Status : " + str(sp_ice.Get_System_Status()))
    print("Get_Version : " + str(sp_ice.Get_Version()))
    #print("Get_XY_Pos : " + str(sp_ice.Get_Version()))

    # RLC Only
    #print("Get_Device_Description_String : " + str(sp_ice.Get_Device_Description_String()))
    #print("Get_Driver_Version : " + str(sp_ice.Get_Driver_Version()))
    #print("Get_Firmware_Version : " + str(sp_ice.Get_Firmware_Version()))
    #print("Get_Hardware_Version : " + str(sp_ice.Get_Hardware_Version()))
    #print("Get_Library_Version : " + str(sp_ice.Get_Library_Version()))
    

if __name__ == "__main__":
    main()
