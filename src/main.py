from modules.Request import donwload
from modules.ControlDate import controltime
from config import config_user

if __name__ == "__main__":

        config = config_user()
        time = controltime()

        donwload(config['ClientReg'], time['start'], time['end'], config['CostConf'], config['DirCostReg'], 'CostAWS_')
        donwload(config['ClientEcu'], time['start'], time['end'], config['CostConf'], config['DirCostEcu'], 'CostAWS_')

