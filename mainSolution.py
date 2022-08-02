from pathlib import Path
import cash_on_hand,overheads,profit_loss,api

def mainsoultion_function():
    fp = Path.cwd()/"summary_report.txt"
    fp.touch()