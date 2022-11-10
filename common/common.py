import subprocess
from common.logger import loggerDEBUG, loggerINFO, loggerWARNING, loggerERROR, loggerCRITICAL


def rs(command): # runShellCommand_and_returnOutput
    try:
        completed = subprocess.check_output(command, shell=True)
        loggerDEBUG(f'shell command {command} - returncode: {completed}')
        return str(completed, 'utf-8', 'ignore')
    except:
        loggerERROR(f"error on shell command: {command}")
        return False
