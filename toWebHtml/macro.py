from connectoffice import Automation, terminateOffice
from execution_example import func, UNOCompos
def macro():  # Function to call from macro
    ctx = XSCRIPTCONTEXT.getComponentContext()
    smgr = ctx.getServiceManager()
    func(ctx, Automation(smgr, UNOCompos))
    terminateOffice(ctx, smgr)
g_exportedScripts = macro,