import os
import boto3

def config_user():
    ### Creao los dir de la app
    folder_download = '../JsonReports/'
    path_control = '../ControlDownload/'

    DirCostReg = folder_download+'CostReg/'
    DirCostEcu = folder_download+'CostEcu/'

    list_paths = [folder_download,
                  path_control,
                  DirCostReg,
                  DirCostEcu,]

    for i in list_paths:
        if not os.path.exists(i):
            os.makedirs(i)
        else:
            pass

    ### Credenciales de usuario Regional
    client_reg = boto3.client('ce',
                              aws_access_key_id='-',
                              aws_secret_access_key='-')

    ### Credenciales de usuario Ecuador
    client_ecu = boto3.client('ce',
                               aws_access_key_id='-',
                               aws_secret_access_key='-')

    ### Configuracion para Costos
    cost = [{
            'Type': 'DIMENSION',
            'Key': 'SERVICE'}]


    dict_confg = {'DirCostReg': DirCostReg,
                  'DirCostEcu': DirCostEcu,
                  'ClientReg': client_reg,
                  'ClientEcu': client_ecu,
                  'CostConf': cost,}

    return dict_confg